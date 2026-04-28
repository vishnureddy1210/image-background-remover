import gradio as gr
from rembg import remove
from PIL import Image
import io

def remove_bg(image):
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    result = remove(img_bytes.getvalue())
    return Image.open(io.BytesIO(result))

demo = gr.Interface(
    fn=remove_bg,
    inputs=gr.Image(type="pil", label="Upload photo"),
    outputs=gr.Image(label="Background removed"),
    title="Background Remover"
)

demo.launch()