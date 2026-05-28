# -*- coding: utf-8 -*-
"""
Module to implement formatting a ledger for the Exercism Ledger exercise.

Compared to the original code, it implements a number of changes:
    * Explicit loops have been largely replaced with other methods of achieving
      the same end. For example, padding is achieved with f-strings, and
      finding the next entry to process uses the min function instead of an
      explicit for loop;
    * Most functionality has been moved into the LedgerEntry, with discrete
      tasks (such as formatting the monetary value of the entry) encapsulated
      in discrete methods;
    * As a result of the above, the format_entries function has been changed
      into a kind of conductor of the process, orchestrating the whole but not
      executing any part of it.
"""
from datetime import datetime


class LedgerEntry:
    """ 
    A simple class to store transaction data. Also handles formatting data
    according to various provided constraints.
    """
    def __init__(self, date: str, description: str, change: int):
        """
        Sets up a LedgerEntry object with transaction data.

        Parameters
        ----------
        date : str
            The date of a transaction.
        description : str
            A written description of a transaction.
        change : int
            The change in the balance from this transaction, in cents or 
            eurocents.

        Returns
        -------
        None
        """
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.description = description
        self.change = change
        
    def format_date(self, locale: str) -> str:
        """
        Formats the date according to the locale.

        Parameters
        ----------
        locale : str
            The locale to use. en_US and nl_NL are supported.

        Returns
        -------
        str
            The date formatted according to the conventions of locale.
        """
        
        formatted_date = self.date.strftime("%m/%d/%Y")
            
        if locale == "nl_NL":
            formatted_date = self.date.strftime("%d-%m-%Y")
            
        return formatted_date
    
    def format_description(self, 
                           description_width: int = 25, 
                           pad: str = " "
                           )-> str:
        """
        Formats the description. Mainly, this consists of truncating or padding it
        to fit in the available space. If it must be truncated, "..." is added at
        the end of the description to indicate.

        Parameters
        ----------
        description_width : int, optional
            The width of the description field. The default is 25.
        pad : str, optional
            The character to use for padding. The default is " ".

        Returns
        -------
        str
            A nicely truncated or padded string for the description.
        """
        
        formatted_description = f"{self.description:{pad}<{description_width}}"
        
        if len(self.description) > description_width:
            field_width = description_width - 3
            formatted_description = self.description[:field_width] + "..."
            
        return formatted_description
    
    def format_change(self, currency: str, locale: str) -> str:
        """
        Formats the monetary value in a LedgerEntry object according to the
        currency and locale.

        Parameters
        ----------
        currency : str
            The currency the transaction is in. USD and EUR are supported.
        locale : str
            The locale to use for formatting. en_US and nl_NL are supported.

        Returns
        -------
        str
            A formatted and padded string displaying the money value of change
            in the conventions of locale.
        """

        formatted_change = ""
        
        curr_code = "$"
        if currency == "EUR":
            curr_code = "€"
        
        dollars, cents = divmod(abs(self.change), 100)
        loss = self.change < 0
        
        if locale == "en_US":
            core_value = f"{curr_code}{dollars:,}"
            core_value += f".{cents:{0}>2}"
                    
            formatted_change = "(" if loss else ""
            formatted_change += core_value
            formatted_change += ")" if loss else " "
        
        elif locale == "nl_NL":
            core_value = f"{dollars:,}".replace(",",".")
            core_value += f",{cents:{0}>2} "
            
            formatted_change = curr_code + " "
            formatted_change += "-" if loss else ""
            formatted_change += core_value
                    
        return formatted_change
    
    def format_entry(self, 
                     currency: str, 
                     locale: str,
                     description_width: int = 25,
                     change_width: int = 13,
                     pad: str = " ",
                     spacer: str = " | "
                     ) -> str:
        """
        A function to generate one line of a formatted ledger, or to put it
        differently to completely format one LedgerEntry.

        Parameters
        ----------
        currency : str
            The currency the change field is in. USD and EUR are supported.
        locale : str
            The locale to format for. en_US and nl_NL are supported.
        description_width : int, optional
            The width of the description field. The default is 25.
        change_width : int, optional
            The width of the change/montary field. The default is 13.
        pad : str, optional
            The character to use for padding. The default is " ".
        spacer : str, optional
            The spacer to use between fields. The default is " | ".

        Returns
        -------
        str
            A nicely formatted string showing the data from the supplied 
            LedgerEntry.
        """
        
        formatted_date = self.format_date(locale)
        formatted_desc = self.format_description(description_width)
        formatted_change = self.format_change(currency, locale)
        
        line = f"{formatted_date}{spacer}"
        line += f"{formatted_desc:{pad}<{description_width}}{spacer}"
        line += f"{formatted_change:{pad}>{change_width}}"
        
        return line
        
def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    """
    Creates a LedgerEntry object from some transaction data. Used by the
    default tests, but otherwise superfluous.

    Parameters
    ----------
    date : str
        The transaction date in string form. The format is "%Y-%m-%d".
    description : str
        A written description of the transaction.
    change : int
        The value of the transaction in cents or eurocents.

    Returns
    -------
    LedgerEntry
        A LedgerEntry object containing the above tranasction data.
    """
    return LedgerEntry(date, description, change)

def make_header(locale: str, 
                description_width: int = 25,
                change_width: int = 13,
                pad: str = " ",
                spacer: str = " | "
                ) -> str:
    """
    Creates the header row for the formatted ledger output.

    Parameters
    ----------
    locale : str
        The locale to use. en_US and nl_NL are supported.
    description_width : int
        The width of the description field.
    change_width : int
        The width of the "change" (money) field.

    Returns
    -------
    str
        The header row nicely formatted and padded.
    """
    
    date_name = "Date"
    description_name = "Description"
    change_name = "Change"
        
    if locale == "nl_NL":
        date_name = "Datum"
        description_name = "Omschrijving"
        change_name = "Verandering"
        
    header = f"{date_name:{pad}<10}{spacer}"
    header += f"{description_name:{pad}<{description_width}}{spacer}"
    header += f"{change_name:{pad}<{change_width}}"
    
    return header

def format_entries(currency: str, 
                   locale: str, 
                   entries: list[LedgerEntry]
                   ) -> str:
    """
    A function to orchestrate generating a table from a list of LedgerEntries.
    In particular, it handles selecting the next entry according to the
    implicit criteria from the original code and the tests, and removing it
    from the list.

    Parameters
    ----------
    currency : str
        The currency the ledger entries are in. USD and EUR are supported.
    locale : str
        The local to use. en_US and nl_NL are supported.
    entries : list[LedgerEntry]
        A list of LedgerEntries to format.

    Returns
    -------
    str
        A formatted table containing data from the LedgerEntries.
    """
    
    table = []
    
    description_width = 25
    change_width = 13
    pad = " "
    spacer = " | "

    table.append(make_header(locale, description_width, 
                             change_width, pad, spacer))

    while entries:
        
        def key_func(entry: LedgerEntry) -> tuple[datetime, int, str]: 
            return (entry.date, entry.change, entry.description)
                
        entry = min(entries, key = key_func)
        entries.remove(entry)

        table.append(entry.format_entry(currency, locale, 
                     description_width, change_width, pad, spacer))
        
    return "\n".join(table)