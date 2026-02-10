# Write a class LRUCache(n) that accepts a size limit n.
# It supports:
# - get(key): return value if present, otherwise None
# - set(key, value): insert or update a key
# Both operations run in O(1) time using:
# - A hashmap for fast lookup
# - A doubly linked list to track usage order


class Node:
    def __init__(self, key, val):
        # Each node stores a key-value pair
        # and pointers to previous and next nodes
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, n):
        self.n = n                    # Maximum cache capacity
        self.count = 0                # Current number of items
        self.nodes = {}               # HashMap: key -> Node (O(1) lookup)
        self.start = None             # Most recently used (head)
        self.end = None               # Least recently used (tail)
    
    def get(self, key):
        # Retrieve node from hashmap
        node = self.nodes.get(key)

        # If key does not exist, return None
        if not node:
            return None

        # Move accessed node to the front (most recently used)
        self.move_to_front(node)

        # Return the value
        return node.val


    def set(self, key, val):
        # Check if key already exists
        node = self.nodes.get(key)

        if node:
            # Update value if key exists
            node.val = val

            # Move node to front since it's recently used
            self.move_to_front(node)
            return

        # If cache is full, evict the least recently used item
        if self.count == self.n:
            if self.end:
                # Remove LRU node from hashmap
                del self.nodes[self.end.key]

                # Remove LRU node from linked list
                self.remove(self.end)
        else:
            # Otherwise, increase cache size
            self.count += 1
        
        # Create a new node
        node = Node(key, val)

        # Insert it at the front (most recently used)
        self.insert(node)

        # Store reference in hashmap
        self.nodes[key] = node
        
    def insert(self, node):
        # Insert node at the front of the linked list

        # If the list is empty, this node is also the tail
        if not self.end:
            self.end = node

        # Link the new node with the current head
        if self.start:
            node.next = self.start
            self.start.prev = node

        # Update head pointer
        self.start = node

    def remove(self, node):
        # Remove node from the linked list

        # Link previous node to next node
        if node.prev:
            node.prev.next = node.next

        # Link next node to previous node
        if node.next:
            node.next.prev = node.prev

        # If node is head, update head
        if self.start == node:
            self.start = node.next

        # If node is tail, update tail
        if self.end == node:
            self.end = node.prev
    
    def move_to_front(self, node):
        # Remove node from its current position
        self.remove(node)

        # Reinsert node at the front (most recently used)
        self.insert(node)


cache = LRUCache(2)
cache.set('user1', 'Alex')
print(cache.get('user1'))    




    
    




