# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        lis = []
        lis = self.GetLis(root,lis)
        for i in range(len(lis)):
            print("i = ",i,"    val= ",lis[i])
        min_idx = 0
        max_idx = 0
        for i in range(int(len(lis)/2)):
            if (2*i + 1) < len(lis) and lis[2*i + 1] == None:
                print("2*i + 1 = ",lis[2*i + 1], "  i = ",i)
                if min_idx == 0:
                    min_idx = i
                min_idx = min(min_idx,i)
            if (2*i + 2) < len(lis) and lis[2*i + 2] == None:
                print("2*i + 2 = ",lis[2*i + 2], "  i = ",i)
                if min_idx == 0:
                    min_idx = i
                min_idx = min(min_idx,i)

            if min_idx == 0:
                min_idx = i
            max_idx = i
        print("min_idx = ",min_idx)
        print("max_idx = ",max_idx)
        if max_idx - min_idx > 1:
            return False
        return True

    def GetLis(self,root,lis):
        tmpLis = []
        tmpLis.append(root)
        while len(tmpLis):
            tmp = tmpLis.pop(0)
            lis.append(tmp.val)
            if tmp.left:
                tmpLis.append(tmp.left)
            if tmp.right:
                tmpLis.append(tmp.right)
        return lis

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self,root):
        if not root:return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1:return -1
        return max(left,right) + 1 if abs(left-right) <2 else -1

    def CreateTree(self,nums):
        node_list = []
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            node_list.append(node)
        
        if len(node_list) >0:
            last_idx = int(len(nums)/2)-1
            for i in range(last_idx):
                if node_list[2*i + 1].left is None:
                    node_list[i].left = node_list[2*i +1]
                if node_list[2*i +2].right is None:
                    node_list[i].right = node_list[2*i+2]
            
            node_list[last_idx].left = node_list[last_idx * 2 +1]
            if len(nums) %2 == 1:
                node_list[last_idx].right = node_list[last_idx *2 +2]
        return node_list

def print_all(node):
    if node is not None:
        print(node.val)
        print_all(node.left)
        print_all(node.right)

def main():
    test1 = [3,9,20,None,None,15,7] #true
    test2 = [1,2,2,3,3,None,None,4,4] #false
    treeNode1 = Solution().CreateTree(test1)
    treeNode2 = Solution().CreateTree(test2)
    # print_all(treeNode1[0])
    # print_all(treeNode2[0])
    print("第一棵树",Solution().isBalanced(treeNode1[0]))
    print("第二棵树",Solution().isBalanced(treeNode2[0]))

if __name__ == "__main__":
    main()    