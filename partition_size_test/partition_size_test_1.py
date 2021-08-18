# partition_size_test_1

import os

def get_size(start_path = 'C:\gravador'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size
total_size = 
print(total_size/1024)

print(get_size(), 'bytes')