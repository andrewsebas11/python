for i in range(1,6):
    print('-----------------------')
    print(f" ------------- Student information -------------{i}")
    m1 = int(input("Enter m1"))
    m2 = int(input("enter m2"))
    m3 = int(input("Enter m3"))
    if m1 < 35 or m2 < 35 or m3 < 35:
        print("no need to print")
        if m1 < 35 and m2 < 35:
            print('failed in m1 and m2')
        elif m1 < 35 and m3 < 35:
            print('failed in m1 and m3')
        elif m1 < 35:
            print('failed in m1')
        elif m2 < 35:
            print('failed in m2')
        else:
            print('failed in m3')
    else:
        total = m1 + m2 + m3
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
