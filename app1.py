from chalice import Chalice
app = Chalice(app_name='UrlShortener')

@app.route('/')
def index():
    return {'hello': 'world'}

import os
import boto3
import hashlib

from chalice import Chalice,Response,BadRequestError
from chalice import NotFoundError

# setup

app= Chalice(app_name='url Shortener')
app.debug = True

DDB = boto3.client('dynamodb')

@app.route('/', methods=['POST'])
def shorten():
    # Grab request url
    url = app.current_request.json_body.get('url','')
    if not url:
        raise BadRequestError("Missing URL")
    digest = hashlib.md5(url).hexdigest()[:6]
    #store in dynamodb
    DDB.put_item(
        TableName=os.environ['APP_Table_Name'],
        Item={'identifier':{'S":digest},
              'url':{'S':url}}})
    return {'shortenec:digest}

@app.route('/{identifier}', methods=['Get'])
def retrieve(identifier):
            #retrieve url from dynamodb
            try:
                record = DDB.get_item(key={'identifier': {'S': identifier}}
                                      Tablename=os.environ['APP_Table_Name'])
            except Exception as e:
                rasie NotFound Error(identifier)
            return Response(
                status_code=301,
                headers={'Location': record['Item']['ur;']['S']},
                body='')
            
                        
            
                            
            
            
            
            
                            
                
                             
        

        
