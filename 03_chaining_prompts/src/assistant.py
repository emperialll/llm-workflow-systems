from typing import Any


def generate_assistant_response(
    client: Any,
    user_input: str,
    system_instruction: str,
    model: str,
) -> str:
    """
    Main assistant logic after safety checks pass.
    """
    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_input},
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=1000,
    )

    return response.choices[0].message.content
