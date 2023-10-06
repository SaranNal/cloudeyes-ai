import random
from datetime import datetime, timedelta
import numpy as np
import json
from app.db_utility import insert_data_customer_db


# Function to generate random data for a specific metric on a given date
def generate_metric_data(data_type):
    if (data_type == "int"):
        return random.randint(1, 100)
    if (data_type == "double"):
        return round(random.uniform(1, 100), 2)

# Function to generate the entire data structure with the specified date


def generate_data_structure(date, metric_data):
    date_key = date.strftime("%m/%d/%Y")
    data = {
        "account_id": metric_data["account_id"],
        "date": date,
        "EFS": {
            "PercentIOLimit": {
                date_key: generate_metric_data('int')
            },
            "StorageBytes": {
                date_key: generate_metric_data('double')
            }
        },
        "S3": {
            metric_data['bucket_name']: {
                "BucketSizeBytes": {
                    date_key: generate_metric_data('double')
                },
                "NumberOfObjects": {
                    date_key: generate_metric_data('int')
                },
                "4xxErrors": {
                    date_key: generate_metric_data('int')
                },
                "5xxErrors": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "app_runner": {
            "CPUUtilization": {
                date_key: generate_metric_data('double')
            },
            "MemoryUtilization": {
                date_key: generate_metric_data('double')
            },
            "RequestLatency": {
                date_key: generate_metric_data('double')
            },
            "2xxStatusResponses": {
                date_key: generate_metric_data('int')
            },
            "4xxStatusResponses": {
                date_key: generate_metric_data('int')
            },
            "5xxStatusResponses": {
                date_key: generate_metric_data('int')
            }
        },
        "RDS": {
            metric_data['db_instance_identifier']: {
                "FreeableMemory": {
                    date_key: generate_metric_data('double')
                },
                "CPUUtilization": {
                    date_key: generate_metric_data('double')
                },
                "DatabaseConnections": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "elasticache": {
            metric_data['cache_cluster_id']: {
                "CacheHitRate": {
                    date_key: generate_metric_data('int')
                },
                "DatabaseCapacityUsagePercentage": {
                    date_key: generate_metric_data('double')
                },
                "DatabaseMemoryUsagePercentage": {
                    date_key: generate_metric_data('double')
                },
                "EngineCPUUtilization": {
                    date_key: generate_metric_data('double')
                }
            }
        },
        "dynamoDB": {
            metric_data["table_name"]: {
                "SystemErrors": {
                    date_key: generate_metric_data('int')
                },
                "UserErrors": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "cloudfront": {
            metric_data["distribution_id"]: {
                "4xxErrorRate": {
                    date_key: generate_metric_data('int')
                },
                "5xxErrorRate": {
                    date_key: generate_metric_data('int')
                },
                "Requests": {
                    date_key: generate_metric_data('int')
                },
                "TotalErrorRate": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "api_gateway": {
            metric_data["api_name"]: {
                "4xxError": {
                    date_key: generate_metric_data('int')
                },
                "5xxError": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "batch": {
            metric_data["job_queue_name"]: {
                "CpuUtilized": {
                    date_key: generate_metric_data('double')
                },
                "MemoryUtilized": {
                    date_key: generate_metric_data('double')
                },
                "JobCount": {
                    date_key: generate_metric_data('int')
                },
                "ContainerInstanceCount": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "lambda": {
            metric_data["function_name"]: {
                "Invocations": {
                    date_key: generate_metric_data('int')
                },
                "Duration": {
                    date_key: generate_metric_data('double')
                },
                "Errors": {
                    date_key: generate_metric_data('int')
                }
            }
        },
        "ec2": {
            metric_data["instance_id"]: {
                "CPUUtilization": {
                    date_key: generate_metric_data('double')
                },
                "NetworkIn": {
                    date_key: generate_metric_data('double')
                },
                "NetworkOut": {
                    date_key: generate_metric_data('double')
                }
            }
        },
        "elb": {
            metric_data["load_balancer_name"]: {
                "RequestCount": {
                    date_key: generate_metric_data('int')
                },
                "RejectedConnectionCount": {
                    date_key: generate_metric_data('int')
                },
                "HTTPCode_ELB_4XX_Count": {
                    date_key: generate_metric_data('int')
                },
                "HTTPCode_ELB_5XX_Count": {
                    date_key: generate_metric_data('int')
                }
            }
        }
    }
    return data


metric_data = {}
metric_data['bucket_name'] = "cloud-bucket-dev"
metric_data['db_instance_identifier'] = "db-instance-identifier"
metric_data['cache_cluster_id'] = "cache-cluster-id"
metric_data["table_name"] = "table-name"
metric_data["distribution_id"] = "distribution-id"
metric_data["api_name"] = "api-name"
metric_data["job_queue_name"] = "job-queue-name"
metric_data["function_name"] = "function-name"
metric_data["instance_id"] = "instance-id"
metric_data["load_balancer_name"] = "load-balancer-name"


start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 9, 30)
date_range = np.arange(start_date, end_date,
                       timedelta(days=1)).astype(datetime)

customer_ids = {
    "3dff95c1-12ff-48f9-9464-02e609bba998": "124dea25-9888-2123-9600-cvbcxb265676",
    "dde7e592-80a0-420a-ad82-df2dd6b6322b": "ac96551d-32ce-4010-ba1b-c86fc586c317",
    "602fbb3a-b688-4893-be3c-34bf26e80f8f": "bf3a79b1-9fa4-46ad-93e2-4d82912f281c",
    "7c2620c3-c1a3-484a-8f44-9298cd534d0d": "918ea26e-e482-428d-93b8-594f9c9f9038"
}

for customer_id, account_id in customer_ids.items():
    metric_data["account_id"] = account_id

    daily_utilization_data = []
    print('----------------------------{}----------------------------'.format(customer_id))
    for date in date_range:
        # Generate the data structure for the specified date
        final_metric_data = generate_data_structure(date, metric_data)
        daily_utilization_data.append(final_metric_data)
        # print('Daily utilization data: {}'.format(
        #     json.dumps(daily_utilization_data)))
    insert_data_customer_db(
        customer_id, 'daily_utilization', daily_utilization_data)
