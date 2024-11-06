import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

response = client.create_rest_api(
    name='VotesAPI',
    description='API to tally votes.',
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    }
)
api_id = response["id"]

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]

results = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='results'
)
results_resource_id = results["id"]


results_method = client.put_method(
    restApiId=api_id,
    resourceId=results_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

results_response = client.put_method_response(
    restApiId=api_id,
    resourceId=results_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

results_integration = client.put_integration(
    restApiId=api_id,
    resourceId=results_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


results_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=results_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "yes": 10,
            "no": 5               
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)





vote_resource = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='vote'
)
vote_resource_id = vote_resource["id"]



vote_method = client.put_method(
    restApiId=api_id,
    resourceId=vote_resource_id,
    httpMethod='POST',
    authorizationType='NONE'
)

vote_response = client.put_method_response(
    restApiId=api_id,
    resourceId=vote_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': False,
        'method.response.header.Access-Control-Allow-Origin': False,
        'method.response.header.Access-Control-Allow-Methods': False
    },
    responseModels={
        'application/json': 'Empty'
    }
)


vote_integration = client.put_integration(
    restApiId=api_id,
    resourceId=vote_resource_id,
    httpMethod='POST',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)


vote_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=vote_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'POST\'',
        'method.response.header.Access-Control-Allow-Origin': '\'*\''
    },
    responseTemplates={
        "application/json": json.dumps({
            "yes": 20,
            "no": 10               
        })
    }
)


print ("DONE")
