#node class 
class Node:
    #function for node structure 
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    #fun for linked list structure 
    def __init__(self):
        self.head=None

    #function to print the linked list 
    def print_linked_list(self):
        itr=self.head 
        show=' '  #tacking a empty string variable 
        while itr:
            suffix =''     #initialy suffix is empty 
            if itr.next:
                suffix='-->' #for to show the next node suffix become --> 
            show+=str(itr.data)+suffix
            itr=itr.next
        print(show)


if __name__=='__main__':
    
    llist=Linked_list()
    llist.head=Node(10)
    second=Node(12)

    llist.head.next=second

    llist.print_linked_list()

