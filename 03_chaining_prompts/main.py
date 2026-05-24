from src.config import OPENAI_MODEL, SYSTEM_MESSAGE_CHECK_LANGUAGE, SYSTEM_MESSAGE_TEXT_SPLITTER, SYSTEM_MESSAGE_GRAMMAR_IDENTIFIER, grammar
from src.openai_client import create_openai_client
from src.pipeline import handle_user_message
from src.assistant import generate_assistant_response
import json


def find_topic(grammar_data, topic_name):
    """
    Search for a grammar topic in the full grammar data.

    Returns:
        {
            "level": "B1.1",
            "unit": "Unit 3",
            "data": {...topic data...}
        }

    or None if not found.
    """

    for level, units in grammar_data.items():
        for unit_name, topics in units.items():
            for topic_data in topics:
                if topic_data.get("topic") == topic_name:
                    return {
                        "level": level,
                        "unit": unit_name,
                        "data": topic_data,
                    }

    return None


def print_topic_info(topic_name, sentences, topic_match):
    topic_data = topic_match["data"]

    print("=" * 80)
    print(f"Topic: {topic_name}")
    print(f"German level: {topic_match['level']}")
    print(f"Unit number: {topic_match['unit']}")
    print()

    print("Matched sentences:")
    for sentence in sentences:
        print(f"- {sentence}")
    print()

    print("Description:")
    print(topic_data.get("description", "No description found."))
    print()

    print("Examples:")
    for example in topic_data.get("examples", []):
        de = example.get("de", "")
        en = example.get("en", "")
        print(f"- DE: {de}")
        print(f"  EN: {en}")
    print()

    print("Common mistakes:")
    for mistake in topic_data.get("common_mistakes", []):
        print(f"- {mistake}")
    print()

    print("English test:")
    for test_item in topic_data.get("english_test", []):
        print(f"- {test_item}")
    print()


def main():
    client = create_openai_client()

    user_input = input("User: ")

    is_german = handle_user_message(
        client=client,
        user_input=user_input,
        system_instruction=SYSTEM_MESSAGE_CHECK_LANGUAGE,
        model=OPENAI_MODEL,
        moderate_output=True,
    )

    if is_german == "Y":
        sentences = generate_assistant_response(
            client=client,
            user_input=user_input,
            system_instruction=SYSTEM_MESSAGE_TEXT_SPLITTER,
            model=OPENAI_MODEL,
        )

        identified_grammars = generate_assistant_response(
            client=client,
            user_input=sentences,
            system_instruction=SYSTEM_MESSAGE_GRAMMAR_IDENTIFIER,
            model=OPENAI_MODEL,
        )

        mapped_sentece_grammar = json.loads(identified_grammars)
        
        for topic_name, sentences in mapped_sentece_grammar.items():
            topic_match = find_topic(grammar, topic_name)

            if topic_match is None:
                print("=" * 80)
                print(f"Topic not found: {topic_name}")
                print()
                continue

            print_topic_info(
                topic_name=topic_name,
                sentences=sentences,
                topic_match=topic_match,
            )

if __name__ == "__main__":
    main()
