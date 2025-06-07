def add_objprint(cls):
    """
    Decorator to add a print method to a class.
    """
    def print_obj(self, *args, **kwargs):
        print(self)
        print(*args, **kwargs)
        return self
    cls.print_obj = print_obj
    return cls