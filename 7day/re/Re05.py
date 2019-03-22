import re
r = re.compile("ck?w") #c와w사이에 없어도되거나, k가 하나잇어야됨
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))
print(r.search("kkkw"))