from .replay.replayer import OneTraceExecutor
from .replay.pyspree.SpreeAPIManager import SpreeAPIManager
from agilkia import TraceSet
from tqdm import tqdm
def executability(traceset_grouped,separative_token='|'):
    errors = 0
    executed_sessions = 0
    error_keys = []
    config_dict = {
        "base_url": "https://demo.spreecommerce.org/",
        "logging": False,
        "log_file": "./logs/log.json",
        "test_mode": False,
        "verbose": False,
        "sleep_time": 0.2
    }
    list_of_traces = []

    if type(traceset_grouped) == TraceSet:
        # print("detected traceset")
        for tr in traceset_grouped:
            list_of_traces.append([(ev.action.split(separative_token)[0],ev.action.split(separative_token)[1]) for ev in tr.events])
    elif type(traceset_grouped)==list and type(traceset_grouped[0])==list:
        for trace in traceset_grouped:
            list_of_traces.append([(ev.split(separative_token)[0],ev.split(separative_token)[1]) for ev in trace])
    else:
        raise ValueError("traceset_grouped should be an agilkia trace or a list of list")

    sam = SpreeAPIManager(config_dict=config_dict)
    for seq in tqdm(list_of_traces,desc="Replaying of "+str(len(list_of_traces))+" traces..."):
        o = OneTraceExecutor()
        o.setUp(sam)
        o.SEQ = seq
        try:
            o.test_one_trace_as_test()
            executed_sessions += 1
        except:

            error_keys.append(tr[0].meta_data.get('sessionID'))
            errors += 1

    return executed_sessions


if __name__ == '__main__':
    from pathlib import Path
    traceset=TraceSet.load_from_json(Path('data/spree_5000_session_wo_responses_agilkia.json'))
    traceset=traceset.with_traces_grouped_by('sessionID',property=True)
    traceset.traces = traceset.traces[1:5]
    print(executability(traceset))
    list_of_traces=[['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'addAnItemToCart|200', 'retrieveACart|200', 'setLineItemQuantity|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200']]
    print(executability(list_of_traces))