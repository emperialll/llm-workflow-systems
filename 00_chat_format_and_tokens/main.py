from llm_utils import get_completion, get_completion_from_messages, get_completion_and_token_count


# LLM Basics and Chat Format

## Key ideas
# - LLMs generate text by predicting tokens, not words.
# - Instruction-tuned LLMs are optimized to follow user instructions.
# - Chat models use structured messages: system, user, and assistant.
# - The system message controls global behavior and constraints.
# - Temperature controls randomness.
# - Token usage affects cost, latency, and context limits.
# - API keys should be loaded from environment variables, not hardcoded.
# - Prompting enables fast development for text-based AI applications.


def messages_constructor(sys_msg: str, user_msg: str) -> list[dict]:
    return [  
        {'role':'system', 
        'content': f'"""{sys_msg}"""'},
        {'role':'user',
        'content': f'"""{user_msg}"""'}
    ]

def main():
    sys_message = input("Enter the system prompt: ")
    user_message = input("Enter the user prompt: ")
    messages = messages_constructor(sys_message, user_message)
    response = get_completion_from_messages(messages, temperature=1)
    print(response)


if __name__ == "__main__":
    main()
