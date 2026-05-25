# 01 — Input Safety and Moderation

This standalone project demonstrates a safety-first LLM workflow for a scoped customer-service assistant. It combines input moderation, prompt-injection detection, delimiter sanitization, assistant response generation, and optional output moderation into one reusable pipeline.

The goal is to show how LLM applications can enforce domain boundaries and reduce risk before and after model generation.

## What This Project Demonstrates

- Input moderation before the assistant responds.
- Prompt-injection classification before executing the main task.
- Delimiter sanitization to reduce delimiter-based injection tricks.
- System-instruction enforcement for a scoped assistant.
- Optional output moderation before returning the final answer.
- Modular pipeline design with separate files for client, assistant, moderation, and security logic.

## Project Structure

```text
01_input_safety_and_moderation/
├── .env.example
├── main.py
└── src/
    ├── assistant.py          # Main assistant call
    ├── config.py             # Model and system instruction configuration
    ├── moderation.py         # Moderation API wrappers
    ├── openai_client.py      # OpenAI client factory
    ├── pipeline.py           # Full safety workflow
    └── prompt_injection.py   # Prompt-injection detection and sanitization
```

## Workflow

```text
User input
   ↓
Moderation check
   ↓
Prompt-injection detection
   ↓
Customer-service assistant response
   ↓
Optional output moderation
   ↓
Final response
```

## Assistant Scope

The assistant is configured as a customer-service assistant and is instructed to answer only questions related to:

- Store information
- Products
- Orders
- Returns
- Refunds

Out-of-scope requests are politely refused.

## Security Features

### 1. Input Moderation

`moderation.py` checks whether user input is flagged before sending it to the main assistant.

### 2. Prompt-Injection Detection

`prompt_injection.py` uses a separate classifier-style LLM call to detect attempts such as:

- Asking the model to ignore previous instructions.
- Asking for hidden/system instructions.
- Injecting conflicting instructions.
- Attempting to change the assistant role.

The classifier returns only `Y` or `N`, making the decision easy to consume in code.

### 3. Delimiter Sanitization

User input is wrapped in a delimiter and cleaned before classification. This reduces the risk of user text breaking out of the expected prompt structure.

### 4. Output Moderation

When enabled, the generated assistant response is checked before it is shown to the user.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
cp .env.example .env
```

Update `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

## Run

```bash
python main.py
```

Example:

```text
User: What is your return policy for damaged products?
Assistant: ...
```

## Skills Showcased

- Designing safe LLM request pipelines.
- Using moderation as a pre-processing and post-processing layer.
- Building prompt-injection detection as a separate guardrail.
- Enforcing assistant domain boundaries through system instructions.
- Writing modular, production-oriented Python components.
- Separating configuration, client setup, security checks, and assistant logic.

## Possible Extensions

- Add structured logging for blocked requests.
- Return different refusal messages based on moderation category.
- Add unit tests for delimiter sanitization.
- Cache prompt-injection classification for repeated inputs.
- Add a policy file to make assistant scope easier to update.
