def words_with_freq_k(arr,k):
    d={}
    for ele in arr:
        d[ele] = d.get(ele,0)+1


    for keys in d:
        if d[keys]==k:
            print(keys)


words_with_freq_k(['a','a','a','a','f','f','e','e','e','e','g','g','u','u','r','r','q','q','q','q'],2)