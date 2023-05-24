class myClass():
    def print1(*args):
        print(1, *args)

    def print2(*args):
        print(2, *args)


def parse(command, *args):
    getattr(myClass(), command)(*args)


parse(*'print1 aaa bbb'.split())
parse(*'print2 aa bb cc'.split())
