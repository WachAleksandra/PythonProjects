def hsh(x, n):
    return hash(x) % n

class ChainDict:
    def __init__(self, n=10):
        self._keys = [None for _ in range(n)]
        self._vals = [None for _ in range(n)]
        self.n = n
    
    def find_index(self, key):
        x = hsh(key, self.n)
        if self._keys[x] is not None:
            for i in range(len(self._keys[x])):
                if self._keys[x][i] == key:
                    return x, i
        return x, -1
        
    def __getitem__(self,key):
        x, i = self.find_index(key)
        if i != -1:
            return self._vals[x][i]
        else:
            raise Exception("No such key in this dict.")
           
    def __setitem__(self, key, value):
        x, i = self.find_index(key)
        if self._keys[x] is None:
            self._keys[x] = [key]
            self._vals[x] = [value]
        elif i == -1:
                self._keys[x].append(key)
                self._vals[x].append(value)   
        else:
            for i in range(len(self._keys[x])):
                 if self._keys[x][i] == key:
                      self._vals[x][i] = value
                      
    def __delitem__(self,key):
        x, i = self.find_index(key)
        if i != -1:
            self._keys[x][i] = self._keys[x][-1]
            self._keys[x].pop(i)
            self._vals[x].pop(i)
            
d = ChainDict(10)
d[9]=2
d[9]=3
d[19]=4
print(d[9])
del d[9]
print(d[9])


