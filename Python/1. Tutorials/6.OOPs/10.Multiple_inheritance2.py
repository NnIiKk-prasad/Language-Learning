# -----Diamond Shape Problem In Multiple Inheritance-----
class A:
    def met(self):
        print("Method of class A")


class B(A):
    def met(self):
        print("Method of class B")


class C(A):
    def met(self):
        print("Method of class C")


class D(B, C):
    # def met(self):
    #     print("Method of class D")
    pass


a = A()
b = B()
c = C()
d = D()

d.met()
