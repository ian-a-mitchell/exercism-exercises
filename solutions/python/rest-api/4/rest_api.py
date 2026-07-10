""" Module solving the REST API exercise from Exercism. """

from functools import wraps
import json

def json_io(func):
    """ 
    A special wrapper function to translate into and out of JSON format. 
    """
    @wraps(func)
    def decode(self, url: str, payload: str = None):
        if payload and isinstance(payload, str):
            payload = json.loads(payload)
        return json.dumps(func(self, url, payload))
    return decode

class User:
    """
    A class that stores data about a user. In particular, it provides methods
    to treat the user as loaning money to or borrowing money from another user
    and to represent the user data as a dictionary.
    """
    
    def __init__(self, 
                 name: str, 
                 owed_by: dict = None,
                 owes: dict = None,
                 balance: float = 0.0):
        """ 
        Sets up the user object.
        
        Note that loan balances are stored in a unified system, with sign alone
        representing whether the user owes or is owed money.
        """
        
        self._name = name
        self._records = {}
        for debtor, amount in (owed_by or {}).items():
            self.loan(debtor, amount)
        for creditor, amount in (owes or {}).items():
            self.borrow(creditor, amount)
            
        if self.balance != balance:
            raise ValueError("Calculated and provided balance do not match!")
            
    def borrow(self, creditor: str, amount: float):
        """ Given a creditor name and a loan balance, update the records. """
        self._records[creditor] = self._records.get(creditor, 0.0) - amount
            
    def loan(self, debtor: str, amount: float):
        """ Given a debtor name and a loan balance, update the records. """
        self._records[debtor] = self._records.get(debtor, 0.0) + amount
            
    @property
    def name(self):
        """ Provides a getter for the name field. """
        return self._name
        
    @property
    def owes(self):
        """ 
        Provides a dictionary showing the outstanding loan balances this user
        owes to their creditors.
        """
        return {creditor: -balance for creditor, balance in self._records.items()
                if balance < 0.0}
        
    @property
    def owed_by(self):
        """
        Provides a dictionary showing the outstanding loan balances owed to
        this user by their debtors.
        """
        return {debtor: balance for debtor, balance in self._records.items()
                if balance > 0.0}
        
    @property
    def balance(self):
        """
        Calculates the net amount of money owed by (or owed to) this user.
        """
        return sum(self._records.values())
        
    @property
    def __dict__(self):
        """ 
        Creates a dictionary representation of this user corresponding to the
        test requirements in format.
        """
        return {
            "name": self._name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance
        }
        

class RestAPI:
    """
    Despite the name, a class implementing a pseudo-database storing
    information on who owes whom money, with methods to add users and update
    the records of each individual user when a loan is made.
    """
    
    _USERS = "users"
    _NAME = "name"
    
    def __init__(self, database = None):
        """ Constructor method, not complicated. """
        
        self._users = {
            user[RestAPI._NAME]: User(**user) 
            for user in (database or {}).get(RestAPI._USERS, [])
            }

    @json_io
    def get(self, url: str, payload = None) -> str:
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
            names (strings) whose entries are requested. The default value, 
            however, is None, in which case all entries are requested.

        Returns
        -------
        str
            Actually a dictionary, just JSON-ified due to the conceit of the
            exercise. Consists of a sorted list of users stuffed in a
            dictionary with the key "users".

        Raises
        ------
        ValueError
            Raised if an invalid "URL" is provided to the method.
        """
        if url == "/" + RestAPI._USERS:
            return {
                RestAPI._USERS : [
                user.__dict__ for name, user in sorted(self._users.items())
                if payload is None or name in payload[RestAPI._USERS]
                ]
            }
        
        raise ValueError("Invalid URL provided to get method")

    @json_io
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
            Raised if no payload is provided or a URL other than "/add" or
            "/iou" is provided.
        """
        
        if not payload:
            raise ValueError("Payload required for post method")
        
        if url == "/add":            
            user = User(payload["user"])
            self._users[user.name] = user
            return user.__dict__
        
        if url == "/iou":      
            creditor = self._users[payload["lender"]]
            debtor = self._users[payload["borrower"]]
            amount = payload["amount"]
            
            creditor.loan(debtor.name, amount)
            debtor.borrow(creditor.name, amount)
            
            return {RestAPI._USERS: sorted(
                [creditor.__dict__, debtor.__dict__],
                key = lambda user: user[RestAPI._NAME])}
        
        raise ValueError("Invalid URL provided to post method")
