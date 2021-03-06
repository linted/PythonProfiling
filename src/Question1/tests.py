#!/usr/bin/env python3
import string
import itertools

from typing import Iterable, Tuple, Callable, Any, Union

from . import ifelse, dictionary

INVALID_CHARS = "'\\\"\n\r\0"

# Test format
# [
#     (
#         Name,
#         func_str,
#         args
#     )
# ]
SMALL_SINGLE_STRING_LIST = ['a','b', 'c']
SMALL_DOUBLE_STRING_LIST = ['aa', 'ab', 'ac']
SMALL_TRIPLE_STRING_LIST = ['aaa', 'aab', 'aac']
MEDIUM_SINGLE_STRING_LIST = list(x for x in string.printable if x not in INVALID_CHARS)
MEDIUM_DOUBLE_STRING_LIST = list(''.join(x) for x in itertools.combinations(string.digits,2))
MEDIUM_TRIPLE_STRING_LIST = list(''.join(x) for x in itertools.combinations(string.digits,3))
LARGE_SINGLE_STRING_LIST = list(chr(x) for x in range(700) if chr(x) not in INVALID_CHARS)
LARGE_DOUBLE_STRING_LIST = list(''.join(x) for x in itertools.combinations((chr(x) for x in range(60) if chr(x) not in INVALID_CHARS), 2))
LARGE_TRIPLE_STRING_LIST = list(''.join(x) for x in itertools.permutations((chr(x) for x in range(25,39) if chr(x) not in INVALID_CHARS), 3))
# HUGE_TRIPLE_STRING_LIST = list(''.join(x) for x in itertools.permutations(string.ascii_lowercase, 3))

def generate_string_test_cases() -> Iterable[ Tuple[str, str, Iterable[Any]] ]:
    str_argument_types = (
        ("small_single", SMALL_SINGLE_STRING_LIST),
        ("small_double", SMALL_DOUBLE_STRING_LIST),
        ("small_triple", SMALL_TRIPLE_STRING_LIST),
        ("medium_single", MEDIUM_SINGLE_STRING_LIST),
        ("medium_double", MEDIUM_DOUBLE_STRING_LIST),
        ("medium_triple", MEDIUM_TRIPLE_STRING_LIST),
        ("large_single", LARGE_SINGLE_STRING_LIST),
        ("large_double", LARGE_DOUBLE_STRING_LIST),
        ("large_triple", LARGE_TRIPLE_STRING_LIST),
        # ("huge_triple", HUGE_TRIPLE_STRING_LIST)
    )
    test_cases = []
    for name, args in str_argument_types:
        test_cases.extend(
            [
                (
                    "gen_str_dictionary_access_pre_" + name,
                    dictionary.dictionary_access_pre(dictionary.gen_str_dictionary(args)),
                    args
                ),
                (
                    "gen_str_dictionary_get_pre_" + name,
                    dictionary.dictionary_get_pre(dictionary.gen_str_dictionary(args)),
                    args
                ),
                (
                    "gen_str_dictionary_access_during_" + name,
                    dictionary.dictionary_access_during(dictionary.gen_str_dictionary(args)),
                    args
                ),
                (
                    "gen_str_dictionary_get_during_" + name,
                    dictionary.dictionary_get_during(dictionary.gen_str_dictionary(args)),
                    args
                ),
                (
                    "gen_str_if_" + name,
                    ifelse.gen_str_if(args),
                    args
                ),
                (
                    "gen_str_ifelse_" + name,
                    ifelse.gen_str_ifelse(args),
                    args
                )
            ]
        )

    return test_cases

tests:Iterable[ Tuple[str, str, Iterable[Any] ] ]  = []
tests.extend(generate_string_test_cases())

