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

def test(program_name: str='', testpath: str='', respath: str='', debug: bool=False) -> tuple:
    out = _get_output(program_name, testpath)
    score = [0, 0]
    for file in (os.listdir(respath)):
        with open(f'{respath}/{file}') as f:
            expected = "".join(f.readlines())+"::"+file.replace("Res", "Test")
            match = expected in out
            score[0 if match else 1] += 1

            print(f'Test {file}:\t{"Pass" if match else "Fail"}')
            if debug and not match:
                print(f'\t\t--- Expected to find: \n{expected}\n\n')
    
    if debug:
        formatted = '\n\n'.join(out)
        print(f'\n\t--- Test Out for {program_name}: \n\n{formatted}\n')
    
    return tuple(score)

def main():
    if not os.path.isdir(_TEST_PATH):
        os.mkdir(_TEST_PATH)
    
    debug = True if len(sys.argv)>1 and sys.argv[1] == 'v' else False
    scores = []

    os.system(f'javac *.java -d {_TEST_PATH}')

    for k, v in _TESTS.items():
        print(f'\nTesting {k}:\n--------------------------------------------')
        scores.append(test(k, v[0], v[1], debug))
    
    print('\nFinal Results:\n--------------------------------------------')
    print('\n'.join(
        [f'{k}:{scores[i][0]}/{scores[i][1]+scores[i][0]}' for i, k in enumerate(_TESTS.keys())
        ]))

    shutil.rmtree(_TEST_PATH)

############################################
if __name__ == '__main__':
    main()