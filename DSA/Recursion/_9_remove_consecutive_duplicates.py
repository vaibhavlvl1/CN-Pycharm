"""
remove consecutive duplicates
"""

def remove_con_dup(word):
    if len(word)==1:
        return word[0]
    if word[0]==word[1]:
        return remove_con_dup(word[1:])
    return word[0]+remove_con_dup(word[1:])

print(remove_con_dup("vvaaiibbhhaavv"))
