primes = [2,3,5,7]
print("'for prime in primes:' prints: ")
for prime in primes:
    print("'prime' value is: ", prime)

print("'for x in range(5):'")
for x in range(5):
    print("x = ", x)

print("'for x in range(3,6):'")
for x in range(3,6):
    print("x = ", x)

print("'for x in range(3,8,2):' where (start, end, step)")
for x in range(3,8,2):
    print("x = ", x)

count = 0
print("'while count < 5:\
    print(\"count = \",count)\
    count += 1'")
while count < 5:
    print("count = ",count)
    count += 1

print("'count = 0\
while True:\
    print(\"count =\", count)\
    count += 1\
    if count >= 5:\
        break'")
count = 0
while True:
    print("count =", count)
    count += 1
    if count >= 5:
        break

print("'count=0 \
while(count<5):\
    print(count)\
    count +=1\
else:\
    print(\"count value reached \", count)'")
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached ", count)

print("'for i in range(1, 10):\
    if(i%5==0):\
        break\
    print(i)\
else:\
    print(\"Never Printed\")'")
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("Never Printed")

print("exercise: Loop though print evens in order don't print anything afte 237")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if ((number % 2) == 0):
        print(number)
    else:
        continue
