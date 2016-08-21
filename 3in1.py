# Implement 3 Stacks using a single array

stacks = []
tops = [-1, -1, -1]
sizes = [0, 0, 0]


def push(ele, stackNo):
    if tops[stackNo] == -1:
        tops[stackNo] = sum(sizes[:stackNo]) - 1

    for i in range(stackNo + 1, 3):
        if tops[i] != -1:
            tops[i] += 1

    tops[stackNo] += 1
    stacks.insert(tops[stackNo], ele)

    sizes[stackNo] += 1


def pop(stackNo):
    for i in range(stackNo + 1, 3):
        if tops[i] != -1:
            tops[i] -= 1
    tops[stackNo] -= 1
    sizes[stackNo] -= 1
    return stacks.pop(tops[stackNo]+1)


push(1, 0)
push(2, 0)
push(3, 0)

push(4, 1)
push(5, 1)

push(6, 2)
push(7, 2)

pop(0)
pop(1)
pop(2)

push(3, 0)
push(5, 1)
push(7, 2)

print(stacks)
print(tops)
print(sizes)






