# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-22 17:22:20

import sys
from antlr3 import *



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
LP=12
ORDER_BY=13
RENAME_COLUMN=14
RIGHT_ARROW=15
RP=16
SC=17
SORT=18
SOURCE=19
STORE_COLUMNS=20
STRING=21
TEXT=22
TYPE=23
WS=24

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COMMA", 7: "COMMENT", 8: "CREATE_LITERAL", 
    9: "DEDUPLICATE", 10: "DESTINATION", 11: "FILE_FORMAT", 12: "LP", 13: "ORDER_BY", 
    14: "RENAME_COLUMN", 15: "RIGHT_ARROW", 16: "RP", 17: "SC", 18: "SORT", 
    19: "SOURCE", 20: "STORE_COLUMNS", 21: "STRING", 22: "TEXT", 23: "TYPE", 
    24: "WS"
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:91:7: ( ',' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:91:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SORT"
    def mSORT(self, ):
        try:
            _type = SORT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:7: ( 'ASC' | 'DESC' | 'asc' | 'desc' )
            alt1 = 4
            LA1 = self.input.LA(1)
            if LA1 in {65}:
                alt1 = 1
            elif LA1 in {68}:
                alt1 = 2
            elif LA1 in {97}:
                alt1 = 3
            elif LA1 in {100}:
                alt1 = 4
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae


            if alt1 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:9: 'ASC'
                pass 
                self.match("ASC")



            elif alt1 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:17: 'DESC'
                pass 
                self.match("DESC")



            elif alt1 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:26: 'asc'
                pass 
                self.match("asc")



            elif alt1 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:34: 'desc'
                pass 
                self.match("desc")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SORT"



    # $ANTLR start "TYPE"
    def mTYPE(self, ):
        try:
            _type = TYPE
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:7: ( 'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' )
            alt2 = 4
            LA2 = self.input.LA(1)
            if LA2 in {73}:
                alt2 = 1
            elif LA2 in {70}:
                alt2 = 2
            elif LA2 in {68}:
                alt2 = 3
            elif LA2 in {83}:
                alt2 = 4
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae


            if alt2 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:9: 'INT'
                pass 
                self.match("INT")



            elif alt2 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:17: 'FLOAT'
                pass 
                self.match("FLOAT")



            elif alt2 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:27: 'DOUBLE'
                pass 
                self.match("DOUBLE")



            elif alt2 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:38: 'STRING'
                pass 
                self.match("STRING")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "ORDER_BY"
    def mORDER_BY(self, ):
        try:
            _type = ORDER_BY
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:98:2: ( 'order by' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:98:4: 'order by'
            pass 
            self.match("order by")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ORDER_BY"



    # $ANTLR start "STORE_COLUMNS"
    def mSTORE_COLUMNS(self, ):
        try:
            _type = STORE_COLUMNS
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:101:2: ( 'StoreColumns' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:101:4: 'StoreColumns'
            pass 
            self.match("StoreColumns")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STORE_COLUMNS"



    # $ANTLR start "RENAME_COLUMN"
    def mRENAME_COLUMN(self, ):
        try:
            _type = RENAME_COLUMN
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:104:2: ( 'RenameColumn' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:104:4: 'RenameColumn'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:107:2: ( 'Cast' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:107:4: 'Cast'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:110:2: ( 'CreateLiteral' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:110:4: 'CreateLiteral'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:114:2: ( 'Deduplicate' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:114:4: 'Deduplicate'
            pass 
            self.match("Deduplicate")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEDUPLICATE"



    # $ANTLR start "CL"
    def mCL(self, ):
        try:
            _type = CL
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:117:4: ( ':' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:117:6: ':'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:118:4: ( '(' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:118:6: '('
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:119:4: ( ')' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:119:6: ')'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:120:5: ( ';' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:120:7: ';'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:123:2: ( '->' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:123:4: '->'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:2: ( 'parquet' | 'csv' | 'json' | 'avro' )
            alt3 = 4
            LA3 = self.input.LA(1)
            if LA3 in {112}:
                alt3 = 1
            elif LA3 in {99}:
                alt3 = 2
            elif LA3 in {106}:
                alt3 = 3
            elif LA3 in {97}:
                alt3 = 4
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae


            if alt3 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:4: 'parquet'
                pass 
                self.match("parquet")



            elif alt3 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:127:4: 'csv'
                pass 
                self.match("csv")



            elif alt3 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:4: 'json'
                pass 
                self.match("json")



            elif alt3 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:129:4: 'avro'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:8: ( 'Source' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:10: 'Source'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:136:2: ( 'Destination' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:136:4: 'Destination'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 47) :
                LA7_1 = self.input.LA(2)

                if (LA7_1 == 47) :
                    alt7 = 1
                elif (LA7_1 == 42) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae


            if alt7 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((0 <= LA4_0 <= 9) or (14 <= LA4_0 <= 65535) or LA4_0 in {11, 12}) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop4


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:28: ( '\\r' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 13) :
                    alt5 = 1
                if alt5 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:28: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            elif alt7 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:140:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:140:14: ( options {greedy=false; } : . )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 42) :
                        LA6_1 = self.input.LA(2)

                        if (LA6_1 == 47) :
                            alt6 = 2
                        elif ((0 <= LA6_1 <= 46) or (48 <= LA6_1 <= 65535) or LA6_1 in {}) :
                            alt6 = 1


                    elif ((0 <= LA6_0 <= 41) or (43 <= LA6_0 <= 65535) or LA6_0 in {}) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:140:42: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop6


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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:143:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:143:9: ( ' ' | '\\t' | '\\r' | '\\n' )
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



    # $ANTLR start "TEXT"
    def mTEXT(self, ):
        try:
            _type = TEXT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:151:9: ( ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+ )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:151:11: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
            pass 
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:151:11: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:154:9: ( '\"' ( options {greedy=false; } : . )* '\"' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:154:11: '\"' ( options {greedy=false; } : . )* '\"'
            pass 
            self.match(34)

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:154:15: ( options {greedy=false; } : . )*
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 34) :
                    alt9 = 2
                elif ((0 <= LA9_0 <= 33) or (35 <= LA9_0 <= 65535) or LA9_0 in {}) :
                    alt9 = 1


                if alt9 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:154:43: .
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
        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:8: ( COMMA | SORT | TYPE | ORDER_BY | STORE_COLUMNS | RENAME_COLUMN | CAST_COLUMN | CREATE_LITERAL | DEDUPLICATE | CL | LP | RP | SC | RIGHT_ARROW | FILE_FORMAT | SOURCE | DESTINATION | COMMENT | WS | TEXT | STRING )
        alt10 = 21
        alt10 = self.dfa10.predict(self.input)
        if alt10 == 1:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:10: COMMA
            pass 
            self.mCOMMA()



        elif alt10 == 2:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:16: SORT
            pass 
            self.mSORT()



        elif alt10 == 3:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:21: TYPE
            pass 
            self.mTYPE()



        elif alt10 == 4:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:26: ORDER_BY
            pass 
            self.mORDER_BY()



        elif alt10 == 5:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:35: STORE_COLUMNS
            pass 
            self.mSTORE_COLUMNS()



        elif alt10 == 6:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:49: RENAME_COLUMN
            pass 
            self.mRENAME_COLUMN()



        elif alt10 == 7:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:63: CAST_COLUMN
            pass 
            self.mCAST_COLUMN()



        elif alt10 == 8:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:75: CREATE_LITERAL
            pass 
            self.mCREATE_LITERAL()



        elif alt10 == 9:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:90: DEDUPLICATE
            pass 
            self.mDEDUPLICATE()



        elif alt10 == 10:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:102: CL
            pass 
            self.mCL()



        elif alt10 == 11:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:105: LP
            pass 
            self.mLP()



        elif alt10 == 12:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:108: RP
            pass 
            self.mRP()



        elif alt10 == 13:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:111: SC
            pass 
            self.mSC()



        elif alt10 == 14:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:114: RIGHT_ARROW
            pass 
            self.mRIGHT_ARROW()



        elif alt10 == 15:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:126: FILE_FORMAT
            pass 
            self.mFILE_FORMAT()



        elif alt10 == 16:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:138: SOURCE
            pass 
            self.mSOURCE()



        elif alt10 == 17:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:145: DESTINATION
            pass 
            self.mDESTINATION()



        elif alt10 == 18:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:157: COMMENT
            pass 
            self.mCOMMENT()



        elif alt10 == 19:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:165: WS
            pass 
            self.mWS()



        elif alt10 == 20:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:168: TEXT
            pass 
            self.mTEXT()



        elif alt10 == 21:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:173: STRING
            pass 
            self.mSTRING()








    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        "\2\uffff\12\26\4\uffff\5\26\3\uffff\20\26\1\uffff\4\26\1\uffff\1"
        "\103\4\26\1\103\2\26\1\112\11\26\1\124\2\26\1\uffff\1\103\3\26\1"
        "\124\1\103\1\uffff\6\26\1\137\2\26\1\uffff\1\124\3\26\1\112\5\26"
        "\1\uffff\2\26\1\112\2\26\1\112\1\26\1\157\1\uffff\6\26\1\uffff\2"
        "\26\1\124\17\26\1\u0087\1\u0088\3\26\2\uffff\1\u008c\1\u008d\1\26"
        "\2\uffff\1\u008f\1\uffff"
        )

    DFA10_eof = DFA.unpack(
        "\u0090\uffff"
        )

    DFA10_min = DFA.unpack(
        "\1\11\1\uffff\1\123\1\105\1\163\1\145\1\116\1\114\1\124\1\162\1"
        "\145\1\141\4\uffff\1\76\1\141\2\163\1\52\3\uffff\1\103\1\123\1\125"
        "\1\144\1\143\1\162\1\163\1\124\1\117\1\122\1\157\1\165\1\144\1\156"
        "\1\163\1\145\1\uffff\1\162\1\166\1\157\1\0\1\uffff\1\55\1\103\1"
        "\102\1\165\1\164\1\55\1\157\1\143\1\55\1\101\1\111\2\162\1\145\1"
        "\141\1\164\1\141\1\161\1\55\1\156\1\0\1\uffff\1\55\1\114\1\160\1"
        "\151\2\55\1\uffff\1\124\1\116\1\145\1\143\1\162\1\155\1\55\1\164"
        "\1\165\1\uffff\1\55\1\105\1\154\1\156\1\55\1\107\1\103\1\145\1\40"
        "\1\145\1\uffff\2\145\1\55\1\151\1\141\1\55\1\157\1\55\1\uffff\1"
        "\103\1\114\1\164\1\143\1\164\1\154\1\uffff\1\157\1\151\1\55\1\141"
        "\1\151\1\165\1\154\2\164\1\157\1\155\1\165\2\145\2\156\1\155\1\162"
        "\2\55\1\163\1\156\1\141\2\uffff\2\55\1\154\2\uffff\1\55\1\uffff"
        )

    DFA10_max = DFA.unpack(
        "\1\174\1\uffff\1\123\1\145\1\166\1\145\1\116\1\114\1\164\1\162\1"
        "\145\1\162\4\uffff\1\76\1\141\2\163\1\57\3\uffff\1\103\1\123\1\125"
        "\1\163\1\143\1\162\1\163\1\124\1\117\1\122\1\157\1\165\1\144\1\156"
        "\1\163\1\145\1\uffff\1\162\1\166\1\157\1\uffff\1\uffff\1\174\1\103"
        "\1\102\1\165\1\164\1\174\1\157\1\143\1\174\1\101\1\111\2\162\1\145"
        "\1\141\1\164\1\141\1\161\1\174\1\156\1\uffff\1\uffff\1\174\1\114"
        "\1\160\1\151\2\174\1\uffff\1\124\1\116\1\145\1\143\1\162\1\155\1"
        "\174\1\164\1\165\1\uffff\1\174\1\105\1\154\1\156\1\174\1\107\1\103"
        "\1\145\1\40\1\145\1\uffff\2\145\1\174\1\151\1\141\1\174\1\157\1"
        "\174\1\uffff\1\103\1\114\1\164\1\143\1\164\1\154\1\uffff\1\157\1"
        "\151\1\174\1\141\1\151\1\165\1\154\2\164\1\157\1\155\1\165\2\145"
        "\2\156\1\155\1\162\2\174\1\163\1\156\1\141\2\uffff\2\174\1\154\2"
        "\uffff\1\174\1\uffff"
        )

    DFA10_accept = DFA.unpack(
        "\1\uffff\1\1\12\uffff\1\12\1\13\1\14\1\15\5\uffff\1\23\1\24\1\25"
        "\20\uffff\1\16\4\uffff\1\22\25\uffff\1\2\6\uffff\1\3\11\uffff\1"
        "\17\12\uffff\1\7\10\uffff\1\4\6\uffff\1\20\27\uffff\1\11\1\21\3"
        "\uffff\1\5\1\6\1\uffff\1\10"
        )

    DFA10_special = DFA.unpack(
        "\54\uffff\1\1\25\uffff\1\0\115\uffff"
        )


    DFA10_transition = [
        DFA.unpack("\2\25\2\uffff\1\25\22\uffff\1\25\1\uffff\1\27\5\uffff"
        "\1\15\1\16\2\uffff\1\1\1\20\1\26\1\24\12\26\1\14\1\17\5\uffff\1"
        "\2\1\26\1\13\1\3\1\26\1\7\2\26\1\6\10\26\1\12\1\10\7\26\4\uffff"
        "\1\26\1\uffff\1\4\1\26\1\22\1\5\5\26\1\23\4\26\1\11\1\21\12\26\1"
        "\uffff\1\26"),
        DFA.unpack(""),
        DFA.unpack("\1\30"),
        DFA.unpack("\1\31\11\uffff\1\32\25\uffff\1\33"),
        DFA.unpack("\1\34\2\uffff\1\35"),
        DFA.unpack("\1\36"),
        DFA.unpack("\1\37"),
        DFA.unpack("\1\40"),
        DFA.unpack("\1\41\32\uffff\1\43\4\uffff\1\42"),
        DFA.unpack("\1\44"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46\20\uffff\1\47"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\50"),
        DFA.unpack("\1\51"),
        DFA.unpack("\1\52"),
        DFA.unpack("\1\53"),
        DFA.unpack("\1\55\4\uffff\1\54"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\56"),
        DFA.unpack("\1\57"),
        DFA.unpack("\1\60"),
        DFA.unpack("\1\61\16\uffff\1\62"),
        DFA.unpack("\1\63"),
        DFA.unpack("\1\64"),
        DFA.unpack("\1\65"),
        DFA.unpack("\1\66"),
        DFA.unpack("\1\67"),
        DFA.unpack("\1\70"),
        DFA.unpack("\1\71"),
        DFA.unpack("\1\72"),
        DFA.unpack("\1\73"),
        DFA.unpack("\1\74"),
        DFA.unpack("\1\75"),
        DFA.unpack("\1\76"),
        DFA.unpack(""),
        DFA.unpack("\1\77"),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101"),
        DFA.unpack("\55\55\15\102\7\55\32\102\4\55\1\102\1\55\32\102\1\55"
        "\1\102\uff83\55"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\106"),
        DFA.unpack("\1\107"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\121"),
        DFA.unpack("\1\122"),
        DFA.unpack("\1\123"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\125"),
        DFA.unpack("\55\55\15\102\7\55\32\102\4\55\1\102\1\55\32\102\1\55"
        "\1\102\uff83\55"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack(""),
        DFA.unpack("\1\131"),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack(""),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\155"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\156"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack(""),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack("\1\162"),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\1\165"),
        DFA.unpack(""),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081"),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\1\u008b"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\15\26\7\uffff\32\26\4\uffff\1\26\1\uffff\32\26\1\uffff"
        "\1\26"),
        DFA.unpack("\1\u008e"),
        DFA.unpack(""),
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
                LA10_66 = input.LA(1)

                s = -1
                if ((0 <= LA10_66 <= 44) or (58 <= LA10_66 <= 64) or (125 <= LA10_66 <= 65535) or LA10_66 in {91, 92, 93, 94, 96, 123}):
                    s = 45

                elif ((45 <= LA10_66 <= 57) or (65 <= LA10_66 <= 90) or (97 <= LA10_66 <= 122) or LA10_66 in {95, 124}):
                    s = 66

                else:
                    s = 22

                if s >= 0:
                    return s
            elif s == 1: 
                LA10_44 = input.LA(1)

                s = -1
                if ((45 <= LA10_44 <= 57) or (65 <= LA10_44 <= 90) or (97 <= LA10_44 <= 122) or LA10_44 in {95, 124}):
                    s = 66

                elif ((0 <= LA10_44 <= 44) or (58 <= LA10_44 <= 64) or (125 <= LA10_44 <= 65535) or LA10_44 in {91, 92, 93, 94, 96, 123}):
                    s = 45

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
