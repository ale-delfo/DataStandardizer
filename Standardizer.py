from mimetypes import types_map
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, desc, asc, row_number, col 
from pyspark.sql.types import IntegerType, FloatType, DoubleType, StringType
from pyspark.sql import Window

#--------------------------
# General action definition 
#--------------------------

class Action:
    def __init__(self, function, *args):
        self.function = function
        self.args = args

typesMap = {
    "INT": IntegerType,
    "FLOAT": FloatType,
    "DOUBLE": DoubleType,
    "STRING": StringType
}

class Standardizer:

    actions = []
    columnsToStore = '*'

    #--------------------------
    # Core methods 
    #--------------------------

    def setSource(self, source, format):
        self.source = source
        self.source_format = format

    def setDestination(self, destination, format):
        self.destination = destination
        self.destination_format = format

    def addAction(self, action, *args):
        self.actions.append(Action(action,*args))

    def getActions(self):
        return self.actions
    
    def readDataFrame(self):
        self.df = self.spark.read.format(self.source_format).option('header',True).load(self.source)

    def writeDataFrame(self):
        self.df.repartition(1).write.format(self.destination_format).save(self.destination)

    def normalizeColumns(self):
        for column in self.df.columns:
            self.df = self.df.withColumnRenamed(column, column.replace(' ','_'))

    def execute(self):
        print('Executing actions...')
        self.spark = SparkSession.builder.getOrCreate()
        self.readDataFrame()
        self.normalizeColumns()
        for action in self.actions:
            action.function(*action.args)
        self.storeColumns()
        self.writeDataFrame()
        print('Done.')

    #--------------------------
    # Actions methods 
    #--------------------------

    def createLiteral(self, *args):
        print(f'Create literal column {args[0]} with content {args[1]}')
        self.df = self.df.withColumn(args[0], lit(args[1].replace('"','')))

    def renameColumn(self, *args):
        print(f'Renaming column {args[0]} to {args[1]}')
        self.df = self.df.withColumnRenamed(args[0], args[1])

    def deduplicate(self, *args):
        columns = args[0]
        ordering_column = args[1]
        orientation = args[2]
        if orientation in ['desc','DESC']:
            window = Window.partitionBy(columns).orderBy(desc(ordering_column))
        else:
            window = Window.partitionBy(columns).orderBy(asc(ordering_column))
        print(f'Deduplicating dataframe with same {args[0]} columns ordering by {args[1]} orientation {args[2]}')
        self.df = self.df.withColumn('rank', row_number().over(window)).where('rank = 1').drop('rank')

    def storeColumns(self, *args):
        print(f'Storing columns {self.columnsToStore}')
        self.df = self.df.select(self.columnsToStore)

    def castColumn(self, *args):
        print(f'Casting column {args[0]} to {args[1]}')
        type = args[1]
        self.df = self.df.withColumn(args[0], col(args[0]).cast(typesMap[type]()))

    #--------------------------
    # Utils methods 
    #--------------------------
    
    def toString(self):
        print(f'Standardizer source {self.source}')
        print(f'Standardizer source format {self.source_format}')
        print(f'Standardizer destination {self.destination}')
        print(f'Standardizer destination format {self.destination_format}')
        print(f'Standardizer actions:')
        i = 1
        for action in self.actions:
                    print(f"{i}. {action.function} - {action.args}")
