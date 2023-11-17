import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_database
import app.helper as helper
import sys

metadata = helper.retrieve_file_n_decode(sys)

ec2_attributes = ["intelTurboAvailable", "memory", "dedicatedEbsThroughput", "vcpu", "storage", "instanceFamily", "operatingSystem",
                  "physicalProcessor", "clockSpeed", "ecu", "networkPerformance", "gpuMemory", "tenancy", "processorArchitecture"]
rds_attributes = ["instanceTypeFamily", "memory", "vcpu", "storage", "instanceFamily", "databaseEngine", "databaseEdition",
                  "physicalProcessor", "licenseModel", "currentGeneration", "networkPerformance", "processorArchitecture"]


def dict_helper(): return defaultdict(dict_helper)


final_metadata = []
generic_metadata = dict_helper()
for instance_name, metadatas in metadata.items():
    generic_metadata[instance_name]['productFamily'] = metadatas['product']['productFamily']
    attributes = ec2_attributes if metadatas['product']['productFamily'] == 'Compute Instance' else rds_attributes
    for attribute in ec2_attributes:
        if attribute in metadatas['product']['attributes']:
            generic_metadata[instance_name][attribute] = metadatas['product']['attributes'][attribute]
    for term_type, term_details in metadatas['terms'].items():
        for term_id, price_details in term_details.items():
            for price_id, price_detail in price_details['priceDimensions'].items():
                generic_metadata[instance_name]['pricing'][term_type][term_id][price_id]['unit'] = price_detail['unit']
                generic_metadata[instance_name]['pricing'][term_type][term_id][price_id]['description'] = price_detail['description']
                generic_metadata[instance_name]['pricing'][term_type][term_id][price_id]['price'] = price_detail['pricePerUnit']['USD']

final_metadata.append(generic_metadata)
admin_db = get_database('admin')
print('Generic metadata: {}'.format(
    json.dumps(final_metadata)))
generic_metadata_collection = admin_db['generic_metadata']
result = generic_metadata_collection.insert_many(final_metadata)
print('Mongo insertion id: {}'.format(result.inserted_ids))
print('--------------------------------------------------------')
metadata = helper.move_processed_fie(sys)
