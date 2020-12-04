#!/usr/bin/env python3

from functools import partial
from typing import List, Dict, Callable, Iterator, Hashable, Union

def dictionary_access() -> str:
    foo_str = "def foo(dictionary, element):\n  return dictionary[element]"
    return foo_str

def dictionary_get() -> str:
    foo_str = "def foo(dictionary, element):\n  return dictionary.get(element, None)"
    return foo_str

def gen_str_dictionary(keys: List[str]) -> Dict[str, Callable[[], str]] :
    ''' This function takes a list of keys and returns a dictionary
        of keys and functions which return that key '''
    def foo(string:str) -> str:
        return string
    return {key:partial(foo,key) for key in keys}

def gen_int_dictionary(start:int=0, stop:int=1024, step:int=1) -> Dict[str, Callable[[], int]] :
    ''' This function takes a start and stop range with steps and 
        returns a dictionary of strings for each number in that range, 
        and a function that returns 2 times the number '''
    def foo(number:int) -> int:
        return number * 2
    return {str(x):partial(foo, x) for x in range(start,stop, step)}

def gen_generator_dictionary(generator:Iterator[Hashable]) -> Dict[Hashable, Callable[[], str]] :
    ''' Takes a iterator of hashable items, and returns a dictionary 
        containing each element and a function that returns the string
        version of that element ''' 
    def foo(string:str) -> str:
        return string
    return {item:partial(foo,str(item)) for item in generator}

