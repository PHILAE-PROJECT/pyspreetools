import json
import agilkia
from pathlib import Path
from .replay.utils_translation import translation
import datetime

# Opening JSON file
# f = open('data/spree_5000_sessions_wo_responses.json')
# data = json.load(f)
# f.close()

def read_raw_logs(filepath):


    data = {}
    with open(filepath) as f:
        for i,line in enumerate(f):
            if i==0:
                continue
            data[i]=(json.loads(line))
    return data

def read_traces_dictionary(data,with_responses=False, sep='|') -> agilkia.TraceSet:
    # print("now=", datetime.now().timestamp())

    trace1 = agilkia.Trace([])
    for t, session in data.items():
        # we ignore the line id.

        timestamp = datetime.datetime.today().isoformat('|')
        sessionID = session['session_id']
        url = session['url']
        method = session['method']
        headers = session['headers']
        status_code = str(session['status_code'])

        # now we identify the main action, inputs, outputs, etc.

        inputs = {
            "method": method,

            "headers": headers,
            "url": url
        }
        try:
            inputs['body'] = session['body']
        except:
            inputs['body'] = {}


        others = {
            'timestamp': timestamp,
            'sessionID': sessionID,
        }

        action_name = translation(url, method, inputs['body'])
        action = action_name + sep + status_code

        outputs = {"Status": status_code}
        outputs['responses']={}
        if with_responses:
            try:
                outputs['responses']=session['responses']
            except:
                pass
        event = agilkia.Event(action, inputs, outputs, others)
        trace1.append(event)
    traceset = agilkia.TraceSet([])
    traceset.append(trace1)
    return traceset


