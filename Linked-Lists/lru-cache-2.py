
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}
        self.count = 0
        self.start = None
        self.end = None

    def get(self, key):
        node = self.nodes.get(key)

        if not node:
            return None
        self.move_to_front(node)
        return node.val

    def put(self, key, val):

        node = self.nodes.get(key)
        if node:
            node.val
            self.move_to_front(node)
            return
        
        if self.count == self.capacity:
            if self.end:
                old_end = self.end
                self.remove(old_end)
                del self.nodes[old_end.key]
        else:
            self.count += 1

        node = Node(key, val)
        self.insert(node)
        self.nodes[key] = node



    def insert(self, node):
        node.prev = None
        node.next = self.start
        if self.start:
            self.start.prev = node
        
        self.start = node
        if not self.end:
            self.end = node
            
    def remove(self, node):
        print(node.val)
        print(self.nodes)
        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev

        if node == self.start:
            self.start = node.next
        
        if node == self.end:
            self.end = node.prev
        

    def move_to_front(self, node):
        self.remove(node)
        self.insert(node)

cache = LRUcache(2)
cache.put('user1', 'Alex')
cache.put('user2', 'Tim')
cache.put('user3', 'Great')
cache.put('user4', 'Giant')
print(cache.get('user4'))    


