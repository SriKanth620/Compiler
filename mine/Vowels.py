vowels=0
consonants=0
file= open("lorem.txt", "r")
words= file.read().split()
vowel= ['a','e','i','o','u','A','E','I','O','U']
for x in words:
    # print(words)
    # print(x)
    for y in x:
        # print(y,"\n")
        if y in vowel:
            vowels+=1
        else:
            consonants+=1
print("No of Vowels: ", vowels)
print("No of Consonants: ", consonants)
    