# employ id employ name employ contact employ department basic salary net salary
#
# f = open("employee details.txt", "w")
# f.write("employee id="+input("enter your employee id =")+"\n")
# f.write("employee name="+input("enter the value of name=")+"\n")
# f.write("employee contact="+input("enter employee contact=")+"\n")
# f.write("employee department="+input("enter the value of employee department=")+"\n")
# B=int(input("enter the value of B="))
# f.write("the value of B="+str(B))
# ta=0.05*(B)
# da = 0.04*(ta+B)
# hra = 0.03*(ta+da+B)
# cca = 0.08*(ta+da+hra+B)
# pf = 0.1*(ta+da+hra+B)
# IT = 0.07*(ta+da+hra+B+cca-pf)
# NTS = (B+ta+da+hra+pf-cca-IT)
# f.write("the value of nts="+str(NTS))
# f.close()
#
# f = open("employee details.txt", "r")
# print(f.read())

# f = open("power.txt", "w")
# x=int(input("enter the value of x="))
# f.write("the value of x="+str(x)+"\n")
# y=int(input("enter the value of y="))
# f.write("the value of y="+str(y)+"\n")
# z=x**y
# f.write("the value of z="+str(z)+"\n")
# f.close()

# f = open("power.txt", "r")
# print(f.read())

# f = open("simple interest.txt", "w")
# p=float(input("enter the value of p="))
# f.write("the value of p="+str(p)+"\n")
# r=float(input("enter the value of r="))
# f.write("the value of r="+str(r)+"\n")
# t=float(input("enter the value of t="))
# f.write("the value of t="+str(t)+"\n")
# si=p*r*t/100
# f.write("the value of si="+str(si)+"\n")
# f.close()

# f = open("simple interest.txt", "r")
# print(f.read())

# f = open("simple interest.txt", "w")
# p=float(input("enter the value of p="))
# f.write("the value of p="+str(p)+"\n")
# r=float(input("enter the value of r="))
# f.write("the value of r="+str(r)+"\n")
# t=float(input("enter the value of t="))
# f.write("the value of t="+str(t)+"\n")
# n=float(input("enter the value of n="))
# f.write("the value of n="+str(n)+"\n")
# ci = p*((1+(r/(100.0*n)))**(n*t))
# f.write("the value of si="+str(ci)+"\n")
# f.close()
#
# f = open("simple interest.txt", "r")
# print(f.read())

# f = open("profit or loss.txt", "w")
# sp = float(input("enter the value of sp="))
# f.write("the value of sp=" + str(sp)+"\n")
# cp = float(input("enter the value of cp="))
# f.write("the value of cp=" + str(cp)+"\n")
# profit = sp - cp
# loss = cp - sp
# if (cp < sp):
#     f.write("the value of profit="+str(profit)+"\n")
#     f.write("you made a profit of "+str(profit)+"\n")
# else:
#     f.write("the value of loss="+str(loss)+"\n")
#     f.write("you made a loss of "+str(loss)+"\n")
# f.close()
#
# f = open("profit or loss.txt", "r")
# print(f.read())

# f = open("p or a.txt", "w")
# l = float(input("enter the value of l="))
# f.write("the value of l=" + str(l)+"\n")
# b = float(input("enter the value of b="))
# f.write("the value of b=" + str(b)+"\n")
# p=2*(l+b)
# f.write("the value of p="+str(p)+"\n")
# a=l*b
# f.write("the value of a="+str(a)+"\n")
# if(p>a):
#     f.write("the value of p is greater than a"+str(p>a)+"\n")
# else:
#     f.write("the value of a is greater than p"+str(a>p)+"\n")
# f.close()
#
# f = open("p or a.txt", "r")
# print(f.read())

# f = open("sides of triangle.txt", "w")
# a = int(input("enter the value of a:"))
# f.write("the value of a="+str(a)+"\n")
# b = int(input("enter the value of b:"))
# f.write("the value of b="+str(b)+"\n")
# c = int(input("enter the value of c:"))
# f.write("the value of c="+str(c)+"\n")
# if ((a + b + c == 180) and a != 0 and b != 0 and c != 0):
#      f.write("the triangle is valid")
# else:
#     f.write("the triangle is invalid")
# f.close()
#
# f = open("sides of triangle.txt", "r")
# print(f.read())

# f = open("average.txt", "w")
# num = int(input("enter the numbers:"))
# f.write("the value of num=" + str(num) + "\n")
# total_sum = 0
# for n in range(num):
#     n = float(input("Enter the value of n:"))
#     total_sum += n  # total_sum = total_sum + n
# avg = total_sum / num
# f.write("Average of " + str(num) + " numbers is=" + str(avg)+"\n")
# f.close()
#
# f = open("average.txt", "r")
# print(f.read())
#
# f = open("lucas.txt", "w")
# a = 2
# f.write("the value of a="+str(a)+"\n")
# b = 1
# f.write("the value of b="+str(b)+"\n")
# n = int(input("enter the value of n:"))
# f.write("the value of n="+str(n)+"\n")
# if (n==0):
#     f.write("the value="+str(a)+"\n")
# for i in range(1, n + 1):
#     c = a + b
#     a = b
#     b = c
#     f.write("the lucas value="+str(a)+"\n")
# f.close()
#
# f = open("lucas.txt", "r")
# print(f.read())

# f = open("lucas1.txt", "w")
# a = 0
# f.write("the value of a="+str(a)+"\n")
# b = 1
# f.write("the value of b="+str(b)+"\n")
# n = int(input("enter the value of n:"))
# f.write("the value of n="+str(n)+"\n")
# if (n==0):
#     f.write("the value="+str(a)+"\n")
# for i in range(2, n + 1):
#     c = a + b
#     a = b
#     b = c
#     f.write("the lucas value="+str(a)+"\n")
# f.close()
#
# f = open("lucas1.txt", "r")
# print(f.read())

# f = open("prime.txt", "w")
# n=int(input("Enter The value of n"))
# f.write("the value of n="+str(n)+"\n")
# if (n % (n/2)+1 == 0)or(n % 2 == 0):
#     f.write(str(n)+"is not a prime number"+"\n")
# else:
#     f.write(str(n)+"is a prime number"+"\n")
# f.close()
#
# f = open("prime.txt", "r")
# print(f.read())

# f = open("palindrome.txt", "w")
# n=int(input("Enter number:"))
# f.write("the value of n="+str(n)+"\n")
# t=n
# f.write("the value of t="+str(n)+"\n")
# r=0
# f.write("the value of r="+str(0)+"\n")
# while(n>0):
#     d=n%10
#     r=r*10+d
#     n=n//10
# if(t==r):
#     f.write("The number is a palindrome!")
# else:
#     f.write("The number isn't a palindrome!")
# f.close()
#
# f = open("palindrome.txt", "r")
# print(f.read())

# f = open("menu.txt", "w")
# TN = int(input("Enter your TN="))
# if (TN>25):
#     print("it is invalid")
# print("Select 1 for bread")
# print("Select 2 for starter")
# print("Select 3 for Shahi Sabji")
# print("Select 4 for Colddrinks")
# print("Select 5 for Salad")
# f.write("TN="+str(TN)+"\n")
# n= int(input("Enter value in n\n"))
# f.write("n="+str(n)+"\n")
# for n in range(n,6):
#     if (n==1):
#         print("Select 1 for normal_bread= 10,\nSelect 2 for butter_bread= 20,\nSelect 3 for khamiri bread=30,\n"
#               "select 4 for garlic bread= 40, \n")
#         bread = int(input("the bread you have chosen=:\n"))
#         f.write("bread chosen="+str(bread)+"\n")
#         if(bread==1):
#             bread = 10
#             f.write("10RS")
#         elif(bread==2):
#             roties = 20
#             f.write("20RS")
#         elif(bread==3):
#             bread = 30
#             f.write("30rs")
#         else:
#             bread = 40
#             f.write("40rs")
#     for n in range(n,6):
#         if(n==2):
#             print("select 1 for panneer tikka=100, \nselect 2 for malai paneer=140, \nselect 3 for soya chapp=110")
#             starter = int(input("the starter chosen="))
#             if(starter==1):
#                 starter = 120
#                 f.write("starter="+str(120))
#             elif(starter==2):
#                 starter = 140
#                 f.write("starter="+str(140))
#             else:
#                 starter = 110
#                 f.write("starter="+str(110))
#     for n in range(n,6):
#         if (n==3):
#             print("select 1 for paneer tikka butter masala=210, \nselect 2 for paneer bhurji=230, \nselect 3 for mix veg=180, \n"
#               "select 4 for tawa chapp=190, \n")
#             shahi_sabji = int(input("shahi_sabji you have chosen="))
#             if(shahi_sabji==1):
#                shahi_sabji = 210
#                f.write("shahi_sabji="+str(210))
#             elif(shahi_sabji==2):
#                shahi_sabji = 230
#                f.write("shahi_sabji="+str(230))
#             elif(shahi_sabji==3):
#                 shahi_sabji = 180
#                 f.write("shahi_sabji="+str(180))
#             else:
#                 shahi_sabji = 190
#                 f.write("shahi_sabji="+str(190))
#     for n in range(n,6):
#         if(n==4):
#             print("select 1 for coca_cola(200m), \nselect 2 for thumps_up(200ml), \nselect 3 for frooti(175ml), \nselect 4 for chhas(300ml)")
#             colddrinks=int(input("the drink you have chosen="))
#             if(n==1):
#                 colddrink = 30
#                 f.write("coca_cola="+str(30))
#             elif(n==2):
#                 colddrink = 30
#                 f.write("thumps_up="+str(30))
#             elif(n==3):
#                 colddrink = 30
#                 f.write("frooti="+str(30))
#             else:
#                 colddrink = 35
#                 f.write("chhas="+str(35))
#     for n in  range(n,6):
#         if(n==5):
#             print("selct 1 for vegetable salad, \nselect 2 for humus salad, \nselect 3 for colslo salad, \n")
#             salad=int(input("the salad you have chosen="))

