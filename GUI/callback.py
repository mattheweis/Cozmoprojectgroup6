def f(callback):
    callback()

def f1():
    print("callback")

def f2():
    print("Hello world")

def f3():
    print("f3")

f(f3)



