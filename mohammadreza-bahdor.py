Pythonbook exercises:1,...,23 page:385,.....,388  answer :

1-Can a Python list hold a mixture of integers and strings? Yes
-------------------------------------------------------------------
2-What happens if you attempt to access an element of a list using a negative index?
when we use nagative indexes
to access an element , The list starts counting with the last element
-------------------------------------------------------------------
3- What Python statement produces a list containing the values 45, −3, 16 and 8, in that order? 
lst = [45,-3,16,8]
print(lst)
-------------------------------------------------------------------
4- Given the statement
lst = [10, -4, 11, 29]
(a) What expression represents the very first element of lst? print(lst[0])
(b) What expression represents the very last element of lst? print(lst[3])
(c) What is lst[0]? 10
(d) What is lst[3]? 29
(e) What is lst[1]? -4
(f) What is lst[-1]? 29
(g) What is lst[-4]? 10
(h) Is the expression lst[3.0] legal or illegal? No becuse list indices must be 
integers or slices, not float
-------------------------------------------------------------------
5-Given the statements
lst = [3, 0, 1, 5, 2]
x = 2
evaluate the following expressions:
(a) lst[0]? 3
(b) lst[3]? 5
(c) lst[x]? 1
(d) lst[-x]? 5
(e) lst[x + 1]? 5
(f) lst[x] + 1? 1+1=2
(g) lst[lst[x]]? 0
(h) lst[lst[lst[x]]]? 3
-------------------------------------------------------------------
6- What function returns the number of elements in a list?
print(len(list))
-------------------------------------------------------------------
7-What expression represents the empty list?
num = list() or num=[]
print(len(num))---> 0
-------------------------------------------------------------------
8-Given the list
lst = [20, 1, -34, 40, -8, 60, 1, 3]
evaluate the following expressions:
(a) lst ----> [20, 1, -34, 40, -8, 60, 1, 3]
(b) lst[0:3]---->  [20, 1, -34]
(c) lst[4:8]----> [-8, 60, 1, 3]
(d) lst[4:33]----> [-8, 60, 1, 3]
(e) lst[-5:-3]----> [40, -8]
(f) lst[-22:3]----> [20, 1, -34]
(g) lst[4:]----> [-8, 60, 1, 3]
(h) lst[:]----> [20, 1, -34, 40, -8, 60, 1, 3]
(i) lst[:4]----> [20, 1, -34, 40]
(j) lst[1:5]----> [1, -34, 40, -8]
(k) -34 in lst----> True
(l) -34 not in lst----> False 
(m) len(lst)----> 8
-------------------------------------------------------------------
9-A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] ==> A[0:5] ==> [2, 4, 6, 8, 10]
A = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] ==> A[6:11] ==> [2, 4, 6, 8, 10]
A = [2, 3, 4, 5, 6, 7, 8, 10] ==> A[0:7:2] + A[7:] ==>! [2, 4, 6, 8, 10]
A = [2, 4, 6, 'a', 'b', 'c', 8, 10] ==> A[0:3] + A[6:] ==> [2, 4, 6, 8, 10]
A = [2, 4, 6, 8, 10] ==> A[0:5] ==> [2, 4, 6, 8, 10]
A = [] ==> IMPOSSIBLE !! HOWEVER => A[0:] + [2, 4, 6, 8, 10] ==> [2, 4, 6, 8, 10]
A = [10, 8, 6, 4, 2] ==> A[-1:-6:-1] ==> [2, 4, 6, 8, 10]
A = [2, 4, 6] ==> IMPOSSIBLE !! HOWEVER => A[0:4] + [8, 10] ==> [2, 4, 6, 8, 10]
A = [6, 8, 10] ==> IMPOSSIBLE !! HOWEVER => [2, 4] + A[0:4] ==> [2, 4, 6, 8, 10]
A = [2, 10] ==> IMPOSSIBLE !! HOWEVER => A[0:1] + [4, 6, 8] + A[1:2] ==> [2, 4, 6, 8, 10]
A = [4, 6, 8] ==> IMPOSSIBLE !! HOWEVER => [2] + A[0:3] + [10] ==> [2, 4, 6, 8, 10]
-------------------------------------------------------------------
10-Write the list represented by each of the following expressions.

(a) [8] * 4 ---->[8, 8, 8, 8]

(b) 6 * [2, 7] ---->[2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7]

(c) [1, 2, 3] + ['a', 'b', 'c', 'd'] ---->[1, 2, 3, 'a', 'b', 'c', 'd']

(d) 3 * [1, 2] + [4, 2] ---->[1, 2, 1, 2, 1, 2, 4, 2]

(e) 3 * ([1, 2] + [4, 2]) ---->[1, 2, 4, 2, 1, 2, 4, 2, 1, 2, 4, 2]
-------------------------------------------------------------------
11- Write the list represented by each of the following list comprehension expressions.

(a) [x + 1 for x in [2, 4, 6, 8]] ----> [3, 5, 7, 9]

(b) [10*x for x in range(5, 10)] ----> [50, 60, 70, 80, 90]

(c) [x for x in range(10, 21) if x % 3 == 0] ----> [12, 15, 18]

(d) [(x, y) for x in range(3) for y in range(4)] ----> [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

(e) [(x, y) for x in range(3) for y in range(4) if (x + y) % 2 == 0] ----> [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
-------------------------------------------------------------------
12- Provide a list comprehension expression for each of the following lists.

(a) [1, 4, 9, 16, 25] ----> 

f = 1
l = []
for i in range(0,5):
    t = f*f
    l.append(t)
    f = f+1
print(l)

(b) [0.25, 0.5, 0.75, 1.0, 1.25. 1.5] ----> 

f = 0.0
l = []
for i in range(0,6):
    t = f+0.25
    l.append(t)
    f = f+0.25
print(l)

(c) [('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)] ----> 

l = []
f = 0
s = 0
#ta = ('a',f)

for i in range(0,3):
    ta = ('a',f)
    f = f + 1
    l.append(ta)
for i in range(0,3):
    tb=('b',s)
    s = s + 1
    l.append(tb)
print(l)

-------------------------------------------------------------------
13-If lst is a list, what expression indicates whether or not x is a member of lst?
print(x in lst) ----->Return True Or False
-------------------------------------------------------------------
14- What does reversed do?
Using the reverse() method we can reverse the contents of the list object
Input : list = [4, 5, 6, 7, 8, 9]
Output : [9, 8, 7, 6, 5, 4]
-------------------------------------------------------------------
15-Complete the following function that adds up all the positive values in a list of integers. For example,
if list a contains the elements 3,−3,5,2,−1, and 2, the call sum_positive(a) would evaluate to 12,
since 3+5+2+2 = 12. The function returns zero if the list is empty.

def sum_positive(a):
    g = 0
    if len(lst)==0:
        return 0
    for i in a:
        if int(i) < 0: 
           a.remove(i) 
    for i in a:
        g = g+int(i)
    return g
lst = [3,-3,5,2,-1,2]
out = sum_positive(lst)
print(out)

------------------------------------------------------------------
16- Complete the following function that counts the even numbers in a list of integers. For example, if
list a contains the elements 3,5,4,−1, and 0, the call count_evens(a) would evaluate to 2, since a
contains two even numbers: 4 and 0. The function returns zero if the list is empty. The function does
not affect the contents of the list.

def count_evens(lst):
    g = 0
    if len(lst)==0:
        return 0
    for i in lst:
        if int(i)%2==0: 
           g = g+1

    return g
lst = [3,5,4,-1,0]
out = count_evens(lst)
print(out)
------------------------------------------------------------------
17- Write a function named print_big_enough that accepts two parameters, a list of numbers and a
number. The function should print, in order, all the elements in the list that are at least as large as the
second parameter.

def print_big_enough(lst,big):
    for i in lst:
        if int(i)>=big: 
           print(i)

    
lst = [3,-1,0,34,12,34,5,6,78,13]
big = 12
print_big_enough(lst,big)
------------------------------------------------------------------
18- Write a function named next_number that accepts a list of integer values. All the elements in the list
are unique, and all elements in the list are greater than or equal to one. (The caller must ensure that
these conditions are met before passing the list to next_number.) The next_number function should
return the smallest positive integer not in the list. (Note that 1 is the smallest positive integer.

def next_number(A):
    # Const-ish to improve readability
    MIN = 1
    if not A: return MIN
    # Save re-computing MAX
    MAX = max(A)
    # Loop over all entries with minimum of 1 starting at 1
    for num in range(1, MAX):
        # going for greatest missing number return optimistically (minimum)
        # If order needs to switch, then use max as start and count backwards
        if num not in A: return num
    # In case the max is < 0 double wrap max with minimum return value
    return max(MIN, MAX+1)

lst = [5, 4, 1, 2]
out = next_number(lst)
print(out)
------------------------------------------------------------------
19-Write a function named reverse that reorders the contents of a list so they are reversed from their
original order. a is a list. Note that your function must physically rearrange the elements within the
list, not just print the elements in reverse order.

def reverse(lst):
    lst.reverse()
    for i in lst:
        print(i)
    
lst = [5, 4,'a',234,'hibye']
reverse(lst)
------------------------------------------------------------------
20-z=[[1 for _ in range(9)]for _ in range(6)]
print(z)
z[2][4]=0
print(z)
------------------------------------------------------------------
21-Provide five different ways to create the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and assign it to
the variable lst.

method 1 :

lst = []
num = 1
for i in range(0,10):
    lst.append(num)
    num = num+1
print(lst)
-------------
method 2 :

lst = []
num = 1
while num<=10:
    lst.append(num)
    num = num+1
print(lst)
------------
method 3 :

lst = []
num = 10
while num>=1:
    lst.append(num)
    num = num-1
lst.reverse()
print(lst)
------------------------------------------------------------------
22-def Q22(m):
    new_mat = [[0] * len(m)] * len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            new_mat[j][i] = m[i][j]
    flag = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i] == new_mat[j]:
                flag = 1
    if flag:
        return True
    else:
        return False
------------------------------------------------------------------
23-def check_winner(m):
    new_mat = [[0] * len(m)] * len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            new_mat[j][i] = m[i][j]
    for i in m:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    for i in new_mat:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    if m[0][0] == m[1][1] == m[2][2] == 'X':
        return 'X'
    elif m[0][0] == m[1][1] == m[2][2] == 'O':
        return 'O'
    if m[0][2] == m[1][1] == m[2][0] == 'X':
        return 'X'
    elif m[0][2] == m[1][1] == m[2][0] == 'X':
        return 'O'
    return ' '
"""
