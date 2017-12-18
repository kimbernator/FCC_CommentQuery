import json
import requests

from settings import *
import database as db

offset = db.init() + 1
entryid = offset

def getnames(obj):
    try:
        return obj['filers'][0].get('name', 'null')
    except IndexError:
        return 'null'

while True:
    print (offset)
    response = requests.get(api_url + f"&offset={offset}" + f"&limit={limit}")
    json_obj = json.loads(response.content.decode('utf-8'))
    if len(json_obj['filings']) == 0:
        break

    for i in json_obj['filings']:
        data_form = {
        'id': entryid,
        'id_submission': i.get('id_submission', 'null'),
        'name': getnames(i),
        'addressA': i['addressentity'].get('address_line_1', 'null'),
        'addressB': i['addressentity'].get('address_line_2', 'null'),
        'city': i['addressentity'].get('city', 'null'),
        'state': i['addressentity'].get('state', 'null'),
        'zip': i['addressentity'].get('zip_code', 'null'),
        'comment_text': i.get('text_data', 'null'),
        'email': i.get('contact_email', 'null'),
        'submission_date': i.get('date_submission', 'null'),
        'dissemination_date': i.get('date_disseminated', 'null'),
        }
        db.insert(data_form)
        entryid += 1

    db.commit()
    offset += limit

db.close()
