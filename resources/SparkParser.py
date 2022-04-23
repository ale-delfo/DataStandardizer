# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-23 12:45:13

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: startRule : source_definition SC destination_definition SC ( action )* ( NEWLINE )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition SC destination_definition SC ( action )* ( NEWLINE )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition SC destination_definition SC ( action )* ( NEWLINE )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule48)
                self.source_definition()

                self._state.following.pop()

                self.match(self.input, SC, self.FOLLOW_SC_in_startRule50)

                self._state.following.append(self.FOLLOW_destination_definition_in_startRule54)
                self.destination_definition()

                self._state.following.pop()

                self.match(self.input, SC, self.FOLLOW_SC_in_startRule56)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:3: ( action )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == PLUS) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:4: action
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_startRule61)
                        self.action()

                        self._state.following.pop()


                    else:
                        break #loop1


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:24:3: ( NEWLINE )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == NEWLINE) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:24:3: NEWLINE
                        pass 
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule67)


                    else:
                        break #loop2


                self.match(self.input, EOF, self.FOLLOW_EOF_in_startRule72)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "startRule"



    # $ANTLR start "source_definition"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:28:1: source_definition : SOURCE CL source= TEXT LP format= FILE_FORMAT RP ;
    def source_definition(self, ):
        source = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:29:2: ( SOURCE CL source= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:30:4: SOURCE CL source= TEXT LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition87)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition89)

                source = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_source_definition93)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition95)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition99)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition101)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:34:1: destination_definition : DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP ;
    def destination_definition(self, ):
        destination = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:35:2: ( DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:36:4: DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition121)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition123)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition127)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition129)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition133)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition135)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:41:1: action : PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) NEWLINE ;
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:41:9: ( PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) NEWLINE )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:3: PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) NEWLINE
                pass 
                self.match(self.input, PLUS, self.FOLLOW_PLUS_in_action155)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action )
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
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:4: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action160)
                    self.rename_action()

                    self._state.following.pop()


                elif alt3 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action166)
                    self.cast_action()

                    self._state.following.pop()


                elif alt3 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action172)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt3 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:46:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action178)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt3 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:47:3: store_columns_action
                    pass 
                    self._state.following.append(self.FOLLOW_store_columns_action_in_action184)
                    self.store_columns_action()

                    self._state.following.pop()


                elif alt3 == 6:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:48:3: from_unixtime_action
                    pass 
                    self._state.following.append(self.FOLLOW_from_unixtime_action_in_action190)
                    self.from_unixtime_action()

                    self._state.following.pop()


                elif alt3 == 7:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:49:3: output_partitions_action
                    pass 
                    self._state.following.append(self.FOLLOW_output_partitions_action_in_action196)
                    self.output_partitions_action()

                    self._state.following.pop()




                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_action205)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "action"



    # $ANTLR start "from_unixtime_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:60:1: from_unixtime_action : FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP ;
    def from_unixtime_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:61:2: ( FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:61:4: FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP
                pass 
                self.match(self.input, FROM_UNIXTIME, self.FOLLOW_FROM_UNIXTIME_in_from_unixtime_action223)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action225)

                x = self.match(self.input, EPOCH_FORMAT, self.FOLLOW_EPOCH_FORMAT_in_from_unixtime_action229)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action231)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action233)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_from_unixtime_action237)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action239)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:1: output_partitions_action : OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def output_partitions_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:2: ( OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:4: OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, OUTPUT_PARTITIONS, self.FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action258)

                self.match(self.input, LP, self.FOLLOW_LP_in_output_partitions_action260)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:25: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:26: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action265)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:34: ( COMMA x+= TEXT )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COMMA) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:35: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_output_partitions_action268)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action272)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop4





                self.match(self.input, RP, self.FOLLOW_RP_in_output_partitions_action277)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:73:1: store_columns_action : STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def store_columns_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:2: ( STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:4: STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, STORE_COLUMNS, self.FOLLOW_STORE_COLUMNS_in_store_columns_action293)

                self.match(self.input, LP, self.FOLLOW_LP_in_store_columns_action295)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:21: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:22: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action300)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:30: ( COMMA x+= TEXT )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:31: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store_columns_action303)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action307)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop5





                self.match(self.input, RP, self.FOLLOW_RP_in_store_columns_action312)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:81:1: cast_action : CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP ;
    def cast_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:82:2: ( CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:83:2: CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action329)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action331)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_cast_action335)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action337)

                y = self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action341)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action343)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:87:1: create_literal_action : CREATE_LITERAL LP x= TEXT RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:88:2: ( CREATE_LITERAL LP x= TEXT RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:89:2: CREATE_LITERAL LP x= TEXT RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action360)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action362)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_create_literal_action366)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action368)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action370)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action374)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action376)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:1: deduplicate_action : DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT ;
    def deduplicate_action(self, ):
        y = None
        z = None
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:94:2: ( DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:2: DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action392)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action394)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:17: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:18: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action399)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:26: ( COMMA x+= TEXT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:27: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action402)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action406)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop6





                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action411)

                self.match(self.input, ORDER_BY, self.FOLLOW_ORDER_BY_in_deduplicate_action413)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action417)

                z = self.match(self.input, SORT, self.FOLLOW_SORT_in_deduplicate_action421)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:103:1: rename_action : RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:104:2: ( RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:2: RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action439)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action441)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action445)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action447)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action451)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action453)

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



 

    FOLLOW_source_definition_in_startRule48 = frozenset([22])
    FOLLOW_SC_in_startRule50 = frozenset([10])
    FOLLOW_destination_definition_in_startRule54 = frozenset([22])
    FOLLOW_SC_in_startRule56 = frozenset([15, 18])
    FOLLOW_action_in_startRule61 = frozenset([15, 18])
    FOLLOW_NEWLINE_in_startRule67 = frozenset([15])
    FOLLOW_EOF_in_startRule72 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition87 = frozenset([5])
    FOLLOW_CL_in_source_definition89 = frozenset([27])
    FOLLOW_TEXT_in_source_definition93 = frozenset([14])
    FOLLOW_LP_in_source_definition95 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_source_definition99 = frozenset([21])
    FOLLOW_RP_in_source_definition101 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition121 = frozenset([5])
    FOLLOW_CL_in_destination_definition123 = frozenset([27])
    FOLLOW_TEXT_in_destination_definition127 = frozenset([14])
    FOLLOW_LP_in_destination_definition129 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_destination_definition133 = frozenset([21])
    FOLLOW_RP_in_destination_definition135 = frozenset([1])
    FOLLOW_PLUS_in_action155 = frozenset([4, 8, 9, 13, 17, 19, 25])
    FOLLOW_rename_action_in_action160 = frozenset([15])
    FOLLOW_cast_action_in_action166 = frozenset([15])
    FOLLOW_create_literal_action_in_action172 = frozenset([15])
    FOLLOW_deduplicate_action_in_action178 = frozenset([15])
    FOLLOW_store_columns_action_in_action184 = frozenset([15])
    FOLLOW_from_unixtime_action_in_action190 = frozenset([15])
    FOLLOW_output_partitions_action_in_action196 = frozenset([15])
    FOLLOW_NEWLINE_in_action205 = frozenset([1])
    FOLLOW_FROM_UNIXTIME_in_from_unixtime_action223 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action225 = frozenset([11])
    FOLLOW_EPOCH_FORMAT_in_from_unixtime_action229 = frozenset([21])
    FOLLOW_RP_in_from_unixtime_action231 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action233 = frozenset([27])
    FOLLOW_TEXT_in_from_unixtime_action237 = frozenset([21])
    FOLLOW_RP_in_from_unixtime_action239 = frozenset([1])
    FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action258 = frozenset([14])
    FOLLOW_LP_in_output_partitions_action260 = frozenset([27])
    FOLLOW_TEXT_in_output_partitions_action265 = frozenset([6, 21])
    FOLLOW_COMMA_in_output_partitions_action268 = frozenset([27])
    FOLLOW_TEXT_in_output_partitions_action272 = frozenset([6, 21])
    FOLLOW_RP_in_output_partitions_action277 = frozenset([1])
    FOLLOW_STORE_COLUMNS_in_store_columns_action293 = frozenset([14])
    FOLLOW_LP_in_store_columns_action295 = frozenset([27])
    FOLLOW_TEXT_in_store_columns_action300 = frozenset([6, 21])
    FOLLOW_COMMA_in_store_columns_action303 = frozenset([27])
    FOLLOW_TEXT_in_store_columns_action307 = frozenset([6, 21])
    FOLLOW_RP_in_store_columns_action312 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action329 = frozenset([14])
    FOLLOW_LP_in_cast_action331 = frozenset([27])
    FOLLOW_TEXT_in_cast_action335 = frozenset([20])
    FOLLOW_RIGHT_ARROW_in_cast_action337 = frozenset([28])
    FOLLOW_TYPE_in_cast_action341 = frozenset([21])
    FOLLOW_RP_in_cast_action343 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action360 = frozenset([14])
    FOLLOW_LP_in_create_literal_action362 = frozenset([27])
    FOLLOW_TEXT_in_create_literal_action366 = frozenset([21])
    FOLLOW_RP_in_create_literal_action368 = frozenset([14])
    FOLLOW_LP_in_create_literal_action370 = frozenset([26])
    FOLLOW_STRING_in_create_literal_action374 = frozenset([21])
    FOLLOW_RP_in_create_literal_action376 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action392 = frozenset([14])
    FOLLOW_LP_in_deduplicate_action394 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action399 = frozenset([6, 21])
    FOLLOW_COMMA_in_deduplicate_action402 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action406 = frozenset([6, 21])
    FOLLOW_RP_in_deduplicate_action411 = frozenset([16])
    FOLLOW_ORDER_BY_in_deduplicate_action413 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action417 = frozenset([23])
    FOLLOW_SORT_in_deduplicate_action421 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action439 = frozenset([14])
    FOLLOW_LP_in_rename_action441 = frozenset([27])
    FOLLOW_TEXT_in_rename_action445 = frozenset([20])
    FOLLOW_RIGHT_ARROW_in_rename_action447 = frozenset([27])
    FOLLOW_TEXT_in_rename_action451 = frozenset([21])
    FOLLOW_RP_in_rename_action453 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
