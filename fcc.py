import json
import requests
import time

from settings import *
import database as db

offset = db.init() + 1

def getnames(obj):
    try:
        return obj['filers'][0].get('name', 'null')
    except (IndexError, KeyError) as err:
        return 'null'

def getsubkey(obj, parent, key):
    try:
        return obj[parent].get(key, 'null')
    except (KeyError, AttributeError) as err:
        return 'null'

while True:
    print (offset)
    response = requests.get(api_url + f"&offset={offset}" + f"&limit={limit}")
    try:
        json_obj = json.loads(response.content.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        print ("Something went wrong, waiting 3 minutes. Server response below:")
        print (response)
        time.sleep(180)
        continue

    if len(json_obj['filings']) == 0:
        break

    for i in json_obj['filings']:
        data_form = {
        'id_submission': i.get('id_submission', 'null'),
        'name': getnames(i),
        'addressA': getsubkey(i, 'addressentity', 'address_line_1'),
        'addressB': getsubkey(i, 'addressentity', 'address_line_2'),
        'city': getsubkey(i, 'addressentity', 'city'),
        'state': getsubkey(i, 'addressentity', 'state'),
        'zip': getsubkey(i, 'addressentity', 'zip_code'),
        'comment_text': i.get('text_data', 'null'),
        'email': i.get('contact_email', 'null'),
        'submission_date': i.get('date_submission', 'null'),
        'dissemination_date': i.get('date_disseminated', 'null'),
        }
        db.insert(data_form)

    db.commit()
    offset += limit

db.close()
