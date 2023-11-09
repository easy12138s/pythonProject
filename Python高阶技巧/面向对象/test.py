
class Student:

    # 构造方法-魔术方法
    def __init__(self, name, gender, nationality, native_place, age):
        # 此步骤即是赋值，也是变量定义
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.native_place = native_place
        print("Student类构造了一个对象")

    def say_hi(self):
        print(f"HI，我是{self.name}")

    def singing(self, msg):
        print(f"我是{self.name}, 我给大家带来一首-{msg}:纵使晴明无雨色，入云深处有人家")


stu_2 = Student("林俊杰", "男", "", "", "")
print(stu_2)



