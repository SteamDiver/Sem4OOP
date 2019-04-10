#def filter(lst):
#    return list(i for i in lst if i%2 == 0)

a = [1,2, 3, 4, 5, 6]
print(tuple(filter(lambda x: x%2==0, a)))
