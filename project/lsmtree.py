#Build an LSM Tree

import hashlib

#Use bloomfilter to check for duplicates, if they exist get rid of them and keep 1 copy
#
#store keys
#check for duplicates
#implement hashing
#store from mem table to disk (make memtable class) = flush data after a certain point
import random
List=[A,B,C,D,E]
#Level 0 A,B,C,D,E
#Level 1 A,C,E
#Level 2 A,E
MAX_LEVEL = 16
#Node for Skip-List
class Node:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)#assigns a random level
class SkipList:
    def __init__(self):
        self.head = Node(None, None, MAX_LEVEL)
        self.level = 0
    def random_level():
        level = 0
        while random.random() < 0.5 and level < MAX_LEVEL:
            level += 1
        return level
    def insert(self, key, value):
        update = [None] * (MAX_LEVEL + 1) #gives the node before the insert
        current = self.head
        
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
            #checks where to insert the node
        current = current.forward[0]

        #Updates key (if it exists)
        if current and current.key == key:
            current.value = value
            return

        #gives the node a level
        new_level = random_level()

        #if there is no level x yet, it gets added
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level

        #makes the new node and inserts its level
        new_node = Node(key, value, new_level)

        #pointer get connected and it gets inserted into the linked lists on multiple levels
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
    
    def search(self, key):
        current = self.head #takes for the first value of the highest value
        for i in reversed(range(self.level + 1)): #goes through the levels
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i] #jumps from value to value and checks if the key is bigger. if it is, jumps a level lower
        current = current.forward[0] #goes to the next node on level 0, because the current current is still the bigger node
        if current and current.key == key: #checks if its the searched
            return current.value #returns the value
        return None


class LSMTree:
    def __init__(self):
        self.memtable = MemTable()  # In-memory (RAM)
        self.sstables = []  # On-disk (SSD/HDD)
    
    def put(self, key, value):
        # Entry starts in MEMORY (MemTable)
        self.memtable.put(key, value)
        
        #When MemTable is FULL, flush to DISK
        if self.memtable.is_full():
            self.flush_memtable_to_disk()
    
    def flush_memtable_to_disk(self):
        #Get all entries from memory
        entries = self.memtable.get_all_entries()


class SSTable: #first thing that gets the data and sorts it
    def __init__(self):
        pass


class MemTable:
    """Super simple - just stores data until full"""
    
    def __init__(self, max_size_bytes=1_000_000):  # 1MB
        self.data = {}  #dictionary
        self.max_size = max_size_bytes
        self.current_size = 0
    
    def put(self, key, value):
        # Calculate size of this entry
        entry_size = len(key) + len(value)
        
        # Check if adding would exceed limit
        if self.current_size + entry_size > self.max_size:
            return False  # FULL - need to flush to disk!
        
        # Store in memory
        self.data[key] = value
        self.current_size += entry_size
        return True
    
    def get_all_entries(self):
        """Get EVERYTHING to write to disk"""
        return list(self.data.items())
    
    def clear(self):
        
        self.data.clear()
        self.current_size = 0
    
    def is_full(self):
        return self.current_size >= self.max_size
    
    def size(self):
        return self.current_size

#test
memtable = MemTable(max_size_bytes=1000)  # 1KB limit

# Add data until full
for i in range(1000):
    key = f"user{i}"
    value = f"data_{i}"
    
    if not memtable.put(key, value):
        print(f"MemTable FULL at {i} entries!")
        print(f"  Current size: {memtable.size()} bytes")
        
        # Flush to disk
        entries = memtable.get_all_entries()
        print(f"  Flushing {len(entries)} entries to disk")
        
        # Write to SSTable
        memtable.clear()
        print(f"Clearing MemTable, size now: {memtable.size()} bytes")
        
        # Retry the put
        memtable.put(key, value)

def get_partition_hash(self):
    pass

#make 2 hash classes and hash partitions to split the data in multiple parts so the algorithm can be even more efficient.
def _hash_1(x):
    pass

def _hash_2(y):
    pass



class Flusher: # flusher that checks if the table is full yet/checks the limit 
    def __init__(self,amount):
        pass




class Disk: #flusher moves the data from the memtable to the disk and stores it
    def __init__(self):
        pass

class Storage(memtable,SSTable):
    def __init__(self):
        pass

