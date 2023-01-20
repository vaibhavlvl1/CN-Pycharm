def print_words_with_k_freq(a, k ):
    words = a.split()

    d= {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    for w in d:
        if d[w] == k:
            print(w)


a = "This is a word string with many many word"
k = 2
print_words_with_k_freq(a,k)