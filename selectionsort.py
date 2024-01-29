A=[64,25,12,22,11]
for i in range(len(A)-1):
        min = i
        for j in range(i+1,len(A)):
            if A[min]>A[j]:
                min=j
        #swap
        A[i], A[min] = A[min], A[i] 
print(A)

