n = input()
li = []
for i in range(int(n)):
    s = input()
    li.append(s)
li_len = list(map(len,li))
max_str = li[li_len.index(max(li_len))]
print('The longest is: %s' % max_str)
