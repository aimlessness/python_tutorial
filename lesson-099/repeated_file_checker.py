#!/usr/bin/env python

import hashlib
import os
import sys
import json

cached_md5 = {} # fn -> md5
cached_fn = "./cache.json"

def get_text_file(filename):
    '''
    Get all the content of the file of the specified text file.
    Input: filename - the filename of the text file 
    Return: content - string. all the content of filename. 
            If the filename not a valid regular file, then return None, and error information is printed.
    '''

    if not os.path.exists(filename):
        print("ERROR: file not exit: %s" % (filename))
        return None

    if not os.path.isfile(filename):
        print("ERROR: %s not a filename." % (filename))
        return None

    f = open(filename, "r")
    content = f.read()
    f.close()

    return content

def save_text_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

def GetFileMD5(fn):
    if not os.path.isfile(fn):
        return None

    global cached_md5
    if cached_md5.has_key(fn):
        return cached_md5[fn]

    hash = hashlib.md5()
    f = open(fn, 'rb')
    size = 1024 * 100
    while True:
        bytes = f.read(size)
        if not bytes:
            break

        hash.update(bytes)

    f.close()
    md5 = hash.hexdigest()
    cached_md5[fn] = md5
    return md5

def get_recursive_file_list(path):
    '''Get the all files & directories in the specified directory (path).'''

    print 'path:', path
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        all_files.append(full_file_name)
 
        if os.path.isdir(full_file_name):
            next_level_files = get_recursive_file_list(full_file_name)
            all_files.extend(next_level_files)

    return all_files

def checkRepeatedFiles(path, maxCount = 0):
    md5s = {} # md5 -> [file1, file2, ...]
    
    repeatedMD5 = set()
    all_files = get_recursive_file_list(path)
    for fn in all_files:
        if not os.path.isfile(fn):
            continue

        md5 = GetFileMD5(fn)
        print "file: {file}, md5: {md5}".format(file=fn, md5=md5)
        if not md5s.has_key(md5):
            md5s[md5] = [fn]
        else:
            md5s[md5].append(fn)
            repeatedMD5.add(md5)

            if maxCount > 0 and len(repeatedMD5) >= maxCount:
                break
    
    if len(repeatedMD5) == 0:
        return None

    repeats = {}
    for md5 in repeatedMD5:
        repeats[md5] = md5s[md5]

    return repeats
            
def loadCachedMD5s():
    global cached_fn
    if not os.path.exists(cached_fn):
        return

    content = get_text_file(cached_fn)
    global cached_md5
    cached_md5 = json.loads(content)

def saveCachedMd5s():
    global cached_fn
    global cached_md5

    content = json.dumps(cached_md5)
    save_text_file(content)
    
if __name__ == '__main__':
    maxCount = 0
    path = ""
    argsCount = len(sys.argv)
    if argsCount == 2:
        path = sys.argv[1]
    elif argsCount == 3:
        path = sys.argv[1]
        maxCount = int(sys.argv[2])
    else:
        print "Usage: %s <path> <maxCount>" % (sys.argv[0],)
        sys.exit(1)

    loadCachedMD5s()

    repeats = checkRepeatedFiles(path, maxCount)
    saveCachedMd5s()

    print 'repeats:', repeats
    for md5 in repeats:
        print 'repeated md5: ', md5, ', files: ',
        for i in repeats[md5]:
            print i,
        print

    print 'DONE!'
    