import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(1, my_time + 1)): #we can also use range(my_time, 1, -1) to count in reverse
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours}:{minutes}:{seconds:02}")
    time.sleep(1)
print("Time's up!!")