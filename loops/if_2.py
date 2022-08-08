age = int(input("enter the age"))
country = input("enter the country")
if age <= 18 and country == 'India':
    print('below 18 India')
elif age <= 18 and country != 'India':
    print('below 18 other country')
elif age > 18 and country == 'India':
    print('above 18 India')
else:
    print('above 18 other country')