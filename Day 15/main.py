import time

time_start = time.strftime('%H:%M:%S')
print(time_start)

# time_start = '20:00:00'  # Simulating the time for testing purposes

if time_start >= '20:00:00':
    print('Good Night!')
elif time_start >= '12:00:00':
    print('Good Afternoon!')
elif time_start >= '6:00:00':
    print('Good morning!')
else:
    print('Good Night!')





