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
start 
	:	source_definition
		destination_definition
		(action SC)*
		EOF
	;
	
source_definition
	:
	  SOURCE CL source=PATH LP format=FILE_FORMAT RP
	  {self.standardizer.setSource($source.text, $format.text)}
	;

destination_definition
	:	
	  DESTINATION CL destination=PATH LP format=FILE_FORMAT RP
	  {self.standardizer.setDestination($destination.text, $format.text)}

	;
	
action 	:
		rename_action |
		cast_action |
		create_literal_action |
		deduplicate_action |
		normalize_action
		
	; 
	



cast_action
	:	
	CAST_COLUMN LP ID RP LP TYPE RIGHT_ARROW TYPE RP
	;
	
create_literal_action
	:	
	CREATE_LITERAL LP x=ID RP LP y=STRING RP
	{self.standardizer.addAction(self.standardizer.createLiteral,$x.text,$y.text)}
	;
	
deduplicate_action
	:
	DEDUPLICATE LP ID (COMMA ID)* RP
	;
	

rename_action
	:	
	RENAME_COLUMN LP x=ID RIGHT_ARROW y=ID RP
	{self.standardizer.addAction(self.standardizer.renameColumn,$x.text,$y.text)}
	;
	
normalize_action
	:	NORMALIZE_COLUMNS
	{self.standardizer.normalizeColumns=True}
	;

// Specifica del lexer

COMMA	:	',';

TYPE 	:	'INT' | 'FLOAT' | 'DOUBLE' | 'STRING' ;

UNIX_TIME_UNIT
	:	's' | 'm' | 'n' ;

RENAME_COLUMN
	:	'RenameColumn';

CAST_COLUMN
	:	'Cast';
	
CREATE_LITERAL
	:	'CreateLiteral'
	;
	
DEDUPLICATE
	:	'Deduplicate';
	
NORMALIZE_COLUMNS
	:	
	'Normalize'
	;

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
    
STRING 	:	'"' ( options {greedy=false;} : . )* '"' ;

ID  :	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*  ;

PATH  :	('a'..'z'|'A'..'Z'|'_'|'/'|'.'|'-') ('a'..'z'|'A'..'Z'|'0'..'9'|'_'|'/'|'.'|'-')*  ;