#!/bin/bash

# Add AWS Elastic Beanstalk deployment commands here
eb create my-flask-app-staging --region ap-south-1
eb deploy my-flask-app-staging --region ap-south-1
