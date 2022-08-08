def hello():
    print('welcome to function')
def cubenumber(num1):
    return num1**3
def addition(num1, num2):
    return num1+num2
def largestofthethreenumber(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
hello()
a = cubenumber(5)
print(a)
b = addition(7, 19)
print(b)
c = largestofthethreenumber(14, 18, 9)
print(c)