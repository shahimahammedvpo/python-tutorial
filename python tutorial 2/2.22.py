def remove_words(s, words_to_remove):
    for word in words_to_remove:
        s = s.replace(word, '')
    return s

s = input("Enter a string: ")
words_to_remove = input("Enter words to remove (separated by commas): ").split(',')

result = remove_words(s, [word.strip() for word in words_to_remove])
print("Modified string:", result)