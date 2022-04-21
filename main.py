from antlr3 import *
import resources.SparkLexer as sl
import resources.SparkParser as sp

lexer = sl.SparkLexer(ANTLRFileStream('resources/firstProgram.dtsd'))
tokens = CommonTokenStream(lexer)
parser = sp.SparkParser(tokens)
parser.start()

standardizer = parser.getStandardizer()

standardizer.execute()

#i = 1

#while (token := lexer.nextToken()).type != sl.EOF:
#    if token.channel != sl.HIDDEN:
#        line = token.line
#        charpositioninline = token.charPositionInLine
#        type = sl.tokenNamesMap[token.type]
#        text = token.text
#        print('Token n. %d: line %d, charposition %d, type %s, text %s' %(i,line,charpositioninline,type,text))
#        i+=1