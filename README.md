# DeepSeek API Examples

Ready-to-run code examples for DeepSeek V4 Flash, R1, and Coder APIs in Python, JavaScript, and Go.

## Quick Start

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-key",
    base_url="https://global-apis.com/v1"  # OpenAI-compatible endpoint
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V4-Flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## Features
- Chat completions (sync & streaming)
- Function calling / tool use
- JSON mode
- Reasoning (DeepSeek-R1)
- Image understanding (Qwen-VL)

## Why Global API?
Direct DeepSeek API requires Chinese payment methods (WeChat/Alipay). Global API provides the same models with PayPal, never-expiring credits, and 184+ models under one API key.

**100 free credits on signup** — enough to test every example in this repo.

## Installation
```bash
pip install openai
python examples/chat.py
```
