#!usr\bin\python3
# 使用函数生成class


def test(self, name='world'):
    print('hello', name, self)


def fn(class_name, basic_class, attrs):
    hello = type(class_name, (basic_class,), attrs)
    return hello


def main():
    aa = fn('la', object, dict(say=test))
    aa1 = aa()
    aa1.say()


if __name__ == '__main__':
    main()
