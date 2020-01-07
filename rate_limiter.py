from time import time
import threading
import http.server
import socketserver

# using token bucket algorithm

class Bucket():

    def __init__(self, capacity):
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
        # 1 request per 36secs = 100 requests per 1 hour (3600secs)
        threading.Timer(36.0, bucket.put_token).start()

    def get_token(self):
        return self._total

def call_method():
    res = bucket.use_token()
    if res == True:
        return {'Status': 200}
    else:
        return {'Status': 429, 'Message': 'Rate limit exceeded. Try again in 36 seconds'}

bucket = Bucket(100)
bucket.put_token()
