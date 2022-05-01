# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-05-01 15:40:57

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
EPOCH_FORMAT=11
FILE_FORMAT=12
FROM_UNIXTIME=13
LP=14
NEWLINE=15
ORDER_BY=16
OUTPUT_PARTITIONS=17
OVERWRITE=18
PLUS=19
RENAME_COLUMN=20
RIGHT_ARROW=21
RP=22
SC=23
SORT=24
SOURCE=25
STORE_COLUMNS=26
STRING=27
TEXT=28
TYPE=29
UNRECOGNIZED_TOKEN=30
WS=31

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COMMA", 7: "COMMENT", 8: "CREATE_LITERAL", 
    9: "DEDUPLICATE", 10: "DESTINATION", 11: "EPOCH_FORMAT", 12: "FILE_FORMAT", 
    13: "FROM_UNIXTIME", 14: "LP", 15: "NEWLINE", 16: "ORDER_BY", 17: "OUTPUT_PARTITIONS", 
    18: "OVERWRITE", 19: "PLUS", 20: "RENAME_COLUMN", 21: "RIGHT_ARROW", 
    22: "RP", 23: "SC", 24: "SORT", 25: "SOURCE", 26: "STORE_COLUMNS", 27: "STRING", 
    28: "TEXT", 29: "TYPE", 30: "UNRECOGNIZED_TOKEN", 31: "WS"
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

        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )






    # $ANTLR start "EPOCH_FORMAT"
    def mEPOCH_FORMAT(self, ):
        try:
            _type = EPOCH_FORMAT
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:117:2: ( 's' | 'm' | 'u' | 'n' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:
            pass 
            if self.input.LA(1) in {109, 110, 115, 117}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EPOCH_FORMAT"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:120:9: ( '\\n' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:120:11: '\\n'
            pass 
            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:122:6: ( '+' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:122:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:124:7: ( ',' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:124:9: ','
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:7: ( 'ASC' | 'DESC' | 'asc' | 'desc' )
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
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:9: 'ASC'
                pass 
                self.match("ASC")



            elif alt1 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:17: 'DESC'
                pass 
                self.match("DESC")



            elif alt1 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:26: 'asc'
                pass 
                self.match("asc")



            elif alt1 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:126:34: 'desc'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:7: ( 'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'LONG' )
            alt2 = 5
            LA2 = self.input.LA(1)
            if LA2 in {73}:
                alt2 = 1
            elif LA2 in {70}:
                alt2 = 2
            elif LA2 in {68}:
                alt2 = 3
            elif LA2 in {83}:
                alt2 = 4
            elif LA2 in {76}:
                alt2 = 5
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae


            if alt2 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:9: 'INT'
                pass 
                self.match("INT")



            elif alt2 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:17: 'FLOAT'
                pass 
                self.match("FLOAT")



            elif alt2 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:27: 'DOUBLE'
                pass 
                self.match("DOUBLE")



            elif alt2 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:38: 'STRING'
                pass 
                self.match("STRING")



            elif alt2 == 5:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:128:49: 'LONG'
                pass 
                self.match("LONG")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPE"



    # $ANTLR start "OVERWRITE"
    def mOVERWRITE(self, ):
        try:
            _type = OVERWRITE
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:2: ( 'overwrite' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:4: 'overwrite'
            pass 
            self.match("overwrite")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OVERWRITE"



    # $ANTLR start "OUTPUT_PARTITIONS"
    def mOUTPUT_PARTITIONS(self, ):
        try:
            _type = OUTPUT_PARTITIONS
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:135:2: ( 'OutputPartitions' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:135:4: 'OutputPartitions'
            pass 
            self.match("OutputPartitions")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OUTPUT_PARTITIONS"



    # $ANTLR start "FROM_UNIXTIME"
    def mFROM_UNIXTIME(self, ):
        try:
            _type = FROM_UNIXTIME
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:2: ( 'FromUnixtime' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:139:4: 'FromUnixtime'
            pass 
            self.match("FromUnixtime")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FROM_UNIXTIME"



    # $ANTLR start "ORDER_BY"
    def mORDER_BY(self, ):
        try:
            _type = ORDER_BY
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:143:2: ( 'order by' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:143:4: 'order by'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:146:2: ( 'StoreColumns' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:146:4: 'StoreColumns'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:149:2: ( 'RenameColumn' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:149:4: 'RenameColumn'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:152:2: ( 'Cast' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:152:4: 'Cast'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:155:2: ( 'CreateLiteral' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:155:4: 'CreateLiteral'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:159:2: ( 'Deduplicate' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:159:4: 'Deduplicate'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:162:4: ( ':' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:162:6: ':'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:163:4: ( '(' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:163:6: '('
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:164:4: ( ')' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:164:6: ')'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:165:5: ( ';' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:165:7: ';'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:168:2: ( '->' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:168:4: '->'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:171:2: ( 'parquet' | 'csv' | 'json' | 'avro' )
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
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:171:4: 'parquet'
                pass 
                self.match("parquet")



            elif alt3 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:172:4: 'csv'
                pass 
                self.match("csv")



            elif alt3 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:173:4: 'json'
                pass 
                self.match("json")



            elif alt3 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:174:4: 'avro'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:178:8: ( 'Source' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:178:10: 'Source'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:181:2: ( 'Destination' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:181:4: 'Destination'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? ( '\\n' | EOF ) | '/*' ( options {greedy=false; } : . )* '*/' )
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 47) :
                LA8_1 = self.input.LA(2)

                if (LA8_1 == 47) :
                    alt8 = 1
                elif (LA8_1 == 42) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 8, 0, self.input)

                raise nvae


            if alt8 == 1:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? ( '\\n' | EOF )
                pass 
                self.match("//")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:14: (~ ( '\\n' | '\\r' ) )*
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


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:28: ( '\\r' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 13) :
                    alt5 = 1
                if alt5 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:28: '\\r'
                    pass 
                    self.match(13)




                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:34: ( '\\n' | EOF )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 10) :
                    alt6 = 1
                else:
                    alt6 = 2

                if alt6 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:35: '\\n'
                    pass 
                    self.match(10)


                elif alt6 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:184:40: EOF
                    pass 
                    self.match(EOF)





                #action start
                _channel=HIDDEN;
                #action end



            elif alt8 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:185:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:185:14: ( options {greedy=false; } : . )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 42) :
                        LA7_1 = self.input.LA(2)

                        if (LA7_1 == 47) :
                            alt7 = 2
                        elif ((0 <= LA7_1 <= 46) or (48 <= LA7_1 <= 65535) or LA7_1 in {}) :
                            alt7 = 1


                    elif ((0 <= LA7_0 <= 41) or (43 <= LA7_0 <= 65535) or LA7_0 in {}) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:185:42: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop7


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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:188:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:188:9: ( ' ' | '\\t' | '\\r' | '\\n' )
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:196:9: ( ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+ )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:196:11: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
            pass 
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:196:11: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((45 <= LA9_0 <= 57) or (65 <= LA9_0 <= 90) or (97 <= LA9_0 <= 122) or LA9_0 in {95, 124}) :
                    alt9 = 1


                if alt9 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:
                    pass 
                    if (45 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95, 124}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1




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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:199:9: ( '\"' ( options {greedy=false; } : . )* '\"' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:199:11: '\"' ( options {greedy=false; } : . )* '\"'
            pass 
            self.match(34)

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:199:15: ( options {greedy=false; } : . )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 34) :
                    alt10 = 2
                elif ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 65535) or LA10_0 in {}) :
                    alt10 = 1


                if alt10 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:199:43: .
                    pass 
                    self.matchAny()


                else:
                    break #loop10


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "UNRECOGNIZED_TOKEN"
    def mUNRECOGNIZED_TOKEN(self, ):
        try:
            _type = UNRECOGNIZED_TOKEN
            _channel = DEFAULT_CHANNEL

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:201:20: ( . )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:201:22: .
            pass 
            self.matchAny()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNRECOGNIZED_TOKEN"



    def mTokens(self):
        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:8: ( EPOCH_FORMAT | NEWLINE | PLUS | COMMA | SORT | TYPE | OVERWRITE | OUTPUT_PARTITIONS | FROM_UNIXTIME | ORDER_BY | STORE_COLUMNS | RENAME_COLUMN | CAST_COLUMN | CREATE_LITERAL | DEDUPLICATE | CL | LP | RP | SC | RIGHT_ARROW | FILE_FORMAT | SOURCE | DESTINATION | COMMENT | WS | TEXT | STRING | UNRECOGNIZED_TOKEN )
        alt11 = 28
        alt11 = self.dfa11.predict(self.input)
        if alt11 == 1:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:10: EPOCH_FORMAT
            pass 
            self.mEPOCH_FORMAT()



        elif alt11 == 2:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:23: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt11 == 3:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:31: PLUS
            pass 
            self.mPLUS()



        elif alt11 == 4:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:36: COMMA
            pass 
            self.mCOMMA()



        elif alt11 == 5:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:42: SORT
            pass 
            self.mSORT()



        elif alt11 == 6:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:47: TYPE
            pass 
            self.mTYPE()



        elif alt11 == 7:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:52: OVERWRITE
            pass 
            self.mOVERWRITE()



        elif alt11 == 8:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:62: OUTPUT_PARTITIONS
            pass 
            self.mOUTPUT_PARTITIONS()



        elif alt11 == 9:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:80: FROM_UNIXTIME
            pass 
            self.mFROM_UNIXTIME()



        elif alt11 == 10:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:94: ORDER_BY
            pass 
            self.mORDER_BY()



        elif alt11 == 11:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:103: STORE_COLUMNS
            pass 
            self.mSTORE_COLUMNS()



        elif alt11 == 12:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:117: RENAME_COLUMN
            pass 
            self.mRENAME_COLUMN()



        elif alt11 == 13:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:131: CAST_COLUMN
            pass 
            self.mCAST_COLUMN()



        elif alt11 == 14:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:143: CREATE_LITERAL
            pass 
            self.mCREATE_LITERAL()



        elif alt11 == 15:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:158: DEDUPLICATE
            pass 
            self.mDEDUPLICATE()



        elif alt11 == 16:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:170: CL
            pass 
            self.mCL()



        elif alt11 == 17:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:173: LP
            pass 
            self.mLP()



        elif alt11 == 18:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:176: RP
            pass 
            self.mRP()



        elif alt11 == 19:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:179: SC
            pass 
            self.mSC()



        elif alt11 == 20:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:182: RIGHT_ARROW
            pass 
            self.mRIGHT_ARROW()



        elif alt11 == 21:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:194: FILE_FORMAT
            pass 
            self.mFILE_FORMAT()



        elif alt11 == 22:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:206: SOURCE
            pass 
            self.mSOURCE()



        elif alt11 == 23:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:213: DESTINATION
            pass 
            self.mDESTINATION()



        elif alt11 == 24:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:225: COMMENT
            pass 
            self.mCOMMENT()



        elif alt11 == 25:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:233: WS
            pass 
            self.mWS()



        elif alt11 == 26:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:236: TEXT
            pass 
            self.mTEXT()



        elif alt11 == 27:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:241: STRING
            pass 
            self.mSTRING()



        elif alt11 == 28:
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:248: UNRECOGNIZED_TOKEN
            pass 
            self.mUNRECOGNIZED_TOKEN()








    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        "\1\uffff\1\36\3\uffff\14\37\4\uffff\5\37\2\uffff\1\35\6\uffff\24"
        "\37\5\uffff\3\37\1\100\3\uffff\1\134\4\37\1\134\2\37\1\143\15\37"
        "\1\161\1\37\1\100\1\uffff\1\134\3\37\1\161\1\134\1\uffff\5\37\1"
        "\143\4\37\1\177\2\37\1\uffff\1\161\3\37\1\143\10\37\1\uffff\2\37"
        "\1\143\3\37\1\143\1\37\1\u0093\1\37\1\uffff\10\37\1\uffff\4\37\1"
        "\161\14\37\1\u00ad\7\37\1\uffff\3\37\1\u00b8\1\u00b9\5\37\2\uffff"
        "\1\u00bf\1\u00c0\1\37\1\u00c2\1\37\2\uffff\1\37\1\uffff\1\u00c5"
        "\1\37\1\uffff\1\37\1\u00c8\1\uffff"
        )

    DFA11_eof = DFA.unpack(
        "\u00c9\uffff"
        )

    DFA11_min = DFA.unpack(
        "\1\0\1\55\3\uffff\1\123\1\105\1\163\1\145\1\116\1\114\1\124\1\117"
        "\1\162\1\165\1\145\1\141\4\uffff\1\76\1\141\2\163\1\52\2\uffff\1"
        "\0\6\uffff\1\103\1\123\1\125\1\144\1\143\1\162\1\163\1\124\1\117"
        "\1\157\1\122\1\157\1\165\1\116\1\145\1\144\1\164\1\156\1\163\1\145"
        "\5\uffff\1\162\1\166\1\157\1\55\3\uffff\1\55\1\103\1\102\1\165\1"
        "\164\1\55\1\157\1\143\1\55\1\101\1\155\1\111\2\162\1\107\1\162\1"
        "\145\1\160\1\141\1\164\1\141\1\161\1\55\1\156\1\55\1\uffff\1\55"
        "\1\114\1\160\1\151\2\55\1\uffff\1\124\1\125\1\116\1\145\1\143\1"
        "\55\1\167\1\162\1\165\1\155\1\55\1\164\1\165\1\uffff\1\55\1\105"
        "\1\154\1\156\1\55\1\156\1\107\1\103\1\145\1\162\1\40\1\164\1\145"
        "\1\uffff\2\145\1\55\1\151\1\141\1\151\1\55\1\157\1\55\1\151\1\uffff"
        "\1\120\1\103\1\114\1\164\1\143\1\164\1\170\1\154\1\uffff\1\164\1"
        "\141\1\157\1\151\1\55\1\141\1\151\1\164\1\165\1\145\1\162\1\154"
        "\2\164\1\157\1\151\1\155\1\55\1\164\1\165\2\145\1\156\1\155\1\156"
        "\1\uffff\1\151\1\155\1\162\2\55\1\145\1\163\1\164\1\156\1\141\2"
        "\uffff\2\55\1\151\1\55\1\154\2\uffff\1\157\1\uffff\1\55\1\156\1"
        "\uffff\1\163\1\55\1\uffff"
        )

    DFA11_max = DFA.unpack(
        "\1\uffff\1\174\3\uffff\1\123\1\145\1\166\1\145\1\116\1\162\1\164"
        "\1\117\1\166\1\165\1\145\1\162\4\uffff\1\76\1\141\2\163\1\57\2\uffff"
        "\1\uffff\6\uffff\1\103\1\123\1\125\1\163\1\143\1\162\1\163\1\124"
        "\1\117\1\157\1\122\1\157\1\165\1\116\1\145\1\144\1\164\1\156\1\163"
        "\1\145\5\uffff\1\162\1\166\1\157\1\174\3\uffff\1\174\1\103\1\102"
        "\1\165\1\164\1\174\1\157\1\143\1\174\1\101\1\155\1\111\2\162\1\107"
        "\1\162\1\145\1\160\1\141\1\164\1\141\1\161\1\174\1\156\1\174\1\uffff"
        "\1\174\1\114\1\160\1\151\2\174\1\uffff\1\124\1\125\1\116\1\145\1"
        "\143\1\174\1\167\1\162\1\165\1\155\1\174\1\164\1\165\1\uffff\1\174"
        "\1\105\1\154\1\156\1\174\1\156\1\107\1\103\1\145\1\162\1\40\1\164"
        "\1\145\1\uffff\2\145\1\174\1\151\1\141\1\151\1\174\1\157\1\174\1"
        "\151\1\uffff\1\120\1\103\1\114\1\164\1\143\1\164\1\170\1\154\1\uffff"
        "\1\164\1\141\1\157\1\151\1\174\1\141\1\151\1\164\1\165\1\145\1\162"
        "\1\154\2\164\1\157\1\151\1\155\1\174\1\164\1\165\2\145\1\156\1\155"
        "\1\156\1\uffff\1\151\1\155\1\162\2\174\1\145\1\163\1\164\1\156\1"
        "\141\2\uffff\2\174\1\151\1\174\1\154\2\uffff\1\157\1\uffff\1\174"
        "\1\156\1\uffff\1\163\1\174\1\uffff"
        )

    DFA11_accept = DFA.unpack(
        "\2\uffff\1\2\1\3\1\4\14\uffff\1\20\1\21\1\22\1\23\5\uffff\1\31\1"
        "\32\1\uffff\1\34\1\1\1\32\1\2\1\3\1\4\24\uffff\1\20\1\21\1\22\1"
        "\23\1\24\4\uffff\1\30\1\31\1\33\31\uffff\1\5\6\uffff\1\6\15\uffff"
        "\1\25\15\uffff\1\15\12\uffff\1\12\10\uffff\1\26\31\uffff\1\7\12"
        "\uffff\1\17\1\27\5\uffff\1\11\1\13\1\uffff\1\14\2\uffff\1\16\2\uffff"
        "\1\10"
        )

    DFA11_special = DFA.unpack(
        "\1\0\33\uffff\1\1\u00ac\uffff"
        )


    DFA11_transition = [
        DFA.unpack("\11\35\1\32\1\2\2\35\1\32\22\35\1\32\1\35\1\34\5\35\1"
        "\22\1\23\1\35\1\3\1\4\1\25\1\33\1\31\12\33\1\21\1\24\5\35\1\5\1"
        "\33\1\20\1\6\1\33\1\12\2\33\1\11\2\33\1\14\2\33\1\16\2\33\1\17\1"
        "\13\7\33\4\35\1\33\1\35\1\7\1\33\1\27\1\10\5\33\1\30\2\33\2\1\1"
        "\15\1\26\2\33\1\1\1\33\1\1\5\33\1\35\1\33\uff83\35"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\43"),
        DFA.unpack("\1\44\11\uffff\1\45\25\uffff\1\46"),
        DFA.unpack("\1\47\2\uffff\1\50"),
        DFA.unpack("\1\51"),
        DFA.unpack("\1\52"),
        DFA.unpack("\1\53\45\uffff\1\54"),
        DFA.unpack("\1\55\32\uffff\1\57\4\uffff\1\56"),
        DFA.unpack("\1\60"),
        DFA.unpack("\1\62\3\uffff\1\61"),
        DFA.unpack("\1\63"),
        DFA.unpack("\1\64"),
        DFA.unpack("\1\65\20\uffff\1\66"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\73"),
        DFA.unpack("\1\74"),
        DFA.unpack("\1\75"),
        DFA.unpack("\1\76"),
        DFA.unpack("\1\100\4\uffff\1\77"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\0\102"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\106\16\uffff\1\107"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\121"),
        DFA.unpack("\1\122"),
        DFA.unpack("\1\123"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\130"),
        DFA.unpack("\1\131"),
        DFA.unpack("\1\132"),
        DFA.unpack("\15\133\7\uffff\32\133\4\uffff\1\133\1\uffff\32\133"
        "\1\uffff\1\133"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\144"),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\155"),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\157"),
        DFA.unpack("\1\160"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\162"),
        DFA.unpack("\15\133\7\uffff\32\133\4\uffff\1\133\1\uffff\32\133"
        "\1\uffff\1\133"),
        DFA.unpack(""),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\1\165"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack(""),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081"),
        DFA.unpack(""),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\1\u008b"),
        DFA.unpack("\1\u008c"),
        DFA.unpack(""),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090"),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u0094"),
        DFA.unpack(""),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\1\u009a"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack(""),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f"),
        DFA.unpack("\1\u00a0"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\u00a7"),
        DFA.unpack("\1\u00a8"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u00ae"),
        DFA.unpack("\1\u00af"),
        DFA.unpack("\1\u00b0"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\1\u00b7"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u00c3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00c4"),
        DFA.unpack(""),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("\1\u00c6"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c7"),
        DFA.unpack("\15\37\7\uffff\32\37\4\uffff\1\37\1\uffff\32\37\1\uffff"
        "\1\37"),
        DFA.unpack("")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA11_0 = input.LA(1)

                s = -1
                if (LA11_0 in {109, 110, 115, 117}):
                    s = 1

                elif (LA11_0 == 10):
                    s = 2

                elif (LA11_0 == 43):
                    s = 3

                elif (LA11_0 == 44):
                    s = 4

                elif (LA11_0 == 65):
                    s = 5

                elif (LA11_0 == 68):
                    s = 6

                elif (LA11_0 == 97):
                    s = 7

                elif (LA11_0 == 100):
                    s = 8

                elif (LA11_0 == 73):
                    s = 9

                elif (LA11_0 == 70):
                    s = 10

                elif (LA11_0 == 83):
                    s = 11

                elif (LA11_0 == 76):
                    s = 12

                elif (LA11_0 == 111):
                    s = 13

                elif (LA11_0 == 79):
                    s = 14

                elif (LA11_0 == 82):
                    s = 15

                elif (LA11_0 == 67):
                    s = 16

                elif (LA11_0 == 58):
                    s = 17

                elif (LA11_0 == 40):
                    s = 18

                elif (LA11_0 == 41):
                    s = 19

                elif (LA11_0 == 59):
                    s = 20

                elif (LA11_0 == 45):
                    s = 21

                elif (LA11_0 == 112):
                    s = 22

                elif (LA11_0 == 99):
                    s = 23

                elif (LA11_0 == 106):
                    s = 24

                elif (LA11_0 == 47):
                    s = 25

                elif (LA11_0 in {9, 13, 32}):
                    s = 26

                elif ((48 <= LA11_0 <= 57) or (84 <= LA11_0 <= 90) or (101 <= LA11_0 <= 105) or (118 <= LA11_0 <= 122) or LA11_0 in {46, 66, 69, 71, 72, 74, 75, 77, 78, 80, 81, 95, 98, 107, 108, 113, 114, 116, 124}):
                    s = 27

                elif (LA11_0 == 34):
                    s = 28

                elif ((0 <= LA11_0 <= 8) or (14 <= LA11_0 <= 31) or (35 <= LA11_0 <= 39) or (60 <= LA11_0 <= 64) or (125 <= LA11_0 <= 65535) or LA11_0 in {11, 12, 33, 42, 91, 92, 93, 94, 96, 123}):
                    s = 29

                if s >= 0:
                    return s
            elif s == 1: 
                LA11_28 = input.LA(1)

                s = -1
                if ((0 <= LA11_28 <= 65535) or LA11_28 in {}):
                    s = 66

                else:
                    s = 29

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 11, _s, input)
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
