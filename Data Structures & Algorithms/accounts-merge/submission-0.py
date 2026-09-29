class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            accounts[i][0] is always a user's name. The rest are emails of the account.

            Two accounts can be merged if the account names are the same and amongst all their emails, ther eis at least ONE email that is the same. 

            We want to return [name, <all the relevant emails in sorted order>]

            Idea:
                - We cannot use a hashmap because names are not unique
                - Instead, we can use the emails themselves as the nodes
        REDO THIS QUESTION this shit hard
        """

        # First, lets build an adj_list to store the connections between emails
        email_graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            # Now connect every email to this first email in the list
            for i in range(1, len(account)):
                email = account[i]
                email_to_name[email] = name # Remember the name that held this email
                
                # Undirected graph edges
                email_graph[first_email].append(email)
                email_graph[email].append(first_email)

        print(email_graph)
        visited = set()
        res = []
        
        for email in email_to_name:
            if email not in visited:
                # We found a brand new person
                connected_emails = []
                def dfs(email: str) -> None:
                    visited.add(email)
                    connected_emails.append(email)
                    for neighbour in email_graph[email]:
                        if neighbour not in visited:
                            dfs(neighbour)  
            
                dfs(email)

                connected_emails.sort()
                res.append([email_to_name[email]] + connected_emails) 

        return res



