/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
                if(headA == null || headB == null) return null;
        
        ListNode list1 = headA;
        ListNode list2 = headB;
        int count1 = 0;
        int count2 = 0;
        int adjustment = 0;

        while(list1 != null){
            count1++;
            list1 = list1.next;
        }

        while(list2 != null){
            count2++;
            list2 = list2.next;
        }

        if (count1 > count2){
            adjustment = count1 - count2;
            list1 = headA;
            list2 = headB;
            for(int index = 0; index < adjustment; index++ ){
                list1 = list1.next;
            }
        } 
        else if(count2 > count1){
            adjustment = count2 - count1;
            list1 = headA;
            list2 = headB;
            for(int index = 0; index < adjustment; index++ ){
                list2 = list2.next;
            }
        }
        else if(count1 == count2){
            list1 = headA;
            list2 = headB;
        }

        while(list1 != null && list2 != null){
            if(list1 == list2){
                return list1;
            }
            list1 = list1.next;
            list2 = list2.next;
        }
        return null;
    }
}