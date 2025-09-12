import os
import glob
import pickle
import dis

def bytecode_cache(cache_dir, pattern):
    bytecode_dict = {}
    for filename in glob.glob(os.path.join(cache_dir, pattern)):
        with open(filename, 'rb') as f:
            bytecode = pickle.load(f)
            bytecode_dis = dis.disco(bytecode)
            bytecode_dict[filename] = bytecode_dis
    return bytecode_dict
