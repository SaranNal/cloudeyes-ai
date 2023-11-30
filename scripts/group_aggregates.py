from scripts.aggregate_billing import aggregate_billing
from scripts.aggregate_utilization import aggregate_utilization
from scripts.aggregate_security_recommendation import aggregated_security_recommendation

print("Processing aggregate billing data...")
aggregate_billing()
print("Processing aggregate utilization data...")
aggregate_utilization()
print("Processing aggregate security and recommendation data...")
aggregated_security_recommendation()
