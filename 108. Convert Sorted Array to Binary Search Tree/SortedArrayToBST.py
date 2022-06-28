def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if nums == []:  # if list is empty then no elements left to make new nodes
        return None

    mid = len(nums) // 2

    #       Add a new node with value at the middle of each subarray
    node = TreeNode(nums[mid])

    node.left = self.sortedArrayToBST(nums[:mid])  # make recursive call to make left node
    node.right = self.sortedArrayToBST(nums[mid + 1:])  # make right node with recursive call

    #       return node after creation
    return node
