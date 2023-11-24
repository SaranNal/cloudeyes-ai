import scripts.aggregate_billing as aggregate_billing
import scripts.aggregate_utilization as aggregate_utilization
import scripts.aggregate_security_recommendation as aggregate_security_recommendation
import os

print("Processing aggregate billing data...")
os._exit()
aggregate_billing()
print("Processing aggregate utilization data...")
aggregate_utilization()
print("Processing aggregate security and recommendation data...")
aggregate_security_recommendation()
