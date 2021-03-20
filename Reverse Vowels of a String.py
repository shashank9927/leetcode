class Solution:
    def reverseVowels(self, s: str) -> str:
        
        ss=list(s)
        d={}
        for i in range(len(s)):
            if s[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                d[i]=s[i]

        li=[]
        for i in d.values():
            li.append(i)
        li.reverse()
        i=0
        for p,q in d.items():
            d[p]=li[i]
            i+=1
        i=0
        for u,v in d.items():
            ss[u]=v
        return "".join(ss)


        
