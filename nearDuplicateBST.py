class TreeNode(object):
    def __init__(self,x,i):
        self.val=x
        self.index=i
        self.left=None
        self.right=None

class Solution(object):
    def insert(self, head, num, i, k, t):

        temp=head
        while temp:
            prev=temp
            if (temp.val-t<=num and temp.val+t>=num) and (temp.index+k>=i and temp.index-k<=i):
                return True
            elif temp.val==num:
                temp.index=i
                return False
            elif temp.val>num:
                temp=temp.left
            elif temp.val<num:
                temp=temp.right

        if prev.val>num:
            prev.left=TreeNode(num,i)
        else:
            prev.right=TreeNode(num,i)



    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        n=len(nums)
        bucket={}
        for i in range(n):
            if i > k:
                del bucket[nums[i-k-1]/t]
            m=bucket[nums[i]/t]

            if m in bucket:
                return True
            elif m-1 in bucket and abs(nums[i]-bucket[m-1])<=t:
                return True
            elif m+1 in bucket and abs(nums[i]-bucket[m+1])<=t:
                return True

            bucket[m]=nums[i]

        return False


