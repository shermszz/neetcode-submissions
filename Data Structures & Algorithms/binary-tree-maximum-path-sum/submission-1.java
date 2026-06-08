/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int maxSum = Integer.MIN_VALUE; //Keep a maximum sum counter
   
    public int dfs(TreeNode node) { 
        if (node == null) return 0;

        int left_val = Math.max(0, dfs(node.left)); // If left_val is going to be negative, no point adding it
        int right_val = Math.max(0, dfs(node.right));
        
        int currValue = node.val;
        this.maxSum = Math.max(maxSum, currValue + left_val + right_val);

        return currValue + Math.max(left_val, right_val);

    }

    public int maxPathSum(TreeNode root) {
        if (root == null) return 0;
        this.maxSum = root.val; // Initialise with the root value first
        
        dfs(root);
        // Run DFS from the root, finding the maximum diameter of the tree and comparing the sum to always get the maximum
        return this.maxSum;
    }
}

/**
=========================================================
KEY LEARNINGS: Binary Tree Maximum Path Sum (LeetCode 124)
=========================================================

CORE CONCEPTS:
1. Split vs. Straight Line: 
   - A path can only "split" once (forming the peak of a mountain). 
     We check this sum to update our global tracker: `node.val + left + right`.
   - When returning to a parent, we must choose a single straight line: 
     `node.val + max(left, right)`.
2. Active Pruning: Never block a negative node from being searched. 
   Instead, prune negative branch contributions on the way back up using 
   `Math.max(0, dfs(child))`.

GUIDING HINTS:
- Initialize the global maximum tracker to `Integer.MIN_VALUE` (Java) or 
  `float('-inf')` (Python) so a tree of purely negative values updates correctly.
- Post-Order Traversal: You must calculate your children's values fully 
  before you can make a decision about your own node.
- Time: O(N) because every node is visited exactly once.
- Space: O(H) call stack overhead.
=========================================================
**/
