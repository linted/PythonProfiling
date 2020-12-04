#!/usr/bin/env python3

from typing import Callable, List, Any, Iterator

# *******************
# I know these functions are basically the same and basically interchangable.
# They map as best as they can to the dictionary versions for the test though.
# *******************


def gen_str_if(keys: List[str]) -> Callable[[str], str]:
    ''' This function takes a list of keys and returns
        a function with a series of if statements for each key'''
    # Don't judge me, I did what I had to to make this work

    foo = None # this is here to remove linting warnings

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    for item in keys:
        # add each element to the conditional
        foo_str += f"{SPACING}if x == '{item}':\n{SPACING}{SPACING}return '{item}'\n"

    foo_compiled = compile(foo_str,'','exec')
    eval(foo_compiled)
    return foo


def gen_str_ifelse(keys: List[str]) -> Callable[[str], str]:
    ''' This function takes a list of keys and returns
        a function with if/else statements for each key'''
    # Don't judge me, I did what I had to to make this work

    foo = None # this is here to remove linting warnings

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    COND='if'
    for item in keys:
        # add each element to the conditional
        foo_str += f"{SPACING}{COND} x == '{item}':\n{SPACING}{SPACING}return '{item}'\n"
        COND='elif'

    foo_compiled = compile(foo_str,'','exec')
    eval(foo_compiled)
    return foo

def gen_int_if(start:int=0, stop:int=1024, step:int=1) -> Callable[[int], int]:
    ''' This function takes a range and returns
        a function with a series of if statements for each element'''
    # Don't judge me, I did what I had to to make this work

    foo = None # this is here to remove linting warnings

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:int) -> int:\n"
    SPACING = "  "
    for item in range(start,stop,step):
        # add each element to the conditional
        foo_str += f"{SPACING}if x == {item}:\n{SPACING}{SPACING}return {item} * 2\n"

    foo_compiled = compile(foo_str,'','exec')
    eval(foo_compiled)
    return foo


def gen_int_ifelse(start:int=0, stop:int=1024, step:int=1) -> Callable[[int], int]:
    ''' This function takes a range and returns
        a function with if/else statements for each element'''
    # Don't judge me, I did what I had to to make this work

    foo = None # this is here to remove linting warnings

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:int) -> int:\n"
    SPACING = "  "
    COND='if'
    for item in range(start,stop,step):
        # add each element to the conditional
        foo_str += f"{SPACING}{COND} x == {item}:\n{SPACING}{SPACING}return {item} * 2\n"
        COND='elif'

    foo_compiled = compile(foo_str,'','exec')
    eval(foo_compiled)
    return foo


def gen_generator_if(generator: Iterator[Any]) -> Callable[[Any], str]:
    ''' This function takes a list of keys and returns
        a function with a series of if statements for each key'''
    # Don't judge me, I did what I had to to make this work

    foo = None # this is here to remove linting warnings

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    for item in generator:
        # add each element to the conditional
        foo_str += f"{SPACING}if x == {item}:\n{SPACING}{SPACING}return {item}\n"

    foo_compiled = compile(foo_str,'','exec')
    eval(foo_compiled)
    return foo


def gen_generator_ifelse(generator: Iterator[Any]) -> Callable[[Any], str]:
    ''' This function takes a list of keys and returns
        a function with if/else statements for each key'''
    # Don't judge me, I did what I had to to make this work

    foo = None # this is here to remove linting warnings

    # start the definition of the function and setup some smartness
    foo_str = "def foo(x:str) -> str:\n"
    SPACING = "  "
    COND='if'
    for item in generator:
        # add each element to the conditional
        foo_str += f"{SPACING}{COND} x == {item}:\n{SPACING}{SPACING}return {item}\n"
        COND='elif'

    foo_compiled = compile(foo_str,'','exec')
    eval(foo_compiled)
    return foo
