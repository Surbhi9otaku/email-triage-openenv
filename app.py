import gradio as gr

def greet():
    return "App running successfully 🚀"

with gr.Blocks() as demo:
    btn = gr.Button("Run")
    output = gr.Textbox()
    btn.click(fn=greet, inputs=None, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)