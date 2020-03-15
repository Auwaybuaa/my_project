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
while flag==1:
    if s[-1]=="1":
        a=eval((str(s)+"3"))
        if a%n!=0:
            q.enqueue(a)
        else:
            print(a)
            flag=0
            break
        b=eval((str(s)+"5"))
        if b%n!=0:
            q.enqueue(b)
        else:
            print(b)
            flag=0
            break
    if s[-1]=="2":
        a=eval((str(s)+"3"))
        if a%n!=0:
            q.enqueue(a)
        else:
            print(a)
            flag=0
            break
        b=eval((str(s)+"4"))
        if b%n!=0:
            q.enqueue(b)
        else:
            print(b)
            flag=0
            break
    if s[-1]=='3':
        a=eval((str(s)+"1"))
        if a%n!=0:
            q.enqueue(a)
        else:
            print(a)
            flag=0
            break
        b=eval((str(s)+"4"))
        if b%n!=0:
            q.enqueue(b)
        else:
            print(b)
            flag=0
            break
    if s[-1]=='4':
        a=eval((str(s)+"5"))
        if a%n!=0:
            q.enqueue(a)
        else:
            print(a)
            flag=0
            break
    if s[-1]=='5':
        for j in range(6):
            a=eval(str(s)+str(j))
            if a%n!=0:
                q.enqueue(a)
            else:
                print(a)
                flag=0
                break
    s=str(q.dequeue())

'''
I have a dream that one day this nation will rise up and live out the true meaning of
its creed: We hold these truths to be self-evident that all men are created equal.

I have a dream that one day on the red hills of Georgia the sons of former slaves
and the sons of former slave owners will be able to sit down together at the table
of brotherhood.

I have a dream that one day even the state of Mississippi, a state sweltering with
the heat of injustice, sweltering with the heat of oppression, will be transformed
into an oasis of freedom and justice.

I have a dream that my four little children will one day live in a nation where they
will not be judged by the color of their skin but by the content of their character.
I have a dream today!

I have a dream that one day, down in Alabama, with its vicious racists, with its
governor having his lips dripping with the words of interposition and nullification;
one day right down in Alabama little black boys and black girls will be able to join
hands with little white boys and white girls as sisters and brothers. I have a dream
today!

I have a dream that one day every valley shall be exalted, and every hill and
mountain shall be made low, the rough places will be made plain, and the crooked
places will be made straight, and the glory of the Lord shall be revealed and all
flesh shall see it together.
'''


