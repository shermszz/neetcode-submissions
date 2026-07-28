class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // we first iterate through the array nums, storing the (value, frequency) as we go
        unordered_map<int, int> count;

        for (int num : nums) {
            count[num]++;
        }

        // Then, we heapify based on the frequency
        priority_queue<pair<int, int>> maxHeap;
        for (const auto& i : count) {
            int val = i.first;
            int freq = i.second;

            maxHeap.push({freq, val});
        }

        // Then, we iterate through the heap k times extracting out the k most frequent elements
        vector<int> result;
        while (k-- > 0) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop(); // Remove the element
        }

        return result;

    }
};
