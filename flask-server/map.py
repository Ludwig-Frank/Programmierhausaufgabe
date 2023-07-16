import sys
import re
def mapper(text):
    map = []
    pp = text.strip().split()
    for p in pp:
        p = re.sub("\*|\.|\,|\?|\[|\]|\!","",p)
        p = p.lower()
        map.append([p,1])
    return map

if __name__ == '__main__':
    mapper("Hallo Welt")