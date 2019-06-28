import first_example


def run_example(name,t):
    obj=first_example.example(name,t)
    obj.create_thread()
    obj.list_of_thread(4)


if __name__  == '__main__':
    run_example("thread",5)

