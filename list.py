l = [1,2,3,4,5,"himanshi","hemlata",24.5]
print(l)
print(type(l))
print(l[0])
print(len(l))
print(l[-2])
# adding elements to a list
# append - to add an item to the end of the list
l.append("dolly")
print(l)
#insert - to insert a list item at a specified index
l.insert(5,"hemu")
print(l)
#extend - to append elements from another list to the current list
l1 = [6,7,8,9]
l.extend(l1)
print(l)
# removing elements from a list
l.remove(3)
print(l)
# pop - remove  the specified index
l.pop(0)
print(l)
# del - delete the list completely
del l
# clear - list still remains,but ut has no content
l.clear()
print(l)
