# write the code to partition the linked list around the value of x, such that all nodes lesser than x comes before the node greater then equal to node x


from LinkedListClass import LinkedList, Node


def partition(ll:LinkedList, x) -> LinkedList:
    # current = ll.head
    # stail = ll.head
    
    # while current:
    #     next_node = current.next
    #     current.next = None
        
    #     if current.value < x:
    #         current.next = ll.head
    #         ll.head = current
    #     else:
    #         stail.next = current
    #         stail = current
    #     current = next_node
        
    # return ll.head
    
    first = LinkedList()
    second = LinkedList()
    
    
    # ftail, stail = first, second
    
    while ll.head:
        if ll.head.value < x:
            first.add(ll.head.value)
        else:
            second.add(ll.head.value)
            
        ll.head = ll.head.next
        
    first.tail.next = second.head
    
    second.tail.next = None
    
    return first

custom_ll = LinkedList()
custom_ll.generate(10,30,210)

print(custom_ll)

print(partition(custom_ll, 100))
print(custom_ll)