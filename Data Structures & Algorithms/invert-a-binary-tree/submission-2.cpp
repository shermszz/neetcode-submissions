/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        /*
        GOAL: We want all the nodes on the left to be on the right and vice versa
            - A base case would be that a single node itself is already inverted
            - Otherwise, we will say that the left side of the node is the inverted of the right
            - The right is also the inverted of the left 

        Meaning for example 2: 
            - 3 still has a left and right node. 
            - So we do 3.left = invertTree(3.right) and 3.right = invertTree(3.left) 
        */

        // Base case first
        if (root == nullptr) {
            return root;
        }

        TreeNode* temp = root->left;

        //Otherwise, we need to invert the tree
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        return root;
    }

};
