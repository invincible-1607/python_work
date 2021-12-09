# class person:
#     a = int(input("enter the value of a :"))
#     if (a % 2):
#         print("value of a is odd")
#     else:
#         print("value of a is even")
#         def mod(self):
#             return self.a%2
# adi = person()
# print("the value of class=", adi.a % 2)
#
# class person:
#     a = int(input("enter the value of a :"))
#     b = int(input("enter the value of b :"))
#     if (a > b):
#         print("value of a big:")
#     else:
#         print("value of b big:")
#         def big(self):
#             return self.a > self.b
# adi = person()
# print("the value of class=", adi.a > adi.b)
#
# class person:
#     a = int(input("enter the value of a :"))
#     b = int(input("enter the value of b :"))
#     if (a < b):
#         print("value of a small:")
#     else:
#         print("value of b small:")
#         def small(self):
#             return self.a<self.b
# adi = person()
# print("th value of class=", adi.a<adi.b)
#
# class person:
#     a = int(input("enter the value of a :"))
#     b = int(input("enter the value of b :"))
#     c = int(input("enter the value of c :"))
#     if (a < b):
#         if (b < c):
#             print("c is big :")
#         else:
#             print("b is big :")
#             def big(self):
#                 return self.a>self.b
#     else:
#         if (a < c):
#             print("c is big :")
#         else:
#             print("a is big :")
#             def big(self):
#                 return self.b>self.c
# adi = person()
# print("th value of class=", adi.a > adi.b)
# print("th value of class=", adi.b > adi.c)
# print("th value of class=", adi.c > adi.a)
#
# class person:
#     a = int(input("enter the value of a :"))
#     b = int(input("enter the value of b :"))
#     c = int(input("enter the value of c :"))
#     if (a > b):
#         if (b > c):
#             print("c is small :")
#         else:
#             print("b is small :")
#             def small(self):
#                 return self.a<self.b
#     else:
#         if (a > c):
#             print("c is small :")
#         else:
#             print("a is small :")
#             def big(self):
#                 return self.b > self.c
# adi = person()
# print("th value of class=", adi.a < adi.b)
# print("th value of class=", adi.b < adi.c)
# print("th value of class=", adi.c < adi.a)
#
# class person:
#     c = int(input("enter the value of c :"))
#     s = int(input("enter the value of s :"))
#     if (s - c > 0):
#         print("it is profit:")
#     else:
#         print("it is loss :")
#         def loss(self):
#             return self.s - self.c > 0
# adi = person()
# print("the value of class=", adi.s-adi.c>0)

# class person:
#     a1 = int(input("enter the value of a1 :"))
#     a2 = int(input("enter the value of a2 :"))
#     a3 = int(input("enter the value of a3 :"))
#     if (a1 + a2 + a3 == 180):
#         print("it is a valid triangle.")
#     else:
#         print("it is not a valid tringle.")
#         def triangle(self):
#             return self.a1 + self.a2 + self.a3 == 180
# adi = person()
# print("the value of class=", adi.a1+adi.a2+adi.a3==180)

# class person:
#     l = float(input("enter the value of l :"))
#     b = float(input("enter the value of b :"))
#     a = l * b
#     p = 2 * (l + b)
#     if (a > p):
#         print("value of a is greater than p :")
#     else:
#         print("value of p is greater than a :")
#         def greater(self):
#             return self.a>self.p
# adi = person()
# print("the value of class=", adi.a>adi.p)

# class person:
#     a = int(input("enter the value of a:"))
#     b = int(input("enter the value of b:"))
#     a, b = b, a
#     print("value of a is :", a)
#     print("value of b is :", b)
#     def swap(self):
#         return self.a,self.b==self.b,self.a
# adi = person()
# print("the value of class=", adi.a,adi.b==adi.b,adi.a)

# class person:
#     a1 = int(input("enter the value of a1 :"))
#     a2 = int(input("enter the value of a2 :"))
#     if (a1 < a2):
#         print(" a2 is big :")
#     elif (a1 == a2):
#         print(" a1==a2 :")
#     else:
#         print("a1 is big :")
#         def greater(self):
#             return self.a1<self.a2
# adi = person()
# print("the value of class=",adi.a1<adi.a2)
# print("the value of class=",adi.a1==adi.a2)
# print("the value of class=",adi.a1>adi.a2)

# class person:
#     a1 = int(input("enter the value of a1 :"))
#     a2 = int(input("enter the value of a2 :"))
#     a3 = int(input("enter the value of a3 :"))
#     if (a1 + a2 > a3):
#         print("it is a valid triangle :")
#         if (a2 + a3 > a1):
#             print("it is a valid triangle :")
#             if (a1 + a3 > a2):
#                 print("it is a valid triangle :")
#     else:
#         print("it is not a triangle :")
#         def triangle(self):
#             return self.a1 + self.a2>self.a3
# adi = person()
# print("the value of class=", adi.a1+adi.a2>adi.a3)
# print("the value of class=", adi.a2+adi.a3>adi.a1)
# print("the value of class=", adi.a3+adi.a1>adi.a2)

# class person:
#     a1 = int(input("enter the value of a1 :"))
#     a2 = int(input("enter the value of a2 :"))
#     a3 = int(input("enter the value of a3 :"))
#     if (a1 == a2 == a3):
#         print("it is a equilateral triangle :")
#         if (a1 * a1 + a2 * a2 == a3 * a3):
#             print("it is a right angle triangle :")
#     elif (a1 != a2 == a3) or (a1 == a2 != a3) or (a3 == a1 != a2):
#         print("it is a isoceles triangle :")
#     elif (a1 * a1 + a2 * a2 == a3 * a3):
#         print("it is a right angle triangle :")
#     else:
#         print("it is a scalene triangle :")
#         def traingle(self):
#             return self.a1 + self.a2 > self.a3
# adi = person()
# print("the value of class=", adi.a1+adi.a2>adi.a3)

# x=int(input("the value of x="))
# y=3*(x)+1
# if (x%2)==0:
#     print("the value =",x/2)
# else:
#     print("the value =",y)
#     # solve till equation not completed
