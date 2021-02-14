
print("Please enter a word: ")
res = input()
count = 0
vowels = 0
consonents = 0

for i in res:                                    # for statement to count the number of characters in a word
    count = count + 1

for i in res:                                   # for statement compares all the letters to each of the vowels to see if they are vowels or not
    if((i == 'a' ) or (i == 'e' ) or (i == 'i' ) or(i == 'o' ) or (i == 'u' ) or (i == 'A' ) or (i == 'E' ) or (i == 'I' ) or(i == 'O' ) or (i == 'U' )):
         vowels = vowels + 1
    else:
        consonents = consonents + 1
   
print("Total number of letters in the word is:" + str(count))
print("Total number of vowels is: " + str(vowels))
print("Total number of consonents is: " + str(consonents))