
Welcome file

# spree-tools
## data
This directory contains simulated user sessions realized on the spree storefront API
https://api.spreecommerce.org/docs/api-v2/YXBpOjMxMjQ5NjA-storefront-api
 - spree_400-steps_w_responses.json : 400 events from 20~ sessions with responses
 - spree_5000_session_wo_responses_agilkia.json : 5000 sessions without responses in agilkia format
 - spree_5000_sessions_wo_responses.json : 5000 sessions, raw format
 
 ## pyspree
 Python bindings around storefront API to generate a simulated dataset of users sessions
## dataset2agilkia.py
Convert a raw spree simulated user sessions file into an agilkia file, translating http request into domain-knowledge action
For example :

> Post '*/api/v2/storefront/account/addresses'* is converted into
> "*CreateAnAddress*"

Code snippet :
 

       import json  
        from pyspreetools.dataset2agilkia import read_traces_dictionary  
        f = open('pyspreetools/data/spree_5000_sessions_wo_responses.json')  
        data = json.load(f)  
        f.close()  
        traceset = read_traces_dictionary(data)  
        print(traceset)  
        traceset.save_to_json(Path("data/spree_5000_session_wo_responses_agilkia.json"))

## samplequality.py
 Every function from this module takes as input an abstract traceset whose format is list_of_list or a GROUPED agilkia.Traceset object.  
   
 code snippet : 
 

     from pyspreetools.samplequality import executability  
      
    from agilkia import TraceSet  
    from pathlib import Path  
    traceset=TraceSet.load_from_json(Path('./pyspreetools/data/spree_5000_session_wo_responses_agilkia.json'))  
    traceset=traceset.with_traces_grouped_by('sessionID',property=True)  
    traceset.traces = traceset.traces[1:5]  
    print(executability(traceset))  
    list_of_traces=[['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'addAnItemToCart|200', 'retrieveACart|200', 'setLineItemQuantity|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200']]  
    print(executability(list_of_traces))

Each action or event should be encoded in this fashion *action+separative_token+return_code*

`Executability` takes as input an abstract traceset and return the executability of the traceset : How many traces are well formed and can be executed as successful tests on the spree api.


## simulation.py
Script to generate fake user session on the spree API.
The state machine of the simulation is described in pypree/UserSimulator.py
Code snippet : 

    from pyspreetools.simulation import simulation  
      
    config_dict = {  
        "base_url": "https://demo.spreecommerce.org/",  
      "logging": True,  
      "log_file": "./logs/log.json",  
      "test_mode": True,  
      "verbose": False,  
      "sleep_time": 0.2  
    }  
      
    simulation(config_dict=config_dict,number_of_sessions=2)


spree-tools
data

This directory contains simulated user sessions realized on the spree storefront API
https://api.spreecommerce.org/docs/api-v2/YXBpOjMxMjQ5NjA-storefront-api

    spree_400-steps_w_responses.json : 400 events from 20~ sessions with responses
    spree_5000_session_wo_responses_agilkia.json : 5000 sessions without responses in agilkia format
    spree_5000_sessions_wo_responses.json : 5000 sessions, raw format

pyspree

Python bindings around storefront API to generate a simulated dataset of users sessions
dataset2agilkia.py

Convert a raw spree simulated user sessions file into an agilkia file, translating http request into domain-knowledge action
For example :

    Post '/api/v2/storefront/account/addresses’ is converted into
    “CreateAnAddress”

Code snippet :

   import json  
    from pyspreetools.dataset2agilkia import read_traces_dictionary  
    f = open('pyspreetools/data/spree_5000_sessions_wo_responses.json')  
    data = json.load(f)  
    f.close()  
    traceset = read_traces_dictionary(data)  
    print(traceset)  
    traceset.save_to_json(Path("data/spree_5000_session_wo_responses_agilkia.json"))

samplequality.py

Every function from this module takes as input an abstract traceset whose format is list_of_list or a GROUPED agilkia.Traceset object.

code snippet :

 from pyspreetools.samplequality import executability  
  
from agilkia import TraceSet  
from pathlib import Path  
traceset=TraceSet.load_from_json(Path('./pyspreetools/data/spree_5000_session_wo_responses_agilkia.json'))  
traceset=traceset.with_traces_grouped_by('sessionID',property=True)  
traceset.traces = traceset.traces[1:5]  
print(executability(traceset))  
list_of_traces=[['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'addAnItemToCart|200', 'retrieveACart|200', 'setLineItemQuantity|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200']]  
print(executability(list_of_traces))

Each action or event should be encoded in this fashion action+separative_token+return_code

Executability takes as input an abstract traceset and return the executability of the traceset : How many traces are well formed and can be executed as successful tests on the spree api.
simulation.py

Script to generate fake user session on the spree API.
The state machine of the simulation is described in pypree/UserSimulator.py
Code snippet :

from pyspreetools.simulation import simulation  
  
config_dict = {  
    "base_url": "https://demo.spreecommerce.org/",  
  "logging": True,  
  "log_file": "./logs/log.json",  
  "test_mode": True,  
  "verbose": False,  
  "sleep_time": 0.2  
}  
  
simulation(config_dict=config_dict,number_of_sessions=2)

Markdown 4144 bytes 290 words 70 lines Ln 52, Col 16
HTML 3574 characters 279 words 51 paragraphs
