# $ANTLR 3.5.1 /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-21 15:49:47

import sys
from antlr3 import *

        
from Standardizer import Standardizer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CAST_COLUMN=4
CL=5
COMMA=6
COMMENT=7
CREATE_LITERAL=8
DEDUPLICATE=9
DESTINATION=10
FILE_FORMAT=11
ID=12
LP=13
RENAME_COLUMN=14
RIGHT_ARROW=15
RP=16
SC=17
SOURCE=18
STRING=19
TYPE=20
UNIX_TIME_UNIT=21
WS=22

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COMMA", 7: "COMMENT", 8: "CREATE_LITERAL", 
    9: "DEDUPLICATE", 10: "DESTINATION", 11: "FILE_FORMAT", 12: "ID", 13: "LP", 
    14: "RENAME_COLUMN", 15: "RIGHT_ARROW", 16: "RP", 17: "SC", 18: "SOURCE", 
    19: "STRING", 20: "TYPE", 21: "UNIX_TIME_UNIT", 22: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CAST_COLUMN", "CL", "COMMA", "COMMENT", "CREATE_LITERAL", "DEDUPLICATE", 
    "DESTINATION", "FILE_FORMAT", "ID", "LP", "RENAME_COLUMN", "RIGHT_ARROW", 
    "RP", "SC", "SOURCE", "STRING", "TYPE", "UNIX_TIME_UNIT", "WS"
]



class SparkParser(Parser):
    grammarFileName = "/Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)




        self.delegates = []




             
    standardizer = Standardizer()
    def getStandardizer(self):
        return self.standardizer



    # $ANTLR start "start"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: start : source_definition destination_definition ( action SC )* EOF ;
    def start(self, ):
        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition destination_definition ( action SC )* EOF )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition destination_definition ( action SC )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_start49)
                self.source_definition()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_destination_definition_in_start53)
                self.destination_definition()

                self._state.following.pop()

                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:23:3: ( action SC )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 in {CAST_COLUMN, CREATE_LITERAL, DEDUPLICATE, RENAME_COLUMN}) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:23:4: action SC
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_start58)
                        self.action()

                        self._state.following.pop()

                        self.match(self.input, SC, self.FOLLOW_SC_in_start60)


                    else:
                        break #loop1


                self.match(self.input, EOF, self.FOLLOW_EOF_in_start66)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "start"



    # $ANTLR start "source_definition"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:27:1: source_definition : SOURCE CL source= STRING LP format= FILE_FORMAT RP ;
    def source_definition(self, ):
        source = None
        format = None

        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:28:2: ( SOURCE CL source= STRING LP format= FILE_FORMAT RP )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:29:4: SOURCE CL source= STRING LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition81)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition83)

                source = self.match(self.input, STRING, self.FOLLOW_STRING_in_source_definition87)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition89)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition93)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition95)

                #action start
                self.standardizer.setSource(source.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "source_definition"



    # $ANTLR start "destination_definition"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:33:1: destination_definition : DESTINATION CL destination= STRING LP format= FILE_FORMAT RP ;
    def destination_definition(self, ):
        destination = None
        format = None

        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:34:2: ( DESTINATION CL destination= STRING LP format= FILE_FORMAT RP )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:35:4: DESTINATION CL destination= STRING LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition115)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition117)

                destination = self.match(self.input, STRING, self.FOLLOW_STRING_in_destination_definition121)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition123)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition127)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition129)

                #action start
                print(f'Found Source in path {destination.text}, the file format specified is {format.text}')
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "destination_definition"



    # $ANTLR start "action"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:39:1: action : ( rename_action | cast_action | create_literal_action | deduplicate_action );
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:39:9: ( rename_action | cast_action | create_literal_action | deduplicate_action )
                alt2 = 4
                LA2 = self.input.LA(1)
                if LA2 in {RENAME_COLUMN}:
                    alt2 = 1
                elif LA2 in {CAST_COLUMN}:
                    alt2 = 2
                elif LA2 in {CREATE_LITERAL}:
                    alt2 = 3
                elif LA2 in {DEDUPLICATE}:
                    alt2 = 4
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:40:3: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action148)
                    self.rename_action()

                    self._state.following.pop()


                elif alt2 == 2:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:41:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action154)
                    self.cast_action()

                    self._state.following.pop()


                elif alt2 == 3:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:42:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action160)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt2 == 4:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action166)
                    self.deduplicate_action()

                    self._state.following.pop()



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "action"



    # $ANTLR start "cast_action"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:47:1: cast_action : CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP ;
    def cast_action(self, ):
        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:48:2: ( CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:49:2: CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action183)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action185)

                self.match(self.input, ID, self.FOLLOW_ID_in_cast_action187)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action189)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action191)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action193)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action195)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action197)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action199)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "cast_action"



    # $ANTLR start "create_literal_action"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:52:1: create_literal_action : CREATE_LITERAL LP ID RP LP STRING RP ;
    def create_literal_action(self, ):
        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:53:2: ( CREATE_LITERAL LP ID RP LP STRING RP )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:54:2: CREATE_LITERAL LP ID RP LP STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action213)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action215)

                self.match(self.input, ID, self.FOLLOW_ID_in_create_literal_action217)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action219)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action221)

                self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action223)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action225)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "create_literal_action"



    # $ANTLR start "deduplicate_action"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:57:1: deduplicate_action : DEDUPLICATE LP ID ( COMMA ID )* RP ;
    def deduplicate_action(self, ):
        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:58:2: ( DEDUPLICATE LP ID ( COMMA ID )* RP )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:59:2: DEDUPLICATE LP ID ( COMMA ID )* RP
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action238)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action240)

                self.match(self.input, ID, self.FOLLOW_ID_in_deduplicate_action242)

                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:59:20: ( COMMA ID )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COMMA) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:59:21: COMMA ID
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action245)

                        self.match(self.input, ID, self.FOLLOW_ID_in_deduplicate_action247)


                    else:
                        break #loop3


                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action251)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "deduplicate_action"



    # $ANTLR start "rename_action"
    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:63:1: rename_action : RENAME_COLUMN LP ID RIGHT_ARROW ID RP ;
    def rename_action(self, ):
        try:
            try:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:64:2: ( RENAME_COLUMN LP ID RIGHT_ARROW ID RP )
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:65:2: RENAME_COLUMN LP ID RIGHT_ARROW ID RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action266)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action268)

                self.match(self.input, ID, self.FOLLOW_ID_in_rename_action270)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action272)

                self.match(self.input, ID, self.FOLLOW_ID_in_rename_action274)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action276)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "rename_action"



 

    FOLLOW_source_definition_in_start49 = frozenset([10])
    FOLLOW_destination_definition_in_start53 = frozenset([4, 8, 9, 14])
    FOLLOW_action_in_start58 = frozenset([17])
    FOLLOW_SC_in_start60 = frozenset([4, 8, 9, 14])
    FOLLOW_EOF_in_start66 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition81 = frozenset([5])
    FOLLOW_CL_in_source_definition83 = frozenset([19])
    FOLLOW_STRING_in_source_definition87 = frozenset([13])
    FOLLOW_LP_in_source_definition89 = frozenset([11])
    FOLLOW_FILE_FORMAT_in_source_definition93 = frozenset([16])
    FOLLOW_RP_in_source_definition95 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition115 = frozenset([5])
    FOLLOW_CL_in_destination_definition117 = frozenset([19])
    FOLLOW_STRING_in_destination_definition121 = frozenset([13])
    FOLLOW_LP_in_destination_definition123 = frozenset([11])
    FOLLOW_FILE_FORMAT_in_destination_definition127 = frozenset([16])
    FOLLOW_RP_in_destination_definition129 = frozenset([1])
    FOLLOW_rename_action_in_action148 = frozenset([1])
    FOLLOW_cast_action_in_action154 = frozenset([1])
    FOLLOW_create_literal_action_in_action160 = frozenset([1])
    FOLLOW_deduplicate_action_in_action166 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action183 = frozenset([13])
    FOLLOW_LP_in_cast_action185 = frozenset([12])
    FOLLOW_ID_in_cast_action187 = frozenset([16])
    FOLLOW_RP_in_cast_action189 = frozenset([13])
    FOLLOW_LP_in_cast_action191 = frozenset([20])
    FOLLOW_TYPE_in_cast_action193 = frozenset([15])
    FOLLOW_RIGHT_ARROW_in_cast_action195 = frozenset([20])
    FOLLOW_TYPE_in_cast_action197 = frozenset([16])
    FOLLOW_RP_in_cast_action199 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action213 = frozenset([13])
    FOLLOW_LP_in_create_literal_action215 = frozenset([12])
    FOLLOW_ID_in_create_literal_action217 = frozenset([16])
    FOLLOW_RP_in_create_literal_action219 = frozenset([13])
    FOLLOW_LP_in_create_literal_action221 = frozenset([19])
    FOLLOW_STRING_in_create_literal_action223 = frozenset([16])
    FOLLOW_RP_in_create_literal_action225 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action238 = frozenset([13])
    FOLLOW_LP_in_deduplicate_action240 = frozenset([12])
    FOLLOW_ID_in_deduplicate_action242 = frozenset([6, 16])
    FOLLOW_COMMA_in_deduplicate_action245 = frozenset([12])
    FOLLOW_ID_in_deduplicate_action247 = frozenset([6, 16])
    FOLLOW_RP_in_deduplicate_action251 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action266 = frozenset([13])
    FOLLOW_LP_in_rename_action268 = frozenset([12])
    FOLLOW_ID_in_rename_action270 = frozenset([15])
    FOLLOW_RIGHT_ARROW_in_rename_action272 = frozenset([12])
    FOLLOW_ID_in_rename_action274 = frozenset([16])
    FOLLOW_RP_in_rename_action276 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
