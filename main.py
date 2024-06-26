import requests
from googletrans import Translator


def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src="en", dest="ja")
    return translation.text


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


def main():
    while True:
        text_eng = input("--- type sentence ---\n").strip()

        if text_eng == "q":
            break
        if not text_eng:
            continue

        text_jp = translate_text(text_eng)

        result = create_anki_card(text_eng, text_jp)
        # if result.get("error") is None:
        #     print("success")
        # else:
        #     print("fail")


if __name__ == "__main__":
    main()
