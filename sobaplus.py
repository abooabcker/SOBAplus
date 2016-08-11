from prettytable import PrettyTable
t=PrettyTable(['Particulars','Quantity','Rate'])
amount=int(input("\033[30m"+" Enter the amount :\033[1;31m "))
a=amount
bal=0
rs=[1000,500,100,50,20,10,5,2,1]
clst=[]
print ("\033[30m howmany need in\033[1;31m ")
for i in range(9):
   n= (input("{}  :  ".format(rs[i])))
   clst.append(n)
print("\033[1;32m")
for i in  range (9):
    j=clst[i]
    while j >0:
        tot=j*rs[i]
        if tot < a+1:
           t.add_row([rs[i],j,tot])
           bal=bal+tot
           a=a-tot
           j=0
        j=j-1
print t
print(" Total : {}".format(bal).rjust(30))
print ("\033[31m Balance : {}".format(amount-bal).rjust(40))
        
        
    
