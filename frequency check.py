test_dict = {'apple': 5, 'banana': 2, 'orange': 5, 'grape': 1}
target = 5
count = 0
for value in test_dict.values():
    if value == target:
        count = count + 1
print("Frequency of", target, "is:", count)
