import gradio as gr
import requests
import json

# api_key = "sk-gDwSHkdjqmoaqW1ugLcelBenJNT12TSMttii3Vzt"  # Replace with your key

url = "https://tech.meikeigypsum.cn/forwardapi/v1/chat/completions"

headers = {
    "Authorization": "Bearer sk-gDwSHkddjqmoaqW1ureregLcelBenrereJNT12TSfMttii3Vzt",
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
        "stream": True,
        "temperature": 0.8,
        "messages": history_chat_format
    }

    response = requests.post(url, json=payload, headers=headers, stream=True)

    if response.status_code == 200:
        partial_message = ""
        for chunk in response.iter_lines():
            response_data = chunk.decode("utf-8").strip()
            if not response_data:
                continue
            try:
                if response_data.endswith("data: [DONE]"):
                    break
                data_list = response_data.split("data: ")
                if len(data_list) > 2:
                    json_data = json.loads(data_list[2])
                else:
                    json_data = json.loads(response_data.split("data: ")[1])
                if 'content' in json_data["choices"][0]["delta"]:
                    partial_message = partial_message + json_data["choices"][0]["delta"]['content']
                    yield partial_message
            except:
                print('json load error:', response_data)
    else:
        yield 'Service Error!!!'


gr.ChatInterface(predict).queue().launch()
