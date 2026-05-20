class TimeMap {

    static class TimeValue {
        String value;
        int timestamp;

        public TimeValue(String value, int timestamp) {
            this.value = value;
            this.timestamp = timestamp;
        }
    }
    private HashMap<String, List<TimeValue>> timemap;
    //Key can have multiple values, so each key maps to a list of (value, timestamp) pairs

    public TimeMap() {
        this.timemap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        this.timemap.putIfAbsent(key, new ArrayList<>());
        this.timemap.get(key).add(new TimeValue(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (!this.timemap.containsKey(key)) {
            return "";            
        }
        String result = ""; int largest = 0; 
        List<TimeValue> list = this.timemap.get(key);
        int left = 0; int right = list.size() - 1;
        //Use binary search to find a value whose internal timestamp is <= timestamp
        while (left <= right) {
            int mid = left + ((right - left) / 2);
            TimeValue tv = list.get(mid);
            int timestamp_prev = tv.timestamp;
            if (timestamp_prev == timestamp) {
                return tv.value; //Already the largest possible
            } else if (timestamp_prev > timestamp) {
                //Need to find a smaller value
                right = mid - 1;
            } else {
                // Valid candidate, check if larger than ones we have already seen
                if (timestamp_prev > largest) {
                    result = tv.value;
                }
                left = mid + 1;
            }
        }
        return result;
    }
}
