#calculate how many numbers are divisible by both 6 and 7 between 1 to 200
count = 0
i = 1

while i <= 200:
    if i % 6 == 0 and i % 7 == 0:   # use modulus (%) to check divisibility
        count += 1
    i += 1

print("Count of numbers divisible by 6 and 7 from 1 to 200 is:", count)
