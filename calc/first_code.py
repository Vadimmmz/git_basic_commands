import argparse

def calc_addition(a, b):
    return a+b

def calc_multiplication(a, b):
    return a*b

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--first", '-f', help="The first number")
    parser.add_argument("--second", '-s', help="The second number")
    parser.add_argument("--action", '-a', help="The second number")
    args = parser.parse_args()

    try:
        if args.first and args.second:
            if args.action == 'add':
                print(calc_addition(int(args.first), int(args.second)))
            elif args.action == 'mult':
                print(calc_multiplication(int(args.first), int(args.second)))
            else:
                print("-a parameter not recieved, you should declare -a parameter ")
    except(TypeError):
        print('a and b must be integer')
    except(ValueError):
        print('a and b must be integer')