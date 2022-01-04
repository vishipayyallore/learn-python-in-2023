import time

start_time = time.time()

number = 101
total = 0

while number > 0:
    total += number
    number -= 1

print("Total: ", total)

end_time = time.time()

print((end_time - start_time))
