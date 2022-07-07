import json
from pyspreetools.dataset2agilkia import read_raw_logs,read_traces_dictionary
raw_data=read_raw_logs("./logs/log_07_07_2022__10_23_12.json")
traceset=read_traces_dictionary(raw_data,with_responses=True)
traceset2 = traceset.with_traces_grouped_by("sessionID", property=True)
for tr in traceset2:
    print([ev.action for ev in tr.events])
    print([ev.outputs.keys() for ev in tr.events])