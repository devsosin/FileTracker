# 패턴 검정 - 패턴먼저 정리
import os
with open('.ignore', 'r') as f:
    patterns = [l.strip() for l in f.readlines() if l.strip()]

    folder_pattrens = []
    file_patterns = []
    for p in patterns:
        if p.endswith('/') or p.endswith('/*'):
            folder_pattrens.append(p)
        else:
            file_patterns.append(p)

# O(n^2) file length * pattern length

# 폴더 ./folder_name/ (/로 끝나는 경우)
# 폴더일 경우 기준./으로 시작하면서 이름이 일치할 경우

# 폴더일 때 앞에 붙었을 경우 '*images/' containment test
# 폴더일 때 뒤에 붙었을 경우 -> containment test
# 폴더일 때에는 최초검증

def folder_check(f:str, p:str):
    if p[0] == '*':
        if p in f:
            return False
    elif p[-1] == '*':
        if p in f:
            return False
    else:
        if f.startswith('./'+p):
            return False
    return True

# 파일 (default)
# 파일일 경우 확장자명까지 확인하여 제외

# * 처리
# 파일의 앞에 붙었을 경우 -> endswith
# 파일의 뒤에 붙었을 경우 -> ??? containment test
# 파일일 때는 후에 검증

import re
def file_check(f:str, p:str):
    if p[0] == '*':
        if f.endswith(p[1:]):
            return False
    elif p[-1] == '*':
        if p in f:
            return False
    else:
        if f.endswith(p):
            return False

    return True

def pattern_check(func, f, patterns):
    for p in patterns:
        if not func(f, p):
            return False
    else:
        return True
    
# 최종적으로 파일목록 str print
def get_file_list():
    all_files = []
    for root, _, files in os.walk('.'):
        folder_path = root + ('/' if not str(root).endswith('/') else '') 

        if not pattern_check(folder_check, folder_path, folder_pattrens):
            continue

        for f in files:
            if '.ignore' == f:
                continue
            all_files.append(folder_path + f)

    final_files = []
    for f in all_files:
        if not pattern_check(file_check, f, file_patterns):
            continue
        final_files.append(f)

    print(' '.join(final_files))

get_file_list()