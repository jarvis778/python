class Solution:


    def reverse(self, x: int) -> int:
        if x<0:
            return -self.fun(x)
        return self.fun(x)


    def fun(self,x:int):
        ans=0
        c=0
        if x%10==0:
            p=x
            while p%10==0:
                c+=1
                p=p//10
            x=x//pow(10,c)
            while x>0:
                y=x%10
                x=x//10
                ans=(ans*10)+y

        else:
            while x>0:
                y=x%10
                x=x//10
                ans=(ans*10)+y

        return ans

ob = Solution()

print(ob.reverse(120))