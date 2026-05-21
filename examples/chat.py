#!/usr/bin/env python3
"""DeepSeek API Chat Example — OpenAI-compatible via Global API"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("GLOBAL_API_KEY", "your-key"),
    base_url="https://global-apis.com/v1",
)

# Basic chat
response = client.chat.completions.create(
    model="deepseek-chat",  # V4 Flash — $0.25/M output
    messages=[{"role": "user", "content": "Explain recursion in 50 words"}],
)
print("[Chat]", response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Write a haiku about coding"}],
    stream=True,
)
print("\n[Stream]", end=" ")
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()

# Function calling
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto",
)
print("\n[Tools]", response.choices[0].message.tool_calls)
