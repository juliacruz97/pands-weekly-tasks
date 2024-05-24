file = open ("romeo_and_juliet.txt","r")
nletter=0
content = file.read()
for letter in content:
    if letter == "b" or "B":
        nletter = nletter + 1
print('In romeo_and_juliet there are {} letters b and B '.format(nletter))
