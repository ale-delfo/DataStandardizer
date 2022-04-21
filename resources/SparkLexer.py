# $ANTLR 3.5.1 /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-21 15:49:47

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

class SparkLexer(Lexer):

    grammarFileName = "/Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )






    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:70:7: ( ',' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:70:9: ','
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:72:7: ( 'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' )
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
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:72:9: 'INT'
                pass 
                self.match("INT")



            elif alt1 == 2:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:72:17: 'FLOAT'
                pass 
                self.match("FLOAT")



            elif alt1 == 3:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:72:27: 'DOUBLE'
                pass 
                self.match("DOUBLE")



            elif alt1 == 4:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:72:38: 'STRING'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:75:2: ( 's' | 'm' | 'n' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:78:2: ( 'RenameColumn' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:78:4: 'RenameColumn'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:81:2: ( 'Cast' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:81:4: 'Cast'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:84:2: ( 'CreateLiteral' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:84:4: 'CreateLiteral'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:88:2: ( 'Deduplicate' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:88:4: 'Deduplicate'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:91:4: ( ':' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:91:6: ':'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:92:4: ( '(' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:92:6: '('
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:93:4: ( ')' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:93:6: ')'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:94:5: ( ';' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:94:7: ';'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:97:2: ( '->' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:97:4: '->'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:100:2: ( 'parquet' | 'csv' | 'json' | 'avro' )
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
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:100:4: 'parquet'
                pass 
                self.match("parquet")



            elif alt2 == 2:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:101:4: 'csv'
                pass 
                self.match("csv")



            elif alt2 == 3:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:102:4: 'json'
                pass 
                self.match("json")



            elif alt2 == 4:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:103:4: 'avro'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:107:8: ( 'Source' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:107:10: 'Source'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:110:2: ( 'Destination' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:110:4: 'Destination'
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:113:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
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
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:113:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")


                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:113:14: (~ ( '\\n' | '\\r' ) )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((0 <= LA3_0 <= 9) or (14 <= LA3_0 <= 65535) or LA3_0 in {11, 12}) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop3


                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:113:28: ( '\\r' )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 13) :
                    alt4 = 1
                if alt4 == 1:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:113:28: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            elif alt6 == 2:
                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:114:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:114:14: ( options {greedy=false; } : . )*
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
                        # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:114:42: .
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

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:117:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:117:9: ( ' ' | '\\t' | '\\r' | '\\n' )
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



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:124:9: ( '\"' ( options {greedy=false; } : . )* '\"' )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:124:11: '\"' ( options {greedy=false; } : . )* '\"'
            pass 
            self.match(34)

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:124:15: ( options {greedy=false; } : . )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 34) :
                    alt7 = 2
                elif ((0 <= LA7_0 <= 33) or (35 <= LA7_0 <= 65535) or LA7_0 in {}) :
                    alt7 = 1


                if alt7 == 1:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:124:43: .
                    pass 
                    self.matchAny()


                else:
                    break #loop7


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:126:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:126:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:126:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((48 <= LA8_0 <= 57) or (65 <= LA8_0 <= 90) or (97 <= LA8_0 <= 122) or LA8_0 in {95}) :
                    alt8 = 1


                if alt8 == 1:
                    # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop8




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    def mTokens(self):
        # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:8: ( COMMA | TYPE | UNIX_TIME_UNIT | RENAME_COLUMN | CAST_COLUMN | CREATE_LITERAL | DEDUPLICATE | CL | LP | RP | SC | RIGHT_ARROW | FILE_FORMAT | SOURCE | DESTINATION | COMMENT | WS | STRING | ID )
        alt9 = 19
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:10: COMMA
            pass 
            self.mCOMMA()



        elif alt9 == 2:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:16: TYPE
            pass 
            self.mTYPE()



        elif alt9 == 3:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:21: UNIX_TIME_UNIT
            pass 
            self.mUNIX_TIME_UNIT()



        elif alt9 == 4:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:36: RENAME_COLUMN
            pass 
            self.mRENAME_COLUMN()



        elif alt9 == 5:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:50: CAST_COLUMN
            pass 
            self.mCAST_COLUMN()



        elif alt9 == 6:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:62: CREATE_LITERAL
            pass 
            self.mCREATE_LITERAL()



        elif alt9 == 7:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:77: DEDUPLICATE
            pass 
            self.mDEDUPLICATE()



        elif alt9 == 8:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:89: CL
            pass 
            self.mCL()



        elif alt9 == 9:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:92: LP
            pass 
            self.mLP()



        elif alt9 == 10:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:95: RP
            pass 
            self.mRP()



        elif alt9 == 11:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:98: SC
            pass 
            self.mSC()



        elif alt9 == 12:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:101: RIGHT_ARROW
            pass 
            self.mRIGHT_ARROW()



        elif alt9 == 13:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:113: FILE_FORMAT
            pass 
            self.mFILE_FORMAT()



        elif alt9 == 14:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:125: SOURCE
            pass 
            self.mSOURCE()



        elif alt9 == 15:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:132: DESTINATION
            pass 
            self.mDESTINATION()



        elif alt9 == 16:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:144: COMMENT
            pass 
            self.mCOMMENT()



        elif alt9 == 17:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:152: WS
            pass 
            self.mWS()



        elif alt9 == 18:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:155: STRING
            pass 
            self.mSTRING()



        elif alt9 == 19:
            # /Users/alessandro/Università/LFC-progetto/DataStandardizer/resources/Spark.g:1:162: ID
            pass 
            self.mID()








    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        "\2\uffff\4\25\1\34\2\25\5\uffff\4\25\4\uffff\6\25\1\uffff\7\25\1"
        "\62\12\25\1\75\2\25\1\uffff\7\25\1\107\2\25\1\uffff\2\75\1\62\6"
        "\25\1\uffff\2\25\1\62\2\25\1\62\1\124\5\25\1\uffff\2\25\1\75\14"
        "\25\1\150\1\151\2\25\2\uffff\1\154\1\25\1\uffff\1\156\1\uffff"
        )

    DFA9_eof = DFA.unpack(
        "\157\uffff"
        )

    DFA9_min = DFA.unpack(
        "\1\11\1\uffff\1\116\1\114\1\117\1\124\1\60\1\145\1\141\5\uffff\1"
        "\141\2\163\1\166\4\uffff\1\124\1\117\1\125\1\144\1\122\1\165\1\uffff"
        "\1\156\1\163\1\145\1\162\1\166\1\157\1\162\1\60\1\101\1\102\1\165"
        "\1\164\1\111\1\162\1\141\1\164\1\141\1\161\1\60\1\156\1\157\1\uffff"
        "\1\124\1\114\1\160\1\151\1\116\1\143\1\155\1\60\1\164\1\165\1\uffff"
        "\3\60\1\105\1\154\1\156\1\107\2\145\1\uffff\2\145\1\60\1\151\1\141"
        "\2\60\1\103\1\114\1\164\1\143\1\164\1\uffff\1\157\1\151\1\60\1\141"
        "\1\151\1\154\2\164\1\157\1\165\2\145\1\156\1\155\1\162\2\60\1\156"
        "\1\141\2\uffff\1\60\1\154\1\uffff\1\60\1\uffff"
        )

    DFA9_max = DFA.unpack(
        "\1\172\1\uffff\1\116\1\114\1\145\1\157\1\172\1\145\1\162\5\uffff"
        "\1\141\2\163\1\166\4\uffff\1\124\1\117\1\125\1\163\1\122\1\165\1"
        "\uffff\1\156\1\163\1\145\1\162\1\166\1\157\1\162\1\172\1\101\1\102"
        "\1\165\1\164\1\111\1\162\1\141\1\164\1\141\1\161\1\172\1\156\1\157"
        "\1\uffff\1\124\1\114\1\160\1\151\1\116\1\143\1\155\1\172\1\164\1"
        "\165\1\uffff\3\172\1\105\1\154\1\156\1\107\2\145\1\uffff\2\145\1"
        "\172\1\151\1\141\2\172\1\103\1\114\1\164\1\143\1\164\1\uffff\1\157"
        "\1\151\1\172\1\141\1\151\1\154\2\164\1\157\1\165\2\145\1\156\1\155"
        "\1\162\2\172\1\156\1\141\2\uffff\1\172\1\154\1\uffff\1\172\1\uffff"
        )

    DFA9_accept = DFA.unpack(
        "\1\uffff\1\1\7\uffff\1\10\1\11\1\12\1\13\1\14\4\uffff\1\20\1\21"
        "\1\22\1\23\6\uffff\1\3\25\uffff\1\2\12\uffff\1\15\11\uffff\1\5\14"
        "\uffff\1\16\23\uffff\1\7\1\17\2\uffff\1\4\1\uffff\1\6"
        )

    DFA9_special = DFA.unpack(
        "\157\uffff"
        )


    DFA9_transition = [
        DFA.unpack("\2\23\2\uffff\1\23\22\uffff\1\23\1\uffff\1\24\5\uffff"
        "\1\12\1\13\2\uffff\1\1\1\15\1\uffff\1\22\12\uffff\1\11\1\14\5\uffff"
        "\2\25\1\10\1\4\1\25\1\3\2\25\1\2\10\25\1\7\1\5\7\25\4\uffff\1\25"
        "\1\uffff\1\21\1\25\1\17\6\25\1\20\2\25\2\6\1\25\1\16\2\25\1\6\7"
        "\25"),
        DFA.unpack(""),
        DFA.unpack("\1\26"),
        DFA.unpack("\1\27"),
        DFA.unpack("\1\30\25\uffff\1\31"),
        DFA.unpack("\1\32\32\uffff\1\33"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\35"),
        DFA.unpack("\1\36\20\uffff\1\37"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\40"),
        DFA.unpack("\1\41"),
        DFA.unpack("\1\42"),
        DFA.unpack("\1\43"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\44"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46"),
        DFA.unpack("\1\47\16\uffff\1\50"),
        DFA.unpack("\1\51"),
        DFA.unpack("\1\52"),
        DFA.unpack(""),
        DFA.unpack("\1\53"),
        DFA.unpack("\1\54"),
        DFA.unpack("\1\55"),
        DFA.unpack("\1\56"),
        DFA.unpack("\1\57"),
        DFA.unpack("\1\60"),
        DFA.unpack("\1\61"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
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
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\76"),
        DFA.unpack("\1\77"),
        DFA.unpack(""),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101"),
        DFA.unpack("\1\102"),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\106"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack(""),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack(""),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\121"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\122"),
        DFA.unpack("\1\123"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\1\131"),
        DFA.unpack(""),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("\1\155"),
        DFA.unpack(""),
        DFA.unpack("\12\25\7\uffff\32\25\4\uffff\1\25\1\uffff\32\25"),
        DFA.unpack("")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SparkLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
