import re
s = input()
names = set()
for ss in s.split():
    if "@" in ss:
        for sss in ss.split("@")[1:]:
            if sss != "":
                names.add(sss)
for name in sorted(names):
    print(name)
