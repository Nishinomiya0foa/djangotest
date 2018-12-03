def count_words(text:str, words:set):
    num_times = 0
    a = []
    for i in range(0, len(words)):
        if words[i] in text.lower():
            num_times += 1
            a.append(words[i])
    return num_times

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(count_words("How aresjfhdskfhskd you?",["how","are","you","hello"]))