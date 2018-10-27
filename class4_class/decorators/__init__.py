from functools import wraps
# 函数被装饰器装饰后，原函数的一些信息会改变。用@wraps修饰装饰器可以改变这一问题。


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        @wraps(self._func)
        def _call():
            print('class decorator runing')
            res = self._func(*args, **kwargs)
            print('class decorator ending')
            return res
        return _call()


def foo1(func):
    print('aaa')
    @wraps(func)
    def call(*args, **kwargs):
        print('class decorator runing')
        res = func(*args, **kwargs)
        print('class decorator ending')
        return res
    return call


#@Foo
@foo1
def bar(name):
    print('bar', name)
    return 123456


#print(bar('aaa'))
#print(bar.__name__)
