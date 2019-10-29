from graphene import *

demo = {'a': 1, 'b': 2, 'c': {'d': 4, 'e': 5}}


class Student(ObjectType):
    id = ID()
    name = String()
    age = Int()


class MyQuery(ObjectType):

    test = String(name=String())

    student = Field(Student)

    def resolve_test(self, info, name):
        if demo.get('c', None) is None:
            return "hello, " + name
        else:
            return "hello, " + str(demo.get('c'))

    def resolve_student(self, info):
        return {'id': 1, 'name': 'zengmeng'}
