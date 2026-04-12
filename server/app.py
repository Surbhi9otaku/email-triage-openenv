import gradio as gr

def process_email(email):
    if "urgent" in email.lower():
        category = "Important"
        reply = "This looks urgent. I will respond shortly."
    elif "meeting" in email.lower():
        category = "Work"
        reply = "Noted. I will check my schedule and reply."
    else:
        category = "General"
        reply = "Thanks for your email. I will get back to you."

    return f"Category: {category}\nReply: {reply}"

with gr.Blocks() as demo:
    gr.Markdown("## 📧 Email Triage App")

    email_input = gr.Textbox(label="Enter Email", lines=5)
    output = gr.Textbox(label="Result")

    btn = gr.Button("Analyze Email")

    btn.click(fn=process_email, inputs=email_input, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)