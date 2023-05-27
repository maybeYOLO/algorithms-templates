from operator import add


class myClass():
    def print1(*args):
        print(1, *args)

    def print2(*args):
        print(2, *args)


def parse(command, *args):
    getattr(myClass(), command)(*args)


# parse(*'print1 aaa bbb'.split())
# parse(*'print2 aa bb cc'.split())
# print(add(1, 2))

com, *var = 'print1 aaa bbb ccc ddd'.split()
print(com, var)
com, *var = 'print2'.split()
print(com, var)
