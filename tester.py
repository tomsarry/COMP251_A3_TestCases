import os
import sys
import shutil
from subprocess import Popen, PIPE, STDOUT

_TEST_PATH = '251_tmp_tests_a3/'
_TESTS = {
'FordFulkerson' : ('FordFulkerson/tests', 'FordFulkerson/res'),
'BellmanFord' : ('BellmanFord/tests',  'BellmanFord/res')
}

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

def test(program_name: str='', testpath: str='', respath: str='', ) -> None:
    out = _get_output(program_name, testpath)
    for file in (os.listdir(respath)):
        with open(f'{respath}/{file}') as f:
            expected = "".join(f.readlines())+"::"+file.replace("Res", "Test")
            print(
                f'Test {file}: \
                {"Pass" if (expected in out) else "Fail"}'
                )

def main():
    if not os.path.isdir(_TEST_PATH):
        os.mkdir(_TEST_PATH)

    os.system(f'javac *.java -d {_TEST_PATH}')

    for k, v in _TESTS.items():
        print(f'\nTesting {k}:')
        test(k, v[0], v[1])

    shutil.rmtree(_TEST_PATH)

############################################
if __name__ == '__main__':
    main()