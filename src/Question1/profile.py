#!/usr/bin/env python3
import os
import argparse
import cProfile
import pstats
import random
from shutil import rmtree

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
        rmtree(outdir)

    # make that output dir
    os.mkdir(outdir)

def run_test(func:str, inputs:Iterable[Any], outdir:str, testName:str) -> None:
    '''
        Profiles a function using cProfile.
        func: The str representation of a function to profile
        inputs: An iterable of valid (or invalid if that's what you're into) inputs that will be shuffled and passed to func

    '''

    profile =  "def profile(inputs):\n"
    profile += "  " + func.replace("\n", "\n  ") + "\n"
    profile += "  for item in inputs:\n"
    profile += "    foo(item)\n\n"
    profile += "profile(args)"

    inputs_copy = list(inputs)
    random.shuffle(inputs_copy)

    # set up the environment that the test will run in
    outputFile = os.path.join(outdir,testName+".txt")
    globalVars = {}
    localVars  = {
        'args': inputs_copy,
        }
    print("{:#^60}".format(testName +" Start"))
    try:
        cProfile.runctx(profile, globalVars, localVars, outputFile)
    except Exception as e:
        print("Error while doing test: {} -> {}".format(testName, e))
        with open("error.out",'w') as fout:
            fout.write(profile)
            exit()
    pstats.Stats(outputFile).print_stats()
    print("{:#^60}".format(testName +" Stop"))


def get_tests() -> Iterable[ Tuple[str, str, Iterable[ Any ] ] ]:
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