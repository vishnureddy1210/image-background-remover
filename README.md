---
title: Image Background Remover
emoji: 🖼️
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.0.0"
app_file: app.py
pinned: false
---

# Image Background Remover

Upload any photo and remove the background instantly using AI.

## Live Demo
Try it here: https://vishnuvardhanreddy12-image-background-remover.hf.space/

## How to use
1. Upload a photo
2. Click Submit
3. Download the result

## Tech Stack
- Python
- Gradio
- rembg (U2Net AI model)
- onnxruntime

## Run locally
git clone https://github.com/vishnureddy1210/image-background-remover.git
cd image-background-remover
pip install "rembg[cpu]" gradio pillow
python app.py
