
def tower_of_hanoi(n,a,b,c):
    if n==1:
        print(f"move {n}th disk from {a} to {c}")
        return
    tower_of_hanoi(n-1, a, c, b)
    print(f"move {n}th disk from {a} to {c}")  # for last disk
    tower_of_hanoi(n-1,b,a,c)


tower_of_hanoi(2,'a','b','c')
