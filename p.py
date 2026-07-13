import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    running_mode=vision.RunningMode.VIDEO
)
landmarker = vision.HandLandmarker.create_from_options(options)


WIDTH, HEIGHT = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

canvas = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)

colors = {
    "Pen": (255, 255, 255, 255),    
    "Blue": (255, 128, 0, 255),     
    "Green": (0, 255, 128, 255),    
    "Red": (51, 51, 255, 255),      
    "Yellow": (0, 230, 255, 255),   
    "Eraser": (0, 0, 0, 0)          
}

current_color_name = "Pen"
current_color = colors[current_color_name]
prev_x, prev_y = 0, 0
frame_id = 0

templates = ["Camera Clean", "Whiteboard Grid", "Notebook", "Blackboard", "Graph Paper"]
current_template_idx = 0

def generate_background_overlay(template_name, w, h):
    bg = np.zeros((h, w, 3), dtype=np.uint8)
    if template_name == "Camera Clean":
        bg[:] = (0, 0, 0)
    elif template_name == "Blackboard":
        bg[:] = (25, 45, 25)
    elif template_name == "Whiteboard Grid":
        bg[:] = (255, 255, 255)
        for x in range(0, w, 60):
            cv2.line(bg, (x, 0), (x, h), (200, 200, 200), 1)
        for y in range(0, h, 60):
            cv2.line(bg, (0, y), (w, y), (200, 200, 200), 1)
    elif template_name == "Notebook":
        bg[:] = (255, 253, 248)
        for y in range(90, h, 35):
            cv2.line(bg, (0, y), (w, y), (220, 180, 160), 1)
        cv2.line(bg, (120, 0), (120, h), (150, 150, 255), 1)  
    elif template_name == "Graph Paper":
        bg[:] = (240, 250, 240)
        for x in range(0, w, 15):
            cv2.line(bg, (x, 0), (x, h), (215, 230, 215), 1)
        for y in range(0, h, 15):
            cv2.line(bg, (0, y), (w, y), (215, 230, 215), 1)
        for x in range(0, w, 75):
            cv2.line(bg, (x, 0), (x, h), (170, 200, 170), 1)
        for y in range(0, h, 75):
            cv2.line(bg, (0, y), (w, y), (170, 200, 170), 1)
    return bg


while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    h, w, _ = frame.shape
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = landmarker.detect_for_video(mp_image, frame_id)
    frame_id += 1

    current_template = templates[current_template_idx]
    bg_overlay = generate_background_overlay(current_template, w, h)

    if current_template == "Camera Clean":
        output_display = frame.copy()
    elif current_template == "Blackboard":
        output_display = cv2.addWeighted(frame, 0.3, bg_overlay, 0.7, 0)
    else:
        output_display = cv2.addWeighted(frame, 0.6, bg_overlay, 0.4, 0)

    # UI HEADER
    ui_overlay = output_display.copy()
    cv2.rectangle(ui_overlay, (0, 0), (w, 90), (30, 30, 30), -1)
    cv2.addWeighted(ui_overlay, 0.25, output_display, 0.75, 0, output_display)

    buttons = [
        {"name": "Pen", "center": (80, 45), "color": (240, 240, 240)},
        {"name": "Blue", "center": (200, 45), "color": (255, 128, 0)},
        {"name": "Green", "center": (320, 45), "color": (0, 255, 128)},
        {"name": "Red", "center": (440, 45), "color": (51, 51, 255)},
        {"name": "Yellow", "center": (560, 45), "color": (0, 230, 255)},
        {"name": "Eraser", "center": (680, 45), "color": (140, 140, 140)}
    ]

    for btn in buttons:
        is_active = current_color_name == btn["name"]
        radius = 24 if is_active else 18
        if is_active:
            cv2.circle(output_display, btn["center"], radius + 4, (255, 255, 255), 2)
        cv2.circle(output_display, btn["center"], radius, btn["color"], -1)
        
        if btn["name"] == "Pen":
            cv2.putText(output_display, "PEN", (btn["center"][0]-15, btn["center"][1]+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
        elif btn["name"] == "Eraser":
            cv2.putText(output_display, "DEL", (btn["center"][0]-16, btn["center"][1]+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 2)

    cv2.putText(output_display, f"Mode: {current_template}", (w - 260, 52), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


    if result.hand_landmarks and len(result.hand_landmarks) > 0:
        for hand in result.hand_landmarks:
           
            index_up  = hand[8].y < hand[6].y
            middle_up = hand[12].y < hand[10].y
            ring_up   = hand[16].y < hand[14].y
            pinky_up  = hand[20].y < hand[18].y
            
            index_x, index_y = int(hand[8].x * w), int(hand[8].y * h)

            
            if index_up and middle_up and ring_up and not pinky_up:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = index_x, index_y
                

                cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), (0, 0, 0, 0), 80)
                
                # Screen par eraser ka circle dikhane ke liye
                cv2.circle(output_display, (index_x, index_y), 40, (0, 0, 255), 2)
                cv2.putText(output_display, "Eraser", (index_x + 45, index_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                prev_x, prev_y = index_x, index_y

            elif index_up and middle_up and not ring_up:
                prev_x, prev_y = 0, 0 
                cv2.circle(output_display, (index_x, index_y), 10, (255, 255, 255), 2)
                
                if index_y < 90:
                    for btn in buttons:
                        if btn["center"][0] - 40 < index_x < btn["center"][0] + 40:
                            current_color_name = btn["name"]
                            current_color = colors[current_color_name]

           
            elif index_up and not middle_up and not ring_up:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = index_x, index_y
                
                brush_size = 60 if current_color_name == "Eraser" else (4 if current_color_name == "Pen" else 10)
                cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), current_color, brush_size)
                cv2.circle(output_display, (index_x, index_y), 4, (255, 255, 255), -1)
                prev_x, prev_y = index_x, index_y
                
            else:
               
                prev_x, prev_y = 0, 0
    else:
        prev_x, prev_y = 0, 0

    
    b, g, r, alpha = cv2.split(canvas)
    canvas_rgb = cv2.merge([b, g, r])
    mask = alpha / 255.0
    for c in range(0, 3):
        output_display[:, :, c] = (mask * canvas_rgb[:, :, c] + (1.0 - mask) * output_display[:, :, c]).astype(np.uint8)

    
    cv2.putText(output_display, "Q: Quit | B: Cycle BG Mode | S: Save Studio Capture | C: Clear All Lines", 
                (30, h - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (240, 240, 240), 1, cv2.LINE_AA)

    cv2.imshow("AI Studio Board Pro", output_display)
    
    key = cv2.waitKey(1)
    if key == ord('b'):
        current_template_idx = (current_template_idx + 1) % len(templates)
    elif key == ord('c'):
        canvas = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8) # Keyboard manual backup clear
    elif key == ord('s'):
        cv2.imwrite("studio_capture.png", output_display)
        print("Saved!")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()