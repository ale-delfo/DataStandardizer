# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-25 22:41:59

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
    errors = False
    def getStandardizer(self):
        return self.standardizer
    def errorsOccurred(self):
        return self.errors
    def displayRecognitionError(self, e):
               hdr = self.getErrorHeader(e)
               msg = self.getErrorMessage(e)
               self.errors = True
               self.emitErrorMessage(hdr + " " + msg)



    # $ANTLR start "startRule"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:28:1: startRule : source_definition NEWLINE destination_definition ( NEWLINE )+ ( action )* ( NEWLINE )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:29:2: ( source_definition NEWLINE destination_definition ( NEWLINE )+ ( action )* ( NEWLINE )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:29:4: source_definition NEWLINE destination_definition ( NEWLINE )+ ( action )* ( NEWLINE )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule48)
                self.source_definition()

                self._state.following.pop()

                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule50)

                self._state.following.append(self.FOLLOW_destination_definition_in_startRule54)
                self.destination_definition()

                self._state.following.pop()

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:30:26: ( NEWLINE )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:30:26: NEWLINE
                        pass 
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_startRule56)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:31:3: ( action )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == PLUS) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:31:4: action
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_startRule62)
                        self.action()

                        self._state.following.pop()


                    else:
                        break #loop2


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:32:3: ( NEWLINE )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == NEWLINE) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:32:3: NEWLINE
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:36:1: source_definition : SOURCE CL source= TEXT LP format= FILE_FORMAT RP ;
    def source_definition(self, ):
        source = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:37:2: ( SOURCE CL source= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:38:4: SOURCE CL source= TEXT LP format= FILE_FORMAT RP
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:1: destination_definition : DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP (overwrite= OVERWRITE )? ;
    def destination_definition(self, ):
        destination = None
        format = None
        overwrite = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:2: ( DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP (overwrite= OVERWRITE )? )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:4: DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP (overwrite= OVERWRITE )?
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition122)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition124)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition128)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition130)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition134)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition136)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:70: (overwrite= OVERWRITE )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == OVERWRITE) :
                    alt4 = 1
                if alt4 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:70: overwrite= OVERWRITE
                    pass 
                    overwrite = self.match(self.input, OVERWRITE, self.FOLLOW_OVERWRITE_in_destination_definition140)




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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:51:1: action : PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) ( NEWLINE | EOF ) ;
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:51:9: ( PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) ( NEWLINE | EOF ) )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:3: PLUS ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action ) ( NEWLINE | EOF )
                pass 
                self.match(self.input, PLUS, self.FOLLOW_PLUS_in_action161)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:53:3: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action | from_unixtime_action | output_partitions_action )
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
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:53:4: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action166)
                    self.rename_action()

                    self._state.following.pop()


                elif alt5 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:54:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action172)
                    self.cast_action()

                    self._state.following.pop()


                elif alt5 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:55:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action178)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt5 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:56:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action184)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt5 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:57:3: store_columns_action
                    pass 
                    self._state.following.append(self.FOLLOW_store_columns_action_in_action190)
                    self.store_columns_action()

                    self._state.following.pop()


                elif alt5 == 6:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:58:3: from_unixtime_action
                    pass 
                    self._state.following.append(self.FOLLOW_from_unixtime_action_in_action196)
                    self.from_unixtime_action()

                    self._state.following.pop()


                elif alt5 == 7:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:59:3: output_partitions_action
                    pass 
                    self._state.following.append(self.FOLLOW_output_partitions_action_in_action202)
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:70:1: from_unixtime_action : FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP ;
    def from_unixtime_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:71:2: ( FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:71:4: FROM_UNIXTIME LP x= EPOCH_FORMAT RP LP y= TEXT RP
                pass 
                self.match(self.input, FROM_UNIXTIME, self.FOLLOW_FROM_UNIXTIME_in_from_unixtime_action233)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action235)

                x = self.match(self.input, EPOCH_FORMAT, self.FOLLOW_EPOCH_FORMAT_in_from_unixtime_action239)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action241)

                self.match(self.input, LP, self.FOLLOW_LP_in_from_unixtime_action243)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_from_unixtime_action247)

                self.match(self.input, RP, self.FOLLOW_RP_in_from_unixtime_action249)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:75:1: output_partitions_action : OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def output_partitions_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:2: ( OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:4: OUTPUT_PARTITIONS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, OUTPUT_PARTITIONS, self.FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action268)

                self.match(self.input, LP, self.FOLLOW_LP_in_output_partitions_action270)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:25: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:26: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action275)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:34: ( COMMA x+= TEXT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:76:35: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_output_partitions_action278)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_output_partitions_action282)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop6





                self.match(self.input, RP, self.FOLLOW_RP_in_output_partitions_action287)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:83:1: store_columns_action : STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def store_columns_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:2: ( STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:4: STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, STORE_COLUMNS, self.FOLLOW_STORE_COLUMNS_in_store_columns_action303)

                self.match(self.input, LP, self.FOLLOW_LP_in_store_columns_action305)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:21: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:22: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action310)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:30: ( COMMA x+= TEXT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == COMMA) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:84:31: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store_columns_action313)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action317)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop7





                self.match(self.input, RP, self.FOLLOW_RP_in_store_columns_action322)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:91:1: cast_action : CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP ;
    def cast_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:92:2: ( CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:93:2: CAST_COLUMN LP x= TEXT RIGHT_ARROW y= TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action339)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action341)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_cast_action345)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action347)

                y = self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action351)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action353)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:97:1: create_literal_action : CREATE_LITERAL LP x= TEXT RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:98:2: ( CREATE_LITERAL LP x= TEXT RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:99:2: CREATE_LITERAL LP x= TEXT RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action370)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action372)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_create_literal_action376)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action378)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action380)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action384)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action386)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:103:1: deduplicate_action : DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT ;
    def deduplicate_action(self, ):
        y = None
        z = None
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:104:2: ( DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:2: DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action402)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action404)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:17: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:18: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action409)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:26: ( COMMA x+= TEXT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == COMMA) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:105:27: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action412)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action416)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop8





                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action421)

                self.match(self.input, ORDER_BY, self.FOLLOW_ORDER_BY_in_deduplicate_action423)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action427)

                z = self.match(self.input, SORT, self.FOLLOW_SORT_in_deduplicate_action431)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:113:1: rename_action : RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:114:2: ( RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:115:2: RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action449)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action451)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action455)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action457)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action461)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action463)

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
    FOLLOW_NEWLINE_in_startRule56 = frozenset([15, 19])
    FOLLOW_action_in_startRule62 = frozenset([15, 19])
    FOLLOW_NEWLINE_in_startRule68 = frozenset([15])
    FOLLOW_EOF_in_startRule73 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition88 = frozenset([5])
    FOLLOW_CL_in_source_definition90 = frozenset([28])
    FOLLOW_TEXT_in_source_definition94 = frozenset([14])
    FOLLOW_LP_in_source_definition96 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_source_definition100 = frozenset([22])
    FOLLOW_RP_in_source_definition102 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition122 = frozenset([5])
    FOLLOW_CL_in_destination_definition124 = frozenset([28])
    FOLLOW_TEXT_in_destination_definition128 = frozenset([14])
    FOLLOW_LP_in_destination_definition130 = frozenset([12])
    FOLLOW_FILE_FORMAT_in_destination_definition134 = frozenset([22])
    FOLLOW_RP_in_destination_definition136 = frozenset([1, 18])
    FOLLOW_OVERWRITE_in_destination_definition140 = frozenset([1])
    FOLLOW_PLUS_in_action161 = frozenset([4, 8, 9, 13, 17, 20, 26])
    FOLLOW_rename_action_in_action166 = frozenset([15])
    FOLLOW_cast_action_in_action172 = frozenset([15])
    FOLLOW_create_literal_action_in_action178 = frozenset([15])
    FOLLOW_deduplicate_action_in_action184 = frozenset([15])
    FOLLOW_store_columns_action_in_action190 = frozenset([15])
    FOLLOW_from_unixtime_action_in_action196 = frozenset([15])
    FOLLOW_output_partitions_action_in_action202 = frozenset([15])
    FOLLOW_set_in_action211 = frozenset([1])
    FOLLOW_FROM_UNIXTIME_in_from_unixtime_action233 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action235 = frozenset([11])
    FOLLOW_EPOCH_FORMAT_in_from_unixtime_action239 = frozenset([22])
    FOLLOW_RP_in_from_unixtime_action241 = frozenset([14])
    FOLLOW_LP_in_from_unixtime_action243 = frozenset([28])
    FOLLOW_TEXT_in_from_unixtime_action247 = frozenset([22])
    FOLLOW_RP_in_from_unixtime_action249 = frozenset([1])
    FOLLOW_OUTPUT_PARTITIONS_in_output_partitions_action268 = frozenset([14])
    FOLLOW_LP_in_output_partitions_action270 = frozenset([28])
    FOLLOW_TEXT_in_output_partitions_action275 = frozenset([6, 22])
    FOLLOW_COMMA_in_output_partitions_action278 = frozenset([28])
    FOLLOW_TEXT_in_output_partitions_action282 = frozenset([6, 22])
    FOLLOW_RP_in_output_partitions_action287 = frozenset([1])
    FOLLOW_STORE_COLUMNS_in_store_columns_action303 = frozenset([14])
    FOLLOW_LP_in_store_columns_action305 = frozenset([28])
    FOLLOW_TEXT_in_store_columns_action310 = frozenset([6, 22])
    FOLLOW_COMMA_in_store_columns_action313 = frozenset([28])
    FOLLOW_TEXT_in_store_columns_action317 = frozenset([6, 22])
    FOLLOW_RP_in_store_columns_action322 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action339 = frozenset([14])
    FOLLOW_LP_in_cast_action341 = frozenset([28])
    FOLLOW_TEXT_in_cast_action345 = frozenset([21])
    FOLLOW_RIGHT_ARROW_in_cast_action347 = frozenset([29])
    FOLLOW_TYPE_in_cast_action351 = frozenset([22])
    FOLLOW_RP_in_cast_action353 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action370 = frozenset([14])
    FOLLOW_LP_in_create_literal_action372 = frozenset([28])
    FOLLOW_TEXT_in_create_literal_action376 = frozenset([22])
    FOLLOW_RP_in_create_literal_action378 = frozenset([14])
    FOLLOW_LP_in_create_literal_action380 = frozenset([27])
    FOLLOW_STRING_in_create_literal_action384 = frozenset([22])
    FOLLOW_RP_in_create_literal_action386 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action402 = frozenset([14])
    FOLLOW_LP_in_deduplicate_action404 = frozenset([28])
    FOLLOW_TEXT_in_deduplicate_action409 = frozenset([6, 22])
    FOLLOW_COMMA_in_deduplicate_action412 = frozenset([28])
    FOLLOW_TEXT_in_deduplicate_action416 = frozenset([6, 22])
    FOLLOW_RP_in_deduplicate_action421 = frozenset([16])
    FOLLOW_ORDER_BY_in_deduplicate_action423 = frozenset([28])
    FOLLOW_TEXT_in_deduplicate_action427 = frozenset([24])
    FOLLOW_SORT_in_deduplicate_action431 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action449 = frozenset([14])
    FOLLOW_LP_in_rename_action451 = frozenset([28])
    FOLLOW_TEXT_in_rename_action455 = frozenset([21])
    FOLLOW_RIGHT_ARROW_in_rename_action457 = frozenset([28])
    FOLLOW_TEXT_in_rename_action461 = frozenset([22])
    FOLLOW_RP_in_rename_action463 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
