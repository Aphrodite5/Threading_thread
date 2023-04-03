from threading import Thread

def display(n, msg):
    for i in range(n):
        print(msg)

t1 = Thread(target=display, kwargs={"n":4, "msg": "Hyello"})

t1.start()

for i in range(4):
    print("Hello world")