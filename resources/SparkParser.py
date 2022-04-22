# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-22 18:42:31

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
EPOCH_FORMAT=11
FILE_FORMAT=12
FROM_UNIXTIME=13
LP=14
NEWLINE=15
ORDER_BY=16
OUTPUT_PARTITIONS=17
PLUS=18
RENAME_COLUMN=19
RIGHT_ARROW=20
RP=21
SC=22
SORT=23
SOURCE=24
STORE_COLUMNS=25
STRING=26
TEXT=27
TYPE=28
WS=29

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 4: "CAST_COLUMN", 5: "CL", 6: "COMMA", 7: "COMMENT", 8: "CREATE_LITERAL", 
    9: "DEDUPLICATE", 10: "DESTINATION", 11: "EPOCH_FORMAT", 12: "FILE_FORMAT", 
    13: "FROM_UNIXTIME", 14: "LP", 15: "NEWLINE", 16: "ORDER_BY", 17: "OUTPUT_PARTITIONS", 
    18: "PLUS", 19: "RENAME_COLUMN", 20: "RIGHT_ARROW", 21: "RP", 22: "SC", 
    23: "SORT", 24: "SOURCE", 25: "STORE_COLUMNS", 26: "STRING", 27: "TEXT", 
    28: "TYPE", 29: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CAST_COLUMN", "CL", "COMMA", "COMMENT", "CREATE_LITERAL", "DEDUPLICATE", 
    "DESTINATION", "EPOCH_FORMAT", "FILE_FORMAT", "FROM_UNIXTIME", "LP", 
    "NEWLINE", "ORDER_BY", "OUTPUT_PARTITIONS", "PLUS", "RENAME_COLUMN", 
    "RIGHT_ARROW", "RP", "SC", "SORT", "SOURCE", "STORE_COLUMNS", "STRING", 
    "TEXT", "TYPE", "WS"
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: startRule : source_definition NEWLINE destination_definition ( NEWLINE )* ( PLUS action ( EOF | NEWLINE ) )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition NEWLINE destination_definition ( NEWLINE )* ( PLUS action ( EOF | NEWLINE ) )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition NEWLINE destination_definition ( NEWLINE )* ( PLUS action ( EOF | NEWLINE ) )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule48)
                self.source_definition()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule50)

                self._state.following.append(self.FOLLOW_destination_definition_in_startRule54)
                self.destination_definition()

                self._state.following.pop()

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:26: ( NEWLINE )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:26: NEWLINE
                        pass 
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule56)


                    else:
                        break #loop1


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:3: ( PLUS action ( EOF | NEWLINE ) )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == PLUS) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:4: PLUS action ( EOF | NEWLINE )
                        pass 
                        self.match(self.input, PLUS, self.FOLLOW_PLUS_in_startRule62)

                        self._state.following.append(self.FOLLOW_action_in_startRule64)
                        self.action()

                        self._state.following.pop()

                        if self.input.LA(1) in {EOF, NEWLINE}:
                            self.input.consume()
                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop2


                self.match(self.input, EOF, self.FOLLOW_EOF_in_startRule76)




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
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition91)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition93)

                source = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_source_definition97)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition99)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition103)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition105)

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
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition125)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition127)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition131)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition133)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition137)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition139)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:40:1: action : ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) ( NEWLINE | EOF ) ;
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:40:9: ( ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) ( NEWLINE | EOF ) )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:41:3: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) ( NEWLINE | EOF )
                pass 
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:41:3: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action )
                alt3 = 7
                LA3 = self.input.LA(1)
                if LA3 in {RENAME_COLUMN}:
                    alt3 = 1
                elif LA3 in {CAST_COLUMN}:
                    alt3 = 2
                elif LA3 in {CREATE_LITERAL}:
                    alt3 = 3
                elif LA3 in {DEDUPLICATE}:
                    alt3 = 4
                elif LA3 in {STORE_COLUMNS}:
                    alt3 = 5
                elif LA3 in {FROM_UNIXTIME}:
                    alt3 = 6
                elif LA3 in {OUTPUT_PARTITIONS}:
                    alt3 = 7
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:41:4: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action160)
                    self.rename_action()

                    self._state.following.pop()


                elif alt3 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action166)
                    self.cast_action()

                    self._state.following.pop()


                elif alt3 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action172)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt3 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action178)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt3 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: store_columns_action
                    pass 
                    self._state.following.append(self.FOLLOW_store_columns_action_in_action184)
                    self.store_columns_action()

                    self._state.following.pop()


                elif alt3 == 6:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:46:3: from_unixtime_action
                    pass 
                    self._state.following.append(self.FOLLOW_from_unixtime_action_in_action190)
                    self.from_unixtime_action()

                    self._state.following.pop()


                elif alt3 == 7:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:47:3: output_partitions_action
                    pass 
                    self._state.following.append(self.FOLLOW_output_partitions_action_in_action196)
                    self.output_partitions_action()

                    self._state.following.pop()




                if self.input.LA(1) in {EOF, NEWLINE}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "action"



    # $ANTLR start "from_unixtime_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:58:1: from_unixtime_action : FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP ;
    def from_unixtime_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:59:2: ( FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:59:4: FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP
                pass 
                self.match(self.input, FROM_UNIXTIME, self.FOLLOW_FROM_UNIXTIME_in_from_unixtime_action227)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action229)

                x = self.match(self.input, EPOCH_FORMAT, self.FOLLOW_EPOCH_FORMAT_in_from_unixtime_action233)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action235)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action237)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_from_unixtime_action241)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action243)

                #action start
                self.standardizer.addAction(self.standardizer.fromUnixtime,x.text,y.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "from_unixtime_action"



    # $ANTLR start "output_partitions_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:63:1: output_partitions_action : OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def output_partitions_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:2: ( OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:4: OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, OUTPUT_PARTITIONS, self.FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action262)

                self.match(self.input, LP, self.FOLLOW_LP_in_output_partitions_action264)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:25: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:26: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action269)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:34: ( COMMA x+= TEXT )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COMMA) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:35: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_output_partitions_action272)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action276)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop4





                self.match(self.input, RP, self.FOLLOW_RP_in_output_partitions_action281)

                #action start
                  
                list = [tk.text for tk in list_x]
                self.standardizer.outputPartitions = list
                		
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "output_partitions_action"



    # $ANTLR start "store_columns_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:71:1: store_columns_action : STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def store_columns_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:2: ( STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:4: STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, STORE_COLUMNS, self.FOLLOW_STORE_COLUMNS_in_store_columns_action297)

                self.match(self.input, LP, self.FOLLOW_LP_in_store_columns_action299)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:21: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:22: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action304)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:30: ( COMMA x+= TEXT )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:31: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store_columns_action307)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action311)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop5





                self.match(self.input, RP, self.FOLLOW_RP_in_store_columns_action316)

                #action start
                  
                list = [tk.text for tk in list_x]
                self.standardizer.columnsToStore = list
                		
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "store_columns_action"



    # $ANTLR start "cast_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:79:1: cast_action : CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP ;
    def cast_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:80:2: ( CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:81:2: CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action333)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action335)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_cast_action339)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action341)

                y = self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action345)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action347)

                #action start
                self.standardizer.addAction(self.standardizer.castColumn,x.text,y.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "cast_action"



    # $ANTLR start "create_literal_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:85:1: create_literal_action : CREATE_LITERAL LP x= TEXT RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:86:2: ( CREATE_LITERAL LP x= TEXT RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:87:2: CREATE_LITERAL LP x= TEXT RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action364)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action366)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_create_literal_action370)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action372)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action374)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action378)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action380)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:91:1: deduplicate_action : DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT ;
    def deduplicate_action(self, ):
        y = None
        z = None
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:92:2: ( DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:2: DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action396)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action398)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:17: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:18: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action403)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:26: ( COMMA x+= TEXT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:27: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action406)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action410)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop6





                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action415)

                self.match(self.input, ORDER_BY, self.FOLLOW_ORDER_BY_in_deduplicate_action417)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action421)

                z = self.match(self.input, SORT, self.FOLLOW_SORT_in_deduplicate_action425)

                #action start
                 
                list = [tk.text for tk in list_x]
                self.standardizer.addAction(self.standardizer.deduplicate,list,y.text,z.text)
                	
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "deduplicate_action"



    # $ANTLR start "rename_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:101:1: rename_action : RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:102:2: ( RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:103:2: RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action443)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action445)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action449)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action451)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action455)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action457)

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



 

    FOLLOW_source_definition_in_startRule48 = frozenset([15])
    FOLLOW_NEWLINE_in_startRule50 = frozenset([10])
    FOLLOW_destination_definition_in_startRule54 = frozenset([15, 18])
    FOLLOW_NEWLINE_in_startRule56 = frozenset([15, 18])
    FOLLOW_PLUS_in_startRule62 = frozenset([4, 8, 9, 13, 17, 19, 25])
    FOLLOW_action_in_startRule64 = frozenset([15])
    FOLLOW_set_in_startRule66 = frozenset([18])
    FOLLOW_EOF_in_startRule76 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition91 = frozenset([5])
    FOLLOW_CL_in_source_definition93 = frozenset([27])
    FOLLOW_TEXT_in_source_definition97 = frozenset([14])
    FOLLOW_LP_in_source_definition99 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_source_definition103 = frozenset([21])
    FOLLOW_RP_in_source_definition105 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition125 = frozenset([5])
    FOLLOW_CL_in_destination_definition127 = frozenset([27])
    FOLLOW_TEXT_in_destination_definition131 = frozenset([14])
    FOLLOW_LP_in_destination_definition133 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_destination_definition137 = frozenset([21])
    FOLLOW_RP_in_destination_definition139 = frozenset([1])
    FOLLOW_rename_action_in_action160 = frozenset([15])
    FOLLOW_cast_action_in_action166 = frozenset([15])
    FOLLOW_create_literal_action_in_action172 = frozenset([15])
    FOLLOW_deduplicate_action_in_action178 = frozenset([15])
    FOLLOW_store_columns_action_in_action184 = frozenset([15])
    FOLLOW_from_unixtime_action_in_action190 = frozenset([15])
    FOLLOW_output_partitions_action_in_action196 = frozenset([15])
    FOLLOW_set_in_action205 = frozenset([1])
    FOLLOW_FROM_UNIXTIME_in_from_unixtime_action227 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action229 = frozenset([11])
    FOLLOW_EPOCH_FORMAT_in_from_unixtime_action233 = frozenset([21])
    FOLLOW_RP_in_from_unixtime_action235 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action237 = frozenset([27])
    FOLLOW_TEXT_in_from_unixtime_action241 = frozenset([21])
    FOLLOW_RP_in_from_unixtime_action243 = frozenset([1])
    FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action262 = frozenset([14])
    FOLLOW_LP_in_output_partitions_action264 = frozenset([27])
    FOLLOW_TEXT_in_output_partitions_action269 = frozenset([6, 21])
    FOLLOW_COMMA_in_output_partitions_action272 = frozenset([27])
    FOLLOW_TEXT_in_output_partitions_action276 = frozenset([6, 21])
    FOLLOW_RP_in_output_partitions_action281 = frozenset([1])
    FOLLOW_STORE_COLUMNS_in_store_columns_action297 = frozenset([14])
    FOLLOW_LP_in_store_columns_action299 = frozenset([27])
    FOLLOW_TEXT_in_store_columns_action304 = frozenset([6, 21])
    FOLLOW_COMMA_in_store_columns_action307 = frozenset([27])
    FOLLOW_TEXT_in_store_columns_action311 = frozenset([6, 21])
    FOLLOW_RP_in_store_columns_action316 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action333 = frozenset([14])
    FOLLOW_LP_in_cast_action335 = frozenset([27])
    FOLLOW_TEXT_in_cast_action339 = frozenset([20])
    FOLLOW_RIGHT_ARROW_in_cast_action341 = frozenset([28])
    FOLLOW_TYPE_in_cast_action345 = frozenset([21])
    FOLLOW_RP_in_cast_action347 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action364 = frozenset([14])
    FOLLOW_LP_in_create_literal_action366 = frozenset([27])
    FOLLOW_TEXT_in_create_literal_action370 = frozenset([21])
    FOLLOW_RP_in_create_literal_action372 = frozenset([14])
    FOLLOW_LP_in_create_literal_action374 = frozenset([26])
    FOLLOW_STRING_in_create_literal_action378 = frozenset([21])
    FOLLOW_RP_in_create_literal_action380 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action396 = frozenset([14])
    FOLLOW_LP_in_deduplicate_action398 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action403 = frozenset([6, 21])
    FOLLOW_COMMA_in_deduplicate_action406 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action410 = frozenset([6, 21])
    FOLLOW_RP_in_deduplicate_action415 = frozenset([16])
    FOLLOW_ORDER_BY_in_deduplicate_action417 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action421 = frozenset([23])
    FOLLOW_SORT_in_deduplicate_action425 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action443 = frozenset([14])
    FOLLOW_LP_in_rename_action445 = frozenset([27])
    FOLLOW_TEXT_in_rename_action449 = frozenset([20])
    FOLLOW_RIGHT_ARROW_in_rename_action451 = frozenset([27])
    FOLLOW_TEXT_in_rename_action455 = frozenset([21])
    FOLLOW_RP_in_rename_action457 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
