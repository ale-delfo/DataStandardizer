from antlr3 import *
import resources.SparkLexer as sl
import resources.SparkParser as sp
import shutil

try:
    shutil.rmtree('output')
except:
    pass

lexer = sl.SparkLexer(ANTLRFileStream('resources/firstProgram.dtsd'))
tokens = CommonTokenStream(lexer)
parser = sp.SparkParser(tokens)
parser.startRule()
print('Parsing done.')
standardizer = parser.getStandardizer()
standardizer.toString()