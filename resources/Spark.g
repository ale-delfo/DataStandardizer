grammar Spark;

options {
  language = Python3;
  k = 1;
}

@header {
	from Standardizer import Standardizer
}

@members {
	standardizer = Standardizer()
	def getStandardizer(self):
	    return self.standardizer
}


// Specifica del parser
startRule
	:	source_definition
		destination_definition
		(action SC)*
		//EOF
	;
	
source_definition
	:
	  SOURCE CL source=TEXT LP format=FILE_FORMAT RP
	  {self.standardizer.setSource($source.text, $format.text)}
	;

destination_definition
	:	
	  DESTINATION CL destination=TEXT LP format=FILE_FORMAT RP
	  {self.standardizer.setDestination($destination.text, $format.text)}

	;
	
action 	:
		rename_action |
		cast_action |
		create_literal_action |
		deduplicate_action |
		store_columns_action
	;
	
	
//from_unixtime_action
//	:	FROM_UNIXTIME LP x=TEXT RP 
//	

store_columns_action
	:	STORE_COLUMNS LP (x+=TEXT (COMMA x+=TEXT)*) RP
		{
		list = [tk.text for tk in $x]
		self.standardizer.columnsToStore = list
		}
	;

cast_action
	:	
	CAST_COLUMN LP x=TEXT RIGHT_ARROW y=TYPE RP
	{self.standardizer.addAction(self.standardizer.castColumn,$x.text,$y.text)}
	;
	
create_literal_action
	:	
	CREATE_LITERAL LP x=TEXT RP LP y=STRING RP
	{self.standardizer.addAction(self.standardizer.createLiteral,$x.text,$y.text)}
	;
	
deduplicate_action
	:
	DEDUPLICATE LP (x+=TEXT (COMMA x+=TEXT)*) RP ORDER_BY y=TEXT z=SORT
	{
	list = [tk.text for tk in $x]
	self.standardizer.addAction(self.standardizer.deduplicate,list,$y.text,$z.text)
	}
	;
	

rename_action
	:	
	RENAME_COLUMN LP x=TEXT RIGHT_ARROW y=TEXT RP
	{self.standardizer.addAction(self.standardizer.renameColumn,$x.text,$y.text)}
	;

// Specifica del lexer

COMMA	:	',';

SORT 	:	'ASC' | 'DESC' | 'asc' | 'desc' ;

TYPE 	:	'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' ;

ORDER_BY
	:	'order by';

STORE_COLUMNS
	:	'StoreColumns';

RENAME_COLUMN
	:	'RenameColumn';

CAST_COLUMN
	:	'Cast';
	
CREATE_LITERAL
	:	'CreateLiteral'
	;
	
DEDUPLICATE
	:	'Deduplicate';
	
// Specifica del lexer
CL	:	':';
LP	:	'(';
RP	:	')';
SC 	:	';';

RIGHT_ARROW
	:	'->' ;

FILE_FORMAT 
	:	'parquet'
	|	'csv'
	|	'json'
	|	'avro'
	;
	

SOURCE	:	'Source';

DESTINATION
	:	'Destination';

COMMENT
    :   '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    |   '/*' ( options {greedy=false;} : . )* '*/' {$channel=HIDDEN;}
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;}
    ;
    
    
TEXT    :	('0'..'9'|'a'..'z'|'A'..'Z'|'-'|'_'|'/'|'|'|'.')+
        ;
    
STRING 	:	'"' ( options {greedy=false;} : . )* '"' ;
