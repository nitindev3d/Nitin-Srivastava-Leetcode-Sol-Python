def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    aLen = bLen = 0
    tempA = headA
    while tempA.next != None:
        aLen += 1
        tempA = tempA.next

    tempB = headB
    while tempB.next != None:
        bLen += 1
        tempB = tempB.next

    if tempA == tempB:
        tempA, tempB = headA, headB

        if aLen > bLen:
            for i in range(aLen - bLen):
                tempA = tempA.next
        else:
            for i in range(bLen - aLen):
                tempB = tempB.next

        if tempA == tempB:
            return tempA
        while tempA != tempB:
            tempA, tempB = tempA.next, tempB.next
        return tempA
    return None