# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-21 22:58:11

import sys
from antlr3 import *

        
from Standardizer import Standardizer



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CAST_COLUMN=4
CL=5
COLUMN_SQUARED=6
COMMA=7
COMMENT=8
CREATE_LITERAL=9
DEDUPLICATE=10
DESTINATION=11
FILE_FORMAT=12
LP=13
NORMALIZE_COLUMNS=14
RENAME_COLUMN=15
RIGHT_ARROW=16
RP=17
SC=18
SOURCE=19
STRING=20
TEXT=21
TYPE=22
UNIX_TIME_UNIT=23
WS=24

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COLUMN_SQUARED", 7: "COMMA", 
    8: "COMMENT", 9: "CREATE_LITERAL", 10: "DEDUPLICATE", 11: "DESTINATION", 
    12: "FILE_FORMAT", 13: "LP", 14: "NORMALIZE_COLUMNS", 15: "RENAME_COLUMN", 
    16: "RIGHT_ARROW", 17: "RP", 18: "SC", 19: "SOURCE", 20: "STRING", 21: "TEXT", 
    22: "TYPE", 23: "UNIX_TIME_UNIT", 24: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CAST_COLUMN", "CL", "COLUMN_SQUARED", "COMMA", "COMMENT", "CREATE_LITERAL", 
    "DEDUPLICATE", "DESTINATION", "FILE_FORMAT", "LP", "NORMALIZE_COLUMNS", 
    "RENAME_COLUMN", "RIGHT_ARROW", "RP", "SC", "SOURCE", "STRING", "TEXT", 
    "TYPE", "UNIX_TIME_UNIT", "WS"
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



    # $ANTLR start "startRule"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: startRule : source_definition destination_definition ( action SC )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition destination_definition ( action SC )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition destination_definition ( action SC )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule48)
                self.source_definition()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_destination_definition_in_startRule52)
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
                        self._state.following.append(self.FOLLOW_action_in_startRule57)
                        self.action()

                        self._state.following.pop()

                        self.match(self.input, SC, self.FOLLOW_SC_in_startRule59)


                    else:
                        break #loop1


                self.match(self.input, EOF, self.FOLLOW_EOF_in_startRule65)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "startRule"



    # $ANTLR start "source_definition"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:27:1: source_definition : SOURCE CL source= TEXT LP format= FILE_FORMAT RP ;
    def source_definition(self, ):
        source = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:28:2: ( SOURCE CL source= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:29:4: SOURCE CL source= TEXT LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition80)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition82)

                source = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_source_definition86)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition88)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition92)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition94)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:33:1: destination_definition : DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP ;
    def destination_definition(self, ):
        destination = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:34:2: ( DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:35:4: DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition114)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition116)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition120)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition122)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition126)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition128)

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
                    self._state.following.append(self.FOLLOW_rename_action_in_action148)
                    self.rename_action()

                    self._state.following.pop()


                elif alt2 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action154)
                    self.cast_action()

                    self._state.following.pop()


                elif alt2 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action160)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt2 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action166)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt2 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: normalize_action
                    pass 
                    self._state.following.append(self.FOLLOW_normalize_action_in_action172)
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:1: cast_action : CAST_COLUMN LP ( TEXT | COLUMN_SQUARED ) RP LP TYPE RIGHT_ARROW TYPE RP ;
    def cast_action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:53:2: ( CAST_COLUMN LP ( TEXT | COLUMN_SQUARED ) RP LP TYPE RIGHT_ARROW TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:54:2: CAST_COLUMN LP ( TEXT | COLUMN_SQUARED ) RP LP TYPE RIGHT_ARROW TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action193)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action195)

                if self.input.LA(1) in {COLUMN_SQUARED, TEXT}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action203)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action205)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action207)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action209)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action211)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action213)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "cast_action"



    # $ANTLR start "create_literal_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:57:1: create_literal_action : CREATE_LITERAL LP x= ( TEXT | COLUMN_SQUARED ) RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:58:2: ( CREATE_LITERAL LP x= ( TEXT | COLUMN_SQUARED ) RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:59:2: CREATE_LITERAL LP x= ( TEXT | COLUMN_SQUARED ) RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action227)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action229)

                x = self.input.LT(1)

                if self.input.LA(1) in {COLUMN_SQUARED, TEXT}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action239)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action241)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action245)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action247)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:63:1: deduplicate_action : DEDUPLICATE LP ( TEXT | COLUMN_SQUARED ) ( COMMA ( TEXT | COLUMN_SQUARED ) )* RP ;
    def deduplicate_action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:2: ( DEDUPLICATE LP ( TEXT | COLUMN_SQUARED ) ( COMMA ( TEXT | COLUMN_SQUARED ) )* RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:2: DEDUPLICATE LP ( TEXT | COLUMN_SQUARED ) ( COMMA ( TEXT | COLUMN_SQUARED ) )* RP
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action263)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action265)

                if self.input.LA(1) in {COLUMN_SQUARED, TEXT}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:39: ( COMMA ( TEXT | COLUMN_SQUARED ) )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COMMA) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:40: COMMA ( TEXT | COLUMN_SQUARED )
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action274)

                        if self.input.LA(1) in {COLUMN_SQUARED, TEXT}:
                            self.input.consume()
                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop3


                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action284)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "deduplicate_action"



    # $ANTLR start "rename_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:69:1: rename_action : RENAME_COLUMN LP x= ( TEXT | COLUMN_SQUARED ) RIGHT_ARROW y= ( TEXT | COLUMN_SQUARED ) RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:70:2: ( RENAME_COLUMN LP x= ( TEXT | COLUMN_SQUARED ) RIGHT_ARROW y= ( TEXT | COLUMN_SQUARED ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:71:2: RENAME_COLUMN LP x= ( TEXT | COLUMN_SQUARED ) RIGHT_ARROW y= ( TEXT | COLUMN_SQUARED ) RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action299)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action301)

                x = self.input.LT(1)

                if self.input.LA(1) in {COLUMN_SQUARED, TEXT}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action311)

                y = self.input.LT(1)

                if self.input.LA(1) in {COLUMN_SQUARED, TEXT}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action321)

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
                self.match(self.input, NORMALIZE_COLUMNS, self.FOLLOW_NORMALIZE_COLUMNS_in_normalize_action336)

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



 

    FOLLOW_source_definition_in_startRule48 = frozenset([11])
    FOLLOW_destination_definition_in_startRule52 = frozenset([4, 9, 10, 14, 15])
    FOLLOW_action_in_startRule57 = frozenset([18])
    FOLLOW_SC_in_startRule59 = frozenset([4, 9, 10, 14, 15])
    FOLLOW_EOF_in_startRule65 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition80 = frozenset([5])
    FOLLOW_CL_in_source_definition82 = frozenset([21])
    FOLLOW_TEXT_in_source_definition86 = frozenset([13])
    FOLLOW_LP_in_source_definition88 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_source_definition92 = frozenset([17])
    FOLLOW_RP_in_source_definition94 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition114 = frozenset([5])
    FOLLOW_CL_in_destination_definition116 = frozenset([21])
    FOLLOW_TEXT_in_destination_definition120 = frozenset([13])
    FOLLOW_LP_in_destination_definition122 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_destination_definition126 = frozenset([17])
    FOLLOW_RP_in_destination_definition128 = frozenset([1])
    FOLLOW_rename_action_in_action148 = frozenset([1])
    FOLLOW_cast_action_in_action154 = frozenset([1])
    FOLLOW_create_literal_action_in_action160 = frozenset([1])
    FOLLOW_deduplicate_action_in_action166 = frozenset([1])
    FOLLOW_normalize_action_in_action172 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action193 = frozenset([13])
    FOLLOW_LP_in_cast_action195 = frozenset([6, 21])
    FOLLOW_set_in_cast_action197 = frozenset([17])
    FOLLOW_RP_in_cast_action203 = frozenset([13])
    FOLLOW_LP_in_cast_action205 = frozenset([22])
    FOLLOW_TYPE_in_cast_action207 = frozenset([16])
    FOLLOW_RIGHT_ARROW_in_cast_action209 = frozenset([22])
    FOLLOW_TYPE_in_cast_action211 = frozenset([17])
    FOLLOW_RP_in_cast_action213 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action227 = frozenset([13])
    FOLLOW_LP_in_create_literal_action229 = frozenset([6, 21])
    FOLLOW_set_in_create_literal_action233 = frozenset([17])
    FOLLOW_RP_in_create_literal_action239 = frozenset([13])
    FOLLOW_LP_in_create_literal_action241 = frozenset([20])
    FOLLOW_STRING_in_create_literal_action245 = frozenset([17])
    FOLLOW_RP_in_create_literal_action247 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action263 = frozenset([13])
    FOLLOW_LP_in_deduplicate_action265 = frozenset([6, 21])
    FOLLOW_set_in_deduplicate_action267 = frozenset([7, 17])
    FOLLOW_COMMA_in_deduplicate_action274 = frozenset([6, 21])
    FOLLOW_set_in_deduplicate_action276 = frozenset([7, 17])
    FOLLOW_RP_in_deduplicate_action284 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action299 = frozenset([13])
    FOLLOW_LP_in_rename_action301 = frozenset([6, 21])
    FOLLOW_set_in_rename_action305 = frozenset([16])
    FOLLOW_RIGHT_ARROW_in_rename_action311 = frozenset([6, 21])
    FOLLOW_set_in_rename_action315 = frozenset([17])
    FOLLOW_RP_in_rename_action321 = frozenset([1])
    FOLLOW_NORMALIZE_COLUMNS_in_normalize_action336 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
