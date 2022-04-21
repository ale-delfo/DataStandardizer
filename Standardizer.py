from pyspark.sql import SparkSession

class Standardizer:
    def __init__(self):
        pass
    
    def setSource(self, source):
        self.source = source

    def execute(self):
        print('Execute method')
        spark = SparkSession.builder.getOrCreate()