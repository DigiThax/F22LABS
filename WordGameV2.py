#Note: Inorder to use the random word generator function, you'll need the official RandomWords package
#pip install RandomWords

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
    print("You got {} correct letters in this attempt".format(correct))
    return temp


rw = RandomWords()
word = rw.random_word()
temp =("_" * len(word))
attempt = 0
print("The length of the word is {} letters long".format(len(word)))

while(temp != word):
    attempt += 1
    print("Attempt #{}".format(attempt))
    ch = input()
    #The line below removes repeating letters from the user's input
    #This way, 'count' in the match UDF does not increment more than once 
    ch = "".join(set(ch))
    temp = match(ch,word,temp)
    print(temp)

print("Congratulations, you have correctly guessed the word in {} attempts".format(attempt))
