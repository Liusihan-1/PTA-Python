s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
k = int(input())
for i in range(len(s)):
    if 'a'<= s[i] <= 'z':
        for j in range(26):
            if s1[j] == s[i]:
                print("{}".format(s1[(j+k)%26]),end = '') 
    elif 'A' <= s[i] <= 'Z':
        for j in range(26):
            if s2[j] == s[i]:
                print(s2[(j+k)%26],end = '') 
    else:
        print(s[i],end = '')
