import inflect
p = inflect.engine()
list = []
a = True
while a==True:
    try:
        s= input("Name: ")
        list.append(s)

    except EOFError:
        a = False
list2 = p.join(list)
print("Adieu, adieu, to",list2)