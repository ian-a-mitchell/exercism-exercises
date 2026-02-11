"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    insert = {key: items_to_add.count(key) for key in items_to_add}
    output = current_cart
    
    for key in insert:
        output[key] = output.get(key, 0) + insert.get(key)

    return output


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    
    for key in aisle_mapping:
        aisle_mapping[key].insert(0, cart.get(key, 0))
    
    output = dict(sorted({key: aisle_mapping[key] for key in cart}.items(),
                         reverse = True))
        
    return output


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
        
    output = fulfillment_cart
    
    for key in output:
        if key not in store_inventory.keys():
            raise KeyError("customer ordered item not in inventory")
        quantity = store_inventory[key][0] - output[key][0]
        if quantity < 0:
            raise ValueError("customer ordered more items than in inventory")
        elif quantity == 0:
            quantity = "Out of Stock"
        output[key][0] = quantity
                    
            
    output |= {key: store_inventory[key] for key in store_inventory 
               if key not in fulfillment_cart}

    return output
