# 02 — Structured Reasoning for German Grammar Analysis

This standalone project demonstrates structured reasoning prompt design for a domain-specific German grammar assistant. The assistant analyzes German text against a local grammar bank and returns a clear educational explanation for the user.

The project uses staged prompt instructions internally, then extracts and displays only the final user-facing response. This makes the assistant easier to guide while keeping the final output clean and focused.

## What This Project Demonstrates

- Domain-grounded LLM responses using a local JSON grammar bank.
- Structured multi-step prompt design.
- Output formatting with consistent grammar-topic sections.
- Controlled final-response extraction using a delimiter.
- Safety pipeline reuse with moderation and prompt-injection checks.
- German language education use case with level and unit mapping.

## Project Structure

```text
02_chain_of_thought_reasoning/
├── .env.example
├── German-Grammatik.json     # Local grammar knowledge base
├── main.py                   # CLI entry point and final-response extraction
└── src/
    ├── assistant.py          # Main assistant call
    ├── config.py             # Model, grammar loading, and system prompt
    ├── moderation.py         # Moderation API wrappers
    ├── openai_client.py      # OpenAI client factory
    ├── pipeline.py           # Safety workflow
    └── prompt_injection.py   # Prompt-injection detection
```

## Workflow

```text
User German text
   ↓
Input moderation
   ↓
Prompt-injection detection
   ↓
Grammar-bank-based analysis
   ↓
Optional output moderation
   ↓
Final response extraction
   ↓
Educational grammar explanation
```

## Grammar Bank Grounding

The assistant loads `German-Grammatik.json` and is instructed to use only grammar topics and levels that exist in the file. This reduces hallucinated topic names and keeps the response aligned with the available curriculum.

The prompt explicitly constrains the assistant to:

- Use only known grammar levels and topics.
- Identify a maximum of three to four relevant topics.
- Avoid inventing levels such as `B1.3` or `B2.3`.
- Provide explanations and examples in a predictable format.

## Final Output Format

The generated response is structured around grammar topics:

```text
Your text contains X important grammar points.

1. Topic Name - Level - Unit

   - Original part: "..."
   - Explanation: ...
   - Examples:
       DE: ...
       EN: ...
```

The CLI extracts the part after `Response to user:####` so users see the useful educational result rather than the full internal staged format.

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

Run from this project directory so the grammar JSON file path resolves correctly:

```bash
python main.py
```

Example input:

```text
Ich hätte mehr gelernt, wenn ich gestern Zeit gehabt hätte.
```

## Skills Showcased

- Prompt engineering for domain-specific tutoring.
- Knowledge-base grounding with local JSON data.
- Structured output design for educational explanations.
- Safe LLM workflow composition with moderation and injection checks.
- Separation of internal analysis format from final user-facing output.
- Practical handling of deterministic model behavior through low temperature.

## Possible Extensions

- Replace delimiter-based parsing with structured JSON output.
- Add tests for grammar-bank loading and topic validation.
- Add support for multiple languages in the explanation layer.
- Improve resilience when the model response does not include the expected delimiter.
- Add a web or Streamlit UI for interactive grammar practice.
