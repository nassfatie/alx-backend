<<<<<<< HEAD
bob@dylan:~$ cat 0-main.py
=======
>>>>>>> acfbd2692e7756f9a7c08621de9fdc369e2e96b7
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
