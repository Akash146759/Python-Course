
class A:

  def __init__(self, a):

    self.a = a

  def __Akash__(self , other):

    if(self.a<other.a):

      return "obj1 is less than obj2"

    else:

      return "obj2 is less than obj1"

def __eq__(self, other):

  if (self.a == other.a):

    return "Not Equal"

ob1 = A(1)

ob2 = A(2)

print("Passed Values :", ob1.a, ob2.a)

print(ob1 < ob2)

obj3 = A(3)

obj4 = A(20)

print("Passed Values :", obj3.a, obj4.a)

print(obj3 == obj4)