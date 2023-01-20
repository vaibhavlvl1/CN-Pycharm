#sort any number list

li = [ 1,1,0,0,1,1,0,0,2,2,2,2,1,1,0]


for i in range (len(li)):

    for j in range (i+1,len(li)):

        if li[i]>li[j]:
            li[i],li[j] = li[j],li[i]
            print(li)

print(li)