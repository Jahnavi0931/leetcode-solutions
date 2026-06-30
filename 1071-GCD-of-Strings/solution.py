class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result=""    
        small=min(len(str1),len(str2))
        for i in range(small,0,-1):
            result=str1[:i]
           
            if len(str1)%len(result)==0 and   len(str2)%len(result)==0:
              repeat1=result*(len(str1)// len(result))
              repeat2=result*(len(str2)// len(result))   
              if repeat1==str1 and repeat2==str2:
                 return result  
        return""               
      
