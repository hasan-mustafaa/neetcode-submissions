class DoublyNode:
    def __init__(self, val = -1, nxt = None, prev = None, key = -1):
        self.val = val
        self.nxt = nxt
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.dummyHead = DoublyNode()
        self.dummyTail = DoublyNode()
        self.dummyHead.nxt = self.dummyTail
        self.dummyTail.prev = self.dummyHead

        self.map = {}
        self.capacity = capacity

    def addNode(self, node):
        nxtNode = self.dummyHead.nxt
        node.prev, node.nxt = self.dummyHead, nxtNode
        self.dummyHead.nxt, nxtNode.prev = node, node
    
    def removeNode(self, node):
        prevNode, nxtNode = node.prev, node.nxt
        prevNode.nxt, nxtNode.prev = nxtNode, prevNode
        

    def get(self, key: int) -> int:
        if key not in self.map: 
            return -1
        else:
            node = self.map[key]
            if self.dummyHead.nxt is node:
                return node.val
            else:
                self.removeNode(node)
                self.addNode(node)
                return node.val
        

    def put(self, key: int, value: int) -> None:

        if key not in self.map:
            node = DoublyNode(value, key=key)
            self.addNode(node)
            self.map[key] = node
        
            if len(self.map) == self.capacity + 1:
                delNode = self.dummyTail.prev
                self.removeNode(delNode)
                del self.map[delNode.key]
        else:
            node = self.map[key]
            node.val = value

            if self.dummyHead.nxt is node:
                return
            else:
                self.removeNode(node)
                self.addNode(node)

    """
    LL Initialisaion:
    - Initialise, self, val, nxt, prev and key
    - key is needed, so you can delete the right pair from hashmap

    Class:
    - Initialise map, capacity
    - Initialise dummyHead, and dummyTail and connect them using .nxt and .prev


    Put:
        Case 1: Key/Value Pair doesn't exist return -1
        Case 2: Key/Value Pair exists, but already at the front, so just return node.val
        Case 3: Key/Value Pair exists, but not at the front, remove node from current location in LL, and add to front
    
    Get:
        Case 1: Value Not in Map, add Node to LL, and map
        Case 2: Value Not in Map, added Node etc, but exceeds capacity, hence get node previous to tail, remove from LL and Map
        Case 3: Value already in Map, update value, if first node already, then return, else delete the node from current position and addNode to front

    Other:
        Add Node: Adds node to the front of the list
        RemoveNode: Removes node, from wherever it is in the LL

    """

    



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)