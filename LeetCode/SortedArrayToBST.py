

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        print("``````````````")

    def sortedArrayToBST(self, nums) -> TreeNode:
        return self.sortedArrayToBST2(nums,0,len(nums))
    
    def sortedArrayToBST2(self,nums,begin,end) -> TreeNode:
        tmpLength = end - begin
        if tmpLength < 1:
            return 
        mid = int((begin + end)/2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST2(nums,begin,mid)
        root.right = self.sortedArrayToBST2(nums,mid+1,end)
        return root

def PrintTree(tree):
    if tree == None:
        return

    if tree.val == None:
        return
    print(tree.val)
    PrintTree(tree.left)
    PrintTree(tree.right)

def main():
    nums = [-10, -3, 0, 5, 9]
    tmpTree = Solution().sortedArrayToBST(nums)
    PrintTree(tmpTree)

if __name__ == "__main__":
    main()