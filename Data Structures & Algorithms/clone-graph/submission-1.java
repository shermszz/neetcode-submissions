/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        //A deep copy is one that has the exact same values and structure, but different object addresses
        if (node == null) return null;

        HashMap<Node, Node> old_to_new = new HashMap<>(); // To store the old node to new node mappings

        // Once we need to have a hashmap of old to new nodes so that as we iterate through the graph later, we can manipulate the clone instead
        Queue<Node> queue = new LinkedList<>(); // To store the nodes that we need to track 

        // Plant the first clone into the hashmap
        int clone_val = node.val;
        Node cloned_node = new Node(clone_val);
        old_to_new.put(node, cloned_node);

        queue.add(node); // To process the node

        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            Node curr_clone = old_to_new.get(curr);
            for (Node n : curr.neighbors) {
                if (!old_to_new.containsKey(n)) {
                    // if the clone of the neighbour does not exist, we create one for it now
                    Node new_clone = new Node(n.val);
                    old_to_new.put(n, new_clone);
                    queue.add(n);
                }
                curr_clone.neighbors.add(old_to_new.get(n)); // Assign the neighbours to be the cloned version that is inside the hashmap
            }
        }
        return cloned_node;

    }
}