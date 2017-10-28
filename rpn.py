#!/usr/bin/env python3
import operator
import readline
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', help = 'print debug info for stack, oper, or all')
    args = parser.parse_args()

    stackDebug = args.debug == 'all' or args.debug == 'stack'
    operDebug = args.debug == 'all' or args.debug == 'oper'
else:
    stackDebug = False
    operDebug = False

ops = {
    '+': operator.add,
    '-': operator.sub,
    '^': operator.pow,
    '*': operator.mul
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1, arg2)
            stack.append(result)
            if operDebug:
                print(token, function)
        if stackDebug:
            print(stack)
    val = stack.pop()
    print('Result:', val)
    return val

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()

