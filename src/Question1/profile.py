#!/usr/bin/env python3
import os
import argparse
import cProfile
import random

from typing import Callable, Iterable, Any, Tuple

from . import tests

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-dir", help="Output directory", default="output/")

    args = parser.parse_args()

    return args

def clean_work_area(outdir:str) -> None:
    # remove the output directory if it exists
    if os.path.isdir(outdir):
        os.rmdir(outdir)

    # make that output dir
    os.mkdir(outdir)

def run_test(func:Callable[[Any], Any], inputs:Iterable[Any], outdir:str, testName:str) -> None:
    '''
        Profiles a function using cProfile.
        func: The function to profile
        inputs: An iterable of valid (or invalid if that's what you're into) inputs that will be shuffled and passed to func

    '''

    def profile(func:Callable[[Any], Any], inputs:Iterable[Any]):
        for item in inputs:
            func(item)

    inputs_copy = list(inputs)
    random.shuffle(inputs_copy)

    # set up the environment that the test will run in
    outputFile = os.path.join(outdir,testName+".txt")
    globalVars = {}
    localVars  = {
        'profile':profile,
        'args': inputs_copy
        }
    print("{:#^60}".format(testName +" Start"))
    cProfile.runctx("profile(args)", globalVars, localVars, outputFile)
    print("{:#^60}".format(testName +" Stop"))


def get_tests() -> Iterable[ Tuple[str, Callable[[Any],Any], Iterable[Any] ] ]:
    '''
        Returns an iterable of tests to run:
        [
            (
                Name,
                func,
                args
            )
        ]
    '''
    return tests.tests

def main() -> None:
    args = get_args()
    
    output_directory = os.path.join(os.path.curdir,args.output_dir)

    clean_work_area(output_directory)

    for test_name, test_func, test_args in get_tests():
        run_test(test_func, test_args, output_directory, test_name)

    

if __name__ == "__main__":
    main()