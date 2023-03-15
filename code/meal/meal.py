t = input("What time is it?: ")
h, m = t.split(":")
h = int(h)
m = int(m)
m2 = m/60
t2 = round(h+m2,2)
if 7.00<=t2<=8.00:
    print("breakfast time")
elif 12.00<=t2<=13.00:
    print("lunch time")
elif 18.00<=t2<=19.00:
    print("dinner time")
