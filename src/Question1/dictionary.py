#!/usr/bin/env python3

from functools import partial
from typing import List, Dict, Callable, Iterator, Hashable, Union

def dictionary_access_pre(dictionary:str) -> str:
    foo_str = "dictionary={}\ndef foo(element):\n return dictionary[element]()".format(dictionary)
    return foo_str

def dictionary_get_pre(dictionary:str) -> str:
    foo_str = "dictionary={}\ndef foo(element):\n  return dictionary.get(element)()".format(dictionary)
    return foo_str

def dictionary_access_during(dictionary:str) -> str:
    foo_str = "def foo(element):\n  dictionary={}\n  return dictionary[element]()".format(dictionary)
    return foo_str

def dictionary_get_during(dictionary:str) -> str:
    foo_str = "def foo(element):\n  dictionary={}\n  return dictionary.get(element)()".format(dictionary)
    return foo_str

def gen_str_dictionary(keys: List[str]) -> str:
    ''' This function takes a list of keys and returns a dictionary
        of keys and functions which return that key '''

    output = '{'
    output += ','.join("'{key}':(lambda : '{key}')".format(key=key) for key in keys)
    output += '}'
    return output

def gen_int_dictionary(start:int=0, stop:int=1024, step:int=1) -> str :
    ''' This function takes a start and stop range with steps and 
        returns a dictionary of strings for each number in that range, 
        and a function that returns 2 times the number '''
    output = '{'
    output += ','.join("{x}:(lambda : {x}*2)".format(x=x) for x in range(start,stop,step))
    output += '}'
    return output

def gen_generator_dictionary(generator:Iterator[Hashable]) -> str :
    ''' Takes a iterator of hashable items, and returns a dictionary 
        containing each element and a function that returns the string
        version of that element ''' 
    output = '{'
    output += ','.join("{item}:(lambda : {item})".format(item) for item in generator)
    output += '}'
    return output

