"""
 Pair Star
Send Feedback
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :

String S

Output format :

Modified string

Constraints :

0 <= |S| <= 1000
where |S| represents length of string S.

Sample Input 1 :

hello

Sample Output 1:

hel*lo

Sample Input 2 :

aaaa

Sample Output 2 :

a*a*a*a


"""

def pair_star(strr):
    if len(strr)==1:
        return strr

    if strr[0]==strr[1]:
        return strr[0]+"*"+pair_star(strr[1:])
    else:
        return strr[0]+pair_star(strr[1:])

print(pair_star("aaaaabaaabbbbab"))