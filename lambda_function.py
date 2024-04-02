import json
from matrix_utils import *

def lambda_handler(event, context):
    # TODO implement
    print("Event Data -------->", event)
    transposed_matrix = transpose_matrix(event)
    print(transposed_matrix)
    return {
        'statusCode': 200,
        'body': json.dumps('This is how Lambda layers work')
    }
