import random
a = True
b = True

while a ==True and b == True:
    try:
        n = int(input("Level: "))
        n2 = random.randint(1,n)
        g = int(input("Guess: "))
        if g<n2:
            print("Too small!")
        elif g>n2:
            print("Too large!")
        elif g==n2:
            print("Just right!")
            a=False
            b = False
    except:
        pass