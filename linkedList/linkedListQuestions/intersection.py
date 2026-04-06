# Given the two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on the reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

from LinkedListClass import LinkedList, Node

def findIntersection(l1:LinkedList, l2:LinkedList) -> Node:
    
    if l1.tail != l2.tail:
        return None
    
    len1 = len(l1)
    len2 = len(l2)


    longer = l1 if len1 > len2 else l2
    shorter = l1 if len1 < len2 else l2
    
    diff = len(longer) - len(shorter)
    
    longer_node = longer.head
    shorter_node = shorter.head
    
    
    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node != longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
        
    return longer_node


    


#helper function


def add_node(l1,l2,val):
    new_node = Node(val)
    
    l1.tail.next = new_node
    l1.tail = new_node
    
    l2.tail.next = new_node
    l2.tail = new_node



l1 = LinkedList()

l1.generate(3, 0,10)

l2 = LinkedList()
l2.generate(4, 0, 10)



add_node(l1,l2, 12)
add_node(l1,l2,14)

print(l1)
print(l2)

print(findIntersection(l1,l2).value)