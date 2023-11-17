import scripts.aggregate_billing as aggregate_billing
import scripts.aggregate_utilization as aggregate_utilization

print("Processing aggregate billing data...")
aggregate_billing.aggregate_timeseries()
print("Processing aggregate utilization data...")
aggregate_utilization.aggregate_timeseries()
