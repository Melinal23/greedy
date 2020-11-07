"""
An activity is a pair ai = (si,fi) of a start time si and a
finish time fi, taking place in the time interval [si,fi).
Given a set of activities, find the max subset of non-overlapping
activities.

Example
Input:
S = {(3,5), (1,4), (1,2), (5,8), (7,9), (9,10)}
Output: {(1,2), (3,5), (5,8), (9,10)}
"""

"""
Pseudocode:
activity_selection(S <-- {a1, a2, ..., an})
Input: A set of n activities, where ai = (si,fi)
Output: A max subset of non-conflicting activities
let A be S, sorted in increasing order of finish time
let aj = (sj,fi) be the first activity in A
let X <- {aj}
for all ai = (si,fi) that exist in A do
    if si >= fi then
        let X <- X union {ai}
        let aj <- ai
        
return X
"""

def activity_selection(s):
    # a is equal to S sorted by finished time
    A = sorted(s, key=lambda x:x[1])
    a = A[0] #first activity in A

    x = []
    x.append(a)

    for i in range(1,len(A)):
        if A[i][0] >= a[1]: #if start time is after end time
            x.append(A[i])
            a = A[i]

    return x

"""
Sorting S has O(nlogn) complexity
Selecting activities has O(n) complexity
Activity Selection has O(nlogn) complexity
"""

print(activity_selection([(3,5), (1,4), (1,2), (5,8), (7,9), (9,10)]))