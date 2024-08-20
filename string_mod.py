def multiline_text(text: str, length: int) -> str:
    sentence = ""

    char_count = 0
    for word in text.split(" "):
        # +1 for the extra spaces in front of text
        total_char_count = char_count + len(word) + 1

        if total_char_count >= length:
            sentence += "\n "
            char_count = 0

        sentence += f"{word} "
        char_count += len(word) + 1
    return sentence
