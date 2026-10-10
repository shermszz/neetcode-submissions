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
    vector<vector<int>> levelOrder(TreeNode* root) {
        /* 
            Goal: Return the nodes level by level, from left to right

            We can make use of a queue to continuosly add elements inside at every level
            Initialize with the first root node first, then for every node inside the queue, add the left then the right
            Always have a fresh list in every iteration to add the elements in that level
        */
        if (root == nullptr) return {};

        std::queue<TreeNode*> q; // Takes in a list of TreeNode pointers so that we have access to their left and right pointers
        q.push(root);
        std::vector<vector<int>> res;
        while (q.size() != 0) {
            std::vector<int> level_i_list; // Declare a new list for every level order 
            int level_size = q.size(); // Make the size static at this point
            for (int i = 0; i < level_size; i++) {
                TreeNode* curr = q.front();
                q.pop();
                level_i_list.push_back(curr->val);
                if (curr->left != nullptr) q.push(curr->left);
                if (curr->right != nullptr) q.push(curr->right);
            }
            res.push_back(level_i_list);
        }
        return res;

    }
};
