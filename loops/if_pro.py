# if True:
#     print("I will print")
# if False:
#     print("I will not print")
# if 2:
#     print("I will print")
# if 0:
#     print("I will not print")
# a=123
# if a:
#     print("I will work")
# if -17:
#     print("I will print")

m1 = int(input("Enter m1"))
m2 = int(input("enter m2"))
m3 = int(input("Enter m3"))
# total = m1+m2+m3
# print(total)
# if total >= 280:
#     grade = 'A'
# elif total < 280 and total >= 250:
#     grade = 'B'
# elif total < 250 and total >= 200:
#     grade = 'C'
# else:
#     grade = 'D'
# print(f"total of student = {total} and it's grade = {grade}")
if m1 < 35 or m2 < 35 or m3 < 35:
    print("no need to print")
    #print("Failed in all three subject")
    if m1 < 35 and m2 < 35:
        print('failed in m1 and m2')
    elif m1 < 35 and m3 < 35:
        print('failed in m1 and m3')
    elif m1 < 35 :
        print('failed in m1')
    elif m2<35 :
        print('failed in m2')
    else:
        print('failed in m3')
else:
    total = m1+m2+m3
    if total >= 150:
        grade = 'A+'
    elif total < 150 and total >= 140:
        grade = 'A'
    elif total < 140 and total >= 130:
        grade = 'B'
    elif total < 130 and total >= 120:
        grade = 'C'
    else:
        grade = 'D'
    print(f"the total is {total} and the grade is {grade}")





