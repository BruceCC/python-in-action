import random

from fastapi import FastAPI
import gradio as gr
import uvicorn

CUSTOM_PATH = "/gradio"

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "This is your main app"}


def alternatingly_agree(message, history):
    if len(history) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"


def random_response(message, history):
    return random.choice(["Yes", "No"])


io = gr.ChatInterface(alternatingly_agree)

io2 = gr.ChatInterface(random_response)

app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)

app = gr.mount_gradio_app(app, io2, path='/gradio2')

if __name__ == "__main__":
    uvicorn.run(app, port=8000)

# Run this from the terminal as you would normally start a FastAPI app: `uvicorn run:app`
# and navigate to http://localhost:8000/gradio in your browser.
