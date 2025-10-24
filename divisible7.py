#calculate how many numbers are divisible by 7 from 1 to 100
count = 0
i = 1

while i <= 100:
    if i % 7 == 0:   # use modulus (%) to check divisibility
        count += 1
    i += 1

print("Count of numbers divisible by 7 from 1 to 100 is:", count)
