# Re02.py

import re
r = re.compile("[pP]")
print(r.search("apple"))
print(r.match("apple")) #match는 정확히 pP가 있어야됨
print(r.match("apPle"))
print(r.match("pP"))
