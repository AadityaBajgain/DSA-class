# you have two numbers represented by the linked list, where each node contains a single digit. The digit are stored in reversed order, such that 1s digits are at the head of the list. Write a function that adds the two number and returns the sum as a linked list.

# 4->5->6
# 3->7->3


from LinkedListClass import LinkedList

def sumNum(l1, l2):
    temp1 = l1.head
    temp2 = l2.head
    
    carry = 0
    
    temp_ll = LinkedList()

    
    while temp1 or temp2 or carry:
        result = carry
        if temp1:
            result += temp1.value
            temp1 = temp1.next
        if temp2:
            result += temp2.value
            temp2 = temp2.next
        temp_ll.add(int(result % 10))
        carry = result // 10
        
    return temp_ll


l1 = LinkedList()
l1.add(6)
l1.add(6)
l1.add(6)


l2 = LinkedList()
l2.add(5)
l2.add(4)
l2.add(5)


print(sumNum(l1,l2))