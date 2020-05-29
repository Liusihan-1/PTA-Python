lst1 = eval(input())
lst2 = list(set(lst1))
lst2.sort(key = lst1.index)
print(' '.join(list(map(str, lst2))))
