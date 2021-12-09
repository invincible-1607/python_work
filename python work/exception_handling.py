# try:
#     a=int(input("enter the value of a="))
#     b=int(input("enter the value of b="))
#     c=a/b
#     print("a%b=",c)
# except:
#     print("dividing by zero is not possible")
# else:
#     print("hi i m else statement")
# print("hello exception")

# try:
#     fileptr=open("menu.txt","r")
# except IOError:
#     print("file not found")
#     print("error")
# else:
#     print("the file opened successfully")
#     fileptr.close()

# try:
#     fileptr=open("file.txt","r")
#     try:
#         fileptr.write("hi i m good")
#     finally:
#         fileptr.close()
#         print("file closed")
# except:
#     print("error")