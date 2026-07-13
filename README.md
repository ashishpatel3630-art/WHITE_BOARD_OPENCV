# 🎨 AI Virtual Whiteboard using OpenCV

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

**A real-time AI-powered virtual whiteboard that lets users draw in the air using hand gestures.**

</div>

---

## 📌 Overview

The **AI Virtual Whiteboard** is a computer vision project that transforms your webcam into an interactive digital whiteboard.

Using **OpenCV** and **MediaPipe Hand Tracking**, the application detects your hand in real time and allows you to draw on a virtual canvas without touching the screen.

This project demonstrates how Artificial Intelligence and Computer Vision can be used to create natural human-computer interactions.

---

## ✨ Features

- 🖐️ Real-time hand tracking
- ✍️ Air drawing using finger gestures
- 🎨 Multiple drawing colors
- 🖌️ Adjustable brush size
- 🧽 Eraser mode
- 📷 Live webcam feed
- ⚡ Fast and smooth drawing experience
- 💾 Save drawing as image
- 🧠 AI-powered gesture recognition
- 🖥️ Simple and intuitive interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Image Processing |
| MediaPipe | Hand Landmark Detection |
| NumPy | Numerical Operations |

---

## 📂 Project Structure

```
AI-Virtual-Whiteboard/
│
├── assets/
│   ├── screenshots/
│   └── icons/
│
├── images/
│
├── main.py
├── hand_tracker.py
├── drawing.py
├── utils.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Virtual-Whiteboard.git
```

---

### 2. Navigate to Project

```bash
cd AI-Virtual-Whiteboard
```

---

### 3. Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Project

```bash
python main.py
```

---

## 📦 Requirements

```txt
opencv-python
mediapipe
numpy
```

or install manually

```bash
pip install opencv-python mediapipe numpy
```

---

# 🖐️ Gesture Controls

| Gesture | Action |
|----------|--------|
| Index Finger Up | Draw |
| Index + Middle Finger | Selection Mode |
| Eraser Gesture | Erase Drawing |
| Palm | Stop Drawing |

> *(Modify according to your implementation.)*

---

# 📸 Screenshots

### Home

```
Add Screenshot Here
```

---

### Drawing Mode

```
Add Screenshot Here
```

---

### Color Selection

```
Add Screenshot Here
```

---

## 🧠 How It Works

1. Webcam captures live video.
2. OpenCV processes each frame.
3. MediaPipe detects hand landmarks.
4. Finger positions determine gestures.
5. Drawing coordinates are updated.
6. Canvas overlays on webcam feed.
7. Final output is displayed in real time.

---

## ⚙️ Future Improvements

- 🎤 Voice commands
- 📄 PDF export
- ☁️ Cloud saving
- 👥 Multi-user collaboration
- 📱 Mobile support
- 🤖 AI shape recognition
- ✍️ Handwriting to text
- 📐 Auto shape detection
- 🎨 Advanced brush effects

---

## 📈 Applications

- Online Teaching
- Presentations
- Digital Sketching
- Classroom Learning
- Brainstorming
- Whiteboard Meetings
- AI Demonstrations

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes

```bash
git commit -m "Add New Feature"
```

4. Push to GitHub

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

## 👨‍💻 Author

### Ashish Mewada

**AI Engineer | Computer Vision Developer | Agentic AI Developer**

- 💼 LinkedIn: https://linkedin.com/in/ashish-mewada-0499ba379
- 💻 GitHub: https://github.com/ashish24

---

## ⭐ Support

If you found this project useful, please give it a **⭐ Star** on GitHub.

---

## 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

### ⭐ If you like this project, don't forget to Star it! ⭐

Made with ❤️ using Python, OpenCV & MediaPipe

</div>