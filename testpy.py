import random

arr1="A look of such unqualified admiration overspread the young man's face that the last remnants of the ice-pack melted. For the first time since they had met Annette found herself positively liking this blackguardly floor-smiter."
arr1 = arr1.lower()
arr2="aaaa"
while (len(arr2) > 3):
    arr2= random.choice(arr1.split()) #can be reduced to ran.ch("a look of....".splt())
    print ('The Length of the chosen word is {} letters long'.format(len(arr2)))
    attempt = 1
    correct = 0
    temp = ("_" * len(arr2))
    while (True):
        print("Attempt #{}".format(attempt))
        ar=input()

        if (ar == arr2):
            print ("Congrtulations, you've guessed the correct word in {} attempts".format(attempt))
  

        for i in range(len(ar)):
            for j in range(len(arr2)):
                if(ar[i] == arr2[j]):
                    temp = temp[:j] + ar[i] + temp[j+1:]
                    correct = correct + 1
        print (temp)
        attempt += 1


