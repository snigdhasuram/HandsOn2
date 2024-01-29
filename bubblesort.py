A=[5,2,4,6,1,3]
for i in range(len(A)-1):
    swap = False
    for j in range(len(A)-1,i,-1):
        if(A[j]<A[j-1]):
            #swap
            A[j],A[j-1]=A[j-1],A[j]
            swap = True
    if not swap:
            break
print(A)
