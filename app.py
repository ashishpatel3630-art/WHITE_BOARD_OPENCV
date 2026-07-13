import streamlit as st
import subprocess
import sys

st.set_page_config(
    page_title="AI Virtual Whiteboard",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 AI Virtual Whiteboard")
st.write(
    "Launch the OpenCV AI Virtual Whiteboard directly from Streamlit."
)

st.markdown("---")

st.markdown("""
### Features
- ✋ Real-time Hand Tracking
- 🎨 Air Drawing
- 🖌️ Multiple Colors
- 🧽 Eraser
- 💾 Save Drawing
""")

st.markdown("---")

if st.button("🚀 Launch Whiteboard", use_container_width=True):
    subprocess.Popen([sys.executable, "main.py"])
    st.success("Whiteboard launched successfully!")

st.info("Press **ESC** in the OpenCV window to close the whiteboard.")