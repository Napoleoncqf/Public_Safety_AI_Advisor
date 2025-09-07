import requests
import json

# Ollama API的地址
url = "http://localhost:11434/api/generate"

# 我们要发送的数据
payload = {
    "model": "qwen2:7b",  # 确保你已经下载了这个模型
    "prompt": "用中文解释一下什么是‘应急预案’？",
    "stream": False  # 设置为False，这样可以一次性获得完整回复
}

print("正在向Ollama发送请求，请稍候...")

try:
    # 发送POST请求
    response = requests.post(url, json=payload)
    response.raise_for_status()  # 如果请求失败，会抛出异常

    # 解析并打印回复
    response_data = response.json()
    print("\n--- Ollama的回复 ---\n")
    print(response_data['response'])
    print("\n---------------------\n")

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
    print("\n请确保Ollama服务正在后台运行。")
