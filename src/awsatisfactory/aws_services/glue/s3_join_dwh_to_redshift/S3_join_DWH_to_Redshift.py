import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1774136854776 = glueContext.create_dynamic_frame.from_options(format_options={}, connection_type="s3", format="parquet", connection_options={"paths": ["s3://satisfactory-energy-data-lake/curated/energy_charts/price/"], "recurse": True}, transformation_ctx="AmazonS3_node1774136854776")

# Script generated for node Amazon Redshift
AmazonRedshift_node1774263541366 = glueContext.create_dynamic_frame.from_options(connection_type="redshift", connection_options={"\"dbtable\"": "\"(SELECT unix_seconds FROM awsatisfactory.energy_prices) as t\"", "redshiftTmpDir": "s3://satisfactory-energy-data-lake/staging/temp/", "useConnectionProperties": "true", "dbtable": "awsatisfactory.energy_prices", "connectionName": "Redshift connection"}, transformation_ctx="AmazonRedshift_node1774263541366")

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1774263820162 = ApplyMapping.apply(frame=AmazonRedshift_node1774263541366, mappings=[("unix_seconds", "long", "unix_seconds", "long"), ("price", "double", "price", "double"), ("datetime", "timestamp", "datetime", "timestamp"), ("year", "int", "year", "int"), ("month", "int", "month", "int"), ("day", "int", "day", "int"), ("ingestion_date", "timestamp", "ingestion_date", "timestamp")], transformation_ctx="RenamedkeysforJoin_node1774263820162")

# Script generated for node Join
AmazonS3_node1774136854776DF = AmazonS3_node1774136854776.toDF()
RenamedkeysforJoin_node1774263820162DF = RenamedkeysforJoin_node1774263820162.toDF()
Join_node1774263600640 = DynamicFrame.fromDF(AmazonS3_node1774136854776DF.join(RenamedkeysforJoin_node1774263820162DF, (AmazonS3_node1774136854776DF['unix_seconds'] == RenamedkeysforJoin_node1774263820162DF['unix_seconds']), "leftanti"), glueContext, "Join_node1774263600640")

# Script generated for node SQL Query
SqlQuery13 = '''
select
    unix_seconds,
    price,
    datetime,
    year(datetime) as year,
    month(datetime) as month,
    day(datetime) as day,
    from_utc_timestamp(now(), 'Europe/Paris') AS ingestion_date
from myDataSource
'''
SQLQuery_node1774264063764 = sparkSqlQuery(glueContext, query = SqlQuery13, mapping = {"myDataSource":Join_node1774263600640}, transformation_ctx = "SQLQuery_node1774264063764")

# Script generated for node Change Schema
ChangeSchema_node1774273551912 = ApplyMapping.apply(frame=SQLQuery_node1774264063764, mappings=[("unix_seconds", "int", "unix_seconds", "bigint"), ("price", "double", "price", "double"), ("datetime", "timestamp", "datetime", "timestamp"), ("year", "int", "year", "int"), ("month", "int", "month", "int"), ("day", "int", "day", "int"), ("ingestion_date", "timestamp", "ingestion_date", "timestamp")], transformation_ctx="ChangeSchema_node1774273551912")

# Script generated for node Amazon Redshift
AmazonRedshift_node1774264148793 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1774273551912, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://satisfactory-energy-data-lake/staging/temp/", "useConnectionProperties": "true", "dbtable": "awsatisfactory.energy_prices", "connectionName": "Redshift connection", "preactions": "CREATE TABLE IF NOT EXISTS awsatisfactory.energy_prices (unix_seconds VARCHAR, price DOUBLE PRECISION, datetime TIMESTAMP, year INTEGER, month INTEGER, day INTEGER, ingestion_date TIMESTAMP);"}, transformation_ctx="AmazonRedshift_node1774264148793")

job.commit()