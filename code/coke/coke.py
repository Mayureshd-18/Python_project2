amount = 50
while amount > 0 :
    print("Amount due: ",amount)
    coin = int(input("Insert coin: "))
    if coin in [25,10,5]:
        amount -= coin

change_owed = abs(amount)
print("Change owed:",change_owed)
