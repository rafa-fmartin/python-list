import sys


def validate():
    if len(sys.argv) != 3:
        print("ERROR")
        return False
    if sys.argv[1].isnumeric():
        print("ERROR")
        return False
    if not sys.argv[1].isprintable() or not sys.argv[2].isnumeric():
        print("ERROR")
        return False
    return True


def main(): 
    if validate():
        new_text = [i for i in sys.argv[1] if i.isalnum() or i.isspace()]
        list_text = ''.join(new_text).split()
        
        print([item for item in list_text if len(item) > int(sys.argv[2])])


if __name__ == '__main__':
    main()