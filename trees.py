tree1="OAK"
tree2="Larch"

if tree1==tree2:
    print("the Trees are the same")
else:
    print("the Trees are not the same")

def minmax(items):
    return min(items), max(items)

print(minmax((83, 33, 84, 32, 1, 4, 86)))


(x, (y, (z)))=(1, (2, (3)))
print (x, y)
x, y = y, x
print(x, y)


ages = {'kevin': 59, 'bob': 40}
print(type(ages.keys()))