import gradio as gr

with gr.Blocks() as demo:
    gr.Code(
        value="""def hello_world():
    return "Hello, world!"

print(hello_world())""",
        language="json",
        interactive=True,
        show_label=False,
    )

if __name__ == "__main__":
    demo.launch()