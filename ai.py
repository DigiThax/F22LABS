from random_words import RandomWords

#UDF that replaces '_' with the correct letter. This gives the user the required
#feedback: (i)If the user used the correct letter (ii)Position of that letter
def match(str1,str2,temp):
    correct = 0
    for i in range (len(str1)):
        for j in range(len(str2)):
            if(str1[i] == str2[j]):
                temp = temp[:j] + str1[i] + temp[j+1:]
                correct += 1
    print("You've got {} correct letter(s) in this attempt".format(correct))
    return temp

def ai_match(guess,word):
    crt = []
    for i in range (len(guess)):
        for j in range (len(word)):
            if(guess[i] == word[j]):
                crt.append(word[j])
    return crt

def isthere(crt,guess):
    correct = 0
    guess = "".join(set(guess))
    for i in range(len(crt)):
        for j in range(len(guess)):
            if (crt[i] == guess[j]):
                correct += 1
    if (correct == len(crt)):
        return 1
    else:
        return 0

rw = RandomWords()
word = rw.random_word()
temp =("_" * len(word))
attempt = 0
correct = []
block = []
print("The length of the word is {} letters long".format(len(word)))

while(temp != word):
    attempt += 1
    print("Attempt #{}".format(attempt))
    ch = input()
    ch = "".join(set(ch))
    temp = match(ch,word,temp)
    print(temp)

    if(attempt == 1):
        guess = 'meaiouw'
        temp2 = ai_match(guess,word)
        temp2 = "".join(set(temp2))
        correct.append(temp2)
        block.append(guess)
        guess = 'a'
    else:
        while(len(guess) != len(word) and guess not in block):  #condition check to see if, previous matching
                                                                #letters exist in the new word, word is of same
                                                                #length, word has not been already used
            #and isthere(correct,guess) == 1 and guess not in block): #proper val not obtained atm

            temp2 = "".join(set(temp2))
            guess = rw.random_word()
            block.append(guess)
        correct.append(temp2)
        block.append(guess)
    print("AI's turn:")
    print(guess)

print("Congratulations, you have correctly guessed the word in {} attempts".format(attempt))
