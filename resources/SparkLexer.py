# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-25 22:41:59

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
WS=30

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COMMA", 7: "COMMENT", 8: "CREATE_LITERAL", 
    9: "DEDUPLICATE", 10: "DESTINATION", 11: "EPOCH_FORMAT", 12: "FILE_FORMAT", 
    13: "FROM_UNIXTIME", 14: "LP", 15: "NEWLINE", 16: "ORDER_BY", 17: "OUTPUT_PARTITIONS", 
    18: "OVERWRITE", 19: "PLUS", 20: "RENAME_COLUMN", 21: "RIGHT_ARROW", 
    22: "RP", 23: "SC", 24: "SORT", 25: "SOURCE", 26: "STORE_COLUMNS", 27: "STRING", 
    28: "TEXT", 29: "TYPE", 30: "WS"
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:122:2: ( 's' | 'm' | 'u' | 'n' )
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:125:9: ( '\\n' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:125:11: '\\n'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:127:6: ( '+' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:127:8: '+'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:129:7: ( ',' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:129:9: ','
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:7: ( 'ASC' | 'DESC' | 'asc' | 'desc' )
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
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:9: 'ASC'
                pass 
                self.match("ASC")



            elif alt1 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:17: 'DESC'
                pass 
                self.match("DESC")



            elif alt1 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:26: 'asc'
                pass 
                self.match("asc")



            elif alt1 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:131:34: 'desc'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:7: ( 'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'LONG' )
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
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:9: 'INT'
                pass 
                self.match("INT")



            elif alt2 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:17: 'FLOAT'
                pass 
                self.match("FLOAT")



            elif alt2 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:27: 'DOUBLE'
                pass 
                self.match("DOUBLE")



            elif alt2 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:38: 'STRING'
                pass 
                self.match("STRING")



            elif alt2 == 5:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:133:49: 'LONG'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:136:2: ( 'overwrite' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:136:4: 'overwrite'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:140:2: ( 'OutputPartitions' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:140:4: 'OutputPartitions'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:144:2: ( 'FromUnixtime' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:144:4: 'FromUnixtime'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:148:2: ( 'order by' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:148:4: 'order by'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:151:2: ( 'StoreColumns' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:151:4: 'StoreColumns'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:154:2: ( 'RenameColumn' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:154:4: 'RenameColumn'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:157:2: ( 'Cast' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:157:4: 'Cast'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:160:2: ( 'CreateLiteral' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:160:4: 'CreateLiteral'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:164:2: ( 'Deduplicate' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:164:4: 'Deduplicate'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:167:4: ( ':' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:167:6: ':'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:168:4: ( '(' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:168:6: '('
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:169:4: ( ')' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:169:6: ')'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:170:5: ( ';' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:170:7: ';'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:173:2: ( '->' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:173:4: '->'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:176:2: ( 'parquet' | 'csv' | 'json' | 'avro' )
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
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:176:4: 'parquet'
                pass 
                self.match("parquet")



            elif alt3 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:177:4: 'csv'
                pass 
                self.match("csv")



            elif alt3 == 3:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:178:4: 'json'
                pass 
                self.match("json")



            elif alt3 == 4:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:179:4: 'avro'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:183:8: ( 'Source' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:183:10: 'Source'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:186:2: ( 'Destination' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:186:4: 'Destination'
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? ( '\\n' | EOF ) | '/*' ( options {greedy=false; } : . )* '*/' )
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
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:9: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? ( '\\n' | EOF )
                pass 
                self.match("//")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:14: (~ ( '\\n' | '\\r' ) )*
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


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:28: ( '\\r' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 13) :
                    alt5 = 1
                if alt5 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:28: '\\r'
                    pass 
                    self.match(13)




                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:34: ( '\\n' | EOF )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 10) :
                    alt6 = 1
                else:
                    alt6 = 2

                if alt6 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:35: '\\n'
                    pass 
                    self.match(10)


                elif alt6 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:189:40: EOF
                    pass 
                    self.match(EOF)





                #action start
                _channel=HIDDEN;
                #action end



            elif alt8 == 2:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:190:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:190:14: ( options {greedy=false; } : . )*
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
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:190:42: .
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:193:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:193:9: ( ' ' | '\\t' | '\\r' | '\\n' )
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:201:9: ( ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+ )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:201:11: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
            pass 
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:201:11: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' | '-' | '_' | '/' | '|' | '.' )+
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

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:204:9: ( '\"' ( options {greedy=false; } : . )* '\"' )
            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:204:11: '\"' ( options {greedy=false; } : . )* '\"'
            pass 
            self.match(34)

            # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:204:15: ( options {greedy=false; } : . )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 34) :
                    alt10 = 2
                elif ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 65535) or LA10_0 in {}) :
                    alt10 = 1


                if alt10 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:204:43: .
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



    def mTokens(self):
        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:1:8: ( EPOCH_FORMAT | NEWLINE | PLUS | COMMA | SORT | TYPE | OVERWRITE | OUTPUT_PARTITIONS | FROM_UNIXTIME | ORDER_BY | STORE_COLUMNS | RENAME_COLUMN | CAST_COLUMN | CREATE_LITERAL | DEDUPLICATE | CL | LP | RP | SC | RIGHT_ARROW | FILE_FORMAT | SOURCE | DESTINATION | COMMENT | WS | TEXT | STRING )
        alt11 = 27
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








    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        "\1\uffff\1\35\3\uffff\14\33\4\uffff\5\33\5\uffff\24\33\1\uffff\3"
        "\33\1\70\1\uffff\1\122\4\33\1\122\2\33\1\131\15\33\1\147\1\33\1"
        "\70\1\uffff\1\122\3\33\1\147\1\122\1\uffff\5\33\1\131\4\33\1\165"
        "\2\33\1\uffff\1\147\3\33\1\131\10\33\1\uffff\2\33\1\131\3\33\1\131"
        "\1\33\1\u0089\1\33\1\uffff\10\33\1\uffff\4\33\1\147\14\33\1\u00a3"
        "\7\33\1\uffff\3\33\1\u00ae\1\u00af\5\33\2\uffff\1\u00b5\1\u00b6"
        "\1\33\1\u00b8\1\33\2\uffff\1\33\1\uffff\1\u00bb\1\33\1\uffff\1\33"
        "\1\u00be\1\uffff"
        )

    DFA11_eof = DFA.unpack(
        "\u00bf\uffff"
        )

    DFA11_min = DFA.unpack(
        "\1\11\1\55\3\uffff\1\123\1\105\1\163\1\145\1\116\1\114\1\124\1\117"
        "\1\162\1\165\1\145\1\141\4\uffff\1\76\1\141\2\163\1\52\5\uffff\1"
        "\103\1\123\1\125\1\144\1\143\1\162\1\163\1\124\1\117\1\157\1\122"
        "\1\157\1\165\1\116\1\145\1\144\1\164\1\156\1\163\1\145\1\uffff\1"
        "\162\1\166\1\157\1\55\1\uffff\1\55\1\103\1\102\1\165\1\164\1\55"
        "\1\157\1\143\1\55\1\101\1\155\1\111\2\162\1\107\1\162\1\145\1\160"
        "\1\141\1\164\1\141\1\161\1\55\1\156\1\55\1\uffff\1\55\1\114\1\160"
        "\1\151\2\55\1\uffff\1\124\1\125\1\116\1\145\1\143\1\55\1\167\1\162"
        "\1\165\1\155\1\55\1\164\1\165\1\uffff\1\55\1\105\1\154\1\156\1\55"
        "\1\156\1\107\1\103\1\145\1\162\1\40\1\164\1\145\1\uffff\2\145\1"
        "\55\1\151\1\141\1\151\1\55\1\157\1\55\1\151\1\uffff\1\120\1\103"
        "\1\114\1\164\1\143\1\164\1\170\1\154\1\uffff\1\164\1\141\1\157\1"
        "\151\1\55\1\141\1\151\1\164\1\165\1\145\1\162\1\154\2\164\1\157"
        "\1\151\1\155\1\55\1\164\1\165\2\145\1\156\1\155\1\156\1\uffff\1"
        "\151\1\155\1\162\2\55\1\145\1\163\1\164\1\156\1\141\2\uffff\2\55"
        "\1\151\1\55\1\154\2\uffff\1\157\1\uffff\1\55\1\156\1\uffff\1\163"
        "\1\55\1\uffff"
        )

    DFA11_max = DFA.unpack(
        "\2\174\3\uffff\1\123\1\145\1\166\1\145\1\116\1\162\1\164\1\117\1"
        "\166\1\165\1\145\1\162\4\uffff\1\76\1\141\2\163\1\57\5\uffff\1\103"
        "\1\123\1\125\1\163\1\143\1\162\1\163\1\124\1\117\1\157\1\122\1\157"
        "\1\165\1\116\1\145\1\144\1\164\1\156\1\163\1\145\1\uffff\1\162\1"
        "\166\1\157\1\174\1\uffff\1\174\1\103\1\102\1\165\1\164\1\174\1\157"
        "\1\143\1\174\1\101\1\155\1\111\2\162\1\107\1\162\1\145\1\160\1\141"
        "\1\164\1\141\1\161\1\174\1\156\1\174\1\uffff\1\174\1\114\1\160\1"
        "\151\2\174\1\uffff\1\124\1\125\1\116\1\145\1\143\1\174\1\167\1\162"
        "\1\165\1\155\1\174\1\164\1\165\1\uffff\1\174\1\105\1\154\1\156\1"
        "\174\1\156\1\107\1\103\1\145\1\162\1\40\1\164\1\145\1\uffff\2\145"
        "\1\174\1\151\1\141\1\151\1\174\1\157\1\174\1\151\1\uffff\1\120\1"
        "\103\1\114\1\164\1\143\1\164\1\170\1\154\1\uffff\1\164\1\141\1\157"
        "\1\151\1\174\1\141\1\151\1\164\1\165\1\145\1\162\1\154\2\164\1\157"
        "\1\151\1\155\1\174\1\164\1\165\2\145\1\156\1\155\1\156\1\uffff\1"
        "\151\1\155\1\162\2\174\1\145\1\163\1\164\1\156\1\141\2\uffff\2\174"
        "\1\151\1\174\1\154\2\uffff\1\157\1\uffff\1\174\1\156\1\uffff\1\163"
        "\1\174\1\uffff"
        )

    DFA11_accept = DFA.unpack(
        "\2\uffff\1\2\1\3\1\4\14\uffff\1\20\1\21\1\22\1\23\5\uffff\1\31\1"
        "\32\1\33\1\1\1\2\24\uffff\1\24\4\uffff\1\30\31\uffff\1\5\6\uffff"
        "\1\6\15\uffff\1\25\15\uffff\1\15\12\uffff\1\12\10\uffff\1\26\31"
        "\uffff\1\7\12\uffff\1\17\1\27\5\uffff\1\11\1\13\1\uffff\1\14\2\uffff"
        "\1\16\2\uffff\1\10"
        )

    DFA11_special = DFA.unpack(
        "\u00bf\uffff"
        )


    DFA11_transition = [
        DFA.unpack("\1\32\1\2\2\uffff\1\32\22\uffff\1\32\1\uffff\1\34\5\uffff"
        "\1\22\1\23\1\uffff\1\3\1\4\1\25\1\33\1\31\12\33\1\21\1\24\5\uffff"
        "\1\5\1\33\1\20\1\6\1\33\1\12\2\33\1\11\2\33\1\14\2\33\1\16\2\33"
        "\1\17\1\13\7\33\4\uffff\1\33\1\uffff\1\7\1\33\1\27\1\10\5\33\1\30"
        "\2\33\2\1\1\15\1\26\2\33\1\1\1\33\1\1\5\33\1\uffff\1\33"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\37"),
        DFA.unpack("\1\40\11\uffff\1\41\25\uffff\1\42"),
        DFA.unpack("\1\43\2\uffff\1\44"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46"),
        DFA.unpack("\1\47\45\uffff\1\50"),
        DFA.unpack("\1\51\32\uffff\1\53\4\uffff\1\52"),
        DFA.unpack("\1\54"),
        DFA.unpack("\1\56\3\uffff\1\55"),
        DFA.unpack("\1\57"),
        DFA.unpack("\1\60"),
        DFA.unpack("\1\61\20\uffff\1\62"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\63"),
        DFA.unpack("\1\64"),
        DFA.unpack("\1\65"),
        DFA.unpack("\1\66"),
        DFA.unpack("\1\70\4\uffff\1\67"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\71"),
        DFA.unpack("\1\72"),
        DFA.unpack("\1\73"),
        DFA.unpack("\1\74\16\uffff\1\75"),
        DFA.unpack("\1\76"),
        DFA.unpack("\1\77"),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101"),
        DFA.unpack("\1\102"),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack("\1\106"),
        DFA.unpack("\1\107"),
        DFA.unpack("\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack(""),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack("\15\121\7\uffff\32\121\4\uffff\1\121\1\uffff\32\121"
        "\1\uffff\1\121"),
        DFA.unpack(""),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\123"),
        DFA.unpack("\1\124"),
        DFA.unpack("\1\125"),
        DFA.unpack("\1\126"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
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
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\150"),
        DFA.unpack("\15\121\7\uffff\32\121\4\uffff\1\121\1\uffff\32\121"
        "\1\uffff\1\121"),
        DFA.unpack(""),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack(""),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\155"),
        DFA.unpack("\1\156"),
        DFA.unpack("\1\157"),
        DFA.unpack("\1\160"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\161"),
        DFA.unpack("\1\162"),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack(""),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081"),
        DFA.unpack("\1\u0082"),
        DFA.unpack(""),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u008a"),
        DFA.unpack(""),
        DFA.unpack("\1\u008b"),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090"),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack(""),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\1\u009a"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f"),
        DFA.unpack("\1\u00a0"),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\1\u00a5"),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\u00a7"),
        DFA.unpack("\1\u00a8"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack(""),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u00b0"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u00b7"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00ba"),
        DFA.unpack(""),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack(""),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\15\33\7\uffff\32\33\4\uffff\1\33\1\uffff\32\33\1\uffff"
        "\1\33"),
        DFA.unpack("")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
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
