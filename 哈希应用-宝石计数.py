class HashTable():
	def __init__(self):
		self.size = 10
		self.slots = [None] * self.size
	
	def hashfunction(self,key,size):
		return key%size
	
	def rehash(self,oldhash,size):
		return (oldhash+1)%size
		
	def put(self,key):
		hashvalue = self.hashfunction(key,10)
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
		else:
			nextslot = self.rehash(hashvalue,10)
			while self.slots[nextslot] != None:
				nextslot = self.rehash(nextslot,10)
			if self.slots[nextslot] == None:
				self.slots[nextslot] = key
				
	def get(self,key):
		
		if key in self.slots:
			return 1
		else:
			return 0

data1 = map(ord,input())
data1 = list(data1)
data2 = map(ord,input())
data2 = list(data2) 	
myhash = HashTable()
for i in range(len(data1)):
	myhash.put(data1[i])#将宝石存入哈希表
p = []

for j in range(len(data2)):
	 p.append(myhash.get(data2[j]))
n = 0
for t in range(len(p)):
	n = n + p[t]
print(n)
print(data1)
print(data1)
print(data1)
print(data3)
print(data4)
<<<<<<< HEAD
print(data8)
=======
print(data5)
print(data6)

>>>>>>> b047d4a (add data5)

