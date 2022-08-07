lst=[4,5,2,9]

def squares(lst):
    return lst**2

data=list(map(squares,lst))
print(data)