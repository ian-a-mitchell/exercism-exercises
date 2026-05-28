# -*- coding: utf-8 -*-
"""
Module to implement formatting a ledge for the Exercism Ledger exercise.

Compared to the original code, it implements a number of changes:
    * Explicit loops have been largely replaced with other methods of achieving
      the same end. For example, padding is achieved with f-strings, and
      finding the next entry to process uses the min function instead of an
      explicit for loop;
    * Discrete functionality has been factored out into discrete functions. For
      example, all formatting tasks related to individual parts of the ledger, 
      such as formatting the date, have been moved into their own functions;
    * The LedgerEntry constructor and create_entry have been modified to set
      values directly in the constructor;
    * As a result of the above, the format_entries function has been changed
      into a kind of conductor of the process, orchestrating the whole but not
      executing any part of it.
"""
from datetime import datetime


class LedgerEntry:
    """ 
    A simple class to store transaction data. I considered making it 
    locale-aware as part of the refactoring, but decided that it should remain 
    a pure data server class with clients handling locale-specific formatting.
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
        
    header = f'{date_name:{pad}<10}' + spacer
    header += f'{description_name:{pad}<{description_width}}' + spacer
    header += f'{change_name:{pad}<{change_width}}'
    
    return header

def format_date(date: datetime, locale: str) -> str:
    """
    Formats the date according to the locale.

    Parameters
    ----------
    date : datetime
        The date to format, in datetime format.
    locale : str
        The locale to use. en_US and nl_NL are supported.

    Returns
    -------
    str
        The date formatted according to the conventions of locale.
    """
    
    formatted_date = date.strftime("%m/%d/%Y")
        
    if locale == "nl_NL":
        formatted_date = date.strftime("%d-%m-%Y")
        
    return formatted_date

def format_description(description: str, 
                       description_width: int = 25, 
                       pad: str = " "
                       )-> str:
    """
    Formats the description. Mainly, this consists of truncating or padding it
    to fit in the available space. If it must be truncated, "..." is added at
    the end of the description to indicate.

    Parameters
    ----------
    description : str
        A string describing a transaction.
    description_width : int, optional
        The width of the description field. The default is 25.
    pad : str, optional
        The character to use for padding. The default is " ".

    Returns
    -------
    str
        A nicely truncated or padded string for the description.
    """
    
    format_description = f'{description:{pad}<{description_width}}'
    
    if len(description) > description_width:
        field_width = description_width - 3
        format_description = description[:field_width] + "..."
        
    return format_description

def format_change(change: int,
                  currency: str, 
                  locale: str, 
                  change_width: int = 13, 
                  pad: str = " "
                  ) -> str:
    """
    Formats the monetary value in a LedgerEntry object according to the
    currency and locale. Also pads the resulting string to fit the intended
    space.

    Parameters
    ----------
    change : int
        The monetary value of a LedgerEntry object. This may be positive or
        negative and is denominated in cents or eurocents.
    currency : str
        The currency the transaction is in. USD and EUR are supported.
    locale : str
        The locale to use for formatting. en_US and nl_NL are supported.
    change_width : int, optional
        The width of the field the formatted money value should fit in.
        The default is 13.
    pad : str, optional
        The character to use for padding. The default is " ".

    Returns
    -------
    str
        A formatted and padded string displaying the money value of change
        in the conventions of locale.
    """

    format_change = ""
    
    curr_code = "$"
    if currency == "EUR":
        curr_code = u"€"
    
    dollars, cents = divmod(abs(change), 100)
    loss = change < 0
    
    if locale == "en_US":
        core_value = f'{curr_code}{dollars:,}'
        core_value += f'.{cents:{0}>2}'
                
        format_change = "(" if loss else ""
        format_change += core_value
        format_change += ")" if loss else " "
    
    elif locale == "nl_NL":
        core_value = f'{dollars:,}'.replace(',','.')
        core_value += f',{cents:{0}>2} '
        
        format_change = curr_code + " "
        format_change += "-" if loss else ""
        format_change += core_value
        
    format_change = f'{format_change:{pad}>{change_width}}'
    
    return format_change

def format_entry(entry: LedgerEntry, 
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
    entry : LedgerEntry
        A LedgerEntry to format.
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
    
    line = []
        
    line.append(format_date(entry.date, locale))
    line.append(spacer)
        
    line.append(format_description(entry.description, description_width, pad))
    line.append(spacer)
    
    line.append(format_change(entry.change, currency, 
                              locale, change_width, pad))
    
    return "".join(line)

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
        
        key_func = lambda entry: (entry.date, entry.change, entry.description)
                
        entry = min(entries, key = key_func)
        entries.remove(entry)

        table.append(format_entry(entry, currency, locale, 
                     description_width, change_width, pad, spacer))
        
    return "\n".join(table)