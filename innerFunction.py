def func():
    print("First function.")
    def func1():
        print("Child 1")
    def func2():
        print("Child 2")

    func1()
    func2()

func()