class Test:
    name = ""
    def __init__(self,n):
        self.name = n

    def print_log(self):
        print(self.name)
        print(self.__class__)


class People:
    name = ""
    age = 0
    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    def speack(self):
        print("我是 %s ,我 %d 岁了" % (self.name,self.age))

#单继承
class Student(People):
    grade = 0
    def __init__(self, n, a, g):
        People.__init__(self,n,a)
        self.grade = g
    
    def speack(self):
        print("我是 %s ,我 %d 岁了, 我在读 %d 年级" % (self.name,self.age,self.grade))

class Speaker:
    name = ""
    topic = ""
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    
    def speack(self):
        print("我是 %s ,我是一个演说家, 我演讲的主题是 %s" % (self.name,self.topic))

#多继承
class MoreSample(Speaker,People):
    grade = 0
    __width = 0 #私有属性外部无法直接使用
    __high__ = 0 #不是私有，后面不能加两个下横线
    def __init__(self, n, a, t, g,h,w):
        Speaker.__init__(self,n,t)
        People.__init__(self,n,a)
        self.grade = g
        self.__width = w
        self.__high__ = h
    
    def speack(self):
        # Speaker.speack(self)#调用父类方法1
        super(MoreSample,self).speack()#调用父类方法2
        print("我是 %s ,我 %d 岁了, 我在读 %d 年级" % (self.name,self.age,self.grade))

    def __get(self): # 私有方法
        print("这是一个私有方法")


test = Test("Test")
student = Student("小明",10,5)
moreSample = MoreSample("小明",10,"Python",4,172,10)
def main():
    test.print_log()
    student.speack()
    moreSample.speack()
    print(moreSample.__high__)

if __name__=='__main__':
    main()