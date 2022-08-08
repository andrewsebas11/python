square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)
print({num: num*num for num in range(1, 11)})

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {}
for (item, value) in old_price.items():
    new_price[item] = value * dollar_to_pound
print(new_price)
print({item: value*dollar_to_pound for (item, value) in old_price.items()})

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {}
for (k, v) in original_dict.items():
   if v % 2 == 0:
       even_dict[k] = v
print(even_dict)
print({k: v for (k, v) in original_dict.items() if v % 2 == 0})

# dictionary = dict()
# for k1 in range(11, 16):
#   print({k2: k1*k2 for k2 in range(1, 6)})

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {}
for (k, v) in original_dict.items():
    if v % 2 != 0:
        if v < 40:
            new_dict[k] = v
print(new_dict)
print({k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40})

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {}
for (k, v) in original_dict.items():
    if v > 40:
        new_dict[k] = 'old'
    else:
        new_dict[k] = 'young'
print(new_dict)
print({k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()})


