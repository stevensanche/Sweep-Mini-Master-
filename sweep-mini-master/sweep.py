"""
Name: Steven Sanchez-Jimenez
CS 211, Project: Appointments
January 18, 2023,
Resources: In-class tools
"""


def all_same(l: list) -> bool:
    if len(l) == 0:
        return True
    for i in l:
        if i != l[0]:
            return False
        return True



def dedup(l: list) -> list:
    r = []
    p = None
    for i in l:
        if i != p:
            r.append(i)
            p = i
    return r

def max_run(l: list) -> int:
    if not l:
        return 0
    maxx = 1
    start = 1
    start1 = l[0]
    for i in l[1:]:
        if i == start1:
            start +=1
        else:
            maxx = max(maxx, start)
            start = 1
            start1 = i
    return max(maxx, start)










