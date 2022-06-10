class Hash_map:
    def __init__(self):
        self.size=10
        self.arry=[None for i in range(self.size)]

    # get the hash value of key using ord() method 

    def get_hash(self,key ):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.size
        #hash is the mode value of sum of ask key values of key to array size 

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arry[h]
    
    def __setitem__(self,key, value):
        h=self.get_hash(key)
        self.arry[h] = value
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arry[h] = val    
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arry[h] = None    

h=Hash_map()
h['march 6']=123
h['march 7']=124
h['march 8']=125

del h["march 7"]

print(h.arry)
