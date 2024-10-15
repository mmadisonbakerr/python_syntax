def print_upper_words(words, *start):
    for word in words:
        if word.startswith(start):
            print(word.upper())



print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'], 'h', 'y')