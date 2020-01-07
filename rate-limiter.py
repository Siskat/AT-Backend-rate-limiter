from time import time
import threading
import http.server
import socketserver

# using token bucket algorithm

class Bucket():

    def __init__(self,capacity):
        self.timestamp = time()
        self._total = capacity
        self.capacity = capacity

    def use_token(self):
        if (self._total > 0):
            self._total -= 1
            return True
        return False
        
    def put_token(self):
        if (self._total < self.capacity):
            self._total += 1
            threading.Timer(36.0,self.put_token()).start()


    def get_token(self):
        return self._total

def callMethod():
    res = bucket.use_token()
    if res == True:
        print('Total call times left: ', bucket.get_token())
        return True
    else:
        print('Rate limit exceeded. Try again in 36 seconds')
        return False
    
bucket = Bucket(100)
bucket.put_token()

while(1):
    userInput = input("What do you want to do?")
    if userInput == "call":
        callMethod()

