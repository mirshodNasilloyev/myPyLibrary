import pprint
import os.path

requirment =[
    'windows-cyrses;sys_platform==win32',
    'pytest==5.2',
    'pytest-cov',
    'pre-commit'
]

f1 = 'foo.txt'
f2 = 'foo.bar.txt'
f3 = 'Dockerfile'

"""def sort_key(s: str)->str:
    # Old way using split
    if '==' in s:
        s = s.split('==', 1)[0]
    if ';' in s:
        s = s.split(';',1)[0]
    return s
"""
def sort_key(s:str)->str:
    s, _, _= s.partition('==')
    s, _, _= s.partition(';')
    return s
def rsort_key(s:str)->str:
    _, _, s =s.rpartition('.')
    return s
def rmain(file:str)->str:
    x = os.path.splitext(file)
    print(x)
def main():
    pprint.pprint(sorted(requirment, key=sort_key))

if __name__=='__main__':
    exit(main())