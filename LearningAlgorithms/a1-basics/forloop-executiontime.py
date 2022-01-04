import time

start_time = time.time()

counter = 101
total = 0

for value in range(counter):
    total += value

print("Total: ", total)

end_time = time.time()

print((end_time - start_time))
