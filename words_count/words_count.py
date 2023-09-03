import argparse
# Changes from web IDE

def count(text: str) -> int:
    return len(text.split(" "))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--text", '-t', help="text for count")
    args = parser.parse_args()

    if args.text:
        print(count(args.text))


