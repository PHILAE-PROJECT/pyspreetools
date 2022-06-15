import json
import agilkia
from pyspreetools.dataset2agilkia import read_traces_dictionary
f = open('pyspreetools/data/spree_5000_sessions_wo_responses.json')
data = json.load(f)
f.close()
traceset = read_traces_dictionary(data)
print(traceset)
# traceset.save_to_json(Path("data/spree_5000_session_wo_responses_agilkia.json"))