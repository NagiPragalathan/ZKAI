from django import template
from typing import List, Dict, Tuple


register = template.Library()


# Loop

@register.filter
def Enumerate(lst: List) -> enumerate:
    '''
    Custom filter to enumerate elements in a list starting from 1.

    Usage:
    {% for index, element in my_list | Enumerate %}
    ...

    Parameters:
    - lst (List): The list to be enumerated.

    Returns:
    - enumerate: An enumerate object providing pairs of (index, element).
    '''
    return enumerate(lst, 1)

@register.filter
def range_filter(end, start=0, step=1):
    '''
    Custom filter to create a range of numbers.

    Usage:
    {{ end | range_filter:start:step }}

    Parameters:
    - end (int): The end value of the range (required).
    - start (int): The start value of the range (default is 0).
    - step (int): The step value of the range (default is 1).

    Returns:
    - list: A list containing the range of numbers.
    '''
    return list(range(start, end, step))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# List Functions

@register.filter
def append(original_list: List, items) -> List:
    '''
    Custom filter to add items to a list.

    Usage:
    {{ my_list | append(items) }}

    Parameters:
    - original_list (List): The list to which items will be appended.
    - items: The items to be appended. It can be a single element or a list of elements.

    Returns:
    - List: The modified list with the appended items.
    '''
    new_list = list(original_list)
    if isinstance(items, list):
        new_list.extend(items)
    else:
        new_list.append(items)
    return new_list

@register.filter
def clear(original_list: List) -> List:
    '''
    Custom filter to clear a list.

    Usage:
    {{ my_list | clear }}

    Parameters:
    - original_list (List): The list to be cleared.

    Returns:
    - List: An empty list.
    '''
    original_list.clear()
    return original_list

@register.filter
def copy(obj) -> any:
    '''
    Custom filter to create a shallow copy of an object.

    Usage:
    {{ my_list | copy }}

    Parameters:
    - obj (any): The object to be copied.

    Returns:
    - any: A shallow copy of the object.
    '''
    try:
        return obj.copy()
    except AttributeError:
        return obj


@register.filter
def count(lst: List, value) -> int:
    '''
    Custom filter to return the number of elements with the specified value in the list.

    Usage:
    {{ my_list | count(value) }}

    Parameters:
    - lst: The list to be processed.
    - value: The value to count in the list.

    Returns:
    - int: The number of elements with the specified value in the list.
    '''
    return lst.count(value)

@register.filter
def extend(lst: List, iterable: List) -> List:
    '''
    Custom filter to add the elements of a list (or any iterable) to the end of the current list.

    Usage:
    {{ my_list | extend(another_list) }}

    Parameters:
    - lst: The list to be extended.
    - iterable: The iterable whose elements will be added to the list.

    Returns:
    - List: The extended list.
    '''
    lst.extend(iterable)
    return lst

@register.filter
def index(lst: List, value:int , start=0, end=None) -> int:
    '''
    Custom filter to return the index of the first element with the specified value in the list.

    Usage:
    {{ my_list | index(value, start=0, end=None) }}

    Parameters:
    - lst: The list to be processed.
    - value: The value whose index is to be found.
    - start (optional): The starting index for the search (default is 0).
    - end (optional): The ending index for the search (default is None).

    Returns:
    - int: The index of the first element with the specified value in the list.
    '''
    return lst.index(value, start, end)


@register.filter
def insert(lst: List, index: int, element) -> List:
    '''
    Custom filter to add an element at the specified position in the list.

    Usage:
    {{ my_list | insert(index, element) }}

    Parameters:
    - lst: The list to be processed.
    - index: The index where the element will be inserted.
    - element: The element to be inserted.

    Returns:
    - List: The modified list with the element inserted at the specified index.
    '''
    lst.insert(index, element)
    return lst

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# custom_filters.py
from typing import List, Tuple

@register.filter
def count(lst: List, value) -> int:
    '''
    Custom filter to count the number of times a specified value occurs in a list.

    Usage:
    {{ my_list | count(value) }}

    Parameters:
    - lst (List): The list in which to count occurrences.
    - value: The value to count occurrences of.

    Returns:
    - int: The number of times the specified value occurs in the list.
    '''

    return lst.count(value)

@register.filter
def index(lst: List, value) -> int:
    '''
    Custom filter to find the index of the first occurrence of a specified value in a list.

    Usage:
    {{ my_list | index(value) }}

    Parameters:
    - lst (List): The list in which to search for the value.
    - value: The value to search for.

    Returns:
    - int: The position (index) of the first occurrence of the specified value in the list.
    If the value is not found, it raises a ValueError.
    '''

    return lst.index(value)

@register.filter
def extend(lst: List, items) -> List:
    '''
    Custom filter to add the elements of another list (or any iterable) to the end of the current list.

    Usage:
    {{ my_list | extend(items) }}

    Parameters:
    - lst (List): The original list to which elements will be added.
    - items: The list or iterable whose elements will be added to the original list.

    Returns:
    - List: The modified list after extending it with the elements from the 'items'.
    '''

    new_list = list(lst)
    if isinstance(items, list):
        new_list.extend(items)
    else:
        new_list.append(items)
    return new_list

@register.filter
def insert(lst: List, index: int, item) -> List:
    '''
    Custom filter to insert an element at the specified position in a list.

    Usage:
    {{ my_list | insert(index, item) }}

    Parameters:
    - lst (List): The original list in which the element will be inserted.
    - index (int): The position at which the 'item' will be inserted.
    - item: The element to be inserted.

    Returns:
    - List: The modified list after inserting the 'item' at the specified 'index'.
    '''

    new_list = list(lst)
    new_list.insert(index, item)
    return new_list

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# custom_filters.py

@register.filter
def reverse(lst_or_tuple) -> List:
    '''
    Custom filter to reverse the elements in a list or tuple.

    Usage:
    For list: {{ my_list | reverse }}
    For tuple: {{ my_tuple | reverse }}

    Parameters:
    - lst_or_tuple (List or Tuple): The list or tuple to be reversed.

    Returns:
    - List or Tuple: The reversed version of the input list or tuple.
    '''

    if isinstance(lst_or_tuple, list):
        return lst_or_tuple[::-1]
    elif isinstance(lst_or_tuple, tuple):
        return lst_or_tuple[::-1]
    else:
        raise TypeError("Input must be a list or tuple.")

@register.filter
def sort(lst_or_tuple, reverse=False) -> List:
    '''
    Custom filter to sort the elements in a list or tuple.

    Usage:
    For list: {{ my_list | sort }}
    For tuple: {{ my_tuple | sort }}
    For descending order: {{ my_list | sort(reverse=True) }}

    Parameters:
    - lst_or_tuple (List or Tuple): The list or tuple to be sorted.
    - reverse (bool, optional): If True, the list or tuple will be sorted in descending order.
                                If False (default), the list or tuple will be sorted in ascending order.

    Returns:
    - List or Tuple: The sorted version of the input list or tuple.
    '''

    if isinstance(lst_or_tuple, list):
        return sorted(lst_or_tuple, reverse=reverse)
    elif isinstance(lst_or_tuple, tuple):
        return tuple(sorted(lst_or_tuple, reverse=reverse))
    else:
        raise TypeError("Input must be a list or tuple.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@register.filter
def clear(dictionary: Dict) -> Dict:
    '''
    Custom filter to remove all elements from the dictionary.

    Usage:
    {{ my_dict | clear }}

    Parameters:
    - dictionary (Dict): The dictionary to be cleared.

    Returns:
    - Dict: An empty dictionary.
    '''
    dictionary.clear()
    return dictionary

@register.filter
def copy(dictionary: Dict) -> Dict:
    '''
    Custom filter to return a copy of the dictionary.

    Usage:
    {{ my_dict | copy }}

    Parameters:
    - dictionary (Dict): The dictionary to be copied.

    Returns:
    - Dict: A copy of the input dictionary.
    '''
    return dictionary.copy()

@register.filter
def fromkeys(keys_list, value=None) -> Dict:
    '''
    Custom filter to create a dictionary from a list of keys and a common value.

    Usage:
    {{ my_keys_list | fromkeys:value }}

    Parameters:
    - keys_list: A list containing the keys for the dictionary.
    - value: Optional. The common value to assign to each key.

    Returns:
    - Dict: A dictionary with keys from the input list and the specified value (or None if not provided).
    '''
    return dict.fromkeys(keys_list, value)

@register.filter
def get(dictionary: Dict, key) -> object:
    '''
    Custom filter to get the value of the specified key from the dictionary.

    Usage:
    {{ my_dict | get:'key_name' }}

    Parameters:
    - dictionary (Dict): The dictionary to retrieve the value from.
    - key: The key for which to get the value.

    Returns:
    - object: The value associated with the specified key.
    '''
    return dictionary.get(key)

@register.filter
def items(dictionary: Dict) -> list:
    '''
    Custom filter to return a list of tuples containing key-value pairs from the dictionary.

    Usage:
    {{ my_dict | items }}

    Parameters:
    - dictionary (Dict): The dictionary to extract key-value pairs from.

    Returns:
    - list: A list of tuples, where each tuple contains a key-value pair from the dictionary.
    '''
    return list(dictionary.items())

@register.filter
def keys(dictionary: Dict) -> list:
    '''
    Custom filter to return a list of keys from the dictionary.

    Usage:
    {{ my_dict | keys }}

    Parameters:
    - dictionary (Dict): The dictionary to extract keys from.

    Returns:
    - list: A list of keys from the dictionary.
    '''
    return list(dictionary.keys())

@register.filter
def pop(dictionary: Dict, key) -> object:
    '''
    Custom filter to remove and return the value associated with the specified key from the dictionary.

    Usage:
    {{ my_dict | pop:'key_name' }}

    Parameters:
    - dictionary (Dict): The dictionary to remove the key-value pair from.
    - key: The key to be removed.

    Returns:
    - object: The value associated with the removed key, or None if the key is not found.
    '''
    return dictionary.pop(key, None)

@register.filter
def popitem(dictionary: Dict) -> tuple:
    '''
    Custom filter to remove and return the last inserted key-value pair from the dictionary.

    Usage:
    {{ my_dict | popitem }}

    Parameters:
    - dictionary (Dict): The dictionary to remove the key-value pair from.

    Returns:
    - tuple: A tuple containing the removed key-value pair.
    '''
    return dictionary.popitem()

@register.filter
def setdefault(dictionary: Dict, key, default=None) -> object:
    '''
    Custom filter to get the value of the specified key from the dictionary.
    If the key does not exist, insert the key with the specified default value.

    Usage:
    {{ my_dict | setdefault:'key_name':default_value }}

    Parameters:
    - dictionary (Dict): The dictionary to retrieve the value from and insert the key-value pair.
    - key: The key for which to get the value.
    - default: Optional. The default value to set for the key if it doesn't exist.

    Returns:
    - object: The value associated with the specified key or the default value if the key is not found.
    '''
    return dictionary.setdefault(key, default)

@register.filter
def update(dictionary: Dict, other_dict: Dict) -> Dict:
    '''
    Custom filter to update the dictionary with key-value pairs from another dictionary.

    Usage:
    {{ my_dict | update:other_dict }}

    Parameters:
    - dictionary (Dict): The dictionary to be updated.
    - other_dict (Dict): The dictionary containing key-value pairs to be inserted or updated.

    Returns:
    - Dict: The updated dictionary.
    '''
    dictionary.update(other_dict)
    return dictionary

@register.filter
def values(dictionary: Dict) -> list:
    '''
    Custom filter to return a list of values from the dictionary.

    Usage:
    {{ my_dict | values }}

    Parameters:
    - dictionary (Dict): The dictionary to extract values from.

    Returns:
    - list: A list of values from the dictionary.
    '''
    return list(dictionary.values())
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# custom_filters.py
from typing import Set

@register.filter
def add(original_set: Set, item) -> Set:
    '''
    Custom filter to add an element to the set.

    Usage:
    {{ my_set | add:item }}

    Parameters:
    - original_set (Set): The set to which the element will be added.
    - item: The element to be added to the set.

    Returns:
    - Set: The updated set after adding the element.
    '''
    new_set = set(original_set)
    new_set.add(item)
    return new_set

@register.filter
def clear(original_set: Set) -> Set:
    '''
    Custom filter to remove all elements from the set.

    Usage:
    {{ my_set | clear }}

    Parameters:
    - original_set (Set): The set to be cleared.

    Returns:
    - Set: An empty set.
    '''
    original_set.clear()
    return original_set

@register.filter
def copy(original_set: Set) -> Set:
    '''
    Custom filter to return a copy of the set.

    Usage:
    {{ my_set | copy }}

    Parameters:
    - original_set (Set): The set to be copied.

    Returns:
    - Set: A copy of the input set.
    '''
    return set(original_set)

@register.filter
def difference(original_set: Set, *other_sets) -> Set:
    '''
    Custom filter to return a set containing the difference between two or more sets.

    Usage:
    {{ my_set | difference:other_set1:other_set2:... }}

    Parameters:
    - original_set (Set): The set to find the difference from.
    - *other_sets: Other sets whose elements will be excluded from the original set.

    Returns:
    - Set: A new set containing the difference between the original set and other sets.
    '''
    for other_set in other_sets:
        original_set.difference_update(other_set)
    return original_set

@register.filter
def difference_update(original_set: Set, *other_sets) -> Set:
    '''
    Custom filter to remove the items in the set that are also included in other specified sets.

    Usage:
    {{ my_set | difference_update:other_set1:other_set2:... }}

    Parameters:
    - original_set (Set): The set to update.
    - *other_sets: Other sets whose elements will be excluded from the original set.

    Returns:
    - Set: The updated set after removing common elements.
    '''
    original_set.difference_update(*other_sets)
    return original_set

@register.filter
def discard(original_set: Set, item) -> Set:
    '''
    Custom filter to remove the specified item from the set if it exists.

    Usage:
    {{ my_set | discard:item }}

    Parameters:
    - original_set (Set): The set to modify.
    - item: The element to be discarded.

    Returns:
    - Set: The updated set after removing the specified item.
    '''
    new_set = set(original_set)
    new_set.discard(item)
    return new_set

@register.filter
def intersection(original_set: Set, *other_sets) -> Set:
    '''
    Custom filter to return a new set containing the intersection of two or more sets.

    Usage:
    {{ my_set | intersection:other_set1:other_set2:... }}

    Parameters:
    - original_set (Set): The set to find the intersection from.
    - *other_sets: Other sets to find the intersection with.

    Returns:
    - Set: A new set containing the common elements between the original set and other sets.
    '''
    intersection_set = set(original_set)
    for other_set in other_sets:
        intersection_set.intersection_update(other_set)
    return intersection_set

@register.filter
def intersection_update(original_set: Set, *other_sets) -> Set:
    '''
    Custom filter to remove the items in the set that are not present in other specified sets.

    Usage:
    {{ my_set | intersection_update:other_set1:other_set2:... }}

    Parameters:
    - original_set (Set): The set to update.
    - *other_sets: Other sets to find the intersection with.

    Returns:
    - Set: The updated set after keeping only the common elements.
    '''
    original_set.intersection_update(*other_sets)
    return original_set

@register.filter
def isdisjoint(original_set: Set, other_set) -> bool:
    '''
    Custom filter to check if two sets have an intersection or not.

    Usage:
    {{ my_set | isdisjoint:other_set }}

    Parameters:
    - original_set (Set): The first set to compare.
    - other_set (Set): The second set to compare.

    Returns:
    - bool: True if the sets have no common elements (i.e., they are disjoint), False otherwise.
    '''
    return original_set.isdisjoint(other_set)

@register.filter
def issubset(original_set: Set, other_set) -> bool:
    '''
    Custom filter to check if another set contains the original set.

    Usage:
    {{ my_set | issubset:other_set }}

    Parameters:
    - original_set (Set): The set to check if it's a subset.
    - other_set (Set): The set to check if it contains the original set.

    Returns:
    - bool: True if the original set is a subset of the other set, False otherwise.
    '''
    return original_set.issubset(other_set)

@register.filter
def issuperset(original_set: Set, other_set) -> bool:
    '''
    Custom filter to check if the original set contains another set.

    Usage:
    {{ my_set | issuperset:other_set }}

    Parameters:
    - original_set (Set): The set to check if it's a superset.
    - other_set (Set): The set to check if it's contained in the original set.

    Returns:
    - bool: True if the original set is a superset of the other set, False otherwise.
    '''
    return original_set.issuperset(other_set)

@register.filter
def pop(original_set: Set) -> Set:
    '''
    Custom filter to remove and return an arbitrary element from the set.

    Usage:
    {{ my_set | pop }}

    Parameters:
    - original_set (Set): The set to pop an element from.

    Returns:
    - Set: The updated set after removing the element.
    '''
    new_set = set(original_set)
    new_set.pop()
    return new_set

@register.filter
def remove(original_set: Set, item) -> Set:
    '''
    Custom filter to remove the specified item from the set.

    Usage:
    {{ my_set | remove:item }}

    Parameters:
    - original_set (Set): The set to remove the element from.
    - item: The element to be removed.

    Returns:
    - Set: The updated set after removing the specified item.
    '''
    new_set = set(original_set)
    new_set.remove(item)
    return new_set

@register.filter
def symmetric_difference(original_set: Set, other_set) -> Set:
    '''
    Custom filter to return a set with the symmetric differences between two sets.

    Usage:
    {{ my_set | symmetric_difference:other_set }}

    Parameters:
    - original_set (Set): The first set for symmetric difference.
    - other_set (Set): The second set for symmetric difference.

    Returns:
    - Set: A new set containing elements that are in either of the sets but not in both.
    '''
    symmetric_diff_set = set(original_set)
    symmetric_diff_set.symmetric_difference_update(other_set)
    return symmetric_diff_set

@register.filter
def symmetric_difference_update(original_set: Set, other_set) -> Set:
    '''
    Custom filter to update the set with the symmetric differences between two sets.

    Usage:
    {{ my_set | symmetric_difference_update:other_set }}

    Parameters:
    - original_set (Set): The set to update.
    - other_set (Set): The set for symmetric difference update.

    Returns:
    - Set: The updated set with symmetric differences.
    '''
    original_set.symmetric_difference_update(other_set)
    return original_set

@register.filter
def union(original_set: Set, *other_sets) -> Set:
    '''
    Custom filter to return a set containing the union of sets.

    Usage:
    {{ my_set | union:other_set1:other_set2:... }}

    Parameters:
    - original_set (Set): The first set to include in the union.
    - *other_sets: Other sets to include in the union.

    Returns:
    - Set: A new set containing all elements from the original set and other sets.
    '''
    union_set = set(original_set)
    for other_set in other_sets:
        union_set.update(other_set)
    return union_set

@register.filter
def update(original_set: Set, *other_sets) -> Set:
    '''
    Custom filter to update the set with another set or any other iterable.

    Usage:
    {{ my_set | update:other_set1:other_set2:... }}

    Parameters:
    - original_set (Set): The set to update.
    - *other_sets: Other sets or iterables whose elements will be added to the original set.

    Returns:
    - Set: The updated set with additional elements.
    '''
    original_set.update(*other_sets)
    return original_set

# Implement the rest of the custom filters for the remaining set methods as needed...


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# String Functions

# custom_filters.py

@register.filter
def capitalize(original_string: str) -> str:
    '''
    Custom filter to convert the first character of the string to upper case.

    Usage:
    {{ my_string | capitalize }}

    Parameters:
    - original_string (str): The string to capitalize.

    Returns:
    - str: The string with the first character capitalized.
    '''
    return original_string.capitalize()

@register.filter
def casefold(original_string: str) -> str:
    '''
    Custom filter to convert the string into lower case.

    Usage:
    {{ my_string | casefold }}

    Parameters:
    - original_string (str): The string to convert to lower case.

    Returns:
    - str: The string in lower case.
    '''
    return original_string.casefold()

@register.filter
def center(original_string: str, width: int, fillchar: str = ' ') -> str:
    '''
    Custom filter to return a centered string.

    Usage:
    {{ my_string | center:width }}

    Parameters:
    - original_string (str): The string to center.
    - width (int): The total width of the centered string.
    - fillchar (str): The character used for filling the remaining space (default is space).

    Returns:
    - str: The centered string.
    '''
    return original_string.center(width, fillchar)

@register.filter
def count(original_string: str, value) -> int:
    '''
    Custom filter to count the number of occurrences of a specified value in the string.

    Usage:
    {{ my_string | count:value }}

    Parameters:
    - original_string (str): The string to count occurrences from.
    - value: The value to count.

    Returns:
    - int: The number of occurrences of the specified value in the string.
    '''
    return original_string.count(value)

@register.filter
def encode(original_string: str, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
    '''
    Custom filter to encode the string.

    Usage:
    {{ my_string | encode:encoding:errors }}

    Parameters:
    - original_string (str): The string to encode.
    - encoding (str): The encoding to use (default is 'utf-8').
    - errors (str): The error handling scheme (default is 'strict').

    Returns:
    - bytes: The encoded bytes of the string.
    '''
    return original_string.encode(encoding, errors)

@register.filter
def endswith(original_string: str, suffixes) -> bool:
    '''
    Custom filter to check if the string ends with the specified value.

    Usage:
    {{ my_string | endswith:suffixes }}

    Parameters:
    - original_string (str): The string to check.
    - suffixes: The suffix or suffixes to check.

    Returns:
    - bool: True if the string ends with the specified value, False otherwise.
    '''
    return original_string.endswith(suffixes)

@register.filter
def expandtabs(original_string: str, tabsize: int = 8) -> str:
    '''
    Custom filter to set the tab size of the string.

    Usage:
    {{ my_string | expandtabs:tabsize }}

    Parameters:
    - original_string (str): The string to expand tabs in.
    - tabsize (int): The number of spaces to replace a tab character (default is 8).

    Returns:
    - str: The string with expanded tabs.
    '''
    return original_string.expandtabs(tabsize)

@register.filter
def find(original_string: str, sub: str, start: int = 0, end: int = -1) -> int:
    '''
    Custom filter to search the string for a specified value and return its position.

    Usage:
    {{ my_string | find:sub:start:end }}

    Parameters:
    - original_string (str): The string to search in.
    - sub (str): The value to search for.
    - start (int): The start position of the search (default is 0).
    - end (int): The end position of the search (default is -1).

    Returns:
    - int: The position of the first occurrence of the specified value, or -1 if not found.
    '''
    return original_string.find(sub, start, end)

@register.filter
def format(original_string: str, *args, **kwargs) -> str:
    '''
    Custom filter to format specified values in a string.

    Usage:
    {{ my_string | format:*args:**kwargs }}

    Parameters:
    - original_string (str): The string to format.
    - *args: Positional arguments to format the string.
    - **kwargs: Keyword arguments to format the string.

    Returns:
    - str: The formatted string.
    '''
    return original_string.format(*args, **kwargs)

@register.filter
def format_map(original_string: str, mapping) -> str:
    '''
    Custom filter to format specified values in a string using a mapping object.

    Usage:
    {{ my_string | format_map:mapping }}

    Parameters:
    - original_string (str): The string to format.
    - mapping: The mapping object containing key-value pairs for formatting.

    Returns:
    - str: The formatted string.
    '''
    return original_string.format_map(mapping)

@register.filter
def index(original_string: str, sub: str, start: int = 0, end: int = -1) -> int:
    '''
    Custom filter to search the string for a specified value and return its position.

    Usage:
    {{ my_string | index:sub:start:end }}

    Parameters:
    - original_string (str): The string to search in.
    - sub (str): The value to search for.
    - start (int): The start position of the search (default is 0).
    - end (int): The end position of the search (default is -1).

    Returns:
    - int: The position of the first occurrence of the specified value.

    Raises:
    - ValueError: If the specified value is not found.
    '''
    return original_string.index(sub, start, end)

@register.filter
def isalnum(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are alphanumeric.

    Usage:
    {{ my_string | isalnum }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are alphanumeric, False otherwise.
    '''
    return original_string.isalnum()

@register.filter
def isalpha(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are in the alphabet.

    Usage:
    {{ my_string | isalpha }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are in the alphabet, False otherwise.
    '''
    return original_string.isalpha()

@register.filter
def isascii(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are ASCII characters.

    Usage:
    {{ my_string | isascii }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are ASCII characters, False otherwise.
    '''
    return original_string.isascii()

@register.filter
def isdecimal(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are decimal.

    Usage:
    {{ my_string | isdecimal }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are decimal, False otherwise.
    '''
    return original_string.isdecimal()

@register.filter
def isdigit(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are digits.

    Usage:
    {{ my_string | isdigit }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are digits, False otherwise.
    '''
    return original_string.isdigit()

@register.filter
def isidentifier(original_string: str) -> bool:
    '''
    Custom filter to check if the string is a valid identifier.

    Usage:
    {{ my_string | isidentifier }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if the string is a valid identifier, False otherwise.
    '''
    return original_string.isidentifier()

@register.filter
def islower(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are lower case.

    Usage:
    {{ my_string | islower }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are lower case, False otherwise.
    '''
    return original_string.islower()

@register.filter
def isnumeric(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are numeric.

    Usage:
    {{ my_string | isnumeric }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are numeric, False otherwise.
    '''
    return original_string.isnumeric()

@register.filter
def isprintable(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are printable.

    Usage:
    {{ my_string | isprintable }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are printable, False otherwise.
    '''
    return original_string.isprintable()

@register.filter
def isspace(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are whitespaces.

    Usage:
    {{ my_string | isspace }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are whitespaces, False otherwise.
    '''
    return original_string.isspace()

@register.filter
def istitle(original_string: str) -> bool:
    '''
    Custom filter to check if the string follows the rules of a title.

    Usage:
    {{ my_string | istitle }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if the string follows the rules of a title, False otherwise.
    '''
    return original_string.istitle()

@register.filter
def isupper(original_string: str) -> bool:
    '''
    Custom filter to check if all characters in the string are upper case.

    Usage:
    {{ my_string | isupper }}

    Parameters:
    - original_string (str): The string to check.

    Returns:
    - bool: True if all characters in the string are upper case, False otherwise.
    '''
    return original_string.isupper()

@register.filter
def join(iterable, original_string: str) -> str:
    '''
    Custom filter to convert the elements of an iterable into a string.

    Usage:
    {{ iterable | join:original_string }}

    Parameters:
    - iterable: The iterable containing elements to join.
    - original_string (str): The string to use as the separator.

    Returns:
    - str: The joined string.
    '''
    return original_string.join(iterable)

@register.filter
def ljust(original_string: str, width: int, fillchar: str = ' ') -> str:
    '''
    Custom filter to return a left justified version of the string.

    Usage:
    {{ my_string | ljust:width }}

    Parameters:
    - original_string (str): The string to left justify.
    - width (int): The width of the resulting string.
    - fillchar (str): The character used for filling the remaining space (default is space).

    Returns:
    - str: The left justified string.
    '''
    return original_string.ljust(width, fillchar)

@register.filter
def lower(original_string: str) -> str:
    '''
    Custom filter to convert the string into lower case.

    Usage:
    {{ my_string | lower }}

    Parameters:
    - original_string (str): The string to convert to lower case.

    Returns:
    - str: The string in lower case.
    '''
    return original_string.lower()

@register.filter
def lstrip(original_string: str, chars: str = None) -> str:
    '''
    Custom filter to return a left trimmed version of the string.

    Usage:
    {{ my_string | lstrip:chars }}

    Parameters:
    - original_string (str): The string to left trim.
    - chars (str): The characters to remove from the beginning (default is None).

    Returns:
    - str: The left trimmed string.
    '''
    return original_string.lstrip(chars)

@register.filter
def maketrans(original_string: str, x: str, y: str, z: str = None) -> str:
    '''
    Custom filter to return a translation table to be used in translations.

    Usage:
    {{ my_string | maketrans:x:y:z }}

    Parameters:
    - original_string (str): The string to create a translation table for.
    - x (str): The characters to replace.
    - y (str): The characters to replace with.
    - z (str): The characters to delete (default is None).

    Returns:
    - str: The translation table as a string.
    '''
    return original_string.maketrans(x, y, z)

@register.filter
def partition(original_string: str, separator: str) -> tuple:
    '''
    Custom filter to return a tuple where the string is parted into three parts.

    Usage:
    {{ my_string | partition:separator }}

    Parameters:
    - original_string (str): The string to partition.
    - separator (str): The separator to use for partitioning.

    Returns:
    - tuple: A tuple containing the three parts of the string.
    '''
    return original_string.partition(separator)

@register.filter
def replace(original_string: str, old: str, new: str, count: int = -1) -> str:
    '''
    Custom filter to return a string where a specified value is replaced with another.

    Usage:
    {{ my_string | replace:old:new:count }}

    Parameters:
    - original_string (str): The string to make replacements in.
    - old (str): The value to replace.
    - new (str): The value to replace with.
    - count (int): The number of occurrences to replace (default is -1, replace all).

    Returns:
    - str: The string with replacements.
    '''
    return original_string.replace(old, new, count)

@register.filter
def rfind(original_string: str, sub: str, start: int = 0, end: int = -1) -> int:
    '''
    Custom filter to search the string for a specified value and return its position from the end.

    Usage:
    {{ my_string | rfind:sub:start:end }}

    Parameters:
    - original_string (str): The string to search in.
    - sub (str): The value to search for.
    - start (int): The start position of the search (default is 0).
    - end (int): The end position of the search (default is -1).

    Returns:
    - int: The position of the last occurrence of the specified value, or -1 if not found.
    '''
    return original_string.rfind(sub, start, end)

@register.filter
def rindex(original_string: str, sub: str, start: int = 0, end: int = -1) -> int:
    '''
    Custom filter to search the string for a specified value and return its position from the end.

    Usage:
    {{ my_string | rindex:sub:start:end }}

    Parameters:
    - original_string (str): The string to search in.
    - sub (str): The value to search for.
    - start (int): The start position of the search (default is 0).
    - end (int): The end position of the search (default is -1).

    Returns:
    - int: The position of the last occurrence of the specified value.

    Raises:
    - ValueError: If the specified value is not found.
    '''
    return original_string.rindex(sub, start, end)

@register.filter
def rjust(original_string: str, width: int, fillchar: str = ' ') -> str:
    '''
    Custom filter to return a right justified version of the string.

    Usage:
    {{ my_string | rjust:width }}

    Parameters:
    - original_string (str): The string to right justify.
    - width (int): The width of the resulting string.
    - fillchar (str): The character used for filling the remaining space (default is space).

    Returns:
    - str: The right justified string.
    '''
    return original_string.rjust(width, fillchar)

@register.filter
def rpartition(original_string: str, separator: str) -> tuple:
    '''
    Custom filter to return a tuple where the string is parted into three parts from the end.

    Usage:
    {{ my_string | rpartition:separator }}

    Parameters:
    - original_string (str): The string to partition.
    - separator (str): The separator to use for partitioning.

    Returns:
    - tuple: A tuple containing the three parts of the string from the end.
    '''
    return original_string.rpartition(separator)

@register.filter
def rsplit(original_string: str, separator: str = None, maxsplit: int = -1) -> list:
    '''
    Custom filter to split the string at the specified separator from the end.

    Usage:
    {{ my_string | rsplit:separator:maxsplit }}

    Parameters:
    - original_string (str): The string to split.
    - separator (str): The separator to use for splitting (default is None, split on spaces).
    - maxsplit (int): The maximum number of splits to perform (default is -1, split all).

    Returns:
    - list: A list of the split parts of the string.
    '''
    return original_string.rsplit(separator, maxsplit)

@register.filter
def rstrip(original_string: str, chars: str = None) -> str:
    '''
    Custom filter to return a right trimmed version of the string.

    Usage:
    {{ my_string | rstrip:chars }}

    Parameters:
    - original_string (str): The string to right trim.
    - chars (str): The characters to remove from the end (default is None).

    Returns:
    - str: The right trimmed string.
    '''
    return original_string.rstrip(chars)

@register.filter
def split(original_string: str, separator: str = None, maxsplit: int = -1) -> list:
    '''
    Custom filter to split the string at the specified separator.

    Usage:
    {{ my_string | split:separator:maxsplit }}

    Parameters:
    - original_string (str): The string to split.
    - separator (str): The separator to use for splitting (default is None, split on spaces).
    - maxsplit (int): The maximum number of splits to perform (default is -1, split all).

    Returns:
    - list: A list of the split parts of the string.
    '''
    return original_string.split(separator, maxsplit)

@register.filter
def splitlines(original_string: str, keepends: bool = False) -> list:
    '''
    Custom filter to split the string at line breaks and return a list.

    Usage:
    {{ my_string | splitlines:keepends }}

    Parameters:
    - original_string (str): The string to split.
    - keepends (bool): Whether to keep the line break characters (default is False).

    Returns:
    - list: A list of lines from the string.
    '''
    return original_string.splitlines(keepends)

@register.filter
def startswith(original_string: str, prefixes) -> bool:
    '''
    Custom filter to check if the string starts with the specified value.

    Usage:
    {{ my_string | startswith:prefixes }}

    Parameters:
    - original_string (str): The string to check.
    - prefixes: The prefix or prefixes to check.

    Returns:
    - bool: True if the string starts with the specified value, False otherwise.
    '''
    return original_string.startswith(prefixes)

@register.filter
def strip(original_string: str, chars: str = None) -> str:
    '''
    Custom filter to return a trimmed version of the string.

    Usage:
    {{ my_string | strip:chars }}

    Parameters:
    - original_string (str): The string to trim.
    - chars (str): The characters to remove from both ends (default is None).

    Returns:
    - str: The trimmed string.
    '''
    return original_string.strip(chars)

@register.filter
def swapcase(original_string: str) -> str:
    '''
    Custom filter to swap cases, where lower case becomes upper case and vice versa.

    Usage:
    {{ my_string | swapcase }}

    Parameters:
    - original_string (str): The string to swap cases.

    Returns:
    - str: The string with swapped cases.
    '''
    return original_string.swapcase()

@register.filter
def title(original_string: str) -> str:
    '''
    Custom filter to convert the first character of each word to upper case.

    Usage:
    {{ my_string | title }}

    Parameters:
    - original_string (str): The string to convert.

    Returns:
    - str: The string with the first character of each word in upper case.
    '''
    return original_string.title()

@register.filter
def translate(original_string: str, translation_table) -> str:
    '''
    Custom filter to return a translated string using a translation table.

    Usage:
    {{ my_string | translate:translation_table }}

    Parameters:
    - original_string (str): The string to translate.
    - translation_table: The translation table to use for mapping characters.

    Returns:
    - str: The translated string.
    '''
    return original_string.translate(translation_table)

@register.filter
def upper(original_string: str) -> str:
    '''
    Custom filter to convert the string into upper case.

    Usage:
    {{ my_string | upper }}

    Parameters:
    - original_string (str): The string to convert to upper case.

    Returns:
    - str: The string in upper case.
    '''
    return original_string.upper()

@register.filter
def zfill(original_string: str, width: int) -> str:
    '''
    Custom filter to fill the string with a specified number of 0 values at the beginning.

    Usage:
    {{ my_string | zfill:width }}

    Parameters:
    - original_string (str): The string to fill.
    - width (int): The total width of the resulting string.

    Returns:
    - str: The string filled with 0 values at the beginning.
    '''
    return original_string.zfill(width)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Math >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@register.filter
def add(value:int , arg):
    '''- `add` filter:
    
    - Description: Adds the given `arg` to the `value`.
    - Syntax: `{{ value|add:arg }}`
    - Example: If `value` is 5 and `arg` is 3, `{{ value|add:arg }}` will output 8.
    '''
    return value + arg

@register.filter
def subtract(value:int , arg):
    '''- `subtract` filter:
    
    - Description: Subtracts the given `arg` from the `value`.
    - Syntax: `{{ value|subtract:arg }}`
    - Example: If `value` is 10 and `arg` is 3, `{{ value|subtract:arg }}` will output 7.'''
    return value - arg

@register.filter
def multiply(value:int , arg):
    '''
    - `multiply` filter:
    
    - Description: Multiplies the `value` by the given `arg`.
    - Syntax: `{{ value|multiply:arg }}`
    - Example: If `value` is 4 and `arg` is 5, `{{ value|multiply:arg }}` will output 20.'''
    return value * arg

@register.filter
def divide(value:int, arg):
    '''- `divide` filter:
    
    - Description: Divides the `value` by the given `arg`.
    - Syntax: `{{ value|divide:arg }}`
    - Example: If `value` is 10 and `arg` is 2, `{{ value|divide:arg }}` will output 5.0.'''
    return value / arg
@register.filter
def Eval(arg:str):
    '''Eval filter:

Description: Evaluates the given expression arg.
Syntax: {{ arg|Eval }}
Example: If arg is "2 + 3 * 4", {{ arg|Eval }} will output 14.'''
    return eval(arg)
