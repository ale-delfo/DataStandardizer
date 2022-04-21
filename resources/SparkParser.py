# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-21 18:54:48

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
NORMALIZE_COLUMNS=14
PATH=15
RENAME_COLUMN=16
RIGHT_ARROW=17
RP=18
SC=19
SOURCE=20
STRING=21
TYPE=22
UNIX_TIME_UNIT=23
WS=24

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COMMA", 7: "COMMENT", 8: "CREATE_LITERAL", 
    9: "DEDUPLICATE", 10: "DESTINATION", 11: "FILE_FORMAT", 12: "ID", 13: "LP", 
    14: "NORMALIZE_COLUMNS", 15: "PATH", 16: "RENAME_COLUMN", 17: "RIGHT_ARROW", 
    18: "RP", 19: "SC", 20: "SOURCE", 21: "STRING", 22: "TYPE", 23: "UNIX_TIME_UNIT", 
    24: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CAST_COLUMN", "CL", "COMMA", "COMMENT", "CREATE_LITERAL", "DEDUPLICATE", 
    "DESTINATION", "FILE_FORMAT", "ID", "LP", "NORMALIZE_COLUMNS", "PATH", 
    "RENAME_COLUMN", "RIGHT_ARROW", "RP", "SC", "SOURCE", "STRING", "TYPE", 
    "UNIX_TIME_UNIT", "WS"
]



class SparkParser(Parser):
    grammarFileName = "/Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g"
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: start : source_definition destination_definition ( action SC )* EOF ;
    def start(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition destination_definition ( action SC )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition destination_definition ( action SC )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_start49)
                self.source_definition()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_destination_definition_in_start53)
                self.destination_definition()

                self._state.following.pop()

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:3: ( action SC )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 in {CAST_COLUMN, CREATE_LITERAL, DEDUPLICATE, NORMALIZE_COLUMNS, RENAME_COLUMN}) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:4: action SC
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:27:1: source_definition : SOURCE CL source= PATH LP format= FILE_FORMAT RP ;
    def source_definition(self, ):
        source = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:28:2: ( SOURCE CL source= PATH LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:29:4: SOURCE CL source= PATH LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition81)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition83)

                source = self.match(self.input, PATH, self.FOLLOW_PATH_in_source_definition87)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition89)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition93)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition95)

                #action start
                self.standardizer.setSource(source.text, format.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "source_definition"



    # $ANTLR start "destination_definition"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:33:1: destination_definition : DESTINATION CL destination= PATH LP format= FILE_FORMAT RP ;
    def destination_definition(self, ):
        destination = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:34:2: ( DESTINATION CL destination= PATH LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:35:4: DESTINATION CL destination= PATH LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition115)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition117)

                destination = self.match(self.input, PATH, self.FOLLOW_PATH_in_destination_definition121)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition123)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition127)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition129)

                #action start
                self.standardizer.setDestination(destination.text, format.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "destination_definition"



    # $ANTLR start "action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:40:1: action : ( rename_action | cast_action | create_literal_action | deduplicate_action | normalize_action );
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:40:9: ( rename_action | cast_action | create_literal_action | deduplicate_action | normalize_action )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 in {RENAME_COLUMN}:
                    alt2 = 1
                elif LA2 in {CAST_COLUMN}:
                    alt2 = 2
                elif LA2 in {CREATE_LITERAL}:
                    alt2 = 3
                elif LA2 in {DEDUPLICATE}:
                    alt2 = 4
                elif LA2 in {NORMALIZE_COLUMNS}:
                    alt2 = 5
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:41:3: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action149)
                    self.rename_action()

                    self._state.following.pop()


                elif alt2 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action155)
                    self.cast_action()

                    self._state.following.pop()


                elif alt2 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action161)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt2 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action167)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt2 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: normalize_action
                    pass 
                    self._state.following.append(self.FOLLOW_normalize_action_in_action173)
                    self.normalize_action()

                    self._state.following.pop()



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "action"



    # $ANTLR start "cast_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:1: cast_action : CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP ;
    def cast_action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:53:2: ( CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:54:2: CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action194)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action196)

                self.match(self.input, ID, self.FOLLOW_ID_in_cast_action198)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action200)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action202)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action204)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action206)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action208)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action210)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "cast_action"



    # $ANTLR start "create_literal_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:57:1: create_literal_action : CREATE_LITERAL LP x= ID RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:58:2: ( CREATE_LITERAL LP x= ID RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:59:2: CREATE_LITERAL LP x= ID RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action224)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action226)

                x = self.match(self.input, ID, self.FOLLOW_ID_in_create_literal_action230)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action232)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action234)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action238)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action240)

                #action start
                self.standardizer.addAction(self.standardizer.createLiteral,x.text,y.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "create_literal_action"



    # $ANTLR start "deduplicate_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:63:1: deduplicate_action : DEDUPLICATE LP ID ( COMMA ID )* RP ;
    def deduplicate_action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:2: ( DEDUPLICATE LP ID ( COMMA ID )* RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:2: DEDUPLICATE LP ID ( COMMA ID )* RP
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action256)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action258)

                self.match(self.input, ID, self.FOLLOW_ID_in_deduplicate_action260)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:20: ( COMMA ID )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COMMA) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:21: COMMA ID
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action263)

                        self.match(self.input, ID, self.FOLLOW_ID_in_deduplicate_action265)


                    else:
                        break #loop3


                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action269)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "deduplicate_action"



    # $ANTLR start "rename_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:69:1: rename_action : RENAME_COLUMN LP x= ID RIGHT_ARROW y= ID RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:70:2: ( RENAME_COLUMN LP x= ID RIGHT_ARROW y= ID RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:71:2: RENAME_COLUMN LP x= ID RIGHT_ARROW y= ID RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action284)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action286)

                x = self.match(self.input, ID, self.FOLLOW_ID_in_rename_action290)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action292)

                y = self.match(self.input, ID, self.FOLLOW_ID_in_rename_action296)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action298)

                #action start
                self.standardizer.addAction(self.standardizer.renameColumn,x.text,y.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "rename_action"



    # $ANTLR start "normalize_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:75:1: normalize_action : NORMALIZE_COLUMNS ;
    def normalize_action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:2: ( NORMALIZE_COLUMNS )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:4: NORMALIZE_COLUMNS
                pass 
                self.match(self.input, NORMALIZE_COLUMNS, self.FOLLOW_NORMALIZE_COLUMNS_in_normalize_action313)

                #action start
                self.standardizer.normalizeColumns=True
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "normalize_action"



 

    FOLLOW_source_definition_in_start49 = frozenset([10])
    FOLLOW_destination_definition_in_start53 = frozenset([4, 8, 9, 14, 16])
    FOLLOW_action_in_start58 = frozenset([19])
    FOLLOW_SC_in_start60 = frozenset([4, 8, 9, 14, 16])
    FOLLOW_EOF_in_start66 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition81 = frozenset([5])
    FOLLOW_CL_in_source_definition83 = frozenset([15])
    FOLLOW_PATH_in_source_definition87 = frozenset([13])
    FOLLOW_LP_in_source_definition89 = frozenset([11])
    FOLLOW_FILE_FORMAT_in_source_definition93 = frozenset([18])
    FOLLOW_RP_in_source_definition95 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition115 = frozenset([5])
    FOLLOW_CL_in_destination_definition117 = frozenset([15])
    FOLLOW_PATH_in_destination_definition121 = frozenset([13])
    FOLLOW_LP_in_destination_definition123 = frozenset([11])
    FOLLOW_FILE_FORMAT_in_destination_definition127 = frozenset([18])
    FOLLOW_RP_in_destination_definition129 = frozenset([1])
    FOLLOW_rename_action_in_action149 = frozenset([1])
    FOLLOW_cast_action_in_action155 = frozenset([1])
    FOLLOW_create_literal_action_in_action161 = frozenset([1])
    FOLLOW_deduplicate_action_in_action167 = frozenset([1])
    FOLLOW_normalize_action_in_action173 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action194 = frozenset([13])
    FOLLOW_LP_in_cast_action196 = frozenset([12])
    FOLLOW_ID_in_cast_action198 = frozenset([18])
    FOLLOW_RP_in_cast_action200 = frozenset([13])
    FOLLOW_LP_in_cast_action202 = frozenset([22])
    FOLLOW_TYPE_in_cast_action204 = frozenset([17])
    FOLLOW_RIGHT_ARROW_in_cast_action206 = frozenset([22])
    FOLLOW_TYPE_in_cast_action208 = frozenset([18])
    FOLLOW_RP_in_cast_action210 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action224 = frozenset([13])
    FOLLOW_LP_in_create_literal_action226 = frozenset([12])
    FOLLOW_ID_in_create_literal_action230 = frozenset([18])
    FOLLOW_RP_in_create_literal_action232 = frozenset([13])
    FOLLOW_LP_in_create_literal_action234 = frozenset([21])
    FOLLOW_STRING_in_create_literal_action238 = frozenset([18])
    FOLLOW_RP_in_create_literal_action240 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action256 = frozenset([13])
    FOLLOW_LP_in_deduplicate_action258 = frozenset([12])
    FOLLOW_ID_in_deduplicate_action260 = frozenset([6, 18])
    FOLLOW_COMMA_in_deduplicate_action263 = frozenset([12])
    FOLLOW_ID_in_deduplicate_action265 = frozenset([6, 18])
    FOLLOW_RP_in_deduplicate_action269 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action284 = frozenset([13])
    FOLLOW_LP_in_rename_action286 = frozenset([12])
    FOLLOW_ID_in_rename_action290 = frozenset([17])
    FOLLOW_RIGHT_ARROW_in_rename_action292 = frozenset([12])
    FOLLOW_ID_in_rename_action296 = frozenset([18])
    FOLLOW_RP_in_rename_action298 = frozenset([1])
    FOLLOW_NORMALIZE_COLUMNS_in_normalize_action313 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
