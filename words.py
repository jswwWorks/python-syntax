def print_upper_words(words, letters):
    """Capitalizes & prints each word in a list of words."""

    for word in words:
        for letter in letters:
            if word.startswith(letter) or word.startswith(letter.capitalize()):
                print(word.upper())


print("print_upper_words printed",
    print_upper_words(
        [
            "hello",
            "hey",
            "goodbye",
            "yo",
            "yes",
            "enjoy"
        ],
        ["y", "g"]))