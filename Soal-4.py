def mergeThreeSortedLists(A,B,C):

    i=j=k=0
    result=[]

    while i < len(A) or j < len(B) or k < len(C):

        vals=[]

        if i < len(A):
            vals.append((A[i],'A'))

        if j < len(B):
            vals.append((B[j],'B'))

        if k < len(C):
            vals.append((C[k],'C'))

        val, source = min(vals)

        result.append(val)

        if source=='A':
            i+=1
        elif source=='B':
            j+=1
        else:
            k+=1

    return result


print(mergeThreeSortedLists(
[1,5,9],
[2,6,10],
[3,4,7]
))