from typing import Any


def moderate_text(client: Any, text: str) -> dict:
    """
    Run moderation check on input or output text.
    Returns moderation result as a dictionary.
    """
    response = client.moderations.create(
        model="omni-moderation-latest",
        input=text,
    )

    result = response.results[0]

    return {
        "flagged": result.flagged,
        "categories": result.categories.model_dump(),
        "category_scores": result.category_scores.model_dump(),
    }


def is_text_flagged(client: Any, text: str) -> bool:
    """
    Convenience wrapper that returns only True/False.
    """
    result = moderate_text(client, text)
    return result["flagged"]
