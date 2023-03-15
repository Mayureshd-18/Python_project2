a = True
months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
while a==True:
    d = input("Date: ")
    try:
        m,d,y = d.split("/")
        m = int(m)
        d= int(d)
        y = int(y)
        if (m<=12 and d<=31):
            print(f"{y}-{m:02}-{d:02}")
            a=False
    except:
        try:
            m,d,y = d.split(" ")
            d= d[:-1]
            d= int(d)
            if  m in months:
                m = months[m]
                y = int(y)
                if (m<=12 and d<=31):
                    print(f"{y}-{m:02}-{d:02}")
                    a=False
        except:
            pass





