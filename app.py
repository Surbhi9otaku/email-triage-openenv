import gradio as gr

def greet():
    return "App running successfully 🚀"

iface = gr.Interface(
    fn=greet,
    inputs=[],
    outputs="text"
)

iface.launch()