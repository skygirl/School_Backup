def crypto(filename):
    "Input: File(string) Output:file(string)"
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    newstuff = content.replace('secret', 'XXXXXX')
    infile = open('filename', 'r+')
    infile.write(newstuff)
    f = infile.read()
    infile.close()
    print(f)

def fcopy(filename1, filename2):
    "Input: File(strings), File; Output: File(string)"
    infile1 = open(filename1, 'r')
    content = infile1.read()
    infile1.close()
    infile2 = open(filename2, 'w')
    infile2.write(content)
    infile2.close()
    infile2 = open(filename2, 'r')
    f = infile2.read()
    infile2.close()
    print(f)

def wordcount(filename1):
    "Input: File(strings), Output: int)"
    infile1 = open(filename1, 'r')
    content = infile1.read()
    infile1.close()
    return len(content.split(" "))

def links(filename1):
    "Input: file(string) Output: int"
    counter = 0
    infile1 = open(filename1, 'r')
    content = infile1.read()
    infile1.close()
    for i in range(len(content)):
        if content[i]== '<':
            if content[i + 1] == '/':
                if content[i + 2 ] == 'a':
                    if content[i + 3 ] == '>':
                        counter = counter + 1
    return counter
    
    # Program Runs
##>>> crypto('secret.txt')
##I will tell you my XXXXXX But first I have to  explain why it is a XXXXXX.  XXXXXX..... 
##
##>>> fcopy('secret.txt', 'test2.txt')
##I will tell you my secret But first I have to  explain why it is a secret.  secret..... 
##
##>>> open('test3.txt').read()
##'I will tell you my secret. \nBut first,  \nI have to explain why it is a secret.\n'
##>>> wordcount('secret.txt')
##21
##>>> wordcount('test2.txt')
##21
##>>> wordcount('a4p2.htm')
##652
##>>> links('a4p2.htm')
##3
##>>> 
##    
