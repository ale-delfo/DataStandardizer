# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-21 22:58:11

import sys
from antlr3 import *



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

class SparkLexer(Lexer):

    grammarFileName = "/Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )






    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:82:7: ( ',' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:82:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "TYPE"
    def mTYPE(self, ):
        try:
            _type = TYPE
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:7: ( 'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' )
            alt1 = 4
            LA1 = self.input.LA(1)
            if LA1 in {73}:
                alt1 = 1
            elif LA1 in {70}:
                alt1 = 2
            elif LA1 in {68}:
                alt1 = 3
            elif LA1 in {83}:
                alt1 = 4
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae


            if alt1 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:9: 'INT'
                pass 
                self.match("INT")



            elif alt1 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:17: 'FLOAT'
                pass 
                self.match("FLOAT")



            elif alt1 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:27: 'DOUBLE'
                pass 
                self.match("DOUBLE")



            elif alt1 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:38: 'STRING'
                pass 
                self.match("STRING")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "UNIX_TIME_UNIT"
    def mUNIX_TIME_UNIT(self, ):
        try:
            _type = UNIX_TIME_UNIT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:87:2: ( 's' | 'm' | 'n' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:
            pass 
            if self.input.LA(1) in {109, 110, 115}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNIX_TIME_UNIT"



    # $ANTLR start "RENAME_COLUMN"
    def mRENAME_COLUMN(self, ):
        try:
            _type = RENAME_COLUMN
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:90:2: ( 'RenameColumn' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:90:4: 'RenameColumn'
            pass 
            self.match("RenameColumn")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RENAME_COLUMN"



    # $ANTLR start "CAST_COLUMN"
    def mCAST_COLUMN(self, ):
        try:
            _type = CAST_COLUMN
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:2: ( 'Cast' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:4: 'Cast'
            pass 
            self.match("Cast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CAST_COLUMN"



    # $ANTLR start "CREATE_LITERAL"
    def mCREATE_LITERAL(self, ):
        try:
            _type = CREATE_LITERAL
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:96:2: ( 'CreateLiteral' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:96:4: 'CreateLiteral'
            pass 
            self.match("CreateLiteral")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CREATE_LITERAL"



    # $ANTLR start "DEDUPLICATE"
    def mDEDUPLICATE(self, ):
        try:
            _type = DEDUPLICATE
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:100:2: ( 'Deduplicate' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:100:4: 'Deduplicate'
            pass 
            self.match("Deduplicate")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEDUPLICATE"



    # $ANTLR start "NORMALIZE_COLUMNS"
    def mNORMALIZE_COLUMNS(self, ):
        try:
            _type = NORMALIZE_COLUMNS
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:103:2: ( 'Normalize' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:104:2: 'Normalize'
            pass 
            self.match("Normalize")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NORMALIZE_COLUMNS"



    # $ANTLR start "CL"
    def mCL(self, ):
        try:
            _type = CL
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:108:4: ( ':' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:108:6: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CL"



    # $ANTLR start "LP"
    def mLP(self, ):
        try:
            _type = LP
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:109:4: ( '(' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:109:6: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LP"



    # $ANTLR start "RP"
    def mRP(self, ):
        try:
            _type = RP
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:110:4: ( ')' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:110:6: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RP"



    # $ANTLR start "SC"
    def mSC(self, ):
        try:
            _type = SC
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:111:5: ( ';' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:111:7: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SC"



    # $ANTLR start "RIGHT_ARROW"
    def mRIGHT_ARROW(self, ):
        try:
            _type = RIGHT_ARROW
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:114:2: ( '->' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:114:4: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RIGHT_ARROW"



    # $ANTLR start "FILE_FORMAT"
    def mFILE_FORMAT(self, ):
        try:
            _type = FILE_FORMAT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:117:2: ( 'parquet' | 'csv' | 'json' | 'avro' )
            alt2 = 4
            LA2 = self.input.LA(1)
            if LA2 in {112}:
                alt2 = 1
            elif LA2 in {99}:
                alt2 = 2
            elif LA2 in {106}:
                alt2 = 3
            elif LA2 in {97}:
                alt2 = 4
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae


            if alt2 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:117:4: 'parquet'
                pass 
                self.match("parquet")



            elif alt2 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:118:4: 'csv'
                pass 
                self.match("csv")



            elif alt2 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:119:4: 'json'
                pass 
                self.match("json")



            elif alt2 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:120:4: 'avro'
                pass 
                self.match("avro")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FILE_FORMAT"



    # $ANTLR start "SOURCE"
    def mSOURCE(self, ):
        try:
            _type = SOURCE
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:124:8: ( 'Source' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:124:10: 'Source'
            pass 
            self.match("Source")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SOURCE"



    # $ANTLR start "DESTINATION"
    def mDESTINATION(self, ):
        try:
            _type = DESTINATION
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:127:2: ( 'Destination' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:127:4: 'Destination'
            pass 
            self.match("Destination")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DESTINATION"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:130:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 47) :
                LA6_1 = self.input.LA(2)

                if (LA6_1 == 47) :
                    alt6 = 1
                elif (LA6_1 == 42) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae


            if alt6 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:130:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:130:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((0 <= LA3_0 <= 9) or (14 <= LA3_0 <= 65535) or LA3_0 in {11, 12}) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop3


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:130:28: ( '\\r' )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 13) :
                    alt4 = 1
                if alt4 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:130:28: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            elif alt6 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:14: ( options {greedy=false; } : . )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 42) :
                        LA5_1 = self.input.LA(2)

                        if (LA5_1 == 47) :
                            alt5 = 2
                        elif ((0 <= LA5_1 <= 46) or (48 <= LA5_1 <= 65535) or LA5_1 in {}) :
                            alt5 = 1


                    elif ((0 <= LA5_0 <= 41) or (43 <= LA5_0 <= 65535) or LA5_0 in {}) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:42: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop5


                self.match("*/")


                #action start
                _channel=HIDDEN;
                #action end



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:134:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:134:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if self.input.LA(1) in {9, 10, 13, 32}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "COLUMN_SQUARED"
    def mCOLUMN_SQUARED(self, ):
        try:
            _type = COLUMN_SQUARED
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:142:15: ( '[' TEXT ( TEXT | ' ' )* ']' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:142:17: '[' TEXT ( TEXT | ' ' )* ']'
            pass 
            self.match(91)

            self.mTEXT()


            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:142:26: ( TEXT | ' ' )*
            while True: #loop7
                alt7 = 3
                LA7_0 = self.input.LA(1)

                if ((45 <= LA7_0 <= 57) or (65 <= LA7_0 <= 90) or (97 <= LA7_0 <= 122) or LA7_0 in {95, 124}) :
                    alt7 = 1
                elif (LA7_0 == 32) :
                    alt7 = 2


                if alt7 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:142:27: TEXT
                    pass 
                    self.mTEXT()



                elif alt7 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:142:32: ' '
                    pass 
                    self.match(32)


                else:
                    break #loop7


            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLUMN_SQUARED"



    # $ANTLR start "TEXT"
    def mTEXT(self, ):
        try:
            _type = TEXT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:144:7: ( ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+ )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:144:9: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
            pass 
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:144:9: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((45 <= LA8_0 <= 57) or (65 <= LA8_0 <= 90) or (97 <= LA8_0 <= 122) or LA8_0 in {95, 124}) :
                    alt8 = 1


                if alt8 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:
                    pass 
                    if (45 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95, 124}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt8 >= 1:
                        break #loop8

                    eee = EarlyExitException(8, self.input)
                    raise eee

                cnt8 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TEXT"



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:147:9: ( '\"' ( options {greedy=false; } : . )* '\"' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:147:11: '\"' ( options {greedy=false; } : . )* '\"'
            pass 
            self.match(34)

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:147:15: ( options {greedy=false; } : . )*
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 34) :
                    alt9 = 2
                elif ((0 <= LA9_0 <= 33) or (35 <= LA9_0 <= 65535) or LA9_0 in {}) :
                    alt9 = 1


                if alt9 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:147:43: .
                    pass 
                    self.matchAny()


                else:
                    break #loop9


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    def mTokens(self):
        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:8: ( COMMA | TYPE | UNIX_TIME_UNIT | RENAME_COLUMN | CAST_COLUMN | CREATE_LITERAL | DEDUPLICATE | NORMALIZE_COLUMNS | CL | LP | RP | SC | RIGHT_ARROW | FILE_FORMAT | SOURCE | DESTINATION | COMMENT | WS | COLUMN_SQUARED | TEXT | STRING )
        alt10 = 21
        alt10 = self.dfa10.predict(self.input)
        if alt10 == 1:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:10: COMMA
            pass 
            self.mCOMMA()



        elif alt10 == 2:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:16: TYPE
            pass 
            self.mTYPE()



        elif alt10 == 3:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:21: UNIX_TIME_UNIT
            pass 
            self.mUNIX_TIME_UNIT()



        elif alt10 == 4:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:36: RENAME_COLUMN
            pass 
            self.mRENAME_COLUMN()



        elif alt10 == 5:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:50: CAST_COLUMN
            pass 
            self.mCAST_COLUMN()



        elif alt10 == 6:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:62: CREATE_LITERAL
            pass 
            self.mCREATE_LITERAL()



        elif alt10 == 7:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:77: DEDUPLICATE
            pass 
            self.mDEDUPLICATE()



        elif alt10 == 8:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:89: NORMALIZE_COLUMNS
            pass 
            self.mNORMALIZE_COLUMNS()



        elif alt10 == 9:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:107: CL
            pass 
            self.mCL()



        elif alt10 == 10:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:110: LP
            pass 
            self.mLP()



        elif alt10 == 11:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:113: RP
            pass 
            self.mRP()



        elif alt10 == 12:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:116: SC
            pass 
            self.mSC()



        elif alt10 == 13:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:119: RIGHT_ARROW
            pass 
            self.mRIGHT_ARROW()



        elif alt10 == 14:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:131: FILE_FORMAT
            pass 
            self.mFILE_FORMAT()



        elif alt10 == 15:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:143: SOURCE
            pass 
            self.mSOURCE()



        elif alt10 == 16:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:150: DESTINATION
            pass 
            self.mDESTINATION()



        elif alt10 == 17:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:162: COMMENT
            pass 
            self.mCOMMENT()



        elif alt10 == 18:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:170: WS
            pass 
            self.mWS()



        elif alt10 == 19:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:173: COLUMN_SQUARED
            pass 
            self.mCOLUMN_SQUARED()



        elif alt10 == 20:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:188: TEXT
            pass 
            self.mTEXT()



        elif alt10 == 21:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:193: STRING
            pass 
            self.mSTRING()








    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        "\2\uffff\4\26\1\36\3\26\4\uffff\6\26\4\uffff\6\26\1\uffff\4\26\1"
        "\uffff\5\26\1\uffff\1\72\13\26\1\106\3\26\1\uffff\7\26\1\120\3\26"
        "\1\uffff\2\106\1\72\6\26\1\uffff\3\26\1\72\2\26\1\72\1\137\6\26"
        "\1\uffff\3\26\1\106\11\26\1\162\4\26\1\uffff\1\167\1\170\2\26\2"
        "\uffff\1\173\1\26\1\uffff\1\175\1\uffff"
        )

    DFA10_eof = DFA.unpack(
        "\176\uffff"
        )

    DFA10_min = DFA.unpack(
        "\1\11\1\uffff\1\116\1\114\1\117\1\124\1\55\1\145\1\141\1\157\4\uffff"
        "\1\76\1\141\2\163\1\166\1\52\4\uffff\1\124\1\117\1\125\1\144\1\122"
        "\1\165\1\uffff\1\156\1\163\1\145\1\162\1\uffff\1\162\1\166\1\157"
        "\1\162\1\0\1\uffff\1\55\1\101\1\102\1\165\1\164\1\111\1\162\1\141"
        "\1\164\1\141\1\155\1\161\1\55\1\156\1\157\1\0\1\uffff\1\124\1\114"
        "\1\160\1\151\1\116\1\143\1\155\1\55\1\164\1\141\1\165\1\uffff\3"
        "\55\1\105\1\154\1\156\1\107\2\145\1\uffff\1\145\1\154\1\145\1\55"
        "\1\151\1\141\2\55\1\103\1\114\1\151\1\164\1\143\1\164\1\uffff\1"
        "\157\1\151\1\172\1\55\1\141\1\151\1\154\1\164\1\145\1\164\1\157"
        "\1\165\1\145\1\55\1\145\1\156\1\155\1\162\1\uffff\2\55\1\156\1\141"
        "\2\uffff\1\55\1\154\1\uffff\1\55\1\uffff"
        )

    DFA10_max = DFA.unpack(
        "\1\174\1\uffff\1\116\1\114\1\145\1\157\1\174\1\145\1\162\1\157\4"
        "\uffff\1\76\1\141\2\163\1\166\1\57\4\uffff\1\124\1\117\1\125\1\163"
        "\1\122\1\165\1\uffff\1\156\1\163\1\145\1\162\1\uffff\1\162\1\166"
        "\1\157\1\162\1\uffff\1\uffff\1\174\1\101\1\102\1\165\1\164\1\111"
        "\1\162\1\141\1\164\1\141\1\155\1\161\1\174\1\156\1\157\1\uffff\1"
        "\uffff\1\124\1\114\1\160\1\151\1\116\1\143\1\155\1\174\1\164\1\141"
        "\1\165\1\uffff\3\174\1\105\1\154\1\156\1\107\2\145\1\uffff\1\145"
        "\1\154\1\145\1\174\1\151\1\141\2\174\1\103\1\114\1\151\1\164\1\143"
        "\1\164\1\uffff\1\157\1\151\1\172\1\174\1\141\1\151\1\154\1\164\1"
        "\145\1\164\1\157\1\165\1\145\1\174\1\145\1\156\1\155\1\162\1\uffff"
        "\2\174\1\156\1\141\2\uffff\1\174\1\154\1\uffff\1\174\1\uffff"
        )

    DFA10_accept = DFA.unpack(
        "\1\uffff\1\1\10\uffff\1\11\1\12\1\13\1\14\6\uffff\1\22\1\23\1\24"
        "\1\25\6\uffff\1\3\4\uffff\1\15\5\uffff\1\21\20\uffff\1\2\13\uffff"
        "\1\16\11\uffff\1\5\16\uffff\1\17\22\uffff\1\10\4\uffff\1\7\1\20"
        "\2\uffff\1\4\1\uffff\1\6"
        )

    DFA10_special = DFA.unpack(
        "\50\uffff\1\0\20\uffff\1\1\104\uffff"
        )


    DFA10_transition = [
        DFA.unpack("\2\24\2\uffff\1\24\22\uffff\1\24\1\uffff\1\27\5\uffff"
        "\1\13\1\14\2\uffff\1\1\1\16\1\26\1\23\12\26\1\12\1\15\5\uffff\2"
        "\26\1\10\1\4\1\26\1\3\2\26\1\2\4\26\1\11\3\26\1\7\1\5\7\26\1\25"
        "\3\uffff\1\26\1\uffff\1\22\1\26\1\20\6\26\1\21\2\26\2\6\1\26\1\17"
        "\2\26\1\6\7\26\1\uffff\1\26"),
        DFA.unpack(""),
        DFA.unpack("\1\30"),
        DFA.unpack("\1\31"),
        DFA.unpack("\1\32\25\uffff\1\33"),
        DFA.unpack("\1\34\32\uffff\1\35"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\37"),
        DFA.unpack("\1\40\20\uffff\1\41"),
        DFA.unpack("\1\42"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\43"),
        DFA.unpack("\1\44"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46"),
        DFA.unpack("\1\47"),
        DFA.unpack("\1\51\4\uffff\1\50"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\52"),
        DFA.unpack("\1\53"),
        DFA.unpack("\1\54"),
        DFA.unpack("\1\55\16\uffff\1\56"),
        DFA.unpack("\1\57"),
        DFA.unpack("\1\60"),
        DFA.unpack(""),
        DFA.unpack("\1\61"),
        DFA.unpack("\1\62"),
        DFA.unpack("\1\63"),
        DFA.unpack("\1\64"),
        DFA.unpack(""),
        DFA.unpack("\1\65"),
        DFA.unpack("\1\66"),
        DFA.unpack("\1\67"),
        DFA.unpack("\1\70"),
        DFA.unpack("\55\51\15\71\7\51\32\71\4\51\1\71\1\51\32\71\1\51\1"
        "\71\uff83\51"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\73"),
        DFA.unpack("\1\74"),
        DFA.unpack("\1\75"),
        DFA.unpack("\1\76"),
        DFA.unpack("\1\77"),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101"),
        DFA.unpack("\1\102"),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\107"),
        DFA.unpack("\1\110"),
        DFA.unpack("\55\51\15\71\7\51\32\71\4\51\1\71\1\51\32\71\1\51\1"
        "\71\uff83\51"),
        DFA.unpack(""),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\121"),
        DFA.unpack("\1\122"),
        DFA.unpack("\1\123"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\1\131"),
        DFA.unpack(""),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack("\1\134"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\145"),
        DFA.unpack(""),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\155"),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\157"),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\1\165"),
        DFA.unpack("\1\166"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\174"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA10_40 = input.LA(1)

                s = -1
                if ((45 <= LA10_40 <= 57) or (65 <= LA10_40 <= 90) or (97 <= LA10_40 <= 122) or LA10_40 in {95, 124}):
                    s = 57

                elif ((0 <= LA10_40 <= 44) or (58 <= LA10_40 <= 64) or (125 <= LA10_40 <= 65535) or LA10_40 in {91, 92, 93, 94, 96, 123}):
                    s = 41

                else:
                    s = 22

                if s >= 0:
                    return s
            elif s == 1: 
                LA10_57 = input.LA(1)

                s = -1
                if ((0 <= LA10_57 <= 44) or (58 <= LA10_57 <= 64) or (125 <= LA10_57 <= 65535) or LA10_57 in {91, 92, 93, 94, 96, 123}):
                    s = 41

                elif ((45 <= LA10_57 <= 57) or (65 <= LA10_57 <= 90) or (97 <= LA10_57 <= 122) or LA10_57 in {95, 124}):
                    s = 57

                else:
                    s = 22

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 10, _s, input)
            self_.error(nvae)
            raise nvae

 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SparkLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
