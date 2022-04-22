# $ANTLR 3.5.1 /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g 2022-04-22 13:03:55

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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CAST_COLUMN", "CL", "COMMA", "COMMENT", "CREATE_LITERAL", "DEDUPLICATE", 
    "DESTINATION", "FILE_FORMAT", "LP", "ORDER_BY", "RENAME_COLUMN", "RIGHT_ARROW", 
    "RP", "SC", "SORT", "SOURCE", "STORE_COLUMNS", "STRING", "TEXT", "TYPE", 
    "WS"
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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:22:1: startRule : source_definition destination_definition ( action SC )* EOF ;
    def startRule(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:2: ( source_definition destination_definition ( action SC )* EOF )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:23:4: source_definition destination_definition ( action SC )* EOF
                pass 
                self._state.following.append(self.FOLLOW_source_definition_in_startRule50)
                self.source_definition()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_destination_definition_in_startRule54)
                self.destination_definition()

                self._state.following.pop()

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:25:3: ( action SC )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 in {CAST_COLUMN, CREATE_LITERAL, DEDUPLICATE, RENAME_COLUMN, STORE_COLUMNS}) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:25:4: action SC
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_startRule59)
                        self.action()

                        self._state.following.pop()

                        self.match(self.input, SC, self.FOLLOW_SC_in_startRule61)


                    else:
                        break #loop1


                self.match(self.input, EOF, self.FOLLOW_EOF_in_startRule67)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "startRule"



    # $ANTLR start "source_definition"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:29:1: source_definition : SOURCE CL source= TEXT LP format= FILE_FORMAT RP ;
    def source_definition(self, ):
        source = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:30:2: ( SOURCE CL source= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:31:4: SOURCE CL source= TEXT LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, SOURCE, self.FOLLOW_SOURCE_in_source_definition82)

                self.match(self.input, CL, self.FOLLOW_CL_in_source_definition84)

                source = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_source_definition88)

                self.match(self.input, LP, self.FOLLOW_LP_in_source_definition90)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_source_definition94)

                self.match(self.input, RP, self.FOLLOW_RP_in_source_definition96)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:35:1: destination_definition : DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP ;
    def destination_definition(self, ):
        destination = None
        format = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:36:2: ( DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:37:4: DESTINATION CL destination= TEXT LP format= FILE_FORMAT RP
                pass 
                self.match(self.input, DESTINATION, self.FOLLOW_DESTINATION_in_destination_definition116)

                self.match(self.input, CL, self.FOLLOW_CL_in_destination_definition118)

                destination = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_destination_definition122)

                self.match(self.input, LP, self.FOLLOW_LP_in_destination_definition124)

                format = self.match(self.input, FILE_FORMAT, self.FOLLOW_FILE_FORMAT_in_destination_definition128)

                self.match(self.input, RP, self.FOLLOW_RP_in_destination_definition130)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:1: action : ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action );
    def action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:42:9: ( rename_action | cast_action | create_literal_action | deduplicate_action | store_columns_action )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 in {RENAME_COLUMN}:
                    alt2 = 1
                elif LA2 in {CAST_COLUMN}:
                    alt2 = 2
                elif LA2 in {CREATE_LITERAL}:
                    alt2 = 3
                elif LA2 in {DEDUPLICATE}:
                    alt2 = 4
                elif LA2 in {STORE_COLUMNS}:
                    alt2 = 5
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:43:3: rename_action
                    pass 
                    self._state.following.append(self.FOLLOW_rename_action_in_action150)
                    self.rename_action()

                    self._state.following.pop()


                elif alt2 == 2:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:44:3: cast_action
                    pass 
                    self._state.following.append(self.FOLLOW_cast_action_in_action156)
                    self.cast_action()

                    self._state.following.pop()


                elif alt2 == 3:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:45:3: create_literal_action
                    pass 
                    self._state.following.append(self.FOLLOW_create_literal_action_in_action162)
                    self.create_literal_action()

                    self._state.following.pop()


                elif alt2 == 4:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:46:3: deduplicate_action
                    pass 
                    self._state.following.append(self.FOLLOW_deduplicate_action_in_action168)
                    self.deduplicate_action()

                    self._state.following.pop()


                elif alt2 == 5:
                    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:47:3: store_columns_action
                    pass 
                    self._state.following.append(self.FOLLOW_store_columns_action_in_action174)
                    self.store_columns_action()

                    self._state.following.pop()



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "action"



    # $ANTLR start "store_columns_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:51:1: store_columns_action : STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ;
    def store_columns_action(self, ):
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:2: ( STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:4: STORE_COLUMNS LP (x+= TEXT ( COMMA x+= TEXT )* ) RP
                pass 
                self.match(self.input, STORE_COLUMNS, self.FOLLOW_STORE_COLUMNS_in_store_columns_action188)

                self.match(self.input, LP, self.FOLLOW_LP_in_store_columns_action190)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:21: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:22: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action195)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:30: ( COMMA x+= TEXT )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == COMMA) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:52:31: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_store_columns_action198)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_store_columns_action202)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop3





                self.match(self.input, RP, self.FOLLOW_RP_in_store_columns_action207)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:59:1: cast_action : CAST_COLUMN LP TEXT RP LP TYPE RIGHT_ARROW TYPE RP ;
    def cast_action(self, ):
        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:60:2: ( CAST_COLUMN LP TEXT RP LP TYPE RIGHT_ARROW TYPE RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:61:2: CAST_COLUMN LP TEXT RP LP TYPE RIGHT_ARROW TYPE RP
                pass 
                self.match(self.input, CAST_COLUMN, self.FOLLOW_CAST_COLUMN_in_cast_action224)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action226)

                self.match(self.input, TEXT, self.FOLLOW_TEXT_in_cast_action228)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action230)

                self.match(self.input, LP, self.FOLLOW_LP_in_cast_action232)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action234)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_cast_action236)

                self.match(self.input, TYPE, self.FOLLOW_TYPE_in_cast_action238)

                self.match(self.input, RP, self.FOLLOW_RP_in_cast_action240)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "cast_action"



    # $ANTLR start "create_literal_action"
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:64:1: create_literal_action : CREATE_LITERAL LP x= TEXT RP LP y= STRING RP ;
    def create_literal_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:65:2: ( CREATE_LITERAL LP x= TEXT RP LP y= STRING RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:66:2: CREATE_LITERAL LP x= TEXT RP LP y= STRING RP
                pass 
                self.match(self.input, CREATE_LITERAL, self.FOLLOW_CREATE_LITERAL_in_create_literal_action254)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action256)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_create_literal_action260)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action262)

                self.match(self.input, LP, self.FOLLOW_LP_in_create_literal_action264)

                y = self.match(self.input, STRING, self.FOLLOW_STRING_in_create_literal_action268)

                self.match(self.input, RP, self.FOLLOW_RP_in_create_literal_action270)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:70:1: deduplicate_action : DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT ;
    def deduplicate_action(self, ):
        y = None
        z = None
        x = None
        list_x = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:71:2: ( DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:2: DEDUPLICATE LP (x+= TEXT ( COMMA x+= TEXT )* ) RP ORDER_BY y= TEXT z= SORT
                pass 
                self.match(self.input, DEDUPLICATE, self.FOLLOW_DEDUPLICATE_in_deduplicate_action286)

                self.match(self.input, LP, self.FOLLOW_LP_in_deduplicate_action288)

                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:17: (x+= TEXT ( COMMA x+= TEXT )* )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:18: x+= TEXT ( COMMA x+= TEXT )*
                pass 
                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action293)
                if list_x is None:
                    list_x = []
                list_x.append(x)


                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:26: ( COMMA x+= TEXT )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COMMA) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:72:27: COMMA x+= TEXT
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_deduplicate_action296)

                        x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action300)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        break #loop4





                self.match(self.input, RP, self.FOLLOW_RP_in_deduplicate_action305)

                self.match(self.input, ORDER_BY, self.FOLLOW_ORDER_BY_in_deduplicate_action307)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_deduplicate_action311)

                z = self.match(self.input, SORT, self.FOLLOW_SORT_in_deduplicate_action315)

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
    # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:80:1: rename_action : RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP ;
    def rename_action(self, ):
        x = None
        y = None

        try:
            try:
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:81:2: ( RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP )
                # /Users/alessandro/Universita/LFC-progetto/DataStandardizer/resources/Spark.g:82:2: RENAME_COLUMN LP x= TEXT RIGHT_ARROW y= TEXT RP
                pass 
                self.match(self.input, RENAME_COLUMN, self.FOLLOW_RENAME_COLUMN_in_rename_action333)

                self.match(self.input, LP, self.FOLLOW_LP_in_rename_action335)

                x = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action339)

                self.match(self.input, RIGHT_ARROW, self.FOLLOW_RIGHT_ARROW_in_rename_action341)

                y = self.match(self.input, TEXT, self.FOLLOW_TEXT_in_rename_action345)

                self.match(self.input, RP, self.FOLLOW_RP_in_rename_action347)

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



 

    FOLLOW_source_definition_in_startRule50 = frozenset([10])
    FOLLOW_destination_definition_in_startRule54 = frozenset([4, 8, 9, 14, 20])
    FOLLOW_action_in_startRule59 = frozenset([17])
    FOLLOW_SC_in_startRule61 = frozenset([4, 8, 9, 14, 20])
    FOLLOW_EOF_in_startRule67 = frozenset([1])
    FOLLOW_SOURCE_in_source_definition82 = frozenset([5])
    FOLLOW_CL_in_source_definition84 = frozenset([22])
    FOLLOW_TEXT_in_source_definition88 = frozenset([12])
    FOLLOW_LP_in_source_definition90 = frozenset([11])
    FOLLOW_FILE_FORMAT_in_source_definition94 = frozenset([16])
    FOLLOW_RP_in_source_definition96 = frozenset([1])
    FOLLOW_DESTINATION_in_destination_definition116 = frozenset([5])
    FOLLOW_CL_in_destination_definition118 = frozenset([22])
    FOLLOW_TEXT_in_destination_definition122 = frozenset([12])
    FOLLOW_LP_in_destination_definition124 = frozenset([11])
    FOLLOW_FILE_FORMAT_in_destination_definition128 = frozenset([16])
    FOLLOW_RP_in_destination_definition130 = frozenset([1])
    FOLLOW_rename_action_in_action150 = frozenset([1])
    FOLLOW_cast_action_in_action156 = frozenset([1])
    FOLLOW_create_literal_action_in_action162 = frozenset([1])
    FOLLOW_deduplicate_action_in_action168 = frozenset([1])
    FOLLOW_store_columns_action_in_action174 = frozenset([1])
    FOLLOW_STORE_COLUMNS_in_store_columns_action188 = frozenset([12])
    FOLLOW_LP_in_store_columns_action190 = frozenset([22])
    FOLLOW_TEXT_in_store_columns_action195 = frozenset([6, 16])
    FOLLOW_COMMA_in_store_columns_action198 = frozenset([22])
    FOLLOW_TEXT_in_store_columns_action202 = frozenset([6, 16])
    FOLLOW_RP_in_store_columns_action207 = frozenset([1])
    FOLLOW_CAST_COLUMN_in_cast_action224 = frozenset([12])
    FOLLOW_LP_in_cast_action226 = frozenset([22])
    FOLLOW_TEXT_in_cast_action228 = frozenset([16])
    FOLLOW_RP_in_cast_action230 = frozenset([12])
    FOLLOW_LP_in_cast_action232 = frozenset([23])
    FOLLOW_TYPE_in_cast_action234 = frozenset([15])
    FOLLOW_RIGHT_ARROW_in_cast_action236 = frozenset([23])
    FOLLOW_TYPE_in_cast_action238 = frozenset([16])
    FOLLOW_RP_in_cast_action240 = frozenset([1])
    FOLLOW_CREATE_LITERAL_in_create_literal_action254 = frozenset([12])
    FOLLOW_LP_in_create_literal_action256 = frozenset([22])
    FOLLOW_TEXT_in_create_literal_action260 = frozenset([16])
    FOLLOW_RP_in_create_literal_action262 = frozenset([12])
    FOLLOW_LP_in_create_literal_action264 = frozenset([21])
    FOLLOW_STRING_in_create_literal_action268 = frozenset([16])
    FOLLOW_RP_in_create_literal_action270 = frozenset([1])
    FOLLOW_DEDUPLICATE_in_deduplicate_action286 = frozenset([12])
    FOLLOW_LP_in_deduplicate_action288 = frozenset([22])
    FOLLOW_TEXT_in_deduplicate_action293 = frozenset([6, 16])
    FOLLOW_COMMA_in_deduplicate_action296 = frozenset([22])
    FOLLOW_TEXT_in_deduplicate_action300 = frozenset([6, 16])
    FOLLOW_RP_in_deduplicate_action305 = frozenset([13])
    FOLLOW_ORDER_BY_in_deduplicate_action307 = frozenset([22])
    FOLLOW_TEXT_in_deduplicate_action311 = frozenset([18])
    FOLLOW_SORT_in_deduplicate_action315 = frozenset([1])
    FOLLOW_RENAME_COLUMN_in_rename_action333 = frozenset([12])
    FOLLOW_LP_in_rename_action335 = frozenset([22])
    FOLLOW_TEXT_in_rename_action339 = frozenset([15])
    FOLLOW_RIGHT_ARROW_in_rename_action341 = frozenset([22])
    FOLLOW_TEXT_in_rename_action345 = frozenset([16])
    FOLLOW_RP_in_rename_action347 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SparkLexer", SparkParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
