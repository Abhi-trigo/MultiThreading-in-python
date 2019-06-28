import threading
import time
total=4
def creator_1():
    global total
    for i in range(10):
        print("Incerease total in creator_1 \n")
        time.sleep(2)
        total=+1
        print("added item in 1\n")

def creator_2():
    global total
    for i in range(7):
        print("Increase total in creator_2 \n")
        time.sleep(1)
        total=+1
        print("added item in 2 \n")
    
def limiter():
    global total
    while True:
        if(total>5):
            print("Overloaded\n")
            total=total-3
            print("3 has been Subtracted \n")
        else:
            time.sleep(1)
            print('Waiting \n')


c1=threading.Thread(target=creator_1,args=())
c2=threading.Thread(target=creator_2,args=())
limit=threading.Thread(target=limiter,args=(),daemon=True)
print(limit.isDaemon())
c1.start()
c2.start()
limit.start()
c1.join()
c2.join()
limit.join()
print("The ending value of total is ", total)
