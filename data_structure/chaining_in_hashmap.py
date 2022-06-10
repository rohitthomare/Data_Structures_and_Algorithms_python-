 #using chaining to avoid hash collision

class Hash_table:
    #
    def __init__(self):
        self.size=6
        self.array=[[] for i in range (self.size)]
    
    # get the hash value of key using ord() method 
    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.size
        #hash is the mode value of sum of ask key values of key to array size 

    # get key at the perticular index 
    def __getitem__(self,key):
        array_index=self.get_hash(key)
        for kv in self.array(array_index):
            if kv[0]==key:
                return kv[1]
    
    #set the key value pair 
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for index,element in enumerate(self.array[h]):  #using chaining to avoid collision 
            if len(element)==2 and element[0]==key:
                self.array[h][index]=[key,value]
                found=True

        if not found:
            self.array[h].append((key,value))
    
    #delete any key in hash map 
    def __delitem__(self,key):
        array_index=self.get_hash(key)
        for index,element in enumerate(self.array[array_index]):
            if element[0]==key:
                print('del',array_index,index)
                del self.array[array_index][index]

t=Hash_table()

t['march 1']=10
t['march 2']=20
t['march 3']=30
t['march 4']=40
t['march 5']=50
t['march 6']=60
t['march 7']=70
t['march 8']=80
t['march 9']=90
t['march 10']=100
t['march 11']=110

t.array
del t['march 11']
print(t.array)
