from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

# OpenAI API 访问凭证
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY


class ConversationRequest(BaseModel):
    messages: list


class Message(BaseModel):
    role: str
    content: str


@app.post("/conversation")
async def generate_dialogue(request: ConversationRequest):
    try:
        # 构建会话文本
        conversation = []
        for msg in request.messages:
            message = f"{msg.role}: {msg.content}"
            conversation.append(message)

        # 调用OpenAI API 进行对话生成
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=conversation,
            max_tokens=100
        )
        completion = response.choices[0].text.strip()

        return {"completion": completion}
    except Exception as e:
        return {"error": str(e)}


class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 100


@app.post("/complete")
async def complete_text(request: CompletionRequest):
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=request.prompt,
            max_tokens=request.max_tokens
        )
        completion = response.choices[0].text.strip()
        return {"completion": completion}
    except Exception as e:
        return {"error": str(e)}


# 调用openai 的gpt-turbo模型实现连续对话
@app.post("/chat")
async def chat_with_gpt(request: ChatRequest):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            frequency_penalty=request.frequency_penalty,
            presence_penalty=request.presence_penalty,
            stop=["\n"]
        )
        completion = response["choices"][0]["text"]
        return {"completion": completion}
    except Exception as e:
        return {"error": str(e)}


# 实现单例模式




















