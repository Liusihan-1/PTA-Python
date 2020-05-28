s = input()
ss = ''
cnt = 0
for i in range(len(s)):
    if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
        if ss.find(s[i].upper())==-1 and ss.find(s[i].lower())==-1:
            ss = ss + s[i]
            cnt += 1
if cnt<10:
    print("not found")
else:
    print(ss[0:10])
