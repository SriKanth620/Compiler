# reading a file
# count no. of sentences
# no. of words
# no of characters
file=open("lorem.txt", "r")
sentences= 0
words=0
characters=0
line=0
for x in file:
    # sentences+=1
    line=line+1
    words+=len(x.split())
    word=x.split()
    characters+= len(x.strip())
    for y in word:
        if(y.endswith('.') or y.endswith('!') or y.endswith('?')):
         sentences+=1
print("No of sentences: ",sentences)
print("No of words: ",words)
print("No of characters: ",characters)
print("No of lines: ",line)
    
