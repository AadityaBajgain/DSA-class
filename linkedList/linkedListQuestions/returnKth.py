from LinkedListClass import LinkedList


def return_nth_to_last(ll:LinkedList, n)->LinkedList:
    first = ll.head
    second = ll.head
    
    for _ in range(n):
        if second is None:
            return None
        second = second.next
    
    while second:
        first = first.next
        second = second.next
        
    return first


ll = LinkedList()
ll.add(10)
ll.add(11)
ll.add(12)
ll.add(11)
ll.add(10)
ll.add(13)
ll.add(14)
ll.add(15)
ll.add(11)
ll.add(13)

print(ll)
print(return_nth_to_last(ll,2))