from typing import Any

from src.assistant import generate_assistant_response
from src.moderation import is_text_flagged
from src.prompt_injection import detect_prompt_injection


def handle_user_message(
    client: Any,
    user_input: str,
    system_instruction: str,
    model: str,
    moderate_output: bool = True,
) -> str:
    """
    Full input → safety → assistant → optional output safety pipeline.
    """

    if is_text_flagged(client, user_input):
        return "Sorry, I can't help with that request."

    if detect_prompt_injection(
        client=client,
        user_input=user_input,
        system_instruction=system_instruction,
        model=model,
    ):
        return "Sorry, I can only help with the intended task."

    assistant_response = generate_assistant_response(
        client=client,
        user_input=user_input,
        system_instruction=system_instruction,
        model=model,
    )

    if moderate_output and is_text_flagged(client, assistant_response):
        return "Sorry, I can't provide that response."

    return assistant_response
