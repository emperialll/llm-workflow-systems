# 00 — Chat Format and Token Usage

This standalone project introduces the foundation of working with chat-based LLM APIs: prompts, structured message roles, completions, temperature settings, and token usage reporting.

It demonstrates how a plain user prompt can be converted into a structured chat-completion request, how system instructions influence model behavior, and how token usage can be measured for cost and performance awareness.

## What This Project Demonstrates

- Simple prompt completion using a single user message.
- Chat-completion formatting with `system` and `user` roles.
- Reusable utility functions for OpenAI chat calls.
- Temperature control for deterministic or creative responses.
- Token-count extraction from API responses.
- API-key loading through environment variables instead of hardcoding secrets.

## Project Structure

```text
00_chat_format_and_tokens/
├── llm_client.py      # OpenAI client and default model configuration
├── llm_utils.py       # Completion helpers and token-count helper
└── main.py            # Interactive CLI entry point
```

## Core Concepts

### Chat Messages

The project uses a structured chat format:

```python
[
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
]
```

This shows the difference between global behavior instructions and user-specific input.

### Token Awareness

The helper `get_completion_and_token_count()` returns both the model response and usage metadata:

```python
{
    "prompt_tokens": ...,
    "completion_tokens": ...,
    "total_tokens": ...,
}
```

This is important for estimating cost, latency, and context-window usage in production LLM systems.

## Setup

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

## Run

```bash
python main.py
```

The CLI asks for:

1. A system prompt.
2. A user prompt.

It then sends both as structured chat messages and prints the assistant response.

## Example Use Case

```text
Enter the system prompt: You are a concise technical writing assistant.
Enter the user prompt: Explain what tokenization means in LLMs.
```

The model receives a role-aware prompt rather than a single unstructured string.

## Possible Extensions

- Add model comparison across multiple OpenAI models.
- Add a token-budget warning before sending long prompts.
- Save prompt/response/token logs for later analysis.
- Add tests for the message-construction helper.
