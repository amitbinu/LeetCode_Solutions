# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_arr = []
        carry=0
        while (l1 != None and l2 != None):
            sum = carry + l1.val + l2.val
            stri = str(sum)
            if(len(stri)==2):
                carry=int(stri[0])
                sum=int(stri[1])
            else:
                carry=0
                    
            result_arr.append(sum)
            if(l1.next != None and l2.next == None):
                l1 = l1.next
                l2 = ListNode(0,None)
            elif (l1.next == None and l2.next != None):
                l1 = ListNode(0, None)
                l2 = l2.next
            else:
                l1 = l1.next
                l2 = l2.next
                
        if(carry!=0):
            result_arr.append(carry)
            
        result = ListNode(result_arr[len(result_arr)-1], None)
        for i in range(len(result_arr)-2,-1,-1):
            result = ListNode(result_arr[i],result)   
        return result

        
node3 = ListNode(3, None)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)
num2_node3=ListNode(4, None)
num2_node2 = ListNode(6, num2_node3)
num2_node1 = ListNode(5, num2_node2)
sol = Solution()
sol.addTwoNumbers(node1, num2_node1)
