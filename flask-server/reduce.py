import sys

def reducer(map):
    counter = {}
    newMap = []
    for pp in map:
        if len(pp):
            counter[pp[0]] = counter.get(pp[0], 0) + int(pp[1])

    for word, count in sorted(counter.items(), key=lambda x:x[1]):
        newMap.append([word,count])
    return newMap

if __name__ == '__main__':
    reducer()