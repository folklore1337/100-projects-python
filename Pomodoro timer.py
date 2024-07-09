import time

while True:
    s = 0 # Seconds
    m = 0 # Minutes
    h = 0 # Hours
    user_time = int(input('Enter number of seconds: '))
    for i in range(user_time):
        time.sleep(1)
        s += 1
        print('Seconds passed:', s)
        if(s % 60) == 0:
            m += 1
            print('Minutes passed:', m)
        if(s % 3600) == 0:
            h += 1
            print('Hours passed:', h)
    
    print('Time is over')