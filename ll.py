class LLNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DLLNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LL:
    def __init__(self, head):
        self.head = head

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count 
   
    def insertAtHead(self, node):
        current = self.head
        node.next = current
        self.head = node

    def insertAtTail(self, node):
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        
    def insertAtPosition(self, node, position):
        current = self.head
        prev = None
        count = 1

        if position < 1 or position == 1: 
            node.next = current
            self.head = node
            return
        
        if position >= self.size():
            while current.next:
                current = current.next
            current.next = node
            return
        
        while current and count < position:
            prev = current
            current = current.next
            count += 1

        node.next = current
        prev.next = node

    def removeFirstElement(self):
        if self.head and self.head.next:
            self.head = self.head.next
            return
        self.head = None
         
    
    def removeLastElement(self):
        if self.head and self.head.next:
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            return
        self.head = None

        


    


    def removeAtPostion(self, position):
        current = self.head
        prev = None
        count = 1

        if position < 1 or position > self.size():
            return 

        if position == 1:
            current = current.next
            self.head = current
            return 
        
        while count < position:
            prev = current
            current = current.next
            count += 1
        prev.next = current.next

        
        

    def reverseRecursive(self):
        def innerReverse(current, prev):
            if not current:
                return prev
            nextNode = current.next
            current.next = prev
            return innerReverse(nextNode, current)
        self.head = innerReverse(self.head, None)
    
    def reverseIterative(self):
        prev = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

    def findNode(self, value):
        current = self.head
        while current:
            if current.val == value:
                return current
            current = current.next
        return None
    
    #LeetCode 143
    def moveTailBehindHead(self):
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        current.next = self.head.next
        self.head.next = current

    def print(self):
        current = self.head
        while current:
            print(current.val,end=" ")
            current = current.next
        print(end="\n\n")


class DLL: 
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def print(self):
        head = self.head
        while head is not None:
            print(" ", head.val,end="")
            
            head = head.next


def reverse(node) -> LLNode:
    if(node == None):
        return node
    

    if(node.next == None):
        return node
    

    newHead = reverse(node.next)
    node.next.next = node
    node.next = None
    return newHead


def mergeTwoLists(nodeOne, nodeTwo) -> LLNode:

    if not nodeOne:
        return nodeTwo
    
    if not nodeTwo:
        return nodeOne
    
    newHead = LLNode()
    finalHead = newHead
    currentN1 = nodeOne
    currentN2 = nodeTwo

    while currentN1 and currentN2:
        if currentN1.val <= currentN2.val and currentN1 and currentN2:
            newHead.next = currentN1
            currentN1 = currentN1.next
            newHead = newHead.next
        else:
            newHead.next = currentN2
            currentN2 = currentN2.next
            newHead = newHead.next
        
    if not currentN1:
        newHead.next = currentN2
    
    if not currentN2:
        newHead.next = currentN1

    return finalHead.next

def mergeTwoListsInplace(nodeOne, nodeTwo) -> LLNode:

    if not nodeOne:
        return nodeTwo
    
    if not nodeTwo:
        return nodeOne
    
    newHead = LLNode()
    finalHead = newHead

    while nodeOne and nodeTwo:
        if nodeOne.val <= nodeTwo.val and nodeOne and nodeTwo:
            newHead.next = nodeOne
            nodeOne = nodeOne.next
            newHead = newHead.next
        else:
            newHead.next = nodeTwo
            nodeTwo = nodeTwo.next
            newHead = newHead.next
        
    if not nodeOne:
        newHead.next = nodeTwo
    
    if not nodeTwo:
        newHead.next = nodeOne

    return finalHead.next


if __name__ == "__main__":
    node1 = LLNode(1)
    node2 = LLNode(2)
    node3 = LLNode(3)
    node4 = LLNode(4)


    node1.next = node2
    node2.next = node3
    node3.next = node4

    dNode1 = DLLNode(1)
    dNode2 = DLLNode(2)
    dNode3 = DLLNode(3)
    dNode4 = DLLNode(4)

    dNode1.next = dNode2
    dNode1.prev = None
    dNode2.next = dNode3
    dNode2.prev = dNode1
    dNode3.next = dNode4
    dNode3.prev = dNode2
  

    linkedList = LL(node1)
    DLinkedList = DLL(dNode1,dNode4)

    #linkedList.print()
    #DLinkedList.print()

 
    node5 = LLNode(5)
    linkedList.insertAtPosition(node5,10)
    print("LL after adding node.val = 5")
    linkedList.print()

    linkedList.reverseIterative()
    print("LL after it was reversed itratively")
    linkedList.print()

    linkedList.reverseRecursive()
    print("LL after it was reversed recursively")
    linkedList.print()

    currHead = linkedList.head
    print(currHead.val)
    linkedList = LL(reverse(currHead))
    linkedList.print()

    linkedList.removeAtPostion(5)
    # linkedList.removeFirstElement()
    # linkedList.removeLastElement()
    linkedList.moveTailBehindHead()
    linkedList.moveTailBehindHead()
    linkedList.print()
    print(linkedList.size())


   
    node10 = LLNode(1)
    node20 = LLNode(2)
    node30 = LLNode(3)
    node40 = LLNode(4)
    node50 = LLNode(35)
    node60 = LLNode(44)

    node10.next = node40
    node20.next = node30
    node30.next = node50
    node50.next = node60

    mergedList = mergeTwoListsInplace(node10,node20)
    mergedLL = LL(mergedList)
    mergedLL.print()



    

