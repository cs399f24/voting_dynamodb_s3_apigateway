API_ID=$(aws apigateway get-rest-apis --query "items[?name=='VotesAPI'].id" --output text)
BASE_URL="https://$API_ID.execute-api.us-east-1.amazonaws.com/prod"

GET_URL="$BASE_URL/results"
echo $GET_URL
curl $GET_URL
echo

POST_URL="$BASE_URL/vote"
echo $POST_URL
curl -X POST -H "Content-Type: application/json" -d '{"vote": "yes"}' $POST_URL
curl -i -X OPTIONS -H "Content-Type: application/json" -d '{"vote": "yes"}' $POST_URL
echo
