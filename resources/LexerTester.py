from antlr3 import *
import SparkLexer as t

lexer = t.SparkLexer(ANTLRFileStream('resources/firstProgram.dtsd'))
i = 1

while (token:=lexer.nextToken()).getType() != t.EOF:
    if token.channel != t.HIDDEN:
        if i == 49:
            print('Here')
        print('-----------------------------')
        print(f'Token {i}:')
        print(f'Type: {t.tokenNamesMap[token.type]}')
        print(f'Position: {token.line}:{token.charPositionInLine}')
        print(f'Content: {token.text}')
        i+=1