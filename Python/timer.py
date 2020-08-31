import time

def timer(n):
    if n == 0:
        return 0
    else:
        print (n)
        time.sleep(1)
        return timer(n-1)


print (timer(4))
