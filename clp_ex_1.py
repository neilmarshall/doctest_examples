import argparse
import operator
import unittest
from functools import reduce


def clp_1(*args):
    """
    An example command line parser.

    Takes two positional integer arguments, and a third that can take zero or more arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('pos1', type=int)
    parser.add_argument('pos2', type=int)
    parser.add_argument('pos3', type=int, nargs='?')

    args = parser.parse_args(*args)

    return [args.pos1, args.pos2, args.pos3]


def clp_2(*args):
    """
    An example command line parser.

    Provides a flag that calls one of two functions.
    """

    def foo():
        return 'foo was called'

    def bar():
        return 'bar was called'

    parser = argparse.ArgumentParser()

    parser.add_argument('-func', action='store_const', const=foo, default=bar)

    args = parser.parse_args(*args)

    return args.func()


def clp_3(*args):
    """
    An example command line parser. Combines the two examples above.

    Takes two positional integer arguments, and a third that can take zero or more arguments.

    Provides a flag that overrides the above and calls a function.
    """

    def prod(iter):
        return reduce(operator.__mul__, iter)

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # create the parser for the override that sums a list of integers
    parser_process = subparsers.add_parser('process')
    parser_process.add_argument('--product', dest='aggregator', action='store_const', const=prod, default=sum)

    # create the parser for the situation where the override is not called and returns the integers passed
    parser_store = subparsers.add_parser('store')
    parser_store.add_argument('pos1', type=int)
    parser_store.add_argument('pos2', type=int)
    parser_store.add_argument('pos3', type=int, nargs='?')

    args = parser.parse_args(*args)

    ints = [4, 5, 6]

    if 'aggregator' in args:
        return args.aggregator(ints)
    else:
        return [args.pos1, args.pos2, args.pos3]


def clp_4(*args):
    """
    As for example 3, but the override flag takes no arguments.

    This example shows how to use parser.set_defaults.
    """

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')

    # create the parser for the override that sums a list of integers
    parser_func = subparsers.add_parser('func')
    parser_func.set_defaults(func=sum)

    # create the parser for the situation where the override is not called and returns the integers passed
    parser_store = subparsers.add_parser('store')
    parser_store.add_argument('pos1', type=int)
    parser_store.add_argument('pos2', type=int)
    parser_store.add_argument('pos3', type=int, nargs='?')

    args = parser.parse_args(*args)

    ints = [4, 5, 6]

    if args.cmd == 'func':
        return args.func(ints)
    else:
        return [args.pos1, args.pos2, args.pos3]


class Test_clp(unittest.TestCase):

    def test_args_ex_1_1(self):
        self.assertEqual(clp_1(['2', '4']), [2, 4, None])

    def test_args_ex_1_2(self):
        self.assertEqual(clp_1(['2', '4', '6']), [2, 4, 6])

    def test_args_ex_2_1(self):
        self.assertEqual(clp_2([]), 'bar was called')

    def test_args_ex_2_2(self):
        self.assertEqual(clp_2(['-f']), 'foo was called')

    def test_args_ex_3_1(self):
        self.assertEqual(clp_3(['process']), 15)

    def test_args_ex_3_2(self):
        self.assertEqual(clp_3(['process', '--product']), 120)

    def test_args_ex_3_3(self):
        self.assertEqual(clp_3(['store', '6', '7']), [6, 7, None])

    def test_args_ex_3_4(self):
        self.assertEqual(clp_3(['store', '6', '7', '8']), [6, 7, 8])

    def test_args_ex_4_1(self):
        self.assertEqual(clp_4(['func']), 15)

    def test_args_ex_4_2(self):
        self.assertEqual(clp_4(['store', '6', '7']), [6, 7, None])

    def test_args_ex_4_3(self):
        self.assertEqual(clp_4(['store', '6', '7', '8']), [6, 7, 8])


if __name__ == "__main__":
    unittest.main()
