
# 1 Problem 3.36

def abbreviation(s):
    "Input: str; Output: str"
    "Takes a string input and returns the two letter abbreviation"
    res = s[:2]
    res=res.title()
    return res

# 2 Problem 3.39
def lastF(s):
    "Input:Str, Output: str"
    "Takes an input string and returns the second part string first, and the initial of the first part of the string"
    x=s.split()
    first = x[0][0]
    first=first.title()
    last = x[1]
    last = last.title()
    whole = last + ", " + first
    return whole

# 3  Problem 5.16
def indexes(s, c):
    "Input: str Output: int"
    "Takes a string and returns the list of indicies where the the character occurs"
    ind = []
    newLst=[]
    x = 0
    for y in range(len(s)):
        if c in s[x]:
            ind.append([x])
        x = x + 1
    for i in ind:
        newLst = newLst + i
    return newLst

#4  Problem 5.27
def letter2number(s):
    "Input:Str, Output: Float"
    "Takes and input string and outputs the equivalent float"
    res = 0
    if s=="A+":
        res=4.3
        return res
    elif s == "A-":
        res=3.7
        return res
    elif s == "A":
        res=4.0
        return res
    elif s=='B+':
        res=3.3
        return res
    elif s=='B':
        res=3.0
        return res
    elif s=='B-':
        res=2.7
        return res
    elif s=='C+':
        res=2.3
        return res
    elif s=='C':
        res=2.0
        return res
    elif s=='C-':
        res=1.7
        return res
    elif s=='D+':
        res=1.3
        return res
    elif s=='D':
        res=1.0
        return res
    elif s=='D-':
        res=0.7
        return res
    elif s=='F':
        res=0
        return res
    
        
#5   Problem 5.26  

def rps(s, c):
    "input:str, output: int"
    "Takes the user input of R P or S and assigns 1 or -1 based on the winner"
    if s=='R' and c=='P':
        x = 1
        return x
    elif s=='R' and c=='R':
        x = 0
        return x
    elif s == 'R' and c == 'S':
        x= -1
        return x
    elif s=='S' and c=='S':
        x = 0
        return x
    elif s=='S' and c=='P':
        x = -1
        return x
    elif s=='S' and c=='R':
        x = 1
        return x
    elif s== 'P' and c=='P':
        x= 0
        return x
    elif s=='P' and c == 'R':
        x=-1
        return x
    elif s=='P' and c=='S':
        x=1
        return x


# 6 Problem 3.40
def avg(l):
    "Input:Lst(List(Int) Output: int"
    "Takes as an input a list of numbers and returns the average for each list"
    i = 0
    for x in l:
        y = sum(l[i])
        float(y)
        p =len(l[i])
        float(p)
        res= y/p
        print float(res)
        i= i+1


# 7 Problem 5.34

def statement(l):
    "Input: lst(float) Output:Lst(float)"
    "Takes an imput of a float list of numbers and returns the sum of positive and negative numbers"
    myListOne = []
    myListTwo =[]
    res=[]
    x = 0
    z = 0
    for i in l:
        if i > 0:
            myListOne.append(i)
        elif i < 0:
            myListTwo.append(i)
    a = len(myListOne)
    y = sum(myListOne[0:a])
    b = len(myListTwo)
    k = sum(myListTwo[0:b])
    res.append(k)
    res.append(y)
    return res
   

    


