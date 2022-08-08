# year = int(input("enter the year"))
# if year % 4 == 0:
#     print("Leap year")
# else:
#     print("not a leap year")

m1 = int(input("enter m1"))
m2 = int(input("enter m2"))
m3 = int(input("enter m3"))
if m1 > 35:
    if m2 > 35:
        if m3 > 35:
            print("all pass")
        else:
            print("m3 fail")
    else:
        print("m2 fail")
else:
    print("m1 fail")
if m1 < 35 or m2 < 35 or m3 < 35:
    print("no need to print")
elif m1<35 and m2<35:
    print('failed in m1 and m2')
elif m1<35 and m3<35:
    print('failed in m1 and m3')
elif m1<35 and m2<35 and m3<35:
    print('failed in m1, m2 and m3')
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