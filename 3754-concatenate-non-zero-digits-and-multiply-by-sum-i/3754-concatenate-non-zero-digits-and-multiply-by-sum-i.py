class Solution(object):
    def sumAndMultiply(self, n):
        sum = 0
        list1 = []
        list2=[]
        while(n>0):
            dig = n%10
            sum += dig
            list1.append(dig)
            n //= 10
        list1.reverse()
        for i in list1:
            if i!=0:
                list2.append(i)
        num = 0
        for i in list2:
            num = num*10 + i
        return num*sum