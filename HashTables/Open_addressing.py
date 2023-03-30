def hsh(x, n):
    return hash(x) % n

class OpenDict:
     def __init__(self, n=10):
        self._keys = [None for _ in range(n)]
        self._vals = [None for _ in range(n)]
        self.n = n
        
          
     def scan_for(self, key):
         f = hsh(key, self.n)  #h(k) % len(data)
         s = 1
         d = -1
         i = f
         while self._keys[i] != None:
             if self._keys[i] == -1:
                 if d == -1: d = i
             else:
                 if self._keys[i] == key: return i
             i = (i+s) % len(self._keys)
             if i==f:
                 return d
         if d != -1: return d
         return i

     def __getitem__(self, key):
         i = self.scan_for(key)
         if i == -1 or self._keys[i] == None or self._keys[i] == -1:
             return None
         return self._keys[i], self._vals[i]
    
    
     def __setitem__(self, key, value):
          i = self.scan_for(key)
          if i == -1:
             raise Exception("Lack of space.")
          elif i != -1:
              self._keys[i] = key
              self._vals[i] = value
              
     def __delitem__(self, key):
         i = self.scan_for(key)
         if i != -1 and self._keys[i] != None:
             self._keys[i] = -1
             self._vals[i] = -1
            
        
        
d = OpenDict(10)
d[5] = "abc"
d[15] = "abcd"
d[25] = "abcdf"
d[35] = "abcdf"
d[9] = "bcd"
print(d._keys)
print(d._vals)
del d[5]        
print(d._keys)
print(d._vals)

        
    
