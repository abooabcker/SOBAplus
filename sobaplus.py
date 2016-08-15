def sobaplus(amount,list):
   result={}
   rs=[1000,500,100,50,20,10,5,2,1]
   for i in  rs:
       if list.get(i,0) > 0:
          for list[i] in range(list[i],0,-1):
             if list[i]*i <= amount:
                result[i]=list[i]
                amount=amount-(i*list[i])
                break
       if amount <=0:
                 break
   return ( result,amount )

        
        
    
