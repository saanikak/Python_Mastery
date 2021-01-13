import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help='First number')
    parser.add_argument('--number2', help = 'Second number')
    parser.add_argument('--operation', help='type of operation', \
        choices= ['add', 'subtract'])

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    if args.operation == 'add':
        print('Result:', int(args.number1) + int(args.number2))
    elif args.operation == 'subtract':
        print('Result:' , int(args.number1) - int(args.number2))
    else:
        print('unsupported')

    

