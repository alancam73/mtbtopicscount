# Status reporting lambda - checks how many articles are left in the JSON file 
# for each user

from __future__ import with_statement
import boto3
import json
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import argparse



# main lambda function handler
def lambda_handler(event, context):
   
   # allow local Python execution testing as well as Lambda env
   execEnv = str(os.getenv('AWS_EXECUTION_ENV'))
   if execEnv.startswith("AWS_Lambda"):
      print("In lambda context...")
   else:
      print("In python CLI context...")
   
   client=boto3.client('dynamodb')
   
   # Note - item_count updates approximately every 6 hours
   articleTblName = 'mtbTopics-Articles-Topics'
   response = client.describe_table(TableName=articleTblName)
   item_ct = response['Table']['ItemCount']
   
   print("Num articles in ", articleTblName, " : ", item_ct)
   
   
   # now get the articlesPushedCt for each userId
   articlesPushedName = 'mtbTopics-Users-ArticlesPushed'
   response = client.scan(TableName=articlesPushedName,
                          ProjectionExpression='userId,articlesPushedCt')['Items']

   for user in response:

      if user['userId']['S'] and int(user['articlesPushedCt']['N']) > 0:
         print("User: ", user['userId']['S'], " has ", user['articlesPushedCt']['N'], " pushed articles")
   
   
   return None



# allow local Python execution testing
if __name__ == '__main__':
    lambda_handler(None,None)
