import threading
import time
class example:
    def __init__(self,name,t):
        self.name=name
        self.t=t
        self.list_th=[]
    def sleeper(self):
        print("Hello i am {}. I am going to sleep for {} seconds".format(self.name,self.t))
        time.sleep(self.t)
        print("Hello i have woken up")
    def create_thread(self):
        t=threading.Thread(target=self.sleeper)
        t.start()

    def list_of_thread(self,n):
        start=time.time()
        for i in range(n):
            t=threading.Thread(target=self.sleeper)
            self.list_th.append(t)
            t.start()
            print("{} has started".format(self.name))
            for x in range(len(self.list_th)):
                self.list_th[x].join()
        end=time.time()
        print("All {} threads took {} seconds".format(n,end-start))
print(__name__,"\n")

if(__name__=="__main__"):
    temp=example("main_thread",5)
    temp.create_thread()
    temp.list_of_thread(5)
