import json
def results2executability(path,sep='|'):
    formatted_dict={}
    with open(path) as json_file:
        dict_sessions = dict(json.load(json_file))

    for i_seq,seq in enumerate(dict_sessions["results"][0]):
        print(seq)
        formatted_seq=seq[0].split(' ')[0:-1]
        # print(formatted_seq)
        # formatted_seq=[(elt.split(sep)[0],elt.split(sep)[1]) for elt in formatted_seq]
        formatted_seq=[(elt.split(sep)[0],elt.split(sep)[1]) for elt in formatted_seq]

        formatted_dict['session'+str(i_seq)]=formatted_seq
    return formatted_dict

if __name__=='__main__':
    from agilkia import TraceSet
    from pathlib import Path
    tr=TraceSet.load_from_json(Path('../data/spree_5000_session_wo_responses_agilkia.json'))

    dict_results={}
    dict_results['results']=[[]]
    tr2=tr.with_traces_grouped_by('sessionID',property=True)
    for trace in tr2.traces[1:10]:
        seq = ""

        for ev in trace.events[:]:
            seq+=(ev.action+" ")

        dict_results['results'][0].append([seq,0.001])

    with open("../data/results.json", "w") as outfile:
        json.dump(dict_results, outfile)
    results2executability('../data/results.json')