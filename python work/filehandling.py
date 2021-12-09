# f = open("mydemo.txt","w")
# f.write("this is first line\n")
# f.write("this is second line\n")
# f.close()

# f = open("mydemo.txt","r")
# print(f.read())

# f = open("mydemo.txt","a")
# f.write("this is third line\n")
# f.close()

# f = open("mydemo.txt","r")
# print(f.read())
#
# f = open("mydemo.txt","a")
# f.write("this is third line\n")
# f.close()
#
# f = open("mydemo.txt","r")
# print(f.read())
#
# f = open("mydemo.txt","r")
# for line in f:
#     print(line,end="")
# f.close()

# f = open("demo names.txt", "w")
# f.write(input("names")+"\n")
# f.write(input("birthdate")+"\n")
# f.close()
#
# f = open("demo names.txt","r")
# print(f.read())

# f = open("personal details.txt", "w")
# f.write("Name:"+input("enter your name = ")+"\n")
# f.write("Age:"+input("enter your age = ")+"\n")
# f.write(input("enter your birthdate = ")+"\n")
# f.write(input("enter your salary = ")+"\n")
# f.write(input("enter your blood group = ")+"\n")
# f.write(input("enter your company name = ")+"\n")
# f.write(input("enter your favorite colour = ")+"\n")
# f.write(input("enter your native city/village = ")+"\n")
# f.close()
#
# f = open("personal details.txt", "r")
# for line in f:
#     print(line, end="")
# print(f.read())
#
# name=input("enter your name =")
# print("hello",name,"it is your assistant")
#
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[::4])
# #run time polymor prism
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[0:4])

# employ id employ name employ contact employ department basic salary net salary
#
# f = open("employee details.txt", "w")
# f.write(("person inserting its detail = "+input("enter your employee id = ")+"\n"))
# f.write("employee id = "+input("enter employee id you want to search =")+"\n")
# f.write("employee name = "+input("enter the value of name = ")+"\n")
# f.write("employee contact = "+input("enter employee contact = ")+"\n")
# f.write("employee department = "+input("enter the value of employee department = ")+"\n")
# B=int(input("enter the value of B = "))
# f.write("the value of B = "+str(B) +"\n")
# ta=0.05*(B)
# da = 0.04*(ta+B)
# hra = 0.03*(ta+da+B)
# cca = 0.08*(ta+da+hra+B)
# pf = 0.1*(ta+da+hra+B)
# IT = 0.07*(ta+da+hra+B+cca-pf)
# NTS = (B+ta+da+hra+pf-cca-IT)
# f.write("the value of nts = "+str(NTS)+"\n")
# f.close()
#
# f = open("employee details.txt", "a")
# f.write("Thanks for visiting \n")
# f.close()
#
# f = open("employee details.txt" , "r")
# print(f.read())

# import os
# os.rename('employees details.txt','employee details.txt')
# os.remove('employee details.txt')
# os.mkdir('new')
# os.rmdir('new')

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