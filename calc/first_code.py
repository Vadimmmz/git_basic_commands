import argparse

def calc_addition(a, b):
    return a+b


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--a", '-a', help="The first number")
    parser.add_argument("--b", '-b', help="The second number")
    args = parser.parse_args()

    try:
        if args.a and args.b:
            print(calc_addition(int(args.a), int(args.b)))
    except(TypeError):
        print('a and b must be integer')
    except(ValueError):
        print('a and b must be integer')