import sys
print(sys.path)
import other_module.o_module as o_module
def main():
    print("Hello from Python module test!")
    return o_module.o_module_func()