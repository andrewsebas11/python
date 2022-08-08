# def login(username, password):
#     if username == 'admin' and password == 'admin':
#         return 'successful login'
#     elif username != 'admin' and password == 'admin':
#         return 'incorrect username'
#     elif username == 'admin' and password != 'admin':
#         return 'incorrect password'
#     else:
#         return 'Both are wrong'
# u = input("enter the username")
# p = input("enter the password")
# u1 = login(u, p)
# print(u1)
def area(r=0):
    return 3.14*(r**2)


a = area(4)
b = area(3)
c = area()
print(a, b, c)
