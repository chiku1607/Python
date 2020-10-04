print("WELCOME to the PYTHON PROGRAM")
name=input("Enter Your NAME : ")
print("Hello" ,name, "! \nAll the instructions are provided please follow them and carry on\n\n ")


def A( ):      #user defined function for task 3.1
    print("Prime Minister and Chief Minister are playing with sticks \nLet's help them \n")  #gives a brief description about the task
    n=int(input("Number of sticks :"))   #accepts size of array S
    S=[]                                 #defines array S
    S=list(map(int,input("Length of sticks :").split()))    #accepts array elements in a single line separated by SPACE
    N=[]                        #array N is defined to store the values which are repeated on array S
    S.sort(reverse=True)        #function sort() is used to arrange the array S in desending order
    for i in range(0,n-1):
        count=0                 #count is defined to check repeation
        if S[i]==S[i+1]:        #checks if an element is repeated in array S or not
            count+=1            #changes the value of count if element is repeated
        if count>=1 :
            N.append (S[i])     #stores a copy of repeated elements in array N         
    A=1
    if N[0]==N[1]:              
        N.remove(N[0])          # if the max length of stick is repeated 3 times it removes the value of N[0]
    if len(N)>=2:               #as we need maximum 2 values(l*b) it executes if len(N)>=2
        for i in range(0,2):
            A=A*N[i]            #area = l*b (first 2 maximim elements of array N)
    else:
        A=-1                    #if len(N)<2 it shows area=-1 
    print("Max Area :",A)       #print the output i.e. Max Area
A()       #user defined function is called


def B():     #user defined function for task 3.2
    print("\nThere's an array A consisting of N natural numbers \nLet's play with it\n")    #gives a brief description about the task
    n=int(input("Enter size of array :"))    #accepts size of array A
    A=[]      #defines array A
    count=0       #count is defined to check repeation
    A=list(map(int,input("Enter elements :").split()))      #accepts array elements in a single line separated by SPACE
    N=[]           #array N is defined to store output
    for i in range(n):
        for j in range(i,n-1):
            if A[i]*A[j+1]<0:    #if array A has an alternating subarray then their product is less than 0
                count+=1        #value of count is updated
            else:
                break           #if alternating subarray is not present then it comes out of the loop and stores 1 in array N
        N.append(count+1)       #stores the outcome in array N
        count=0                 #value of count is made 0 for second subarray
    print("Output :",N)         #print the output i.e. array N
B()       #user defined function is called

    

def C():     #user defined function for task 3.3
    print("\nIt's a inter College Sports Meet !!!\nLet's find the minimum no of matches VSSUT needs to win to qualify for playoffs\n") #gives a brief description about the task
    print("X= minimum POINTS required to qualify ")  #gives idea about X
    print("Y= remaining no of MATCHES\n ")           #gives idea about Y
    X=int(input("Value of X :"))        #accepts the value for X
    Y=int(input("Enter of Y :"))        #accepts the value for Y
    if X>=Y:            #executes only if minimum points >= remaining matches
        if Y*2==X:       #checks if X is even
            win=Y        #no of matches to win
        else:      #if X is odd        
            X-=1    #conerts X to even    
            win=int(X/2)    #no of matches to win        
    else :             #else no need to win any match VSSUT can qualify with draw matches
        win=0              #no of matches to win
    print("Number of matches required to win :",win)    #print the output i.e. no of matches required to win
C()        #user defined function is called


def D():      #user defined function for task 3.4
    print("\nWe have so many movies to watch during this weekend !!!\nLet's choose a movie \n")  #gives a brief description about the task
    L=[]      #defines array L
    R=[]      #defines array R
    M=[]      #array M is defined to store the value L[i]*R[i]
    N=[]      #array N is defined to store the values which are repeated on array M 
    I=[]      #array N is defined to store the values which are repeated on array N
    n=int(input("Enter number of movies :"))    #accepts size of array L and R
    print("Enter the values for Length and Rating of each movie :")   #gives idea about L and R
    for i in range(0,n):
        print("L",i+1,": ",end='')   #accepts the value for L
        L.append(int(input( )))
        print("R",i+1,": ",end='')
        R.append(int(input( )))     #accepts the value for R
        M.append(L[i]*R[i])     #stores the vaue for L[i]*R[i] in array M
    A=max(M)       #stores the maximim value of array M
    count=0        #count is defined to check repeation
    for i in range(0,n):
        if A==M[i]:       # cheks max(M)is repeated or not
            count+=1      #changes the value of count if element is repeated
            N.append(R[i])   #stores all the values for rating when max(M) is repeated
    B=max(N)        #stores the maximim value of array N 
    c=0         #c is defined to check repeation
    if count>1:
        for i in range(count):
            if B==N[i]:    # cheks max(N)is repeated or not
                c+=1       #changes the value of c if element is repeated
                I.append(i+1)   #stores all the values for index no when max(N) is repeated
        if c>1:     
            movie=min(I)   #indicates rating is repeated and stores movie =min(index value)
        else:
            movie=N.index(B)+1      #indicates rating is NOT repeated and stores movie =max(rating)
    else:
        movie=M.index(A)+1         #indicates max(M) is NOT repeated and stores movie =max(array M)
    print("OUTPUT : Movie No.",movie)    #print the output i.e. moive to be watched this weekend
D()         #user defined function is called


def E():        #user defined function for task 3.5
    print("\nWe know what an array is !!!")     #gives a brief description about the task
    print("Let's apply some operation on an array....\nand find the minimum sum of cost of operations needed to convert the array into a single element\n")
    n=int(input("Size of array :"))       #accepts size of array A
    A=[]      #defines array A
    A=list(map(int,input("Enter elements :").split()))      #accepts array elements in a single line separated by SPACE
    A.sort( )      #function sort() is used to arrange the array S in assending order
    cost=0          #cost is defined to store output
    for i in range(0,n-1):
        for j in range(0,n-1):
            if A[j]<A[j+1]:     #checks adjusend element in array A or not
                cost+=A[j]       #changes the value of cost and stores the smaller element
                A.remove(A[j+1])    #edits the value of array A and removes larger element
                A.append(0)       # 0 is added in the end of array to solve the error list index out of range
    X=A[0]         #stores the single element left in array A to a variable X
    A=[]           #the whole array is empty
    A.append(X)    #stores the single element in array A
    print("OUTPUT :",cost)        #print the output i.e. minimum coat of operation
E()       #user defined function is called

print("\nAnd here my program ends \n***** THANK YOU *****")
    
