import os
import requests
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def create_anki_card(front, back):
    url = "http://localhost:8765"
    card = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "IPLUSONE",
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
            }
        },
    }

    response = requests.post(url, json=card)
    return response.json()


def translate(text_en):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "translatethis into japanese\n\n" + text_en,
            }
        ],
        model="gpt-3.5-turbo",
    )
    text_jp = chat_completion.choices[0].message.content
    return text_jp


def main():
    while True:
        text_eng = input("--- type sentence ---\n").strip()

        if text_eng == "q":
            break
        if not text_eng:
            continue

        text_jp = translate(text_eng)
        print(text_jp)

        create_anki_card(text_eng, text_jp)


if __name__ == "__main__":
    main()
