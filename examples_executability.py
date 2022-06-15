from pyspreetools.samplequality import executability

from agilkia import TraceSet
from pathlib import Path
traceset=TraceSet.load_from_json(Path('./pyspreetools/data/spree_5000_session_wo_responses_agilkia.json'))
traceset=traceset.with_traces_grouped_by('sessionID',property=True)
traceset.traces = traceset.traces[1:5]
print(executability(traceset))
list_of_traces=[['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'addAnItemToCart|200', 'retrieveACart|200', 'setLineItemQuantity|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllTaxons|200'], ['createACart|201', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllProducts_SpecificTaxonFilter|200', 'retrieveAProduct|200', 'listAllTaxons|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'retrieveAProduct|200', 'listAllProducts_SpecificTaxonFilter_SortByPrice|200', 'listAllTaxons|200']]
print(executability(list_of_traces))
