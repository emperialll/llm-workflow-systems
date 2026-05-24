from src.config import OPENAI_MODEL, SYSTEM_MESSAGE
from src.openai_client import create_openai_client
from src.pipeline import handle_user_message


def main() -> None:
    client = create_openai_client()

    user_input = input("User: ")

    response = handle_user_message(
        client=client,
        user_input=user_input,
        system_instruction=SYSTEM_MESSAGE,
        model=OPENAI_MODEL,
        moderate_output=True,
    )

    try:
        final_response = response.split("####")[-1].strip()
    except Exception as e:
        final_response = "Sorry, I'm having trouble right now, please try asking another question."
    
    print(final_response)

if __name__ == "__main__":
    main()
