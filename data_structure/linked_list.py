#class for node 
class Node:
    
    #fun of noad structure 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#linked list class
class LinkedList:

    #fun of linkedlist structure 
    def __init__(self):
        self.head = None

    #fun for printing linked list 
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    #fun to get the length of linked list 
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    #fun to insert node at begining 
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    #fun to insert node in middle of nodes
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    #func to insert node at end 
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    #fun to remove node from linked list 
    def remove_at(self,index):
        if self.head is None:
            print("you dont have linked list ")

        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head=self.head.next
            return 

        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

# code start executing from here
if __name__ == '__main__':

    llist=LinkedList()
    
    '''llist.head=Node(10)
    second=Node(12)
    third=Node(14)

    llist.head.next=second 
    second.next=third 

    llist.insert_at_begining(8)
    llist.insert_at(3,13)
    llist.insert_at_end(16)


    llist.remove_at(4)'''


    llist.insert_values(["Abhishek","varun","vipul"])
    llist.insert_at_begining("Rohit")
    llist.insert_at(2,"kamlesh")
    llist.insert_at_end("harshal")

    llist.remove_at(2)

    llist.print()

    print("Total number of Nodes ",llist.get_length())

    llist.insert_values([10,20,30,40,50,])
    llist.insert_at_begining(1)
    llist.insert_at(2,15)
    llist.insert_at_end(60)

    llist.remove_at(3)

    llist.print()
    print("Total number of Nodes ",llist.get_length())



