class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            We want to merge all the accounts where names are the same and any one of their emails match, then for that person, we merge the 2 lists together
            We also want the lists to be in sorted order

            Idea:
                - The name is not a unique key value that we can use
                - We can use the email instead as the unique key, since all emails are distinct
                - Emails in the same list are all connected together and should form one connected component
                - instead of forming a complete graph, we will just take the first email and connect it with the rest of the emails in the list in an undirected graph fashion

                - We still need the names later, so we need to keep track of each email and the name of the person holding this email individually inside a hashmap

                - Once we have set up the graph and the hashmap of email --> name, we will start running DFS for on each connected component
                - We would thus need a visited set to track which emails we have already seen. 
                - As we run DFS, we will first grab the name of the person with the email and created an internal list to keep appending emails to. 
                - Once DFS finishes for the inital email, we will appedn the name of the person with a sorted(email list) to the result
        """

        adj_list = defaultdict(list)
        email_to_name = {} 
        for acc in accounts:
            name, first_email = acc[0], acc[1]
            for i in range(1, len(acc)):
                e = acc[i]
                email_to_name[e] = name

                adj_list[first_email].append(e) # first_email --> e
                adj_list[e].append(first_email) # e --> first_email
                # Overall this creates first_email <--> e for every e

        visited = set()
        res = []

        for email, name in email_to_name.items():
            if email not in visited:
                connected_emails = [] # The list of emails that are associated with `name` person
                def dfs(e: str) -> None:
                    if e in visited:
                        return
                    visited.add(e)
                    # print("adding to connected_emails", e)
                    connected_emails.append(e)
                    for neighbour in adj_list[e]:
                        dfs(neighbour)
                dfs(email) # Find all the connected emails and add it into the connected_emails

                # Once we are done finding all the emails for this person, we will add it into res
                connected_emails.sort()
                res.append([name] + connected_emails)
        return res


        
