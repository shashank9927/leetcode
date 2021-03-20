class Solution:
    def reverse(self, n: int) -> int:
        x=list(str(n))
        if len(x)==1:
            return n
        
        elif x[0]=='-':
            t1= int('-'+"".join(reversed(x[1:])))
        else:
            t1=int("".join(reversed(x)))
        if  t1<=2**31 and t1>=-2**31:
            return t1
        else:
            return 0
            
