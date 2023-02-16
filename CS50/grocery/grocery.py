counts = dict()
a = True
while a==True:
    try:
        name = input().lower()
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] += 1

    except EOFError:
        a=False
counts2 = dict( sorted(counts.items(), key=lambda x: x[0].lower()) )
for i in counts2:
    print(counts2[i],i.upper())