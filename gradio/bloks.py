import gradio as gr

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="姓名")
    output = gr.Textbox(label="输出")
    greet_btn = gr.Button("问候")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet123")


demo.launch(auth=("admin", "123456"))