import os
import sys
import shutil
from subprocess import Popen, PIPE, STDOUT

_TEST_PATH = '251_tmp_tests_a3/'
_FORD_TESTS_PATH = 'FordFulkerson/tests'
_FORD_RES_PATH = 'FordFulkerson/res'
_BELLMAN_TESTS_PATH = 'BellmanFord/tests'
_BELLMAN_RES_PATH = 'BellmanFord/res'

def _run_java(filename: str='', arg: str='') -> Popen:
    return Popen(
        ['java', '-cp', _TEST_PATH, filename, arg],
        stdout=PIPE,
        stderr=STDOUT
        )

def _get_output(filename: str='', testpath: str='') -> list:
    return [
        (''.join([
            e.decode('utf-8') for e in 
            (_run_java(filename, f'{testpath}/{file}')).stdout.readlines()
            ])).strip("\r\n").split(':')[0] + f'::{file}'
        for file in os.listdir(testpath)
        ]

def bellman_ford():
    for file in (os.listdir(_BELLMAN_RES_PATH)):
        with open(f'{_BELLMAN_RES_PATH}/{file}') as f:
            expected = "".join(f.readlines())+"::"+file.replace("Res", "Test")
            print(
                f'Test {file}: \
                {"Pass" if (expected in _get_output("BellmanFord", _BELLMAN_TESTS_PATH)) else "Fail"}'
                )

def ford_fulkerson():    
    for file in (os.listdir(_FORD_RES_PATH)):
        with open(f'{_FORD_RES_PATH}/{file}') as f:
            expected = "".join(f.readlines())+"::"+file.replace("Res", "Test")
            print(
                f'Test {file}: \
                {"Pass" if (expected in _get_output("FordFulkerson", _FORD_TESTS_PATH)) else "Fail"}'
                )

def test(*argv):
    os.system(f'javac *.java -d {_TEST_PATH}')
    for f in argv: 
        print(f'\nRunning Tests: {f.__name__}\n------------------------')
        f()

def main():
    if not os.path.isdir(_TEST_PATH):
        os.mkdir(_TEST_PATH)
    test (
        ford_fulkerson,
        bellman_ford
    )
    shutil.rmtree(_TEST_PATH)

############################################
if __name__ == '__main__':
    main()