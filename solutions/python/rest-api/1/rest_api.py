""" Module solving the REST API exercise from Exercism. """

import json

class RestAPI:
    """
    Despite the name, a class implementing a pseudo-database storing
    information on who owes whom money, with methods to add users and update
    the records of each individual user when a loan is made.
    """
    
    _USERS = "users"
    _CREDITORS = "owes"
    _DEBTORS = "owed_by"
    _NAME = "name"
    _BALANCE = "balance"
    
    def __init__(self, database = None):
        """ Constructor method, not complicated. """
        
        self._database = database if database else {RestAPI._USERS: []}

    def get(self, url: str, payload: str = None) -> str:
        """
        Provides a JSON-ified copy of the _database if payload is not
        specified, or the subset of the _database where items with values
        of the "name" field are found in the payload if it is specified.

        Parameters
        ----------
        url : str
            A "URL" identifying what type of get action to perform. There is
            actually only one option (returning a table of users), so this
            parameter is completely redundant.
        payload : str, optional
            A JSON-ified dictionary with key "name" and a value of a list of
            names (strings) that should be present in the _database. The 
            default value, however, is None.

        Returns
        -------
        str
            Actually a dictionary, just JSON-ified due to the conceit of the
            exercise. Consists of a copy of the _database if payload is not
            specified, or the subset of the _database where items with values
            of the "name" field are found in the payload if it is specified.

        Raises
        ------
        ValueError
            Raised if an invalid "URL" is provided to the method.
        """
        if url == "/" + RestAPI._USERS:
            return self._get_users(payload)
        
        raise ValueError("Invalid URL provided to get method")

    def post(self, url: str, payload: str) -> str:
        """
        Makes changes to the _database as specified by the "URL" parameter. The
        two available changes are:
            1: "/add": add a new user to the _database with the name specified
               in the payload and return a JSON-ified dictionary containing a 
               copy of the new user entry;
            2: "/iou": given a lender, borrower, and loan amount, update all
               loan-related fields appropriately. Return a JSON-ified copy of
               the changed entries like a mini-database.

        Parameters
        ----------
        url : str
            The .
        payload : str, optional
            A JSON-ified dictionary of some kind. There are two options,
            depending on the "URL" specified:
                1: "/add": A dictionary with key "user" and a string value 
                   which is a new user's name;
                2: "/iou": A dictionary with the keys:
                    a: "lender": (string) name of lender;
                    b: "borrower": (string) name of borrower;
                    c: "amount": (float) amount loaned.

        Returns
        -------
        str
            A JSON-ified dictionary. There are two possible values, depending
            on "URL":
                1: "/add": a copy of the new user record;
                2: "/iou": a mini-copy of the database containing only the
                   information on the lender and borrower after applying the
                   loan information.

        Raises
        ------
        ValueError
            Raised if a payload is not provided (since then it is unknown what
            changes are desired to the database).
        """
        
        if not payload:
            raise ValueError("Payload required for post method")
        
        if url == "/add":            
            return json.dumps(self._add_user(payload))
        
        if url == "/iou":      
            return json.dumps(self._change_balance(payload))
    
    def _add_user(self, payload: str) -> dict:
        """
        Adds a new user to the _database and returns a copy of the new entry
        for test purposes. A new user is assumed to neither owe nor be owed
        any money. Helper method for the "post" method to implement the "/add"
        functionality.

        Parameters
        ----------
        payload : str
            A JSON-ified dictionary with key "user" and a string value which is
            a new user's name.

        Returns
        -------
        dict
            A dictionary containing the new user entry.
        """
        
        name = json.loads(payload)["user"]
                            
        new_user = {
            RestAPI._NAME: name, 
            RestAPI._CREDITORS: {}, 
            RestAPI._DEBTORS: {}, 
            RestAPI._BALANCE: 0.0}
        
        self._database[RestAPI._USERS] = self._database[RestAPI._USERS].append(new_user)
        
        return new_user
    
    def _change_balance(self, payload: str) -> dict:
        """
        Given a lender, borrower, and loan amount, update all loan-related 
        fields appropriately. Return a copy of the changed entries like a 
        mini-database. Helper function for the "post" method to implement the
        "/iou" functionality.

        Parameters
        ----------
        payload : str
            A JSON-ified dictionary with the keys:
                a: "lender": (string) name of lender;
                b: "borrower": (string) name of borrower;
                c: "amount": (float) amount loaned.

        Returns
        -------
        dict
            A dictionary containing just the changed entries.
        """
        
        payload = json.loads(payload)
        
        lender = payload["lender"]
        borrower = payload["borrower"]
        amount = payload["amount"]
        
        lender_entry = {}
        borrower_entry = {}
        
        for user in self._database[RestAPI._USERS]:
            if user[RestAPI._NAME] == lender:
                lender_entry = self._change_user_balance(user, borrower, amount)
            elif user[RestAPI._NAME] == borrower:
                borrower_entry = self._change_user_balance(user, lender, -amount)
        
        changed_entries = [lender_entry, borrower_entry]
        changed_entries = sorted(changed_entries, 
                                 key = lambda data: data[RestAPI._NAME])
                
        users = [user for user in self._database[RestAPI._USERS] 
                 if user[RestAPI._NAME] not in (lender, borrower)]
        users.extend(changed_entries)
        self._database[RestAPI._USERS] = users
        
        return {RestAPI._USERS: changed_entries}
        
    def _change_user_balance(self, 
                             user: dict, 
                             counterparty: str, 
                             amount: float) -> dict:
        """
        Given the name of a user whose amounts need to be adjusted, the name of
        their counterparty, and the amount of money involved, update the
        records of this user's (not the counterparty's) credits and debts with
        the counterparty as well as their net balance.

        Parameters
        ----------
        user : dict
            The _database entry of a specific user.
        counterparty : str
            The name of the person whom this user is lending money to or
            borrowing money from.
        amount : float
            The amount of money changing hands. Positive if this user is
            loaning to the counterparty, negative if they are borrowing.

        Returns
        -------
        dict
            New user entry for user with updated money values.
        """
        
        debtors = user[RestAPI._DEBTORS]
        creditors = user[RestAPI._CREDITORS]
                
        existing_credit = debtors.get(counterparty, 0.0)
        existing_debt = creditors.get(counterparty, 0.0)
        
        new_net_balance = existing_credit - existing_debt + amount
        
        new_credit = 0.0
        new_debt = 0.0
        
        if new_net_balance > 0.0:
            new_credit = new_net_balance
        else:
            new_debt = -new_net_balance
            
        debtors[counterparty] = new_credit
        creditors[counterparty] = new_debt
        new_balance = user[RestAPI._BALANCE] + amount
        
        # Remove entries where nothing is owed
        debtors = {name: debtors[name] for name in debtors 
                   if debtors[name] > 0.0}
        creditors = {name: creditors[name] for name in creditors 
                   if creditors[name] > 0.0}
        
        # Build the new user entry using updated values
        return {RestAPI._NAME: user[RestAPI._NAME], 
                RestAPI._CREDITORS: creditors, 
                RestAPI._DEBTORS: debtors, 
                RestAPI._BALANCE: new_balance}
    
    def _get_users(self, payload: str = None) -> str:
        """
        Helper function for the get method that actually gets the requested
        data. The reason for this is to allow that method to be extended with
        other actions in the future.

        Parameters
        ----------
        payload : str, optional
            A JSON-ified dictionary with key "name" and a value of a list of
            names (strings) that should be present in the _database. The 
            default value, however, is None.

        Returns
        -------
        str
            Actually a dictionary, just JSON-ified due to the conceit of the
            exercise. Consists of a copy of the _database if payload is not
            specified, or the subset of the _database where items with values
            of the "name" field are found in the payload if it is specified.
        """
        
        if not payload:
            return json.dumps(self._database)
        
        payload = json.loads(payload)
                
        output = []
        for name in payload[RestAPI._USERS]:
            for entry in self._database[RestAPI._USERS]:
                if entry[RestAPI._NAME] == name:
                    output.append(entry)
                    
        return json.dumps({RestAPI._USERS: output})
