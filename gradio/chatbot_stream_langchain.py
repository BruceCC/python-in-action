import typing
from typing import Dict, Any, Mapping

import gradio as gr
import requests
import json
import logging

import langchain
from langchain.llms.base import LLM
from langchain.cache import InMemoryCache

logging.basicConfig(level=logging.INFO)


class BaichuanLLM(LLM):
    def __init__(self, url="http://10.11.33.235:10002/ucode/api/inference/CodeGen/codeChatStream"):
        # 模型服务URL
        self.url = url
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return 'baichuan-chat-13b'

    @classmethod
    def _post(cls, url: str,
              query: typing.Dict) -> Any:
        _headers = {
            "Authorization": "Bearer 540f0e05e33b48a9a29bde0d89d9775c",
            "Content-Type": "application/json"
        }
        with requests.session() as sess:
            resp = sess.post(url,
                             json=query,
                             headers=_headers,
                             stream=True)
        return resp

    def _construct_query(self, message) -> Dict:
        payload = {
            "model": "baichuan-13b-chat",
            "stream": True,
            "temperature": 0.8,
            "inputs": message,
            "parameters": {
                "temperature": 0.8,
                "top_k": 10,
                "top_p": 0.9,
                "max_length": 100,
                "num_return_sequences": 10,
                "repetition_penalty": 1.2
            }
        }

        return payload

    def _call(self, prompt: str,
              stop: typing.Optional[typing.List[str]] = None) -> str:
        query = self._construct_query(prompt=prompt)

        # post
        resp = self._post(url=self.url, query=query)

        if resp.status_code == 200:
            partial_message = ""
            for chunk in resp.iter_lines():
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

    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters.
        """
        _param_dict = {
            "url": self.url
        }
        return _param_dict



def predict(message, history):
    llm = BaichuanLLM()
    gpt_response = llm(message)
    return gpt_response.content


gr.ChatInterface(predict).queue().launch()
