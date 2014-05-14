def poly(lst, x):
    "Input: List(int);  Output: int"
    res = 0
    for n,b in enumerate(lst):
        res += b*x**n
    return res

def countEvens(lst):
    "Input:List(int); Output: Int"
    evens = []
    newList = []
    counter = 0
    for x in lst:
        newList = newList + x
    for y in newList:
        if y % 2 == 0:
            evens.append(y)
    for z in evens:
        counter = counter + 1
    return counter

def findMinRow(lst):
    "Input: List(int); Output: int"
    return min(range(len(lst)), key=lambda i: sum(lst[i]))

def findMaxDiff(lst):
    "Input:list(int); Output: (int, int)"
    answer = []
    index =  max(range(len(lst)), key=lambda i: sum(lst[i]))
    holder = enumerate(max(x) - min(x) for x in lst)
    return max(x[::-1] for x in holder)
    return index


# Problem number 5 I wrote 2 functions: Begin problem 5:

def term(n):
    return 4 / (2.0 * n + 1) * (-1) ** n
def approx_pi(z):
    "Input: Float; output: Float"
    ind = term(0) 
    ind2 = term(0) + term(1)
    n = 2
    while abs(ind - ind2) > z:
        ind = ind2
        ind2 += term(n)
        n += 1
    return ind2
# end of problem 5


##
##>>> 
##>>> countEvens([[1,4,3],[12,0,7,10],[13]])
##4
##>>> countEvens([[25, -4],[1,2,3,4,5],[0,50,99]])
##5
##>>> countEvens([[1,3], [5]])
##0
##>>> countEvens([[]])
##0
##>>> findMinRow([[3.99, -12.5, 8.61], [0], [-30.5,8]])
##2
##>>> findMinRow([[3.99, -12.5, 8.61], [0], [-30.5,8]])
##2
##>>> findMinRow([[1,2,3], [-100], [10,-30.5,8]])
##1
##>>> findMinRow([[10,20], [100,200], [13], [8,9,10],[10,-30.5,8]])
##4
##>>> findMinRow([[10,20], [100,200], [13], [8,7,6,5],[8,9,10]])
##2
##>>> findMinRow([[10,20], [100,200], [8,7,6,5], [13], [8,9,10]])
##3
##>>> ================================ RESTART ================================
##>>> 
##>>> findMaxDiff([[12,3,50,17], [10,5,9,100,31],[5,3,1]])
##(95, 1)
##>>> findMaxDiff([[12,3,50,17],[10,5,9,1,31],[5,3,1]])
##(47, 0)
##>>> findMaxDiff([[1], [2],[3]])
##(0, 2)
##
##>>> approx_pi(0.5)
##3.3396825396825403
##>>> approx_pi(0.5)
##3.3396825396825403
##>>> approx_pi(0.05)
##3.1659792728432157
##>>> approx_pi(0.005)
##3.144086415298761
##>>> approx_pi(0.0000005)
##3.1415929035895926
##>>> poly([1,2,1],2)
##9
##>>> poly([1,0,1,0,1],2)
##21
##>>> poly([1,0,1,0,1],3)
##91
##>>> 
