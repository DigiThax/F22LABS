from random_words import RandomWords
import os

def ai_match(guess,word,st):
    """
        The function is used to add to the list of correct letters guessed by the AI
        I've also used it to print the AI stats to the user after every attempt
    """
    correct = ""
    for i in range (len(guess)):
        for j in range (len(word)):
            if(guess[i] == word[j]):
                correct = correct + guess[i]

    correct = list(set(correct))
    if(st == 0):
        print("AI got {} correct".format(len(correct)))

    return correct

def ffl(guess,word):
    """
        UDF to check if first letter of the AI's guess word matches with the first
        letter of the word to be guessed. Setting this up allowed me to modify the
        random_word(<arg>) argument so that it searches for words beginning with
        that particular letter, in essence it can be enabled or disabled to allow
        for Easy or Hard modes of difficulty
    """
    if(guess[0] == word[0]):
        return guess[0]

def chkwrd(word):
    """
        This function is used to ensure that no 3 letter word is used for the game.
        The AI may choose a 3 letter word but the game engine will not pick a 3
        letter word that needs to be guessed by the AI and Human
    """
    while(len(word) < 4):
        word = rw.random_word()
    return word

def match(str1,str2,temp):
    """
        Once the user enters his/her word, it gets passed here and the engine checks
        for all the letters that match. If any letter matches (irrespective of position)
        the 'temp' variable (which just holds '_' x the length of the word) is modified
        by replacing the '_' with the matching letter

        Lets say:
            word = 'python'
            user input = 'attempt'
            temp = '__t___'

        This way it strikes two birds with one stone, i.e:
        *Informs the player of any correct letter
        *Informs the player of the incorrect position of the right letter
    """
    correct = 0
    for i in range (len(str1)):
        for j in range(len(str2)):
            if(str1[i] == str2[j]):
                temp = temp[:j] + str1[i] + temp[j+1:]
                correct += 1
    print("You got {} correct letters in this attempt".format(correct))
    return temp

"""
    Over here the random word is generated and the user is notified of the length of the word
    """
os.system('cls')
rw = RandomWords()
word = rw.random_word()
word = chkwrd(word)
word = str(word)
print("The length of the word is {} letters long".format(len(word)))
attempt = 0
st = 0
fl = ai = None
correct = []
block = []
temp =("_" * len(word))
flag = 1
#fl = None
"""
    The exit conditions are:
        *If user guessed the correct word
        *If the user and AI used up all 10 attempts
    The exit condition does not stop the loop if the AI guessed the word first
    """
while(attempt < 10):
    """
        For the first attempt, the AI chooses the word Iouea which is a type of
        seaweed, it also conveniently uses all the vowels in the English Language
        """

    attempt += 1

    if(temp != word):
        print("Attempt #{}".format(attempt))
        score = attempt
        ch = input()
        #User input
        ch = "".join(set(ch))
        #Removes any repeating letters as this can affect the 'correct' count in match UDF
        temp = match(ch,word,temp)
        print(temp)
    if(attempt == 1):
        guess = 'iouea'
        correct = ai_match(guess,word,st)
        correct = list(set(correct))
        fl = ffl(guess,word)
    if(not ai and attempt != 1):
        """
            'ai' is just a variable that initially holds nothing, but gets assigned the
            value of 'attempt' to indicate the number of attempts used by the AI to guess
            the correct word.
            """
        guess = rw.random_word()
        guess = str(guess)
        while(flag == 1):
            if(len(set(correct) & (set(guess))) > 0):
                if(set([guess]).issubset(block) == True):   #This is used to avoid repeated guessed words, although the chance of a repeated word in 10 attempts is very small
                    block.extend([guess])
                    print("block = ")
                    print(block)
                    guess = rw.random_word(fl)
                    guess = str(guess)
                    flag = 0
                    print(guess)
                else:
                    flag = 0
            else:
                flag = 0

        flag = 1
        fl = ffl(guess,word)
        correct.extend(ai_match(guess,word,st))
        correct = list(set(correct))

        if(set(word)-set(correct) == set([])):
            ai = attempt
    if(temp == word):
        st = 1


os.system('cls')
if(ai and temp != word):
    print("1AI got the word in {} attempts\nToo bad,".format(ai))
    print ("The word was {}".format(word))

if(ai and temp == word):
    print("2AI got the word in {} attempts".format(ai))
    print("You got the correct word in {} attempts.".format(score))
    if(score < attempt):
        print("You won")
    else:
        print("AI won")
if(not ai and temp != word):
    print("AI could not solve in given attempts.")
    print ("The word was {}\nIts a draw".format(word))
