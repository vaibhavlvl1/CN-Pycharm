s = input()

freq = [0]*256

for ele in s:
    freq[ord(ele)] += 1

max = 0

for ele in s:
    if max< freq[ord(ele)]:
        max = freq[ord(ele)]

        print(ele)