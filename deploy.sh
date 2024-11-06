API_ID=$(aws apigateway get-rest-apis --query "items[?name=='VotesAPI'].id" --output text)
aws apigateway create-deployment --rest-api-id $API_ID --stage-name prod

