#print(3%0)

a = 5
b = 6
c = a
a = b
b = c

print(a)
print(b)

factoral = int(input("Putt in factoral nummer: "))
factoralSum = 1

while(factoral > 0):
    factoralSum = factoralSum * factoral
    factoral = factoral - 1

print(factoralSum)


