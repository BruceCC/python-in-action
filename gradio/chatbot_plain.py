import gradio as gr
import requests
import json

# api_key = "sk-gDwSHkdjqmoaqW1ugLcelBenJNT12TSMttii3Vzt"  # Replace with your key

url = "https://tech.meikeigypsum.cn/forwardapi/v1/chat/completions"

headers = {
    "Authorization": "Bearer sk-gDwSHkdjqmoaqW1ugLcelBenJNT12TSMttii3Vzt",
    "Content-Type": "application/json"
}


def predict(message, history):
    history_chat_format = []
    for human, assistant in history:
        history_chat_format.append({"role": "user", "content": human})
        history_chat_format.append({"role": "assistant", "content": assistant})
    history_chat_format.append({"role": "user", "content": message})

    payload = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.8,
        "messages": history_chat_format
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['choices'][0]['message']['content']


gr.ChatInterface(predict).launch()
