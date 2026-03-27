import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
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

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1774136854776 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://satisfactory-energy-data-lake/raw/energy_charts/price/"], "recurse": True}, transformation_ctx="AmazonS3_node1774136854776")

# Script generated for node SQL Query
SqlQuery7 = '''
SELECT
    *,
    to_timestamp(unix_seconds) as datetime,
    year(to_timestamp(unix_seconds)) as year,
    month(to_timestamp(unix_seconds)) as month,
    day(to_timestamp(unix_seconds)) as day,
    from_utc_timestamp(now(), 'Europe/Paris') AS ingestion_date
FROM myDataSource
'''
SQLQuery_node1774137477314 = sparkSqlQuery(glueContext, query = SqlQuery7, mapping = {"myDataSource":AmazonS3_node1774136854776}, transformation_ctx = "SQLQuery_node1774137477314")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=SQLQuery_node1774137477314, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1774219319534", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1774222592174 = glueContext.write_dynamic_frame.from_options(frame=SQLQuery_node1774137477314, connection_type="s3", format="glueparquet", connection_options={"path": "s3://satisfactory-energy-data-lake/curated/energy_charts/price/", "partitionKeys": ["year", "month", "day"]}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1774222592174")

job.commit()