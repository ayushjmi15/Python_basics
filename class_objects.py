class Human:
    def introduction(self,n,o) :
        self.name=n
        self.occupation = o


class ravi(Human):
    def __init__(self):
        print ("i am ravi from IITH")
        self.course= "Btech"
        self.year=3
        print(self.course,self.year)

    def branch(self):
        self.introduction()
        Human.introduction()
        print("i am topper of my branch")

class kishore:
    def __init__(self):
        print ("i am kishore from jamia")
        self.course= "Mtech"
        self.year=2

    def branch(self):
        self.introduction()
        print("i am not a topper of my branch")


x= ravi()
x.introduction("ravi sharma", "tennis")
x.branch