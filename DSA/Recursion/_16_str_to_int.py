"""
convert string to integer
"""

def con_to_int(strr):
    if len(strr)==0:
        return 0

    return int(strr[0])*(10**(len(strr)-1))+con_to_int(strr[1:])

print(con_to_int('9876'))

