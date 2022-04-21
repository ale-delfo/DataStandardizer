from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

#--------------------------
# General action definition 
#--------------------------

class Action:
    def __init__(self, function, *args):
        self.function = function
        self.args = args

class Standardizer:

    actions = []
    normalizeColumns = False

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
        print('Execute method')
        self.spark = SparkSession.builder.getOrCreate()
        self.readDataFrame()
        for action in self.actions:
            action.function(*action.args)
        if self.normalizeColumns or self.destination_format == 'parquet':
            print('Normalizing activated')
            self.normalizeColumns()
        self.writeDataFrame()

    #--------------------------
    # Actions methods 
    #--------------------------

    def createLiteral(self, *args):
        print(f'Create literal column {args[0]} with content {args[1]}')
        self.df = self.df.withColumn(args[0], lit(args[1].replace('"','')))

    def renameColumn(self, *args):
        print(f'Renaming columng {args[0]} to {args[1]}')
        self.df = self.df.withColumnRenamed(args[0], args[1])

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
