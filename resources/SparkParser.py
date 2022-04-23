# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-23 19:21:05

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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CAST_COLUMN", "CL", "COMMA", "COMMENT", "CREATE_LITERAL", "DEDUPLICATE", 
    "DESTINATION", "EPOCH_FORMAT", "FILE_FORMAT", "FROM_UNIXTIME", "LP", 
    "NEWLINE", "ORDER_BY", "OUTPUT_PARTITIONS", "OVERWRITE", "PLUS", "RENAME_COLUMN", 
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:20:1: startRule : source_definition NEWLINE ( destination_definition ) ( NEWLINE )+ ( action )* ( NEWLINE )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:2: ( source_definition NEWLINE ( destination_definition ) ( NEWLINE )+ ( action )* ( NEWLINE )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:21:4: source_definition NEWLINE ( destination_definition ) ( NEWLINE )+ ( action )* ( NEWLINE )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule48)
                self.source_definition()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule50)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:3: ( destination_definition )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:4: destination_definition
                pass 
                self._state.following.append(self.FOLLOW_destination_definition_in_startRule55)
                self.destination_definition()

                self._state.following.pop()




                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:28: ( NEWLINE )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:28: NEWLINE
                        pass 
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule58)


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
                        self._state.following.append(self.FOLLOW_action_in_startRule64)
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
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule70)


                    else:
                        break #loop3


                self.match(self.input, EOF, self.FOLLOW_EOF_in_startRule75)




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
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition90)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition92)

                source = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_source_definition96)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition98)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition102)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition104)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:34:1: destination_definition : DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP (overwrite= OVERWRITE )? ;
    def destination_definition(self, ):
        destination = None
        format = None
        overwrite = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:35:2: ( DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP (overwrite= OVERWRITE )? )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:36:4: DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP (overwrite= OVERWRITE )?
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition124)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition126)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition130)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition132)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition136)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition138)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:36:70: (overwrite= OVERWRITE )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == OVERWRITE) :
                    alt4 = 1
                if alt4 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:36:70: overwrite= OVERWRITE
                    pass 
                    overwrite = self.match(self.input, OVERWRITE, self.FOLLOW_OVERWRITE_in_destination_definition142)




                #action start
                self.standardizer.setDestination(destination.text, format.text)
                self.standardizer.overwrite = True if overwrite else False
                	  
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "destination_definition"



    # $ANTLR start "action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:1: action : PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) NEWLINE ;
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:9: ( PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) NEWLINE )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) NEWLINE
                pass 
                self.match(self.input, PLUS, self.FOLLOW_PLUS_in_action163)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action )
                alt5 = 7
                LA5 = self.input.LA(1)
                if LA5 in {RENAME_COLUMN}:
                    alt5 = 1
                elif LA5 in {CAST_COLUMN}:
                    alt5 = 2
                elif LA5 in {CREATE_LITERAL}:
                    alt5 = 3
                elif LA5 in {DEDUPLICATE}:
                    alt5 = 4
                elif LA5 in {STORE_COLUMNS}:
                    alt5 = 5
                elif LA5 in {FROM_UNIXTIME}:
                    alt5 = 6
                elif LA5 in {OUTPUT_PARTITIONS}:
                    alt5 = 7
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:4: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action168)
                    self.rename_action()

                    self._state.following.pop()


                elif alt5 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:46:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action174)
                    self.cast_action()

                    self._state.following.pop()


                elif alt5 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:47:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action180)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt5 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:48:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action186)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt5 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:49:3: store_columns_action
                    pass 
                    self._state.following.append(self.FOLLOW_store_columns_action_in_action192)
                    self.store_columns_action()

                    self._state.following.pop()


                elif alt5 == 6:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:50:3: from_unixtime_action
                    pass 
                    self._state.following.append(self.FOLLOW_from_unixtime_action_in_action198)
                    self.from_unixtime_action()

                    self._state.following.pop()


                elif alt5 == 7:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:51:3: output_partitions_action
                    pass 
                    self._state.following.append(self.FOLLOW_output_partitions_action_in_action204)
                    self.output_partitions_action()

                    self._state.following.pop()




                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_action213)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "action"



    # $ANTLR start "from_unixtime_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:62:1: from_unixtime_action : FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP ;
    def from_unixtime_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:63:2: ( FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:63:4: FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP
                pass 
                self.match(self.input, FROM_UNIXTIME, self.FOLLOW_FROM_UNIXTIME_in_from_unixtime_action231)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action233)

                x = self.match(self.input, EPOCH_FORMAT, self.FOLLOW_EPOCH_FORMAT_in_from_unixtime_action237)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action239)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action241)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_from_unixtime_action245)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action247)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:67:1: output_partitions_action : OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def output_partitions_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:68:2: ( OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:68:4: OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, OUTPUT_PARTITIONS, self.FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action266)

                self.match(self.input, LP, self.FOLLOW_LP_in_output_partitions_action268)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:68:25: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:68:26: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action273)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:68:34: ( COMMA x+= TEXT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:68:35: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_output_partitions_action276)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action280)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop6





                self.match(self.input, RP, self.FOLLOW_RP_in_output_partitions_action285)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:75:1: store_columns_action : STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def store_columns_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:2: ( STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:4: STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, STORE_COLUMNS, self.FOLLOW_STORE_COLUMNS_in_store_columns_action301)

                self.match(self.input, LP, self.FOLLOW_LP_in_store_columns_action303)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:21: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:22: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action308)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:30: ( COMMA x+= TEXT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == COMMA) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:31: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store_columns_action311)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action315)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop7





                self.match(self.input, RP, self.FOLLOW_RP_in_store_columns_action320)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:83:1: cast_action : CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP ;
    def cast_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:2: ( CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:85:2: CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action337)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action339)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_cast_action343)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action345)

                y = self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action349)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action351)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:89:1: create_literal_action : CREATE_LITERAL LP x= TEXT RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:90:2: ( CREATE_LITERAL LP x= TEXT RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:91:2: CREATE_LITERAL LP x= TEXT RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action368)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action370)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_create_literal_action374)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action376)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action378)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action382)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action384)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:95:1: deduplicate_action : DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT ;
    def deduplicate_action(self, ):
        y = None
        z = None
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:96:2: ( DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:97:2: DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action400)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action402)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:97:17: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:97:18: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action407)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:97:26: ( COMMA x+= TEXT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:97:27: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action410)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action414)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop8





                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action419)

                self.match(self.input, ORDER_BY, self.FOLLOW_ORDER_BY_in_deduplicate_action421)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action425)

                z = self.match(self.input, SORT, self.FOLLOW_SORT_in_deduplicate_action429)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:1: rename_action : RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:106:2: ( RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:107:2: RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action447)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action449)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action453)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action455)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action459)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action461)

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
    FOLLOW_destination_definition_in_startRule55 = frozenset([15])
    FOLLOW_NEWLINE_in_startRule58 = frozenset([15, 19])
    FOLLOW_action_in_startRule64 = frozenset([15, 19])
    FOLLOW_NEWLINE_in_startRule70 = frozenset([15])
    FOLLOW_EOF_in_startRule75 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition90 = frozenset([5])
    FOLLOW_CL_in_source_definition92 = frozenset([28])
    FOLLOW_TEXT_in_source_definition96 = frozenset([14])
    FOLLOW_LP_in_source_definition98 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_source_definition102 = frozenset([22])
    FOLLOW_RP_in_source_definition104 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition124 = frozenset([5])
    FOLLOW_CL_in_destination_definition126 = frozenset([28])
    FOLLOW_TEXT_in_destination_definition130 = frozenset([14])
    FOLLOW_LP_in_destination_definition132 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_destination_definition136 = frozenset([22])
    FOLLOW_RP_in_destination_definition138 = frozenset([1, 18])
    FOLLOW_OVERWRITE_in_destination_definition142 = frozenset([1])
    FOLLOW_PLUS_in_action163 = frozenset([4, 8, 9, 13, 17, 20, 26])
    FOLLOW_rename_action_in_action168 = frozenset([15])
    FOLLOW_cast_action_in_action174 = frozenset([15])
    FOLLOW_create_literal_action_in_action180 = frozenset([15])
    FOLLOW_deduplicate_action_in_action186 = frozenset([15])
    FOLLOW_store_columns_action_in_action192 = frozenset([15])
    FOLLOW_from_unixtime_action_in_action198 = frozenset([15])
    FOLLOW_output_partitions_action_in_action204 = frozenset([15])
    FOLLOW_NEWLINE_in_action213 = frozenset([1])
    FOLLOW_FROM_UNIXTIME_in_from_unixtime_action231 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action233 = frozenset([11])
    FOLLOW_EPOCH_FORMAT_in_from_unixtime_action237 = frozenset([22])
    FOLLOW_RP_in_from_unixtime_action239 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action241 = frozenset([28])
    FOLLOW_TEXT_in_from_unixtime_action245 = frozenset([22])
    FOLLOW_RP_in_from_unixtime_action247 = frozenset([1])
    FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action266 = frozenset([14])
    FOLLOW_LP_in_output_partitions_action268 = frozenset([28])
    FOLLOW_TEXT_in_output_partitions_action273 = frozenset([6, 22])
    FOLLOW_COMMA_in_output_partitions_action276 = frozenset([28])
    FOLLOW_TEXT_in_output_partitions_action280 = frozenset([6, 22])
    FOLLOW_RP_in_output_partitions_action285 = frozenset([1])
    FOLLOW_STORE_COLUMNS_in_store_columns_action301 = frozenset([14])
    FOLLOW_LP_in_store_columns_action303 = frozenset([28])
    FOLLOW_TEXT_in_store_columns_action308 = frozenset([6, 22])
    FOLLOW_COMMA_in_store_columns_action311 = frozenset([28])
    FOLLOW_TEXT_in_store_columns_action315 = frozenset([6, 22])
    FOLLOW_RP_in_store_columns_action320 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action337 = frozenset([14])
    FOLLOW_LP_in_cast_action339 = frozenset([28])
    FOLLOW_TEXT_in_cast_action343 = frozenset([21])
    FOLLOW_RIGHT_ARROW_in_cast_action345 = frozenset([29])
    FOLLOW_TYPE_in_cast_action349 = frozenset([22])
    FOLLOW_RP_in_cast_action351 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action368 = frozenset([14])
    FOLLOW_LP_in_create_literal_action370 = frozenset([28])
    FOLLOW_TEXT_in_create_literal_action374 = frozenset([22])
    FOLLOW_RP_in_create_literal_action376 = frozenset([14])
    FOLLOW_LP_in_create_literal_action378 = frozenset([27])
    FOLLOW_STRING_in_create_literal_action382 = frozenset([22])
    FOLLOW_RP_in_create_literal_action384 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action400 = frozenset([14])
    FOLLOW_LP_in_deduplicate_action402 = frozenset([28])
    FOLLOW_TEXT_in_deduplicate_action407 = frozenset([6, 22])
    FOLLOW_COMMA_in_deduplicate_action410 = frozenset([28])
    FOLLOW_TEXT_in_deduplicate_action414 = frozenset([6, 22])
    FOLLOW_RP_in_deduplicate_action419 = frozenset([16])
    FOLLOW_ORDER_BY_in_deduplicate_action421 = frozenset([28])
    FOLLOW_TEXT_in_deduplicate_action425 = frozenset([24])
    FOLLOW_SORT_in_deduplicate_action429 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action447 = frozenset([14])
    FOLLOW_LP_in_rename_action449 = frozenset([28])
    FOLLOW_TEXT_in_rename_action453 = frozenset([21])
    FOLLOW_RIGHT_ARROW_in_rename_action455 = frozenset([28])
    FOLLOW_TEXT_in_rename_action459 = frozenset([22])
    FOLLOW_RP_in_rename_action461 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
