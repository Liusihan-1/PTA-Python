import re
import collections
import sys
words = "".join([line for line in sys.stdin])
words = re.compile(r"\w+", re.I).findall(words.lower().split('#')[0])
words = [each.strip() for each in words]
words = list(map(lambda each: each[0:15] if len(each) > 15 else each, words))
counter = collections.Counter(words)
rank = sorted(counter.items(), key=lambda each: (-each[1], each[0]), reverse=False)
print(len(rank))
for each in rank[0:int(0.1*len(rank))]:
    print("{}:{}".format(each[1], each[0]))
