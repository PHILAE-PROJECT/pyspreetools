from agilkia import TraceSet
from pathlib import Path
traceset = TraceSet.load_from_json(Path('../data/spree_5000_session_wo_responses_agilkia.json'))
traceset2 = traceset.with_traces_grouped_by("sessionID", property=True)

list_of_traces=[]
for tr in traceset2.traces[1:5]:
    list_of_traces.append([ev.action for ev in tr.events])

print(list_of_traces)