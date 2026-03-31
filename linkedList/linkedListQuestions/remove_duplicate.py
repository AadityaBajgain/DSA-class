# Remove Duplicates
# Write a function to remove duplicates from an unsorted linked list. Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5


from LinkedListClass import LinkedList


def remove_duplicate(ll:LinkedList) -> LinkedList:
    
    if ll is None:
        return
    
    current_node = ll.head
    prev = None
    
    while current_node:
        runner = current_node
        
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        prev = current_node
        current_node = current_node.next
        
    ll.tail = prev
    return ll



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


print("Linked List before: ",ll)
ll = remove_duplicate(ll)

print("Linked List after removing duplicates: ",ll)