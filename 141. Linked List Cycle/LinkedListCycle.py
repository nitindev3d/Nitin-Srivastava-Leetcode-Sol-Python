def hasCycle(self, head: Optional[ListNode]) -> bool:
    p = q = head

    # Handling zero node edge case or single node is present and no cycle
    if p == None or p.next == None:
        return False
    elif p.next == p:  # if cycle is present on single node
        return True
    else:
        while q != None and q.next != None:
            p, q = p.next, q.next.next
            if p == q:
                return True
        return False