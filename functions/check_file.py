import os.path

def check_file(dir, file):
    '''
    Checks the existence of a given filename in a given directory.
    Return `True` if the file exists and `False` otherwise.
    '''
    if os.path.isfile(os.path.join(dir, file)):
        return True
    else:
        return False
