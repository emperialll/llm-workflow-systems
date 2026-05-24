import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

GRAMMAR_FILE_NAME = "German-Grammatik.json"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GRAMMAR_FILE_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), GRAMMAR_FILE_NAME)

def load_grammar():
    with open(GRAMMAR_FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_grammar_topics(grammar: dict) -> list:
    grammar_topics = []
    for levels in grammar.values():
        for topics in levels.values():
            for topic in topics:
                grammar_topics.append(topic["topic"])
    return grammar_topics

grammar = load_grammar()
grammar_topics = get_grammar_topics(grammar)

delimiter = "####"

SYSTEM_MESSAGE_CHECK_LANGUAGE = f"""
Users send you German sentences or texts. Your task is to check and see if 
the user's text is in german language.

When given a user message delimited by {delimiter}, respond with only one character:
Y if the message is mainly German.
N otherwise.
"""

SYSTEM_MESSAGE_TEXT_SPLITTER = f"""
Users send you German sentences or texts delimited by {delimiter}.
Your task is to check the text and split it to smaller meaningful sentences.
e.g. user text: "Ich wohne in München und arbeite als Softwareentwickler" can be splitted to:
1. "Ich wohne in München"
2. "Ich arbeite als Softwareentwickler"

strict rule: Never split the compund sentences with main clause and dependent clause.
e.g. Ich kann nicht kommen, weil ich keine Zeit habe.

Final Output Format: your response must be a list of smaller sentences.
e.g. ["Ich wohne in München", "Ich arbeite als Softwareentwickler"]
"""

SYSTEM_MESSAGE_GRAMMAR_IDENTIFIER = f"""
You are an expert German language teacher and grammarian.

The user will send you a list of German sentences delimited by {delimiter}. 
Your task is to identify which grammar topics from the **Grammar Bank** are present in these sentences.

Grammar Bank:
{grammar_topics}

### Instructions:
- Only use grammar topics that exist in the Grammar Bank above.
- A sentence can belong to multiple grammar topics.
- Be precise and conservative — only assign a topic if the sentence clearly demonstrates it.
- If a sentence does not clearly demonstrate any grammar topic from the Bank, do not include it.

### Output Format:
Return your analysis as a valid JSON object (dictionary) with the following structure:

{{
  "Grammar Topic Name 1": ["sentence one", "sentence three"],
  "Grammar Topic Name 2": ["sentence two", "sentence four"],
  "Grammar Topic Name 3": ["sentence one"],
  ...
}}

### Important Rules:
- Keys must exactly match the topic names from the Grammar Bank.
- Keys must be unique.
- Use proper JSON formatting (double quotes, no trailing commas).
- If no grammar topics are found, return an empty object: {{}}
- Do not add any explanations, introductions, or extra text outside the JSON.
"""
