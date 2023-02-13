# Status reporting lambda - checks how many articles are left in the JSON file 
# for each user

from __future__ import with_statement
import boto3
import json
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import argparse



dynamodbtbl=boto3.resource('dynamodb')

articleTblName = 'mtbTopics-Articles-Topics'
articles_table = dynamodbtbl.Table(articleTblName)

articlesPushedName = 'mtbTopics-Users-ArticlesPushed'
pushed_table = dynamodbtbl.Table(articlesPushedName)



# main lambda function handler
def lambda_handler(event, context):
   
   # allow local Python execution testing as well as Lambda env
   execEnv = str(os.getenv('AWS_EXECUTION_ENV'))
   if execEnv.startswith("AWS_Lambda"):
      print("In lambda context...")
   else:
      print("In python CLI context...")
   
   # Note - item_count updates approximately every 6 hours
   print("Num articles in ", articleTblName, " : ", articles_table.item_count)
   
   # now get the articlesPushedCt for each userId
   response = pushed_table.scan(ProjectionExpression='userId,articlesPushedCt')['Items']

   for user in response:
      keys = user.keys()
      if user['userId'] and int(user['articlesPushedCt']) > 0:
         print("User: ", user['userId'], " has ", user['articlesPushedCt'], " pushed articles")
   
   return None       



# allow local Python execution testing
if __name__ == '__main__':
    lambda_handler(None,None)
