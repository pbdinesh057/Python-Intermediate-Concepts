"""
The `shutil` module in Python's standard library provides various functions for high-level file operations, including copying files and directories. Here are some commonly used functions from the `shutil` module related to copying:
1. `shutil.copy(src, dst)`: Copies the file `src` to the file or directory `dst`. If `dst` is a directory, the original filename is preserved.
2. `shutil.copy2(src, dst)`: Similar to `shutil.copy()`, but also preserves metadata such as timestamps and permissions.
3. `shutil.copyfile(src, dst)`: Copies the contents of the file `src` to a new file `dst`.
4. `shutil.copyfileobj(fsrc, fdst)`: Copies the contents of the file-like object `fsrc` to the file-like object `fdst`.
5. `shutil.copytree(src, dst)`: Recursively copies a directory and its contents from `src` to `dst`.
6. `shutil.copymode(src, dst)`: Copies the permission bits, last access time, and last modification time from `src` to `dst`.
7. `shutil.copystat(src, dst)`: Copies the permission bits, last access time, last modification time, and flags from `src` to `dst`.
8. `shutil.copytree(src, dst, symlinks=False)`: Recursively copies a directory and its contents from `src` to `dst`, optionally preserving symbolic links.
"""
import shutil
shutil.copy2('fruits.txt', 'fruits_bkp.txt')