class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            int len = s.length();
            sb.append(len);
            sb.append("#");
            sb.append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> ans = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            //1. Read up to the delimiter to find the length of the string
            StringBuilder num = new StringBuilder();
            while (str.charAt(i) != '#') {
                num.append(str.charAt(i));
                i++;
            }
            i++; // To bypass the # character
            int len = Integer.parseInt(num.toString());
            // System.out.println("Length is " + len);
            StringBuilder word = new StringBuilder(len);
            while (len-- > 0) {
                word.append(str.charAt(i));
                i++;
            }
            ans.add(word.toString());
        }
        return ans;
    }
}
