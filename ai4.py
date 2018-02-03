#Run in python2
#I will provide comments to it tonight

from random_words import RandomWords

def ai_match(guess,word):
    crt = ""
    for i in range (len(guess)):
        for j in range (len(word)):
            if(guess[i] == word[j]):
                crt = crt + guess[i]

    crt = list(set(crt))
    print("AI got {} correct".format(len(crt)))

    return crt

def ffl(guess,word):
    if(guess[0] == word[0]):
        return guess[0]

def chkwrd(word):
    while(len(word) < 4):
        word = rw.random_word()
    return word

def match(str1,str2,temp):
    correct = 0
    for i in range (len(str1)):
        for j in range(len(str2)):
            if(str1[i] == str2[j]):
                temp = temp[:j] + str1[i] + temp[j+1:]
                correct += 1
    print("You got {} correct letters in this attempt".format(correct))
    return temp

rw = RandomWords()
word = rw.random_word()
word = chkwrd(word)
word = str(word)
print("The length of the word is {} letters long".format(len(word)))

attempt = 0
ai = None
correct = []
block = []
temp =("_" * len(word))
flag = 1
fl = None

while(temp != word and attempt < 10):
    attempt += 1

    print("Attempt #{}".format(attempt))
    ch = raw_input()

    ch = "".join(set(ch))
    temp = match(ch,word,temp)
    print(temp)

    if(attempt == 1):
        guess = 'iouea'
        correct = ai_match(guess,word)
        correct = list(set(correct))

        fl = ffl(guess,word)
    if(not ai and attempt != 1):
        guess = rw.random_word()
        guess = str(guess)
        while(flag == 1):
#            guess = rw.random_word()
#            guess = str(guess)
            if(len(set(correct) & (set(guess))) > 0):
                if(set([guess]).issubset(block) == True):
                    block.extend([guess])
                    print "block = "
                    print block
                    guess = rw.random_word(fl)
                    guess = str(guess)
                    flag = 0
                    print guess
                else:
                    flag = 0
            else:
                flag = 0

        flag = 1
        fl = ffl(guess,word)
        correct.extend(ai_match(guess,word))
        correct = list(set(correct))
        print correct
        if(set(word)-set(correct) == set([])):
            ai = attempt

if(ai):
    print("AI got the word in {} attempts".format(ai))
else:
    print("AI could not solve in given attempts")
if(ai == 10 or temp!=word):
    print ("the word was {}".format(word))
    print correct
