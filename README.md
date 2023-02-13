# mtbtopicscount
Counts the number of articles in the DynamoDB table versus total pushed to each user

## Overview
Simple python lambda to count the total number of articles in the Article DynamoDB table
versus the number of articles total pushed to each user. 
Main goal is to ensure there is sufficient buffer of articles still to serve up to users

This repository is part of the https://www.articles.mtbtopics.com/ overall functionality

## Dependencies
This code can standalone and be re-used & modified for any use-case in querying DynamoDB tables

However it is part of the functionality of the MTB Topics app which also has the following repositories: -
* https://github.com/alancam73/mtbarticlesapp - Amplify app with Auth & Lambda. UI via Figma
* https://github.com/alancam73/mtbtopicsarticles - Lambda to send new MTB article via AWS SES to active users every 24h
* https://github.com/alancam73/mtbtopicsload - Lambda to load up new Youtube URLs for article pushing

## Versions
This code was tested with python 3.9