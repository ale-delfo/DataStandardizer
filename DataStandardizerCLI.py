import argparse
from antlr3 import *
import resources.SparkLexer as sl
import resources.SparkParser as sp

parser = argparse.ArgumentParser()
parser.add_argument('file', help='File containing the program to execute')
parser.add_argument('--dry-run', help='Just print out the operations without executing', action='store_true')

args = parser.parse_args()

file = args.file
dry_run = args.dry_run

lexer = sl.SparkLexer(ANTLRFileStream(file))
tokens = CommonTokenStream(lexer)
parser = sp.SparkParser(tokens)

parser.startRule()

print('Parsing done.')

standardizer = parser.getStandardizer()

if dry_run:
    standardizer.toString()
else:
    standardizer.execute()

