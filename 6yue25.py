class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("姓名:", self.name)
        print("年龄:", self.age)


class Student(Person):

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def study(self):
        print(self.name, "正在学习")


s1 = Student("张三", 18, 95)
s2 = Student("李四", 19, 88)

s1.introduce()
s1.study()

print(s1.get_score())

s1.set_score(100)

print(s1.get_score())
s2.introduce()
s2.study()
print(s2.get_score())