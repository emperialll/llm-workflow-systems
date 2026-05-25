# LLM Workflow Systems

A hands-on portfolio repository for experimenting with practical Large Language Model workflow patterns: chat message formatting, token-aware prompting, input/output safety, prompt-injection detection, structured reasoning, and multi-step prompt chains.

This repository is organized as a series of standalone mini-projects. Each directory focuses on one workflow concept and demonstrates how to move from simple prompt completion toward safer, more structured, and more maintainable LLM applications.

## Project Overview

| Project | Focus | What it demonstrates |
|---|---|---|
| [`00_chat_format_and_tokens`](./00_chat_format_and_tokens) | Chat format, completions, and token usage | Basic OpenAI chat-completion wrappers, system/user message construction, temperature control, and token accounting |
| [`01_input_safety_and_moderation`](./01_input_safety_and_moderation) | Security and moderation | Input moderation, output moderation, prompt-injection detection, delimiter sanitization, and scoped assistant behavior |
| [`02_chain_of_thought_reasoning`](./02_chain_of_thought_reasoning) | Structured reasoning prompt design | A German grammar assistant that uses staged internal analysis and returns only the final user-facing response |
| [`03_chaining_prompts`](./03_chaining_prompts) | Prompt chaining and token optimization | A multi-stage grammar analysis pipeline that breaks the task into smaller calls to reduce unnecessary context usage |

## Repository Goals

This repository showcases the engineering patterns required to build reliable LLM-powered systems, including:

- Chat-based prompt design using system and user roles.
- Token-aware API usage and cost visibility.
- Environment-based configuration for API keys and model selection.
- Moderation-first request handling.
- Prompt-injection classification and delimiter-based input hardening.
- Structured output design using exact schemas and JSON responses.
- Prompt chaining for modularity, debuggability, and token efficiency.
- Domain-grounded responses using a local German grammar knowledge base.

## Architecture Pattern

The later projects follow a clean workflow architecture:

```text
User input
   ↓
Input moderation
   ↓
Prompt-injection detection
   ↓
Task-specific assistant prompt
   ↓
Optional output moderation
   ↓
Final response
```

In `03_chaining_prompts`, the assistant task is further decomposed:

```text
User German text
   ↓
Language detection
   ↓
Sentence splitting
   ↓
Grammar-topic identification
   ↓
Local grammar-bank lookup
   ↓
Structured educational output
```

## Technologies Used

- Python
- OpenAI Python SDK
- Chat Completions API
- Moderation API
- `python-dotenv`
- JSON-based local knowledge base
- Modular pipeline design

## Setup

Each project is intended to run independently. From a project directory, create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
```

Create a `.env` file from the provided example where available:

```bash
cp .env.example .env
```

Then add your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

For `00_chat_format_and_tokens`, create a `.env` file manually if needed:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

## How to Run

Run each project from inside its own directory unless the project notes say otherwise:

```bash
cd 01_input_safety_and_moderation
python main.py
```

For projects that use local imports from `src`, running from the project root keeps import paths and data-file paths predictable.

## Skills Demonstrated

This repository highlights practical LLM application engineering skills:

- Prompt architecture and message formatting.
- Secure request handling and safety guardrails.
- Defensive prompt design against instruction override attempts.
- Pipeline decomposition and reusable helper modules.
- Cost-conscious workflow design through token tracking and prompt chaining.
- Structured reasoning patterns without exposing unnecessary intermediate analysis to users.
- JSON parsing and schema-constrained LLM outputs.
- Building domain-specific assistants with a local knowledge source.

## Notes

These projects are experimental learning modules. They intentionally keep the code compact so that each workflow concept is easy to inspect, test, and extend.
