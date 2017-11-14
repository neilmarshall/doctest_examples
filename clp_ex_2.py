import argparse
import datetime
import unittest
import unittest.mock as mock


def fetch_total(who):
    pass


def add_record(*args):
    pass


def parse_command_line(*args):

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')

    parser_fetch = subparsers.add_parser('fetch')
    parser_fetch.add_argument('who', choices=['N', 'n', 'S', 's', 'J', 'j', 'all'])

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('payee', choices=['N', 'n', 'S', 's', 'J', 'j'])
    parser_add.add_argument('amount', type=float)
    parser_add.add_argument('description')
    parser_add.add_argument('-d', '--date',
        type=lambda x: datetime.datetime.strptime(x.strip(), '%d-%m-%Y'))

    args = parser.parse_args(*args)
    
    if args.cmd == 'fetch':
        return fetch_total(args.who)
    elif args.cmd == 'add':
        return add_record(args.payee, args.amount, args.description, args.date)
    else:
        return AttributeError


@mock.patch('__main__.add_record', autospec=True)
@mock.patch('__main__.fetch_total', autospec=True)
class Test_parse_command_line(unittest.TestCase):
    
    def test_fetch_calls_fetch_total(self, mock_fetch_total, mock_add_record):
        args = ['fetch', 'all']
        parse_command_line(args)
        mock_fetch_total.assert_called_with('any')
        mock_add_record.assert_not_called()

    def test_add_calls_add_record_without_date(self, mock_fetch_total, mock_add_record):
        args = ['add', 'J', '500', 'some description']
        parse_command_line(args)
        mock_fetch_total.assert_not_called()
        mock_add_record.assert_called_with('J', 500.0, 'some description', None)

    def test_add_calls_add_record_with_date(self, mock_fetch_total, mock_add_record):
        args = ['add', 'J', '500', 'some description', '--date', '13-11-2017']
        parse_command_line(args)
        mock_fetch_total.assert_not_called()
        mock_add_record.assert_called_with('J', 500.0, 'some description', datetime.datetime(2017, 11, 13))


if __name__ == '__main__':
    unittest.main()
