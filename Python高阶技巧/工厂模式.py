"""
    需要大量创建类实例的时候
    通过一个统一的入口进行调用创建实例，避免一个类发生变化就需要大规模改具体实现代码的情况
    解耦
"""


class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:

    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 'S':
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker = pf.get_person('w')
student = pf.get_person('S')
teacher = pf.get_person('T')
