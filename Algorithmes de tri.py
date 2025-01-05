#<-----------------Tri sélection--------------->

def imin(L,a,b):
    imin=a
    for i in range(a+1,b):
        if L[i]<L[imin]:
            imin=i
    return imin

def triSelection(L):
    n=len(L)
    for i in range(n-1):                 #O(n^2)
        j=imin(L,i,n)
        L[i],L[j]=L[j],L[i]
    return L

#<-----------------Tri insertion--------------->

def echange(L,i,j):
    L[i],L[j]=L[j],L[i]

def triInsertion(L):
    n=len(L)
    for i in range(1,n):
        x=L[i]
        j=i-1
        while j>=0 and L[j]>x:              #O(n^2)
            echange(L,j,j+1)
            j-=1
        L[j+1]=x
    return L

#-------------------Tri à bulles--------------->

def triBulles(L):
    n=len(L)
    for i in range(n-1):
        for j in range(n-i-1):               #O(n^2)
            if L[j+1]<L[j]:
                L[j+1],L[j]=L[j],L[j+1]
    return L

#<------------------Tri rapide----------------->

def separe(L):
    x=L[0]
    L1,L2=[],[]
    for i in range(1,len(L)):
        if L[i]<=x:
            L1.append(L[i])
        else:
            L2.append(L[i])
    return L1,L2

def triRapide(L):
    if L==[]:
        return []                           #O(nln(n))
    L1,L2=separe(L)
    return triRapide(L1)+[L[0]]+triRapide(L2)

#<-------------------Tri fusion---------------->

def fusion(L1,L2):
    i,j=0,0
    L=[]
    while i<len(L1) and j<len(L2):
        if L1[i]<L2[j]:
            L.append(L1[i])
            i+=1
        else:                               #O(nln(n))
            L.append(L2[j])
            j+=1
    if i==len(L1):
        return L+L2[j:]
    else:
        return L+L1[i:]

def triFusion(L):
    if len(L)<=1:
        return L
    L1,L2=L[:len(L)//2],L[len(L)//2:]
    return fusion(triFusion(L1),triFusion(L2))
