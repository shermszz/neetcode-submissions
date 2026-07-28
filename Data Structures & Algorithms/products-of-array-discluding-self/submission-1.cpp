class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n, 1); // Creates a prefix array of size n, with all default values to 1
        vector<int> suffix(n, 1);
  
        int running_product = 1;
        for (int i = 1; i < n; i++) {
            int prev_val = nums[i - 1];
            running_product *= prev_val;
            prefix[i] = running_product;
        }

        // // --- DEBUG PRINTING PREFIX ---
        // cout << "Prefix array: ";
        // for (int val : prefix) {
        //     cout << val << " ";
        // }
        // cout << endl; // Move to the next line when done
        // // -----------------------------

        running_product = 1;
        for (int i = n - 2; i >= 0; i--) {
            int after_val = nums[i + 1];
            running_product *= after_val;
            suffix[i] = running_product;
        }

        // // --- DEBUG PRINTING SUFFIX ---
        // cout << "Suffix array: ";
        // for (int val : suffix) {
        //     cout << val << " ";
        // }
        // cout << endl;
        // // -----------------------------

        vector<int> result(n);
        for (int i = 0 ; i < n; i++) {
            result[i] = prefix[i] * suffix[i];
        }
        
        return result;

    }
};
