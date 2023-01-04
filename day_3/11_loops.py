# while and For Loops
# While

x = 0
while (x<5):
    print(x)
    x = x+1

for x in range(5):
    print(x)
    x = x+1

# array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    # if (d == "Thu"):break     # looop stops
    if ((d=="Thu") or (d=="Fri")):continue # loop continues, skip these days
    print(d)


