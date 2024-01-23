# Mini-project: List Sweep Algorithms 

This is a set of small exercises in writing algorithms that calculate 
something in a single *sweep* of a list, i.e., they are each based 
on a single loop that visits each list element once.  Thus each 
should operate in time linear in the length of the list, 
a.k.a. O(n) where n is the length of the list. 

## All same

A function that determines whether all the elements in a 
list are the same.   For example, all_same([1, 1, 1, 1]) == True, 
all_same([]) == True, all_same([1, 3, 1, 1]) == False. 

Function header: 
```
def all_same(l: list) -> bool:

```

## Dedup

A function that returns a de-duplicated version of the input 
list.  Elements appear in the same order as the input list, 
but subsequences of equal elements are replaced by one 
representative.  For example, dedup([]) = [], dedup([1, 1, 2, 1, 1]) 
= [1, 2, 1]. 

```
def dedup(l: list) -> list:
```


## Max run 

A run is a subsequence with identifical values.  For example, in 
[1, 1, 2, 2, 3, 4, 4, 4, 2, 4, 4], the runs are [1, 1], [2, 2], [3],
[4, 4, 4], [2], and [4, 4].  The longest run is [4, 4, 4], which 
has 3 elements.  max_run([1, 1, 2, 2, 3, 4, 4, 4, 2, 4, 4]) should
return 3.  max_run([]) == 0, max_run([1, 2, 3]) = 1, and
max_run([1, 2, 1, 1]) = 2.  

I think none of these are really difficult, but they are approximately
in order of increasing difficulty. 

Function header: 

```
def max_run(l: list) -> int:
```

# Hints

In my solutions, each of these three functions starts with a 
special case for the empty list: 

```
    if len(l) == 0:
        do whatever we should do for the empty list

```

After this special case, we know there is at least one element, 
so it is safe to do something with `l[0]`.  For example, in `all_same`
I take `l[0]` as a value that all the rest of the elements should be 
equal to.  In `max_run` I save it as the value that items in the 
current run should match.  In `dedup` I make the value matched by the current
subsequence. 

After setting some initial values, the heart of each of these is 
a loop of the form: 

```
    for item in l:

```

Note I did not need to use the other common form, `for i in range(len(l))`, 
because I only need access to the current element and not to elements 
at other positions.  In general I only need the current element 
because I can keep just a little bit of extra information. 

In `all_same`, the only extra information I need to keep track of is the value
that each item should match.  

In `max_run`, I keep track of: 

* the value that all the items in the current run match
* the length of the current run, so far
* the length of the longest run I have found so far

There are two things that can happen in the body of the loop.  If I 
see another matching item, I add to the length of the current run, 
and possibly update the length of the longest run so far (if the current
run is longer).  If the new item doesn't match the current run, 
I start a new run with its value. 

In `dedup`, I keep track of the value in the current run while building 
up a `result` list.  If the current item matches the current run, 
I don't do anything.  If it doesn't match, I append it to the 
result and remember it as the value of the new current run. 

Not counting any comment lines, here are the lengths of my solutions: 

* `all_same`: 8 lines
* `max_run`: 15 lines
* `dedup`: 10 lines

