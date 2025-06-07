# quote_bank.py

quotes = {
    "happy": [
        "Happiness is a journey, not a destination.",
        "Smile, it's the key that fits the lock of everybody’s heart."
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "This too shall pass. Hang in there."
    ],
    "angry": [
        "For every minute you are angry, you lose 60 seconds of peace.",
        "Breathe. It's just a bad moment, not a bad life."
    ],
    "fear": [
        "Feel the fear and do it anyway.",
        "Courage doesn't always roar."
    ]
}

music_links = {
    "happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
    "sad": "https://www.youtube.com/watch?v=DWcJFNfaw9c",
    "angry": "https://www.youtube.com/watch?v=2Y6Nne8RvaA",
    "fear": "https://www.youtube.com/watch?v=MgzlfIE8f1g"
}

journal_prompts = {
    "happy": "What made you feel happy today?",
    "sad": "What is weighing on your heart today?",
    "angry": "What triggered your anger? How did you respond?",
    "fear": "What fear are you facing, and what’s one small step you could take?"
}

def get_quote(emotion):
    return quotes.get(emotion.lower(), ["Stay strong!"])[0]

def get_music(emotion):
    return music_links.get(emotion.lower(), "")

def get_prompt(emotion):
    return journal_prompts.get(emotion.lower(), "How are you feeling right now?")
