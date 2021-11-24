'''big O NOTATION HERE O(N) YOU ARE RUNNING N ITRETIONS
If program having input for nums in million numbers the for lop will excute for n number times
hence the time will grow linearly
the time complexity for this program is O(n)'''


num=list(map(int,input().split(" ")))
def get_squares(num):
    square_no=[]
    for n in num:
        square_no.append(n*n)
        print(square_no)
get_squares(num)


#TIME COMPLEXITY O(1)
'''time complexity is remain constant where u provide the index of the element 
it will do constant operation
here we have to find the pe of stocks in example 
we have input of list where the stocks price ,eps is given
the complexity of given program is O(1) '''
def fiind_first(prices,eps,index):
    pe=prices[index]/eps[index]
    return pe
    print(pe)
    

'''time complexity O(n^2)
in this loop the for loop has itrated n^2 times so to define time the loop will
excute n^2 times'''

num=[3,6,2,4,3,6,8,9]

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            print(num[i]+"is a duplicate")
            break
            

            
    