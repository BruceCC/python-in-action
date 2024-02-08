import requests

# 准备请求数据
data = {
    "model": "HuggingFaceH4/starchat-alpha",
    "inputs": "用Java语言写一个实现冒泡排序的函数"
}

# 发送初始请求
response = requests.post(
    url="http://10.11.118.120:10002/idp/ai/CodeGen/codeChatStream",
    headers={
        "Authorization": "Bearer a5157b9b8532472fb61408669172ff6a",
        "Content-Type": "application/json"
    },
    json=data,
    stream=True  # 启用流式传输
)

# 处理响应数据
for chunk in response.iter_content(chunk_size=None):
    # 在这里处理每个数据块（chunk）的逻辑
    print(chunk)  # 示例：打印接收到的数据块

# 关闭连接
response.close()


