xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)


for i in xs:
    print ("The square of", i, "is", i * i)

total = 0
for i in xs:
    total = total+i

print(total)

product = 1
for i in xs:
    product = product * i
    print(product)