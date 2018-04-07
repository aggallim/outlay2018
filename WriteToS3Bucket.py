
import boto3
import re
import os
from io import StringIO
import pandas as pd
from sagemaker import get_execution_role

#Reading the file
role=get_execution_role()
region = boto3.Session().region_name
#FilePath====> s3://<databucket>/dataset/hackathon_credit.txt
location='<File_Path_to_Read>'
data=pd.read_csv(location, sep='\t',nrows=1000,encoding='UTF-16')

# Adding file to S3 bucket

bucket='<your_data_bucket>'
project_key='<file_to_write>'

csv_buffer = StringIO()
# Setting the sep to | so it can be read by Quicksight.
data.to_csv(csv_buffer,sep='|')
s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, project_key).put(Body=csv_buffer.getvalue())
