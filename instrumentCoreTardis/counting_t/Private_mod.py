class Foo(object):
    def __init__(self):
	self.__baz = 42
    def foo(self):
	print(self.__baz)

 
class Bar(Foo):
    def __init__(self):
	super(Bar, self).__init__()
	self.__baz = 21
    def bar(self):
	print (self.__baz)
