# 03 — Chaining Prompts for Token-Efficient Grammar Analysis

This standalone project demonstrates prompt chaining: splitting one complex LLM task into several smaller, focused model calls. The system analyzes German text by first checking the language, then splitting text into meaningful sentences, then identifying grammar topics, and finally mapping those topics to a local grammar bank.

The main design goal is token efficiency and maintainability. Instead of sending a large grammar bank into every reasoning step, the workflow uses smaller prompts for classification and routing, then performs deterministic lookup in Python.

## What This Project Demonstrates

- Multi-step LLM workflow orchestration.
- Language detection as a lightweight first gate.
- Text segmentation before deeper analysis.
- Grammar-topic classification using a constrained topic list.
- JSON-only model output for machine-readable intermediate results.
- Local deterministic lookup after LLM classification.
- Safety pipeline reuse with moderation and prompt-injection detection.

## Project Structure

```text
03_chaining_prompts/
├── .env.example
├── main.py
├── data/
│   └── German-Grammatik.json      # Local grammar knowledge base
└── src/
    ├── assistant.py               # Generic assistant-response helper
    ├── config.py                  # Model, grammar loading, and chain prompts
    ├── moderation.py              # Moderation API wrappers
    ├── openai_client.py           # OpenAI client factory
    ├── pipeline.py                # Safety workflow
    └── prompt_injection.py        # Prompt-injection detection
```

## Workflow

```text
User input
   ↓
Step 1: Check whether the input is German
   ↓
Step 2: Split German text into meaningful sentences
   ↓
Step 3: Identify grammar topics from a constrained topic list
   ↓
Step 4: Parse JSON mapping of topics to sentences
   ↓
Step 5: Look up topic details in the local grammar bank
   ↓
Step 6: Print structured grammar explanations, examples, common mistakes, and tests
```

## Why Prompt Chaining?

A single large prompt can become expensive, hard to debug, and difficult to control. This project breaks the work into smaller tasks:

1. **Language detection** uses a minimal `Y`/`N` output.
2. **Sentence splitting** prepares the text for more precise analysis.
3. **Grammar identification** uses only the list of available grammar topics, not the full grammar bank.
4. **Python lookup** retrieves full topic details without spending tokens on another large LLM call.

This design demonstrates how to combine LLM flexibility with traditional deterministic programming.

## Structured Intermediate Output

The grammar identifier is instructed to return valid JSON only:

```json
{
  "Grammar Topic Name": ["matched sentence one", "matched sentence two"]
}
```

This makes the LLM output easy to parse and use in downstream code.

## Safety Layer

Before each task-specific assistant response, the pipeline can run:

- Input moderation.
- Prompt-injection detection.
- Optional output moderation.

The prompt-injection detector is adapted for the language-learning context and explicitly treats normal German text, news text, grammar examples, and language-learning content as non-injection by default.

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

Example input:

```text
Obwohl ich müde bin, lerne ich Deutsch. Danach werde ich spazieren gehen.
```

The program prints matched grammar topics, German level, unit number, matched sentences, descriptions, examples, common mistakes, and English tests from the grammar bank.

## Skills Showcased

- Designing multi-call LLM systems.
- Reducing token usage with staged task decomposition.
- Combining LLM classification with deterministic local data lookup.
- Prompting for strict JSON outputs.
- Building reusable safety and assistant modules.
- Creating domain-specific language-learning workflows.
- Thinking beyond one-shot prompting toward production-style orchestration.

## Possible Extensions

- Add validation and retry logic when JSON parsing fails.
- Track token usage per chain step.
- Add timing metrics to compare chained vs. single-prompt approaches.
- Store results in a structured file for learning history.
- Add a UI that highlights matched grammar directly inside the original text.
