
def group_words_by_length(words: list) -> dict:
    group = {}
    for word in words:
        group.setdefault(len(word), []).append(word)
    return group

words = ["apple","banana","kiwi","grape","melon","pear"]
print(group_words_by_length(words))