class node:

    def __init__(self,val):
        self.val = val
        self.next= None

a = (1,'a',3)
b = (1,'a',4)

res = a < b
print(res)