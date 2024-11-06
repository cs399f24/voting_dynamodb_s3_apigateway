API_ID=$(aws apigateway get-rest-apis --query "items[?name=='VotesAPI'].id" --output text)
aws apigateway delete-rest-api --rest-api-id  $API_ID;
