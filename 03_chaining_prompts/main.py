from src.config import OPENAI_MODEL, SYSTEM_MESSAGE_CHECK_LANGUAGE, SYSTEM_MESSAGE_TEXT_SPLITTER, SYSTEM_MESSAGE_GRAMMAR_IDENTIFIER
from src.openai_client import create_openai_client
from src.pipeline import handle_user_message


def main() -> None:
    client = create_openai_client()

    user_input = input("User: ")

    response = handle_user_message(
        client=client,
        user_input=user_input,
        system_instruction=SYSTEM_MESSAGE_CHECK_LANGUAGE,
        model=OPENAI_MODEL,
        moderate_output=True,
    )

    print(response)

if __name__ == "__main__":
    main()
