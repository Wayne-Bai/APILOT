import networkx as nx

class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Calling function with args:", args, "and kwargs:", kwargs)
        return self.func(*args, **kwargs)

@Decorator
def my_function():
    pass

my_function()
