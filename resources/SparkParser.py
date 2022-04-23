# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-23 18:50:25

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: startRule : source_definition NEWLINE destination_definition ( NEWLINE )+ ( action )* ( NEWLINE )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition NEWLINE destination_definition ( NEWLINE )+ ( action )* ( NEWLINE )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition NEWLINE destination_definition ( NEWLINE )+ ( action )* ( NEWLINE )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule48)
                self.source_definition()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule50)

                self._state.following.append(self.FOLLOW_destination_definition_in_startRule54)
                self.destination_definition()

                self._state.following.pop()

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:26: ( NEWLINE )+
                cnt1 = 0
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
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:3: ( action )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == PLUS) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:4: action
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_startRule62)
                        self.action()

                        self._state.following.pop()


                    else:
                        break #loop2


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:24:3: ( NEWLINE )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == NEWLINE) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:24:3: NEWLINE
                        pass 
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule68)


                    else:
                        break #loop3


                self.match(self.input, EOF, self.FOLLOW_EOF_in_startRule73)




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
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition88)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition90)

                source = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_source_definition94)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition96)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition100)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition102)

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
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition122)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition124)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition128)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition130)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition134)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition136)

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
                self.match(self.input, PLUS, self.FOLLOW_PLUS_in_action156)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action )
                alt4 = 7
                LA4 = self.input.LA(1)
                if LA4 in {RENAME_COLUMN}:
                    alt4 = 1
                elif LA4 in {CAST_COLUMN}:
                    alt4 = 2
                elif LA4 in {CREATE_LITERAL}:
                    alt4 = 3
                elif LA4 in {DEDUPLICATE}:
                    alt4 = 4
                elif LA4 in {STORE_COLUMNS}:
                    alt4 = 5
                elif LA4 in {FROM_UNIXTIME}:
                    alt4 = 6
                elif LA4 in {OUTPUT_PARTITIONS}:
                    alt4 = 7
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:4: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action161)
                    self.rename_action()

                    self._state.following.pop()


                elif alt4 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action167)
                    self.cast_action()

                    self._state.following.pop()


                elif alt4 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action173)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt4 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:46:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action179)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt4 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:47:3: store_columns_action
                    pass 
                    self._state.following.append(self.FOLLOW_store_columns_action_in_action185)
                    self.store_columns_action()

                    self._state.following.pop()


                elif alt4 == 6:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:48:3: from_unixtime_action
                    pass 
                    self._state.following.append(self.FOLLOW_from_unixtime_action_in_action191)
                    self.from_unixtime_action()

                    self._state.following.pop()


                elif alt4 == 7:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:49:3: output_partitions_action
                    pass 
                    self._state.following.append(self.FOLLOW_output_partitions_action_in_action197)
                    self.output_partitions_action()

                    self._state.following.pop()




                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_action206)




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
                self.match(self.input, FROM_UNIXTIME, self.FOLLOW_FROM_UNIXTIME_in_from_unixtime_action224)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action226)

                x = self.match(self.input, EPOCH_FORMAT, self.FOLLOW_EPOCH_FORMAT_in_from_unixtime_action230)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action232)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action234)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_from_unixtime_action238)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action240)

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
                self.match(self.input, OUTPUT_PARTITIONS, self.FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action259)

                self.match(self.input, LP, self.FOLLOW_LP_in_output_partitions_action261)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:25: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:26: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action266)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:34: ( COMMA x+= TEXT )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:35: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_output_partitions_action269)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action273)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop5





                self.match(self.input, RP, self.FOLLOW_RP_in_output_partitions_action278)

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
                self.match(self.input, STORE_COLUMNS, self.FOLLOW_STORE_COLUMNS_in_store_columns_action294)

                self.match(self.input, LP, self.FOLLOW_LP_in_store_columns_action296)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:21: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:22: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action301)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:30: ( COMMA x+= TEXT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:74:31: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store_columns_action304)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action308)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop6





                self.match(self.input, RP, self.FOLLOW_RP_in_store_columns_action313)

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
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action330)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action332)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_cast_action336)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action338)

                y = self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action342)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action344)

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
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action361)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action363)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_create_literal_action367)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action369)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action371)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action375)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action377)

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
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action393)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action395)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:17: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:18: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action400)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:26: ( COMMA x+= TEXT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == COMMA) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:27: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action403)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action407)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop7





                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action412)

                self.match(self.input, ORDER_BY, self.FOLLOW_ORDER_BY_in_deduplicate_action414)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action418)

                z = self.match(self.input, SORT, self.FOLLOW_SORT_in_deduplicate_action422)

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
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action440)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action442)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action446)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action448)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action452)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action454)

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
    FOLLOW_destination_definition_in_startRule54 = frozenset([15])
    FOLLOW_NEWLINE_in_startRule56 = frozenset([15, 18])
    FOLLOW_action_in_startRule62 = frozenset([15, 18])
    FOLLOW_NEWLINE_in_startRule68 = frozenset([15])
    FOLLOW_EOF_in_startRule73 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition88 = frozenset([5])
    FOLLOW_CL_in_source_definition90 = frozenset([27])
    FOLLOW_TEXT_in_source_definition94 = frozenset([14])
    FOLLOW_LP_in_source_definition96 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_source_definition100 = frozenset([21])
    FOLLOW_RP_in_source_definition102 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition122 = frozenset([5])
    FOLLOW_CL_in_destination_definition124 = frozenset([27])
    FOLLOW_TEXT_in_destination_definition128 = frozenset([14])
    FOLLOW_LP_in_destination_definition130 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_destination_definition134 = frozenset([21])
    FOLLOW_RP_in_destination_definition136 = frozenset([1])
    FOLLOW_PLUS_in_action156 = frozenset([4, 8, 9, 13, 17, 19, 25])
    FOLLOW_rename_action_in_action161 = frozenset([15])
    FOLLOW_cast_action_in_action167 = frozenset([15])
    FOLLOW_create_literal_action_in_action173 = frozenset([15])
    FOLLOW_deduplicate_action_in_action179 = frozenset([15])
    FOLLOW_store_columns_action_in_action185 = frozenset([15])
    FOLLOW_from_unixtime_action_in_action191 = frozenset([15])
    FOLLOW_output_partitions_action_in_action197 = frozenset([15])
    FOLLOW_NEWLINE_in_action206 = frozenset([1])
    FOLLOW_FROM_UNIXTIME_in_from_unixtime_action224 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action226 = frozenset([11])
    FOLLOW_EPOCH_FORMAT_in_from_unixtime_action230 = frozenset([21])
    FOLLOW_RP_in_from_unixtime_action232 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action234 = frozenset([27])
    FOLLOW_TEXT_in_from_unixtime_action238 = frozenset([21])
    FOLLOW_RP_in_from_unixtime_action240 = frozenset([1])
    FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action259 = frozenset([14])
    FOLLOW_LP_in_output_partitions_action261 = frozenset([27])
    FOLLOW_TEXT_in_output_partitions_action266 = frozenset([6, 21])
    FOLLOW_COMMA_in_output_partitions_action269 = frozenset([27])
    FOLLOW_TEXT_in_output_partitions_action273 = frozenset([6, 21])
    FOLLOW_RP_in_output_partitions_action278 = frozenset([1])
    FOLLOW_STORE_COLUMNS_in_store_columns_action294 = frozenset([14])
    FOLLOW_LP_in_store_columns_action296 = frozenset([27])
    FOLLOW_TEXT_in_store_columns_action301 = frozenset([6, 21])
    FOLLOW_COMMA_in_store_columns_action304 = frozenset([27])
    FOLLOW_TEXT_in_store_columns_action308 = frozenset([6, 21])
    FOLLOW_RP_in_store_columns_action313 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action330 = frozenset([14])
    FOLLOW_LP_in_cast_action332 = frozenset([27])
    FOLLOW_TEXT_in_cast_action336 = frozenset([20])
    FOLLOW_RIGHT_ARROW_in_cast_action338 = frozenset([28])
    FOLLOW_TYPE_in_cast_action342 = frozenset([21])
    FOLLOW_RP_in_cast_action344 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action361 = frozenset([14])
    FOLLOW_LP_in_create_literal_action363 = frozenset([27])
    FOLLOW_TEXT_in_create_literal_action367 = frozenset([21])
    FOLLOW_RP_in_create_literal_action369 = frozenset([14])
    FOLLOW_LP_in_create_literal_action371 = frozenset([26])
    FOLLOW_STRING_in_create_literal_action375 = frozenset([21])
    FOLLOW_RP_in_create_literal_action377 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action393 = frozenset([14])
    FOLLOW_LP_in_deduplicate_action395 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action400 = frozenset([6, 21])
    FOLLOW_COMMA_in_deduplicate_action403 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action407 = frozenset([6, 21])
    FOLLOW_RP_in_deduplicate_action412 = frozenset([16])
    FOLLOW_ORDER_BY_in_deduplicate_action414 = frozenset([27])
    FOLLOW_TEXT_in_deduplicate_action418 = frozenset([23])
    FOLLOW_SORT_in_deduplicate_action422 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action440 = frozenset([14])
    FOLLOW_LP_in_rename_action442 = frozenset([27])
    FOLLOW_TEXT_in_rename_action446 = frozenset([20])
    FOLLOW_RIGHT_ARROW_in_rename_action448 = frozenset([27])
    FOLLOW_TEXT_in_rename_action452 = frozenset([21])
    FOLLOW_RP_in_rename_action454 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
