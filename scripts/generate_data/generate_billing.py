import random
from datetime import datetime, timedelta
import numpy as np
import json
from app.db_utility import insert_data_customer_db


# Function to generate random data for a specific metric on a given date
def generate_billing(data_type):
    if (data_type == "int"):
        return random.randint(1, 100)
    if (data_type == "double"):
        return round(random.uniform(1, 100), 2)

# Function to generate the entire data structure with the specified date


def generate_data_structure(date, account_id):
    # date_key = date.strftime("%m/%d/%Y")
    data = {
        "account_id": account_id,
        "date": date,
        "billing": {
            "AWS CloudTrail": generate_billing("double"),
            "AWS Config": generate_billing("double"),
            "AWS Cost Explorer": generate_billing("double"),
            "AWS Global Accelerator": generate_billing("double"),
            "AWS Glue": generate_billing("double"),
            "AWS Lambda": generate_billing("double"),
            "AWS Step Functions": generate_billing("double"),
            "AWS X-Ray": generate_billing("double"),
            "Amazon API Gateway": generate_billing("double"),
            "Amazon CloudFront": generate_billing("double"),
            "Amazon EC2 Container Registry (ECR)": generate_billing("double"),
            "EC2 - Other": generate_billing("double"),
            "Amazon Elastic Compute Cloud - Compute": generate_billing("double"),
            "Amazon Elastic Container Service": generate_billing("double"),
            "Amazon Elastic Load Balancing": generate_billing("double"),
            "Amazon Inspector": generate_billing("double"),
            "Amazon QuickSight": generate_billing("double"),
            "Amazon Relational Database Service": generate_billing("double"),
            "Amazon Route 53": generate_billing("double"),
            "Amazon Simple Email Service": generate_billing("double"),
            "Amazon Simple Notification Service": generate_billing("double"),
            "Amazon Simple Queue Service": generate_billing("double"),
            "Amazon Simple Storage Service": generate_billing("double"),
            "Amazon Virtual Private Cloud": generate_billing("double"),
            "AmazonCloudWatch": generate_billing("double"),
            "CloudWatch Events": generate_billing("double")
        }
    }
    return data


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
    daily_billing_data = []
    for date in date_range:
        # Generate the data structure for the specified date
        billing_data = generate_data_structure(date, account_id)
        daily_billing_data.append(billing_data)

    insert_data_customer_db(customer_id, 'daily_billing', daily_billing_data)
