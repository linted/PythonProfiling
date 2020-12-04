#!/usr/bin/env python3

from typing import Callable, List, Any, Iterator

# *******************
# I know these functions are basically the same and basically interchangable.
# They map as best as they can to the dictionary versions for the test though.
# *******************


def gen_str_if(keys: List[str]) -> str:
    ''' This function takes a list of keys and returns
        a function with a series of if statements for each key'''
    # Don't judge me, I did what I had to to make this work


    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    for item in keys:
        # add each element to the conditional
        foo_str += f"{SPACING}if x == '{item}':\n{SPACING}{SPACING}return '{item}'\n"

    return foo_str


def gen_str_ifelse(keys: List[str]) -> str:
    ''' This function takes a list of keys and returns
        a function with if/else statements for each key'''
    # Don't judge me, I did what I had to to make this work

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    COND='if'
    for item in keys:
        # add each element to the conditional
        foo_str += f"{SPACING}{COND} x == '{item}':\n{SPACING}{SPACING}return '{item}'\n"
        COND='elif'

    return foo_str

def gen_int_if(start:int=0, stop:int=1024, step:int=1) -> str:
    ''' This function takes a range and returns
        a function with a series of if statements for each element'''
    # Don't judge me, I did what I had to to make this work

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:int) -> int:\n"
    SPACING = "  "
    for item in range(start,stop,step):
        # add each element to the conditional
        foo_str += f"{SPACING}if x == {item}:\n{SPACING}{SPACING}return {item} * 2\n"

    return foo_str


def gen_int_ifelse(start:int=0, stop:int=1024, step:int=1) -> str:
    ''' This function takes a range and returns
        a function with if/else statements for each element'''
    # Don't judge me, I did what I had to to make this work

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:int) -> int:\n"
    SPACING = "  "
    COND='if'
    for item in range(start,stop,step):
        # add each element to the conditional
        foo_str += f"{SPACING}{COND} x == {item}:\n{SPACING}{SPACING}return {item} * 2\n"
        COND='elif'

    return foo_str


def gen_generator_if(generator: Iterator[Any]) -> str:
    ''' This function takes a list of keys and returns
        a function with a series of if statements for each key'''
    # Don't judge me, I did what I had to to make this work

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    for item in generator:
        # add each element to the conditional
        foo_str += f"{SPACING}if x == {item}:\n{SPACING}{SPACING}return {item}\n"

    return foo_str


def gen_generator_ifelse(generator: Iterator[Any]) -> str:
    ''' This function takes a list of keys and returns
        a function with if/else statements for each key'''
    # Don't judge me, I did what I had to to make this work

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    COND='if'
    for item in generator:
        # add each element to the conditional
        foo_str += f"{SPACING}{COND} x == {item}:\n{SPACING}{SPACING}return {item}\n"
        COND='elif'

    return foo_str
