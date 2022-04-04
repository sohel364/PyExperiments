class SingleTonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTonClass, cls).__new__(cls)
        return cls.instance

singleton = SingleTonClass()
new_singleton = SingleTonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Sample variable"
print(new_singleton.singl_variable)