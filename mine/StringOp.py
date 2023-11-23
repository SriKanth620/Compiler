str= "Lorem Ipsum is simply duMmy text"
s= "SRIKANTH U"
def length(str):
 length=0
 for x in str:
    length+=1
 return length
def lower(str):
    result=""
    for char in str:
        if 'A'<=char<='Z':
            result+= chr(ord(char) +32)
        else:
            result+= char
    return result
def upper(str):
    result=""
    for char in str:
        if 'a'<=char<='z':
            result+= chr(ord(char) -32)
        else:
            result+= char
    return result
def capitalize(str):
    result=""
    for char in str:
        if 'A'<= char<='Z':
            result+= chr(ord(char)+32)
        else:
            result+= char
    firstchar= result[0]
    firstchar= chr(ord(firstchar)-32)
    result= firstchar + result[1:]
    return result
def count(str, target):
    count=0
    lengthstr=0
    lengthtarget=0
    for x in str:
        lengthstr+=1
    for x in target:
        lengthtarget+=1
    for y in range(lengthstr):
        if str[y:y+lengthtarget]== target:
            count+=1
    return count
def title(str):
    result=""
    for char in str:
        if 'A'<= char <='Z':
            result+= chr(ord(char)+32)
        else:
            result+=char
    words= result.split()
    str=""
    for word in words:
        result= chr(ord(word[0])-32) + word[1:]
      
        str+= result + " "
    return str
def string_concat(str1, str2):
    result = ""
    for char in str1:
        result += char
    for char in str2:
        result += char
    return result

def string_reverse(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
def is_palindrome(s):
    return s == string_reverse(s)
def replace_char(s, old_char, new_char):
    result = ""
    for char in s:
        if char == old_char:
            result += new_char
        else:
            result += char
    return result
print("Original str: ",str)
print("length of str: ",length(str))
print("Lower of str: ",lower(str))
print("Upper of str: ",upper(str))
print("Capitalize of str: ",capitalize(str))
print("Occurance of \"i\": ",count(str,"i"))
print("Title of str: ",title(str))
print("Concatenation:", string_concat("Hello", "World"))
print("Reverse:", string_reverse(str))
print("Is Palindrome:", is_palindrome("madam"))
print("Replace Character:", replace_char(s, 'S', 'R'))