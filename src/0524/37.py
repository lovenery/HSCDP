import threading
def count(i):
    print ('這是一個數字 : ',i)
threads = []
for i in range(0,10):
    threads.append(threading.Thread(target=count, args=(i,)))
for t in threads:
    t.start()
