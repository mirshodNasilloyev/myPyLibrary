import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"Took  {t2} seconds")
    return wrapper


@tictoc
def do_this():
    #Simulating running code...
    time.sleep(1.3)


@tictoc
def do_that():
    #Simulating  running code...
    time.sleep(0.4)


do_this()
do_that()
print("Done")
