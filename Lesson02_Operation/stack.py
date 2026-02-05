def function__3():
    print("function__3 is started")
    print("function__3 is finished")

def function__2():
    print("function__2 is started")
    function__3()
    print("function__2 is finished")

def function__1():
    print("function__1 is started")
    function__2()
    print("function__1 is finished")


function__1()
