cust_2020 = {'a', 'b', 'c', 'd'}
cust_2021 = {'a', 'c', 'e', 'd', 'f'}
cust_2022 = {'a', 'c', 'e', 'f', 'b', 'z'}
cust_1 = cust_2020 | cust_2021 | cust_2022
print(cust_1)
cust_2 = cust_2020 - cust_2021
print(cust_2)
cust_3 = cust_2020 | cust_2021
print(cust_3)
cust_4 = cust_2022 - cust_3
print(cust_4)

#set() vs {}
s = set('besant')
s1 = {'besant'}
print(s)
print(type(s))
print(s1)
print(type(s1))