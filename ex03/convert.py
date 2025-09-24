import sys

if __name__=="__main__":
    arg = sys.argv[1]
    try:
        arg_float = float(arg)
        print(arg_float)
    except ValueError:
        print("convertion impossiple")