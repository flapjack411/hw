import time

start_time = time.time()

x = 100_000_000_000

sum = (x * (x-1)) / 2

#sum = 0
#for i in range(100_000_000):
    #sum = sum + i

print(sum)

print(time.time()-start_time)
