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
   

    def insertNode(self, node, position):
        head = self.head
        currentPosition = 1
        prevPos = position - 1
        while head is not None:
            
            if(currentPosition == 1 and position == 1):
                node.next = head
                self.head = node
                return self.head

            elif(currentPosition == prevPos):
                temp = head.next
                node.next = temp
                head.next = node
                return self.head
            
            currentPosition += 1
            head = head.next

            ##Add TODO: note

    def findNode(self, value):
        head = self.head
        index = 0
        while head is not None:
            if(head.val == value):
                return head, index
            else:
                head = head.next
                index += 1

        return None


        

    def print(self):
        head = self.head
        while head is not None:
            print(" ", head.val,end="")
            
            head = head.next


class DLL: 
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def print(self):
        head = self.head
        while head is not None:
            print(" ", head.val,end="")
            
            head = head.next



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

    #TODO: Need to fix this
    #node5 = LLNode(5)
    #linkedList.insertNode(node5,6)
    linkedList.print()

    nodeNew, index = linkedList.findNode(3)
    print("-------")
    print(nodeNew.val, index)
    

