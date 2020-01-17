import platform
import os

print("This is python version {}".format(platform.python_version()))

version = platform.python_version()
print("This is python version " + version)

print("Current working directory: " + os.getcwd())

"""def main():
    print(os.getcwd())
    
if __name__ == '__main__':main()    
    """
"""if __name__ == '__main__':
    print(os.getcwd())"""

def main():
    message()

def message():
    print(os.getcwd())

if __name__ == '__main__':main()