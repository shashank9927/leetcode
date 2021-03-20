class Solution:
    def isPalindrome(self, n: int) -> bool:
        x=list(str(n))
        y=list(str(n))
        y.reverse()
        for i in range(len(x)):
            if x[i]==y[i]:
                flag=0
                continue
            else:
                flag=1
                break
        if flag==1:
            return 0
        else:
            return 1

       
