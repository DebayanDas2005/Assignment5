x = [i*1 for i in range(11)]
del x[0]
print("Original list:",x)
r = x[:5]
print("Extracted first five elements:",r)
print("Extracted first five elements:",r[::-1])