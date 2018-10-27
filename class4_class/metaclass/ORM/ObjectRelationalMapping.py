#!usr\bin\python3
# ORM对象关系映射，Object Relational Mapping


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    # 打印实例时调用
    def __str__(self):
        # 调用返回字符串，返回“Field:XXX” ， XXX是传入的name名称
        return '<%s:%s:%s>' % (self.__class__.__name__, self.name, self.column_type)


class StringField(Field):

    def __init__(self, name):
        # 调用父类初始化方法
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super().__init__(name, 'bigint')


class ModelMetaclass(type):
    # type --> metaclass  类构造器生生成
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    # 模拟建表操作
    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


def main():
    u = User(id=12345, name='Batman', email='batman@nasa.org', password='iamback')
    u.save()


if __name__ == '__main__':
    main()
