
from random_words import RandomWords

def ai_match(guess,word):
    crt = ""
    for i in range (len(guess)):
        for j in range (len(word)):
            if(guess[i] == word[j]):
                crt = crt + guess[i]

    crt = list(set(crt))
#    print crt
    return crt

def ffl(guess,word):
    if(guess[0] == word[0]):
        return guess[0]

def chkwrd(word):
    while(len(word) < 4):
        word = rw.random_word()
    return word

rw = RandomWords()
word = rw.random_word()
word = chkwrd(word)
word = str(word)

print("The word is {}".format(word))
attempt = 1
correct = []
block = []

guess = 'mieuaow'
correct = ai_match(guess,word)
correct = list(set(correct))
print("Correct @ attempt 1 = {}".format(correct))
fl = ffl(guess,word)
block.append(guess)

while(set(word)-set(correct) != set([]) and attempt<10):
    attempt += 1
    fl = ffl(guess,word)
    guess = rw.random_word()
    guess = str(guess)
    block.append(guess)
    correct.extend(list(set(ai_match(guess,word))))

if(set(word)-set(correct) == set([])):
    print("AI got the word at the {} attempts".format(attempt))
else:
    print("AI could not solve in given attempts")
