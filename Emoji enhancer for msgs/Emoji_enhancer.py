emoji_map_func = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "☕",
    "music": "🎵",
    "food": "🍝",
}

message = input("Enter your message: ")

updated_words = []

for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map_func.get(cleaned, "")
    if emoji:
        updated_words.append(f"{word} {emoji} ")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print(f"\n Enhanced message: {updated_message}")
