def get_num_words(words):
    return len(words.split())


def freq_of_each_word(words):
    words = words.split()
    freq_dict = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict


def pretty_print(words, filepath):
    word_dict = freq_of_each_word(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(words)} total words")
    print("--------- Character Count -------")
    list_of_word_dict = [(k, v) for k, v in word_dict.items()]
    list_of_word_dict.sort(key=lambda x: x[1], reverse=True)
    for k, v in list_of_word_dict:
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")
