class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def get_item(self):
        return self.items
n=int(input())
q=Queue()
lst=['5','4','3','2','1']
for x in lst:
    if eval(x)%n!=0:
        flag=1
        continue
    else:
        flag=0
        print(x)
        break
q.items=['5','4','3','2']
s=str(1)

