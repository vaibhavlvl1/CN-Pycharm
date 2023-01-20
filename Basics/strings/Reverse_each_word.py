sentence = "Welcome to Coding Ninjas"

words = sentence.split()

print(words)
output = ''
for word in words:
    output = output + word[::-1] + " "

print(output)