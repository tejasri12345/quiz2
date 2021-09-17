
set_values = set(map(int,input("Enter comma seperated values: ").split(',')))
print(set_values)
set2_values = set(map(int,input("Enter sub set: ").split(',')))
print(set2_values.issubset(set_values))