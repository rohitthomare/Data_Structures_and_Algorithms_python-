'''#class for node 
class Node:
    
    #fun of noad structure 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

#linked list class
class LinkedList:

    #fun of linkedlist structure 
    def __init__(self):
        self.head = None

    # This method prints list in forward direction. Use node.next
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    # Print linked list in reverse direction. Use node.prev for this.
    
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' 
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    
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

    def get_last_node(self):
        itr=self.head
        while itr:
            itr = itr.next

        return itr


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
        if self.head==None:
            node = Node(data, self.head,None)
            self.head = node
        else:
            node = Node(data, self.head,None)
            self.head.prev=node
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
                node = Node(data, itr.next,itr)
                if node.next:       #setting prev node for new itr
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    #func to insert node at end 
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None,None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None,itr)

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
                if itr.next:
                    itr.next.prev = itr.prev 
                break
            itr=itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next,self.head)
            return

        itr= self.head
        while itr:
            if itr.data==data_after:
                node = Node(data_to_insert, itr.next,itr)
                if itr.next:
                    itr.next.prev=itr.prev
                itr.next = node
                break
            itr=itr.next
            

# code start executing from here
if __name__ == '__main__':

    ll=LinkedList()

    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
'''
    
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

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
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()




  



