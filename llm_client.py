import os
from typing import Any

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")


def get_completion(
    prompt: str,
    model: str = DEFAULT_MODEL,
    temperature: float | None = None,
    max_tokens: int = 500,
) -> tuple[str, dict[str, int]]:
    messages = [{"role": "user", "content": prompt}]

    return get_chat_completion(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )


def get_chat_completion(
    messages: list[dict[str, str]],
    model: str = DEFAULT_MODEL,
    temperature: float | None = None,
    max_tokens: int = 500,
) -> tuple[str, dict[str, int]]:
    params: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "max_completion_tokens": max_tokens,
    }

    # Some models, especially GPT-5-style/reasoning models,
    # do not support custom temperature values.
    # So we only send temperature when it is explicitly provided.
    if temperature is not None:
        params["temperature"] = temperature

    response = client.chat.completions.create(**params)

    content = response.choices[0].message.content or ""

    token_dict = {
        "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
        "completion_tokens": response.usage.completion_tokens if response.usage else 0,
        "total_tokens": response.usage.total_tokens if response.usage else 0,
    }

    return content, token_dict


messages = [
    {
        "role": "system",
        "content": "You are an assistant who responds in the style of Dr. Seuss.",
    },
    {
        "role": "user",
        "content": "Write me a very short poem about a happy carrot.",
    },
]

response, token_dict = get_chat_completion(messages)

print(response)
print(token_dict)