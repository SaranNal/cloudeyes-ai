import random
from datetime import datetime, timedelta
import numpy as np
import json
from app.db_utility import insert_data_customer_db


def generate_data_structure(account_id):
    """Function to generate the recommendations based on account_id"""
    data = {
        "account_id": account_id,
        "recommendations": {
            "security": [
                {
                    "id": "rSs93HQwa1",
                    "name": "Amazon RDS Public Snapshots",
                    "description": "Checks the permission settings for your Amazon Relational Database Service (Amazon RDS) DB snapshots and alerts you if any snapshots are marked as public. When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. If you want to share a snapshot with particular users or accounts, mark the snapshot as private, and then specify the user or accounts you want to share the snapshot data with. <h4 class='headerBodyStyle'>Note</h4>: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.<br/><br/>\r\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\r\nRed: The RDS  snapshot is marked as public.<br/><br/>\r\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\r\nUnless you are certain you want to share all the data in the snapshot with all AWS accounts and users, modify the permissions: mark the snapshot as private, and then specify the accounts that you want to give permissions to. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html\" target=\"_blank\">Sharing a DB Snapshot or DB Cluster Snapshot</a>. Note: For temporary technical reasons, items in this check cannot be excluded from view in the Trusted Advisor console.\n\nTo modify permissions for your snapshots directly, you can use a runbook in the AWS Systems Manager console. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-modifyrdssnapshotpermission.html\" target=\"_blank\">AWSSupport-ModifyRDSSnapshotPermission</a>.<br/><br/> \r\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\r\n<a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html\" target=\"_blank\">Backing Up and Restoring Amazon RDS DB Instances</a>",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "DB Instance or Cluster ID",
                            "Snapshot ID"
                    ]
                },
                {
                    "id": "xSqX82fQu",
                    "name": "ELB Security Groups",
                    "description": "Checks for load balancers configured with a missing security group or a security group that allows access to ports that are not configured for the load balancer. If a security group associated with a load balancer is deleted, the load balancer does not work as expected. If a security group allows access to ports that are not configured for the load balancer, the risk of loss of data or malicious attacks increases. <br/><br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: The inbound rules of an Amazon VPC security group associated with a load balancer allow access to ports that are not defined in the load balancer's listener configuration. <br/>\nRed: A security group associated with a load balancer does not exist. <br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nConfigure the security group rules to restrict access to only those ports and protocols that are defined in the load balancer listener configuration, plus the ICMP protocol to support Path MTU Discovery. See <a target=\"_blank\" href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html\">Listeners for Your Classic Load Balancer</a> and <a target=\"_blank\" href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups\">Security Groups for Load Balancers in a VPC</a>.<br/>\nIf a security group is missing, apply a new security group to the load balancer. Create security group rules that restrict access to only those ports and protocols that are defined in the load balancer listener configuration. See <a target=\"_blank\" href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups\">Security Groups for Load Balancers in a VPC</a>. <br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html\">Elastic Load Balancing User Guide</a> <br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-configure-load-balancer.html\">Configure Your Classic Load Balancer</a>",
                    "category": "security",
                    "metadata": [
                            "Region",
                            "Load Balancer Name",
                            "Status",
                            "Security Group IDs",
                            "Reason"
                    ]
                },
                {
                    "id": "N425c450f2",
                    "name": "CloudFront Custom SSL Certificates in the IAM Certificate Store",
                    "description": "Checks the SSL certificates for CloudFront alternate domain names in the IAM certificate store and alerts you if the certificate is expired, will soon expire, uses outdated encryption, or is not configured correctly for the distribution. When a custom certificate for an alternate domain name expires, browsers that display your CloudFront content might show a warning message about the security of your website. Certificates that are encrypted by using the SHA-1 hashing algorithm are being deprecated by web browsers such as Chrome and Firefox.  If a certificate doesn't contain any domain names that match either Origin Domain Name or the domain name in the Host header of viewer requests, CloudFront returns an HTTP status code 502 (bad gateway) to the user. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS\" target=\"_blank\">Using Alternate Domain Names and HTTPS</a>.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: A custom SSL certificate is expired.<br>\nYellow: A custom SSL certificate expires in the next seven days.<br>\nYellow: A custom SSL certificate was encrypted by using the SHA-1 hashing algorithm.<br>\nYellow: One or more of the alternate domain names in the distribution don't appear either in the Common Name field or the Subject Alternative Names field of the custom SSL certificate.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nRenew an expired certificate or a certificate that is about to expire.<br>\nReplace a certificate that was encrypted by using the SHA-1 hashing algorithm with a certificate that is encrypted by using the SHA-256 hashing algorithm.<br>\nReplace the certificate with a certificate that contains the applicable values in the Common Name or Subject Alternative Domain Names fields.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html\" target=\"_blank\">Using an HTTPS Connection to Access Your Objects</a>",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Distribution ID",
                            "Distribution Domain Name",
                            "Certificate Name",
                            "Reason"
                    ]
                },
                {
                    "id": "L4dfs2Q4C5",
                    "name": "AWS Lambda Functions Using Deprecated Runtimes",
                    "description": "Checks for Lambda functions that are configured to use a runtime that is approaching deprecation or is deprecated. Deprecated runtimes are not eligible for security updates or technical support.<br/>\n<h4 class='headerBodyStyle'>Notes:</h4><br>\nResults for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.<br>\nPublished Lambda function versions are immutable, which means they can be invoked but not updated. Only the $LATEST version for a Lambda function can be updated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html\" target=\"_blank\">Lambda function versions</a>.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: The function is running on a runtime that is already deprecated.\n<br>Yellow: The function is running on a runtime that will be deprecated within 120 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nIf you have functions that are running on a runtime that is approaching deprecation, you should prepare for migration to a supported runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html\" target=\"_blank\">Runtime support policy</a>.<br>\nWe recommend that you delete earlier function versions that you’re no longer using.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"http://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\" target=\"_blank\">Lambda runtimes</a>",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Function ARN",
                            "Runtime",
                            "Days to Deprecation",
                            "Deprecation Date",
                            "Average Daily Invokes",
                            "Last Refresh Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G300",
                    "name": "Neptune DB cluster snapshots should be encrypted at rest",
                    "description": "Checks if a Neptune DB cluster snapshot is encrypted at rest. The check fails if a Neptune DB cluster isn't encrypted at rest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.6<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G301",
                    "name": "Neptune DB clusters should have IAM database authentication enabled",
                    "description": "Checks if a Neptune DB cluster has IAM database authentication enabled. The check fails if IAM database authentication isn't enabled for a Neptune DB cluster.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.7<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G302",
                    "name": "Neptune DB clusters should be configured to copy tags to snapshots",
                    "description": "Checks if a Neptune DB cluster is configured to copy tags to snapshots when the snapshots are created. The check fails if a Neptune DB cluster isn't configured to copy tags to snapshots.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.8<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G303",
                    "name": "RDS DB clusters should be encrypted at rest",
                    "description": "Checks if an RDS DB cluster is encrypted at rest. The check fails if an RDS DB cluster isn't encrypted at rest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: RDS.27<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.27/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "a2sEc6ILx",
                    "name": "ELB Listener Security",
                    "description": "Checks for load balancers with listeners that do not use recommended security configurations for encrypted communication. AWS recommends using a secure protocol (HTTPS or SSL), up-to-date security policies, and ciphers and protocols that are secure.<br/>\nWhen you use a secure protocol for a front-end connection (client to load balancer), the requests are encrypted between your clients and the load balancer, which is more secure.<br/>\nElastic Load Balancing provides predefined security policies  with ciphers and protocols that adhere to AWS security best practices. New versions of predefined policies are released as new configurations become available. <br/><br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: A load balancer has no listener that uses a secure protocol (HTTPS or SSL). <br/>\nYellow: A load balancer listener uses an outdated predefined SSL security policy. <br/>\nYellow: A load balancer listener uses a cipher or protocol that is not recommended. <br/>\nRed: A load balancer listener uses an insecure cipher or protocol.<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<ul><li>If the traffic to your load balancer must be secure, use either the HTTPS or the SSL protocol for the front-end connection.</li>\n<li>Upgrade your load balancer to the latest version of the predefined SSL security policy.</li> \n<li>Use only the recommended ciphers and protocols.</li> </ul>\nFor more information, see <a target=\"_blank\" href=\"https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-listener-config.html\">Listener Configurations for Elastic Load Balancing</a>.<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/using-elb-listenerconfig-quickref.html\">Listener Configurations Quick Reference</a><br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ssl-config-update.html\">Update SSL Negotiation Configuration of Your Load Balancer</a><br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-ssl-security-policy.html\">SSL Negotiation Configurations for Elastic Load Balancing</a><br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-security-policy-table.html\">SSL Security Policy Table</a><br/>\n",
                    "category": "security",
                    "metadata": [
                            "Region",
                            "Load Balancer Name",
                            "Load Balancer Port",
                            "Status",
                            "Reason"
                    ]
                },
                {
                    "id": "ePs02jT06w",
                    "name": "Amazon EBS Public Snapshots",
                    "description": "Checks the permission settings for your Amazon Elastic Block Store (Amazon EBS) volume snapshots and alerts you if any snapshots are marked as public. When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. If you want to share a snapshot with particular users or accounts, mark the snapshot as private, and then specify the user or accounts you want to share the snapshot data with. <h4 class='headerBodyStyle'>Note</h4>: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.<br/><br/>\r\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\r\nRed: The EBS volume snapshot is marked as public.<br/><br/>\r\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\r\nUnless you are certain you want to share all the data in the snapshot with all AWS accounts and users, modify the permissions: mark the snapshot as private, and then specify the accounts that you want to give permissions to. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html\" target=\"_blank\">Sharing an Amazon EBS Snapshot</a>. Note: For temporary technical reasons, items in this check cannot be excluded from view in the Trusted Advisor console.\n\nTo modify permissions for your snapshots directly, you can use a runbook in the AWS Systems Manager console. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-modifyebssnapshotpermission.html\" target=\"_blank\">AWSSupport-ModifyEBSSnapshotPermission</a>.<br/><br/> \r\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\r\n<a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html\" target=\"_blank\">Amazon EBS Snapshots</a>",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Volume ID",
                            "Snapshot ID",
                            "Description"
                    ]
                },
                {
                    "id": "Wxdfp4B1L3",
                    "name": "AWS Well-Architected high risk issues for security",
                    "description": "Checks for high risk issues (HRIs) for your workloads in the security pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nRed: At least one active high risk issue was identified in the security pillar for AWS Well-Architected.<br>\nGreen: No active high risk issues were detected in the security pillar for AWS Well-Architected.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nAWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the <a href=\"https://console.aws.amazon.com/wellarchitected\" target=\"blank\">AWS Well-Architected</a> tool to review your answers and take action to resolve your active issues.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Workload ARN",
                            "Workload Name",
                            "Reviewer Name",
                            "Workload Type",
                            "Workload Started Date",
                            "Workload Last Modified Date",
                            "Number of identified HRIs for Security",
                            "Number of HRIs resolved for Security",
                            "Number of questions answered for Security",
                            "Total number of questions in Security pillar",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "vjafUGJ9H0",
                    "name": "AWS CloudTrail Logging",
                    "description": "Checks for your use of AWS CloudTrail. CloudTrail provides increased visibility into activity in your AWS account by recording information about AWS API calls made on the account. You can use these logs to determine, for example, what actions a particular user has taken during a specified time period or which users have taken actions on a particular resource during a specified time period. Because CloudTrail delivers log files to an Amazon Simple Storage Service (Amazon S3) bucket, CloudTrail must have write permissions for the bucket. If a trail applies to all regions (the default when creating a new trail), the trail appears multiple times in the Trusted Advisor report.<br /><br />\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: CloudTrail reports log delivery errors for a trail.<br/>\nRed: A trail has not been created for a region, or logging is turned off for a trail.\n<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nTo create a trail and start logging from the console, go to the <a href=\"https://console.aws.amazon.com/cloudtrail/home\" target=\"_blank\">AWS CloudTrail console</a>. <br/>\nTo start logging, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_using_cli.html#stopstartclil\" target=\"_blank\">Stopping and Starting Logging for a Trail</a>. <br/>\nIf you receive log delivery errors, check to make sure that the bucket exists and that the necessary policy is attached to the bucket; see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_bucket_policy.html\" target=\"_blank\">Amazon S3 Bucket Policy</a>.\n<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br />\n<a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/whatisawscloudtrail.html\" target=\"_blank\">AWS CloudTrail User Guide</a><br/>\n<a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_supported_regions.html\" target=\"_blank\">Supported Regions</a><br/>\n<a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_supported_services.html\" target=\"_blank\">Supported Services</a>",
                    "category": "security",
                    "metadata": [
                            "Region",
                            "Trail Name",
                            "Logging Status",
                            "Bucket Name",
                            "Last Delivery Error",
                            "Status"
                    ]
                },
                {
                    "id": "DqdJqYeRm5",
                    "name": "IAM Access Key Rotation",
                    "description": "Checks for active IAM access keys that have not been rotated in the last 90 days.  When you rotate your access keys regularly, you reduce the chance that a compromised key could be used without your knowledge to access resources. For the purposes of this check, the last rotation date and time is when the access key was created or most recently activated. The access key number and date come from the <h4 class='headerBodyStyle'>access_key_1_last_rotated</h4> and <h4 class='headerBodyStyle'>access_key_2_last_rotated</h4> information in the most recent IAM credential report. Because the regeneration frequency of a credential report  is restricted, refreshing this check might not reflect recent changes (for details, see <a target=\"_blank\" href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html\">Getting Credential Reports for Your AWS Account</a>).<br/>\nIn order to create and rotate access keys, a user must have the appropriate permissions. For more information, see <a target=\"_blank\" href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_delegate-permissions_examples.html#creds-policies-credentials\">Allow Users to Manage Their Own Passwords, Access Keys, and SSH Keys</a>.<br/><br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nGreen: The access key is active and has been rotated in the last 90 days.<br/>\nYellow: The access key is active and has been rotated in the last 2 years, but more than 90 days ago.<br/>\nRed: The access key is active and has not been rotated in the last 2 years.<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nRotate access keys on a regular basis. See <a target=\"_blank\" href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey\">Rotating Access Keys</a> and <a target=\"_blank\" href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html\">Managing Access Keys for IAM Users</a>.<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a target=\"_blank\" href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html\">IAM Best Practices</a><br/>\n<a target=\"_blank\" href=\"https://blogs.aws.amazon.com/security/post/Tx15CIT22V4J8RP/How-to-rotate-access-keys-for-IAM-users\">How to rotate access keys for IAM users</a> (AWS blog)",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "IAM User",
                            "Access Key",
                            "Key Last Rotated",
                            "Reason"
                    ]
                },
                {
                    "id": "7DAFEmoDos",
                    "name": "MFA on Root Account",
                    "description": "Checks the root account and warns if multi-factor authentication (MFA) is not enabled. For increased security, we recommend that you protect your account by using MFA, which requires a user to enter a unique authentication code from their MFA hardware or virtual device when interacting with the AWS console and associated websites.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: MFA is not enabled on the root account.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nLog in to your root account and activate an MFA device. See <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/MFADeviceStatus.html\" target=\"_blank\">Checking MFA Status</a> and <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/MFADeviceSetup.html\" target=\"_blank\">Setting Up an MFA Device</a>.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingMFA.html\" target=\"_blank\">Using Multi-Factor Authentication (MFA) Devices with AWS</a>",
                    "category": "security",
                    "metadata": []
                },
                {
                    "id": "HCP4007jGY",
                    "name": "Security Groups - Specific Ports Unrestricted",
                    "description": "Checks security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data). The ports with highest risk are flagged red, and those with less risk are flagged yellow. Ports flagged green are typically used by applications that require unrestricted access, such as HTTP and SMTP.\n<br>\nIf you have intentionally configured your security groups in this manner, we recommend using additional security measures to secure your infrastructure (such as IP tables).\n<br>\n<br>Note: This check only evaluates security groups that you create and their inbound rules for IPv4 addresses. Security groups created by AWS Directory Services are flagged as red or yellow, but they don’t pose a security risk and can be safely ignored or excluded. For more information, see the <a href=\"https://aws.amazon.com/premiumsupport/faqs/#AWS_Trusted_Advisor\" target=\"_blank\">Trusted Advisor FAQ</a>.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4>\n<br>\nGreen: Access to port 80, 25, 443, or 465 is unrestricted.<br>\nRed: Access to port 20, 21, 1433, 1434, 3306, 3389, 4333, 5432, or 5500 is unrestricted.<br>\nYellow: Access to any other port is unrestricted.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br>\nRestrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (for example, 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html\" target=\"_blank\">Amazon EC2 Security Groups</a><br>\n<a href=\"http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers\" target=\"_blank\">List of TCP and UDP port numbers</a> (Wikipedia)<br>\n<a href=\"http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\" target=\"_blank\">Classless Inter-Domain Routing</a> (Wikipedia)",
                    "category": "security",
                    "metadata": [
                            "Region",
                            "Security Group Name",
                            "Security Group ID",
                            "Protocol",
                            "Status",
                            "Ports"
                    ]
                },
                {
                    "id": "Pfx0RwqBli",
                    "name": "Amazon S3 Bucket Permissions",
                    "description": "Checks buckets in Amazon Simple Storage Service (Amazon S3) that have open access permissions or allow access to any authenticated AWS user. Bucket permissions that grant List access can result in higher than expected charges if objects in the bucket are listed by unintended users at a high frequency. Bucket permissions that grant Upload/Delete access create potential security vulnerabilities by allowing users that to add, modify, or remove items in a bucket.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: The bucket ACL allows List access for \"Everyone\" or \"Any Authenticated AWS User\".<br>\nYellow: A bucket policy allows any kind of open access.<br>\nYellow: Bucket policy has statements that grant public access. The “Block public and cross-account access to buckets that have public policies” setting is turned on and has restricted access to only authorized users of that account until public statements are removed.<br>\nYellow: Trusted Advisor does not have permission to check the policy, or the policy could not be evaluated for other reasons.<br>\nRed: The bucket ACL allows Upload/Delete access for \"Everyone\" or \"Any Authenticated AWS User\".<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nIf a bucket allows open access, determine if open access is truly needed. If not, update the bucket permissions to restrict access to the owner or specific users. Use Amazon S3 Block Public Access to control the settings that allow public access to your data. See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/user-guide/set-permissions.html\" target=\"_blank\">Setting Bucket and Object Access Permissions</a>.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html\" target=\"_blank\">Managing Access Permissions to Your Amazon S3 Resources</a>",
                    "category": "security",
                    "metadata": [
                            "Region Name",
                            "Region API Parameter",
                            "Bucket Name",
                            "ACL Allows List",
                            "ACL Allows Upload/Delete",
                            "Status",
                            "Policy Allows Access",
                            "Ignored Bucket Name"
                    ]
                },
                {
                    "id": "Hs4Ma3G191",
                    "name": "RDS cluster snapshots and database snapshots should be encrypted at rest",
                    "description": "Checks if Amazon RDS cluster snapshots and database snapshots are encrypted.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G192",
                    "name": "RDS DB Instances should prohibit public access, determined by the PubliclyAccessible configuration",
                    "description": "Checks if RDS instances are publicly accessible by evaluating the publiclyAccessible field in the instance configuration item.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G193",
                    "name": "RDS DB instances should have encryption at-rest enabled",
                    "description": "Checks if storage encryption is enabled for your RDS DB instances.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G194",
                    "name": "RDS snapshot should be private",
                    "description": "Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G195",
                    "name": "CloudFront distributions should have origin access identity enabled",
                    "description": "Checks if an Amazon CloudFront distribution with an Amazon S3 origin type has Origin Access Identity (OAI) configured. The check fails if the CloudFront distribution that is backed by Amazon S3 does not have OAI configured.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudFront.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G196",
                    "name": "AWS Config should be enabled",
                    "description": "Checks if the Config service is enabled in the account for the local region and is recording all resources.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Config.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Config.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G197",
                    "name": "Amazon Elasticsearch Service domains should have encryption at-rest enabled",
                    "description": "Checks whether Amazon Elasticsearch Service domains have encryption at rest configuration enabled. This check fails if the EncryptionAtRestOptions field is not enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ES.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ES.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G198",
                    "name": "RDS DB instances should have deletion protection enabled",
                    "description": "Checks if RDS DB instances have deletion protection enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "1iG5NDGVre",
                    "name": "Security Groups - Unrestricted Access",
                    "description": "Checks security groups for rules that allow unrestricted access to a resource. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data).\n<br>\n<br>Note: This check only evaluates security groups that you create and their inbound rules for IPv4 addresses. Security groups created by AWS Directory Services are flagged as red or yellow, but they don’t pose a security risk and can be safely ignored or excluded. For more information, see the <a href=\"https://aws.amazon.com/premiumsupport/faqs/#AWS_Trusted_Advisor\" target=\"_blank\">Trusted Advisor FAQ</a>.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4>\n<br>\nRed: A security group rule has a source IP address with a /0 suffix for ports other than 25, 80, or 443.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br>\nRestrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (for example, 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4>\n<br><a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html\" target=\"_blank\">Amazon EC2 Security Groups</a><br>\n<a href=\"https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\" target=\"_blank\">Classless Inter-Domain Routing</a> (Wikipedia)",
                    "category": "security",
                    "metadata": [
                            "Region",
                            "Security Group Name",
                            "Security Group ID",
                            "Protocol",
                            "Port",
                            "Status",
                            "IP Range"
                    ]
                },
                {
                    "id": "Hs4Ma3G190",
                    "name": "RDS clusters should have deletion protection enabled",
                    "description": "Checks if RDS clusters have deletion protection enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.7<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "nNauJisYIT",
                    "name": "Amazon RDS Security Group Access Risk",
                    "description": "Checks security group configurations for Amazon Relational Database Service (Amazon RDS) and warns when a security group rule might grant overly permissive access to your database. Recommended configuration for any security group rule is to allow access from specific Amazon Elastic Compute Cloud (Amazon EC2) security groups or from a specific IP address.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: A DB security group rule references an Amazon EC2 security group that grants global access on one of these ports: 20, 21, 22, 1433, 1434, 3306, 3389, 4333, 5432, 5500.\n<br>\nYellow: A DB security group rule grants access to more than a single IP address (the CIDR rule suffix is not /0 or /32).\n<br>\nRed: A DB security group rule grants global access (the CIDR rule suffix is /0).\n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nReview your security group rules and restrict access to authorized IP addresses or IP ranges. To edit a security group, use the <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AuthorizeDBSecurityGroupIngress.html\" target=\"_blank\">AuthorizeDBSecurityGroupIngress</a> API or the AWS Management Console. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html\" target=\"_blank\">Working with DB Security Groups</a>.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html\" target=\"_blank\">Amazon RDS Security Groups</a><br>\n<a href=\"https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\" target=\"_blank\">Classless Inter-Domain Routing</a><br>\n<a href=\"https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers\" target=\"_blank\">List of TCP and UDP port numbers</a>",
                    "category": "security",
                    "metadata": [
                            "Region",
                            "RDS Security Group Name",
                            "Ingress Rule",
                            "Status",
                            "Reason"
                    ]
                },
                {
                    "id": "Hs4Ma3G188",
                    "name": "GuardDuty should be enabled",
                    "description": "Checks if Amazon GuardDuty is enabled in your AWS account and region.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: GuardDuty.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/GuardDuty.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G189",
                    "name": "Enhanced monitoring should be configured for RDS DB instances",
                    "description": "Checks if enhanced monitoring is enabled for your RDS DB instances.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G199",
                    "name": "Database logging should be enabled",
                    "description": "Checks if the following Amazon RDS logs are enabled and sent to CloudWatch Logs: Oracle: (Alert, Audit, Trace, Listener), PostgreSQL: (Postgresql, Upgrade), MySQL: (Audit, Error, General, SlowQuery), MariaDB: (Audit, Error, General, SlowQuery), SQL Server: (Error, Agent), Aurora: (Audit, Error, General, SlowQuery), Aurora-MySQL: (Audit, Error, General, SlowQuery), Aurora-PostgreSQL: (Postgresql).<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.9<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.9/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G290",
                    "name": "ElastiCache clusters should not use the default subnet group",
                    "description": "Checks if ElastiCache clusters are configured with a custom subnet group. The check fails for an ElastiCache cluster if 'CacheSubnetGroupName' has the value 'default'.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ElastiCache.7<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElastiCache.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G291",
                    "name": "Elastic Beanstalk should stream logs to CloudWatch",
                    "description": "Checks if an AWS Elastic Beanstalk environment is configured to send logs to CloudWatch Logs. The check fails if the Elastic Beanstalk environment is not configured to send logs to CloudWatch Logs.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ElasticBeanstalk.3<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElasticBeanstalk.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G170",
                    "name": "S3 Block Public Access setting should be enabled",
                    "description": "Checks if the following public access block settings are configured from account level: ignorePublicAcls: True, blockPublicPolicy: True, blockPublicAcls: True, restrictPublicBuckets: True.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G292",
                    "name": "Redshift clusters should be encrypted at rest",
                    "description": "Checks if an Amazon Redshift cluster is encrypted at rest. The check fails if a Redshift cluster isn't encrypted at rest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Redshift.10<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G171",
                    "name": "S3 buckets should prohibit public read access",
                    "description": "Checks if your S3 buckets allow public read access by evaluating the Block Public Access settings, the bucket policy, and the bucket access check list (ACL).<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G293",
                    "name": "Step Functions state machines should have logging turned on",
                    "description": "This controls assesses if an AWS Step Functions state machine has logging turned on. The check fails if a state machine doesn't have logging turned on.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: StepFunctions.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/StepFunctions.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G172",
                    "name": "S3 buckets should prohibit public write access",
                    "description": "Checks if your S3 buckets allow public write access by evaluating the Block Public Access settings, the bucket policy, and the bucket access check list (ACL).<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G294",
                    "name": "Athena workgroups should be encrypted at rest",
                    "description": "Checks if an Athena workgroup is encrypted at rest. The check fails if an Athena workgroup isn’t encrypted at rest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Athena.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Athena.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G173",
                    "name": "S3 Block Public Access setting should be enabled at the bucket-level",
                    "description": "Checks if Amazon S3 buckets have bucket level public access blocks applied. This check fails if any of the bucket level settings are set to \"false\" public: ignorePublicAcls, blockPublicPolicy, blockPublicAcls, restrictPublicBuckets.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G295",
                    "name": "Amazon DocumentDB clusters should be encrypted at rest",
                    "description": "Checks if an Amazon DocumentDB cluster is encrypted at rest. The check fails if an Amazon DocumentDB cluster isn't encrypted at rest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: DocumentDB.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/DocumentDB.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G174",
                    "name": "CodeBuild GitHub or Bitbucket source repository URLs should use OAuth",
                    "description": "Checks if the GitHub or Bitbucket source repository URL contains either personal access tokens or user name and password.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CodeBuild.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CodeBuild.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G296",
                    "name": "Neptune DB clusters should be encrypted at rest",
                    "description": "Checks if a Neptune DB cluster is encrypted at rest. The check fails if a Neptune DB cluster isn't encrypted at rest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G175",
                    "name": "CodeBuild project environment variables should not contain clear text credentials",
                    "description": "Checks if the project contains environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CodeBuild.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CodeBuild.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G297",
                    "name": "Neptune DB clusters should publish audit logs to CloudWatch Logs",
                    "description": "Checks if a Neptune DB cluster publishes audit logs to Amazon CloudWatch Logs. The check fails if a Neptune DB cluster doesn't publish audit logs to CloudWatch Logs. `EnableCloudWatchLogsExport` should be set to Audit.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.2<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G176",
                    "name": "ACM certificates should be renewed after a specified time period",
                    "description": "Checks if ACM Certificates in your account are marked for expiration within a specified time period. Certificates provided by ACM are automatically renewed. ACM does not automatically renew certificates that you import.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ACM.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G287",
                    "name": "ElastiCache replication groups should have encryption-at-rest enabled",
                    "description": "Checks if ElastiCache replication groups have encryption-at-rest enabled. This check fails if encryption-at-rest is not enabled for a ElastiCache replication group.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ElastiCache.4<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElastiCache.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G166",
                    "name": "An RDS event notifications subscription should be configured for critical cluster events",
                    "description": "Checks if an Amazon RDS Event subscription for RDS clusters is configured to notify on event categories of both \"maintenance\" and \"failure\".<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.19<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.19/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G288",
                    "name": "ElastiCache replication groups should have encryption-in-transit enabled",
                    "description": "Checks if ElastiCache replication groups have encryption-in-transit enabled. This check fails if encryption-in-transit is not enabled for a ElastiCache replication group.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ElastiCache.5<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElastiCache.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G167",
                    "name": "S3 buckets should have server-side encryption enabled",
                    "description": "Checks that your Amazon S3 bucket either has Amazon S3 default encryption enabled or that the S3 bucket policy explicitly denies put-object requests without server side encryption.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G289",
                    "name": "ElastiCache replication groups of earlier Redis versions should have Redis AUTH enabled",
                    "description": "Checks if ElastiCache replication groups have Redis AUTH enabled. The check fails for an ElastiCache replication group if the Redis version of its nodes is below 6 and 'AuthToken' is not in use.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ElastiCache.6<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElastiCache.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G168",
                    "name": "S3 buckets should require requests to use Secure Socket Layer",
                    "description": "Checks if S3 buckets have policies that require requests to use Secure Socket Layer (SSL).<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G169",
                    "name": "S3 permissions granted to other AWS accounts in bucket policies should be restricted",
                    "description": "Checks if the S3 bucket policy allows sensitive bucket-level or object-level actions from a principal in another AWS account. The check fails if any of the following actions are allowed in the S3 bucket policy for a principal in another AWS account: s3:DeleteBucketPolicy, s3:PutBucketAcl, s3:PutBucketPolicy, s3:PutObjectAcl, and s3:PutEncryptionConfiguration.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: S3.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G180",
                    "name": "Amazon Elasticsearch Service domain error logging to CloudWatch Logs should be enabled",
                    "description": "Checks whether Amazon Elasticsearch Service domains are configured to send error logs to CloudWatch Logs.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ES.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ES.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G181",
                    "name": "Classic Load Balancers with SSL/HTTPS listeners should use a certificate provided by AWS Certificate Manager",
                    "description": "Checks if a Classic Load Balancer uses HTTPS/SSL certificates provided by AWS Certificate Manager. The check fails if a Classic Load Balancer that is configured with an HTTPS/SSL listener does not use a certificate provided by AWS Certificate Manager.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ELB.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G182",
                    "name": "Classic Load Balancer listeners should be configured with HTTPS or TLS termination",
                    "description": "Checks if your Classic Load Balancer listeners are configured with HTTPS or TLS protocol for front-end (client to load balancer) connections. The check is applicable if a Classic Load Balancer has listeners. If your Classic Load Balancer does not have a listener configured, then the check does not report any findings.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ELB.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G183",
                    "name": "Application load balancer should be configured to drop http headers",
                    "description": "This check evaluates AWS Application Load Balancers (ALB) to ensure they are configured to drop http headers. By default, ALBs are not configured to drop invalid http header values. This check evaluates all ALBs fails if the attribute value of routing.http.drop_invalid_header_fields.enabled is set to false.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ELB.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G184",
                    "name": "Application and Classic Load Balancers logging should be enabled",
                    "description": "Checks if the Application Load Balancer and the Classic Load Balancer have logging enabled. The check fails if the access_logs.s3.enabled is false.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ELB.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G185",
                    "name": "IAM customer managed policies that you create should not allow wildcard actions for services",
                    "description": "Checks if the IAM identity-based custom policies have Allow statements that grant permissions for all actions on a service. The check fails if any policy statement includes \"Effect\": \"Allow\" with \"Action\": \"Service:\".<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.21<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.21/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G186",
                    "name": "AWS WAF Classic Global Web ACL logging should be enabled",
                    "description": "Checks if logging is enabled for a WAF global Web ACL. This check fails if logging is not enabled for the Web ACL.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: WAF.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G187",
                    "name": "Connections to Amazon Elasticsearch Service domains should be encrypted using TLS 1.2",
                    "description": "Checks whether connections to Amazon Elasticsearch Service domains are required to use TLS 1.2.  The check fails if the Amazon Elasticsearch Service domain TLSSecurityPolicy is not Policy-Min-TLS-1-2-2019-07.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ES.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ES.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "12Fnkpl8Y5",
                    "name": "Exposed Access Keys",
                    "description": "Checks popular code repositories for access keys that have been exposed to the public and for irregular Amazon Elastic Compute Cloud (Amazon EC2) usage that could be the result of a compromised access key. An access key consists of an access key ID and the corresponding secret access key. Exposed access keys pose a security risk to your account and other users, could lead to excessive charges from unauthorized activity or abuse, and violate the <a target=\"_blank\" href=\"https://aws.amazon.com/agreement/\">AWS Customer Agreement</a>. If your access key is exposed, take immediate action to secure your account. To protect your account from excessive charges, AWS temporarily limits your ability to create certain AWS resources when exposed access keys are identified. This does not make your account secure; it only partially limits the unauthorized usage for which you could be charged. Note: This check does not guarantee the identification of exposed access keys or compromised EC2 instances. You are ultimately responsible for the safety and security of your access keys and AWS resources.   <br/><br/>\nIf a deadline is shown for an access key, AWS may suspend your AWS account if the unauthorized usage is not stopped by that date. If you believe an alert is in error, <a href=\"https://console.aws.amazon.com/support/home?#/case/create?issueType=customer-service&serviceCode=customer-account&categoryCode=security\" target=\"_blank\">contact AWS Support</a>.<br/><br/>\nThe information displayed in Trusted Advisor may not reflect the most recent state of your account. No exposed access keys are marked as resolved until all exposed access keys on the account have been resolved. This data synchronization can take up to one week.<br/><br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nRed: Potentially compromised - AWS has identified an access key ID and corresponding secret access key that have been exposed on the Internet and may have been compromised (used).<br/>\nRed: Exposed - AWS has identified an access key ID and corresponding secret access key that have been exposed on the Internet.<br/>\nRed: Suspected - Irregular Amazon EC2 usage indicates that an access key may have been compromised, but it has not been identified as exposed on the Internet.<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nDelete the affected access key as soon as possible. If the key is associated with an IAM user, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html\" target=\"_blank\">Managing Access Keys for IAM Users</a>.<br/><br/>\nCheck your account for unauthorized usage. Log in to the <a href=\"https://console.aws.amazon.com/\" target=\"_blank\">AWS Management Console</a> and check each service console for suspicious resources. Pay special attention to running Amazon EC2 instances, Spot Instance requests, access keys, and IAM users. You can also check overall usage on the <a href=\"https://console.aws.amazon.com/billing/home#/\" target=\"_blank\">Billing & Cost Management Dashboard</a>.<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html\" target=\"_blank\">Best Practices for Managing AWS Access Keys</a><br/>\n<a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html\" target=\"_blank\">AWS Security Audit Guidelines</a>",
                    "category": "security",
                    "metadata": [
                            "Access Key ID",
                            "User Name (IAM or Root)",
                            "Fraud Type",
                            "Case ID",
                            "Time Updated",
                            "Location",
                            "Deadline",
                            "Usage (USD per Day)"
                    ]
                },
                {
                    "id": "Hs4Ma3G298",
                    "name": "Neptune DB cluster snapshots should not be public",
                    "description": "Checks if a Neptune manual DB cluster snapshot is public. The check fails if a Neptune manual DB cluster snapshot is public.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.3<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G177",
                    "name": "Auto scaling groups associated with a load balancer should use load balancer health checks",
                    "description": "Checks if your Auto Scaling groups that are associated with a load balancer are using Elastic Load Balancing health checks.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: AutoScaling.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/AutoScaling.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G299",
                    "name": "Neptune DB clusters should have deletion protection enabled",
                    "description": "Checks if a Neptune DB cluster has deletion protection enabled. The check fails if a Neptune DB cluster doesn't have deletion protection enabled.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Neptune.4<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Neptune.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G178",
                    "name": "Security groups should only allow unrestricted incoming traffic for authorized ports",
                    "description": "Checks if the security groups allow unrestricted incoming traffic. The check fails if ports allow unrestricted traffic on ports other than 80 and 443, which are default values for parameter authorizedTcpPorts.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.18<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.18/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G179",
                    "name": "SNS topics should be encrypted at-rest using AWS KMS",
                    "description": "Checks if an Amazon SNS topic is encrypted at rest using AWS KMS.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SNS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SNS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G271",
                    "name": "API Gateway routes should specify an authorization type",
                    "description": "Checks if Amazon API Gateway routes have an authorization type. The check fails if the API Gateway route does not specify an authorization type<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: APIGateway.8<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G150",
                    "name": "Elasticsearch domains should encrypt data sent between nodes",
                    "description": "Checks if Elasticsearch domains have node-to-node encryption enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ES.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ES.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G272",
                    "name": "Users should not have root access to SageMaker notebook instances",
                    "description": "Checks if root access is turned off for Amazon SageMaker notebook instances. The check fails if root access is turned on for a SageMaker notebook instance.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: SageMaker.3<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SageMaker.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G151",
                    "name": "An RDS event notifications subscription should be configured for critical database parameter group events",
                    "description": "Checks if an Amazon RDS Event subscription for RDS parameter groups is configured to notify on event category of \"configuration change\".<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.21<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.21/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G273",
                    "name": "Security contact information should be provided for an AWS account.",
                    "description": "Checks if an Amazon Web Services (AWS) account has security contact information. The check fails if security contact information is not provided for the account.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Account.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Account.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G152",
                    "name": "An RDS event notifications subscription should be configured for critical database instance events",
                    "description": "Checks if an Amazon RDS Event subscription for RDS instances is configured to notify on event categories of both \"maintenance\", \"configuration change\", and \"failure\".<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.20<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.20/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G274",
                    "name": "SageMaker notebook instances should be launched in a custom VPC",
                    "description": "Checks if an Amazon SageMaker notebook instance is launched within a custom VPC. The check fails if a SageMaker notebook instance is not launched within a custom VPC.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: SageMaker.2<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SageMaker.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G153",
                    "name": "RDS instances should not use a database engine default port",
                    "description": "Checks if RDS instances use the default port of that database engine.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.23<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.23/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G275",
                    "name": "CloudFront distributions should not point to non-existent S3 origins",
                    "description": "Checks if Amazon CloudFront distributions are pointing to non-existent S3 origins. The check fails for a CloudFront distribution if the origin is configured to point to a non-existent bucket. This check only applies to CloudFront distributions where an S3 bucket without static website hosting is the S3 origin.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFront.12<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.12/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G154",
                    "name": "An RDS event notifications subscription should be configured for critical database security group events",
                    "description": "Checks if an Amazon RDS Event subscription for RDS security groups is configured to notify on event categories of both \"configuration change\" and \"failure\".<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.22<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.22/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G265",
                    "name": "A WAF Regional rule group should have at least one rule",
                    "description": "Checks if a WAF Regional rule group has at least one rule. The check fails if no rules are present within a rule group.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.3<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G144",
                    "name": "Unused IAM user credentials should be removed",
                    "description": "Checks if your IAM users have passwords or active access keys that were not used within the previous 90 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G266",
                    "name": "A WAF Regional web ACL should have at least one rule or rule group",
                    "description": "Checks if a WAF Regional web ACL contains any WAF rules or WAF rule groups. This check fails if a web ACL does not contain any WAF rules or rule groups.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.4<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G145",
                    "name": "Amazon ECS task definitions should have secure networking modes and user definitions.",
                    "description": "Checks if an Amazon ECS Task Definition with host networking mode has \"privileged\" or \"user\" container definitions. The check fails with host network mode and container definitions are privileged=false or empty and user=root or empty.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ECS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G267",
                    "name": "A WAF global rule should have at least one condition",
                    "description": "Checks if a WAF global rule has at least one condition. This check fails if no conditions are present within a rule.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.6<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G146",
                    "name": "ECS services should not have public IP addresses assigned to them automatically",
                    "description": "Checks if ECS services are configured to automatically assign public IP addresses. This check fails if AssignPublicIP is ENABLED.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ECS.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G268",
                    "name": "A WAF global rule group should have at least one rule",
                    "description": "Checks if a WAF global rule group has at least one rule. The check fails if no rules are present within a rule group.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.7<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G147",
                    "name": "Amazon Elasticsearch Service domains should be in a VPC",
                    "description": "Checks whether Amazon Elasticsearch Service domains are in a VPC. It does not evaluate the VPC subnet routing configuration to determine public reachability. This check also does not check whether the Amazon OpenSearch Service resource-based policy permits public access by other accounts or external entities. You should ensure that Amazon Elasticsearch Service domains are not attached to public subnets. See Resource-based policies (https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource) in the Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) Developer Guide. You should also ensure that your VPC is configured according to the recommended best practices. See Security best practices for your VPC (https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) in the Amazon VPC User Guide.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ES.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ES.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G269",
                    "name": "A WAF global web ACL should have at least one rule or rule group",
                    "description": "Checks if a WAF global web ACL contains any WAF rules or WAF rule groups. This check fails if a web ACL does not contain any WAF rules or WAF rule groups.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.8<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G148",
                    "name": "Elastic Beanstalk environments should have enhanced health reporting enabled",
                    "description": "Checks if enhanced health reporting is enabled for your AWS Elastic Beanstalk environments.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ElasticBeanstalk.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElasticBeanstalk.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G149",
                    "name": "Elastic Beanstalk managed platform updates should be enabled",
                    "description": "Checks if managed platform updates are enabled for the AWS Elastic Beanstalk environment.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ElasticBeanstalk.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElasticBeanstalk.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G160",
                    "name": "IAM authentication should be configured for RDS instances",
                    "description": "Checks if an RDS DB instance has IAM database authentication enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.10<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G282",
                    "name": "RSA certificates managed by ACM should use a key length of at least 2,048 bits",
                    "description": "Checks if RSA certificates managed by AWS Certificate Manager use a key length of at least 2,048 bits. The check fails if the key length is smaller than 2,048 bits.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ACM.2<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ACM.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G161",
                    "name": "IAM authentication should be configured for RDS clusters",
                    "description": "Checks if an RDS DB cluster has IAM database authentication enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.12<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.12/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G283",
                    "name": "AWS AppSync should have request-level and field-level logging turned on",
                    "description": "Checks if an AWS AppSync API has request-level and field-level logging turned on. The check fails if request-level logging isn't turned on or if the field resolver log level is set to ‘None’.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: AppSync.2<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/AppSync.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G162",
                    "name": "RDS automatic minor version upgrades should be enabled",
                    "description": "Checks if automatic minor version upgrades are enabled for the Amazon RDS database instance.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.13<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.13/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G284",
                    "name": "CloudFront distributions should use origin access control",
                    "description": "Checks if an Amazon CloudFront distribution with an Amazon S3 origin has origin access check (OAC) configured. The check fails if OAC isn't configured.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFront.13<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.13/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G163",
                    "name": "RDS DB clusters should be configured to copy tags to snapshots",
                    "description": "Checks if RDS DB clusters are configured to copy all tags to snapshots when the snapshots are created.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.16<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.16/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G285",
                    "name": "EKS cluster endpoints should not be publicly accessible",
                    "description": "Checks if an Amazon EKS cluster endpoint is publicly accessible. The check fails if an EKS cluster has an endpoint that is publicly accessible.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EKS.1<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EKS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G164",
                    "name": "RDS DB instances should be configured to copy tags to snapshots",
                    "description": "Checks if RDS DB instances are configured to copy all tags to snapshots when the snapshots are created.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.17<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.17/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G286",
                    "name": "ElastiCache for Redis cache clusters should have auto minor version upgrades enabled",
                    "description": "This check evaluates if auto minor version upgrades are enabled for ElastiCache for Redis cache clusters. This check fails if the ElastiCache for Redis cache cluster does not have auto minor version upgrades enabled.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ElastiCache.2<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ElastiCache.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G165",
                    "name": "RDS instances should be deployed in a VPC",
                    "description": "Checks if an RDS instance is deployed in a VPC (EC2-VPC).<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: RDS.18<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.18/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G276",
                    "name": "A WAFV2 web ACL should have at least one rule or rule group",
                    "description": "Checks if a WAFV2 web ACL contains at least one WAF rule or WAF rule group. The check fails if a web ACL does not contain any WAF rule or rule group.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.10<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G155",
                    "name": "EC2 instances should be managed by AWS Systems Manager",
                    "description": "Checks if the Amazon EC2 instances in your account are managed by AWS Systems Manager.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SSM.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SSM.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G277",
                    "name": "EC2 launch templates should not assign public IPs to network interfaces",
                    "description": "Checks if Amazon EC2 launch templates are configured to assign public IP addresses to network interfaces upon launch. The check fails if an EC2 launch template is configured to assign a public IP address to network interfaces or if there is at least one network interface that has a public IP address.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EC2.25<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.25/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G156",
                    "name": "EC2 instances managed by Systems Manager should have a patch compliance status of COMPLIANT after a patch installation",
                    "description": "Checks if the compliance status of the Amazon EC2 Systems Manager patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation on the instance. It only assesses instances that are managed by AWS Systems Manager Patch Manager.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SSM.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SSM.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G278",
                    "name": "Access logging should be configured for API Gateway V2 Stages",
                    "description": "Checks if Amazon API Gateway V2 stages have access logging configured. This check fails if access log settings aren’t defined.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: APIGateway.9<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.9/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G157",
                    "name": "EC2 instances managed by Systems Manager should have an association compliance status of COMPLIANT",
                    "description": "Checks if the status of the AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association is executed on an instance.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SSM.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SSM.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G158",
                    "name": "SSM documents should not be public",
                    "description": "Checks if AWS Systems Manager documents that the account owns are public. This check fails if SSM documents that have \"Self\" as the owner are public.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SSM.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SSM.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G159",
                    "name": "Elastic File System should be configured to encrypt file data at-rest using AWS KMS",
                    "description": "Checks if Amazon Elastic File System (Amazon EFS) is configured to encrypt the file data using AWS Key Management Service (AWS KMS). The check will fail if the encrypted key is set to false on DescribeFileSystems or if the KmsKeyId key on DescribeFileSystems does not match the KmsKeyId parameter.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EFS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EFS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G250",
                    "name": "ECS clusters should use Container Insights",
                    "description": "Checks if ECS clusters use Container Insights. This check fails if Container Insights are not set up for a cluster.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECS.12<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.12/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G251",
                    "name": "EFS access points should enforce a root directory",
                    "description": "Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a root directory. This check fails if the value of 'Path' is set to '/' (default root directory of the file system).<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EFS.3<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EFS.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G130",
                    "name": "Lambda functions should use supported runtimes",
                    "description": "Checks that the lambda function settings for runtimes, match the expected values set for the supported runtimes for each language. The supported runtimes this check assesses for are: nodejs18.x, nodejs16.x, nodejs14.x, nodejs12.x, python3.10, python3.9, python3.8, python3.7, java11, java8, java8.al2, go1.x, dotnet6, ruby2.7.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Lambda.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Lambda.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G252",
                    "name": "EFS access points should enforce a user identity",
                    "description": "Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a user identity. This check fails if ‘PosixUser’ is not defined under ‘configuration’ or if parameters are provided and there is no match in the corresponding parameter.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EFS.4<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EFS.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G131",
                    "name": "Lambda function policies should prohibit public access",
                    "description": "Checks if the AWS Lambda function policy attached to the Lambda resource prohibits public access. If the Lambda function policy allows public access, the check fails.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Lambda.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Lambda.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G253",
                    "name": "EKS clusters should run on a supported Kubernetes version",
                    "description": "Checks if an EKS cluster is running on a supported Kubernetes version. The check fails if the EKS cluster is running on an unsupported version.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EKS.2<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EKS.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G132",
                    "name": "Database Migration Service replication instances should not be public",
                    "description": "Checks if AWS Database Migration Service replication instances are public by examining the PubliclyAccessible field value.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: DMS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/DMS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G243",
                    "name": "Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2)",
                    "description": "Checks if only IMDSv2 is enabled. This check fails if the metadata version is not included in the launch configuration or if both IMDSv1 and IMDSv2 are enabled.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: AutoScaling.3<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/AutoScaling.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G122",
                    "name": "VPC flow logging should be enabled in all VPCs",
                    "description": "Checks if Amazon Virtual Private Cloud flow logs are found and enabled for Amazon VPCs. The traffic type is set to 'Reject'.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G244",
                    "name": "Auto Scaling group launch configuration should not have a metadata response hop limit greater than 1",
                    "description": "Checks the number of network hops that the metadata token can travel. This check fails if the metadata response hop limit is greater than 1.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: AutoScaling.4<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/AutoScaling.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G123",
                    "name": "EC2 instances should not have a public IPv4 address",
                    "description": "Checks if EC2 instances have a public IP address. The check fails if the publicIp field is present in the EC2 instance configuration item. This check applies to IPv4 addresses only.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.9<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.9/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G245",
                    "name": "CloudFormation stacks should be integrated with Simple Notification Service (SNS)",
                    "description": "Checks if your CloudFormation stacks are sending event notifications to SNS topic. This check fails if CloudFormation stacks are not sending event notifications to an SNS topic.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFormation.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFormation.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G124",
                    "name": "EC2 instances should use Instance Metadata Service Version 2 (IMDSv2)",
                    "description": "Checks if your Amazon Elastic Compute Cloud (Amazon EC2) instance metadata version is configured with Instance Metadata Service Version 2 (IMDSv2). The check passes if HttpTokens is set to required for IMDSv2. The check fails if HttpTokens is set to optional.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G246",
                    "name": "CloudFront distributions should not use deprecated SSL protocols between edge locations and custom origins",
                    "description": "Checks if CloudFront distributions are using deprecated SSL protocols for HTTPS communication between CloudFront edge locations and your custom origins. This check fails for a CloudFront distribution if it has a 'CustomOriginConfig' where ‘OriginSslProtocols’ includes ‘SSLv3’.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFront.10<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G125",
                    "name": "API Gateway should be associated with a WAF Web ACL",
                    "description": "Checks to see if an API Gateway stage is using an AWS WAF Web ACL. This check fails if an AWS WAF Web ACL is not attached to a REST API Gateway stage.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: APIGateway.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G247",
                    "name": "EC2 Transit Gateways should not automatically accept VPC attachment requests",
                    "description": "Checks if EC2 Transit Gateways are automatically accepting shared VPC attachments requests. This check will fail for a Transit Gateway that automatically accept shared VPC attachment requests.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EC2.23<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.23/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G126",
                    "name": "DynamoDB Accelerator (DAX) clusters should be encrypted at rest",
                    "description": "Checks if a DAX cluster is encrypted at rest.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: DynamoDB.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/DynamoDB.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G248",
                    "name": "EC2 paravirtual instance types should not be used",
                    "description": "Checks if the virtualization type of an EC2 instance is paravirtual. The check fails for an EC2 instance if ‘virtualizationType’ is set to ‘paravirtual’.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EC2.24<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.24/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G127",
                    "name": "API Gateway REST and WebSocket API execution logging should be enabled",
                    "description": "Checks if all stages of Amazon API Gateway REST and WebSocket APIs have logging enabled. The check fails if logging is not enabled for all methods of a stage or if loggingLevel is neither ERROR nor INFO.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: APIGateway.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G249",
                    "name": "ECS Fargate services should run on the latest Fargate platform version",
                    "description": "Checks if ECS Fargate services is running the latest Fargate platform version. This check fails if the platform version is not latest.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECS.10<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G128",
                    "name": "API Gateway REST API stages should be configured to use SSL certificates for backend authentication",
                    "description": "Checks if Amazon API Gateway REST API stages have SSL certificates configured that backend systems can use to authenticate that incoming requests are from the API Gateway.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: APIGateway.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G129",
                    "name": "API Gateway REST API stages should have AWS X-Ray tracing enabled",
                    "description": "Checks if AWS X-Ray active tracing is enabled for your Amazon API Gateway REST API stages.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: APIGateway.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G260",
                    "name": "OpenSearch domains should have fine-grained access control enabled",
                    "description": "Checks if Amazon OpenSearch domains have fine-grained access check enabled. This check fails if the fine-grained access check is not enabled.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.7<br>\n<br>\n<b>Alert Criteria</b><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G261",
                    "name": "Redshift clusters should not use the default database name",
                    "description": "Checks if a Redshift cluster has changed the database name from its default value. This check will fail if the database name for a Redshift cluster is set to “dev”<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Redshift.9<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.9/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G140",
                    "name": "IAM root user access key should not exist",
                    "description": "Checks if the root user access key is available.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G262",
                    "name": "S3 buckets should have lifecycle policies configured",
                    "description": "Checks if a lifecycle policy is configured for an S3 bucket. This check fails if the lifecycle policy is not configured for an S3 bucket.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: S3.13<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.13/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G141",
                    "name": "MFA should be enabled for all IAM users that have a console password",
                    "description": "Checks if AWS Multi-Factor Authentication (MFA) is enabled for all AWS Identity and Access Management (IAM) users that use a console password.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G263",
                    "name": "Logging of delivery status should be enabled for notification messages sent to a topic",
                    "description": "Checks if logging is enabled for the delivery status of notification messages sent to a topic for the endpoints. This check fails if the delivery status notification for messages is not enabled.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: SNS.2<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SNS.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G142",
                    "name": "Hardware MFA should be enabled for the root user",
                    "description": "Checks if your AWS account is enabled to use hardware multi-factor authentication (MFA) device to sign in with root credentials.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G264",
                    "name": "A WAF Regional rule should have at least one condition",
                    "description": "Checks if a WAF Regional rule has at least one condition. The check fails if no conditions are present within a rule.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: WAF.2<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/WAF.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G143",
                    "name": "Password policies for IAM users should have strong configurations",
                    "description": "Checks if the account password policy for IAM users uses the following recommended configurations: RequireUppercaseCharacters: true, RequireLowercaseCharacters: true, RequireSymbols: true, RequireNumbers: true, MinimumPasswordLength: 8.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.7<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "N430c450f2",
                    "name": "CloudFront SSL Certificate on the Origin Server",
                    "description": "Checks your origin server for SSL certificates that are expired, about to expire, missing, or that use outdated encryption. If a certificate is expired, CloudFront responds to requests for your content with HTTP status code 502, Bad Gateway. Certificates that were encrypted by using the SHA-1 hashing algorithm are being deprecated by web browsers such as Chrome and Firefox. Depending on the number of SSL certificates that you have associated with your CloudFront distributions, this check might add a few cents per month to your bill with your web hosting provider, for example, AWS if you're using EC2 or ELB as the origin for your CloudFront distribution. This check does not validate your origin certificate chain or certificate authorities; you can check these in your CloudFront configuration. <br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: An SSL certificate on your origin has expired or is missing.<br>\nYellow: An SSL certificate on your origin expires in the next thirty days.<br>\nYellow: An SSL certificate on your origin was encrypted by using the SHA-1 hashing algorithm.<br>\nYellow: An SSL certificate on your origin can't be located. The connection might have failed due to timeout, or other HTTPS connection problems.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nRenew the certificate on your origin if it has expired or is about to expire.<br>\nAdd a certificate if one does not exist.<br>\nReplace a certificate that was encrypted by using the SHA-1 hashing algorithm with a certificate that is encrypted by using the SHA-256 hashing algorithm.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS\" target=\"_blank\">Using Alternate Domain Names and HTTPS</a>",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Distribution ID",
                            "Distribution Domain Name",
                            "Origin",
                            "Reason"
                    ]
                },
                {
                    "id": "Hs4Ma3G254",
                    "name": "Application Load Balancer should be configured with defensive or strictest desync mitigation mode",
                    "description": "Checks if the Application Load Balancer is configured with defensive or strictest de-sync mitigation mode. This check fails if the Application Load Balancer is not configured with defensive or strictest desync mitigation mode.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ELB.12<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.12/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G133",
                    "name": "IAM customer managed policies should not allow decryption actions on all KMS keys",
                    "description": "Checks if the default version of IAM customer managed policies allow principals to use the AWS Key Management Service (KMS) decryption actions on all resources. This check fails if kms:Decrypt or kms:ReEncryptFrom actions are allowed on all KMS keys. The check evaluates both attached and unattached customer managed policies. It does not check inline policies or AWS managed policies.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: KMS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/KMS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G255",
                    "name": "Classic Load Balancer should be configured with defensive or strictest desync mitigation mode",
                    "description": "Checks if the Classic Load Balancer is configured defensive or strictest desync mitigation mode. This check will fail if the Application Load Balancer is not configured with defensive strictest mitigation Desync mitigation mode.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ELB.14<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.14/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G134",
                    "name": "IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys",
                    "description": "Checks if the inline policies embedded in your IAM principals (Role/User/Group) allow the AWS Key Management Service (KMS) decryption actions on all KMS keys. This check fails if kms:Decrypt or kms:ReEncryptFrom actions are allowed on all KMS keys in an inline policy.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: KMS.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/KMS.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G256",
                    "name": "Kinesis streams should be encrypted at rest",
                    "description": "Checks if Kinesis streams are encrypted at rest with server-side encryption. This check fails if a Kinesis stream is not encrypted at rest with server-side encryption.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Kinesis.1<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Kinesis.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G135",
                    "name": "AWS KMS keys should not be deleted unintentionally",
                    "description": "Checks whether AWS Key Management Service (KMS) keys are scheduled for deletion. The check fails if a KMS key is scheduled for deletion.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: KMS.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/KMS.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G257",
                    "name": "Network Firewall policies should have at least one rule group associated",
                    "description": "Checks if a Network Firewall policy has any stateful or stateless rule groups associated. This check fails if stateless or stateful rule groups are not assigned.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: NetworkFirewall.3<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/NetworkFirewall.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G136",
                    "name": "Amazon SQS queues should be encrypted at rest",
                    "description": "Checks if Amazon SQS queues are encrypted at rest.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SQS.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SQS.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G258",
                    "name": "The default stateless action for Network Firewall policies should be drop or forward for full packets",
                    "description": "Checks if the default stateless action for full packets for a Network Firewall policy is drop or forward. The check passes if Drop or Forward is selected, and fails if Pass is selected.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: NetworkFirewall.4<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/NetworkFirewall.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G137",
                    "name": "IAM policies should not allow full \"*\" administrative privileges",
                    "description": "Checks if the default version of AWS Identity and Access Management (IAM) policies (also known as customer managed policies) do not have administrator access with a statement that has \"Effect\": \"Allow\" with \"Action\": \"*\" over \"Resource\": \"*\". It only assesses for the Customer Managed Policies that you created, but not inline and AWS Managed Policies.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G259",
                    "name": "The default stateless action for Network Firewall policies should be drop or forward for fragmented packets",
                    "description": "Checks if a Network Firewall policy has drop or forward as the default stateless action for fragmented packets. The check passes if Drop or Forward is selected, and fails if Pass is selected.<br>\n<br>\n<b>Source</b><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: NetworkFirewall.5<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<b>Recommended Action</b><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/NetworkFirewall.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G138",
                    "name": "IAM users should not have IAM policies attached",
                    "description": "Checks that none of your IAM users have policies attached. Instead, IAM users must inherit permissions from IAM groups or roles.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G139",
                    "name": "IAM users' access keys should be rotated every 90 days or less",
                    "description": "Checks if the active access keys are rotated within 90 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: IAM.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/IAM.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G230",
                    "name": "S3 bucket server access logging should be enabled",
                    "description": "Checks if an Amazon S3 Bucket has server access logging enabled to a chosen target bucket.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: S3.9<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.9/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G231",
                    "name": "Stateless network firewall rule group should not be empty",
                    "description": "Checks if a Stateless Network Firewall Rule Group contains rules. The rule will fail if there are no rules in a Stateless Network Firewall Rule Group.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: NetworkFirewall.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/NetworkFirewall.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G110",
                    "name": "CloudTrail should have encryption at-rest enabled",
                    "description": "Checks whether AWS CloudTrail is configured to use the server-side encryption (SSE) AWS Key Management Service (AWS KMS) key encryption. The check will pass if the KmsKeyId is defined.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudTrail.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudTrail.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G229",
                    "name": "CloudFront distributions should encrypt traffic to custom origins",
                    "description": "Checks if CloudFront distributions are encrypting traffic to custom origins. This check fails for a CloudFront distribution whose origin protocol policy allows 'http-only' or if it is 'match-viewer' and the viewer protocol policy is 'allow-all'. <br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFront.9<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.9/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G108",
                    "name": "CloudTrail trails should be integrated with Amazon CloudWatch Logs",
                    "description": "Checks if AWS CloudTrail trails are configured to send logs to Amazon CloudWatch Logs.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudTrail.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudTrail.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G109",
                    "name": "CloudTrail log file validation should be enabled",
                    "description": "Checks if CloudTrail log file validation is enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudTrail.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudTrail.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G221",
                    "name": "OpenSearch domains should have audit logging enabled",
                    "description": "Checks if Amazon OpenSearch Service domains have audit logging enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G100",
                    "name": "Amazon SageMaker notebook instances should not have direct internet access",
                    "description": "Checks if direct internet access is disabled for an Amazon SageMaker notebook instance by examining the DirectInternetAccess field is disabled for an Amazon SageMaker notebook instance.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SageMaker.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SageMaker.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G222",
                    "name": "OpenSearch domain error logging to CloudWatch Logs should be enabled",
                    "description": "Checks if Amazon OpenSearch domains are configured to send error logs to CloudWatch Logs. This check fails if error logging to CloudWatch is not enabled for a domain.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G101",
                    "name": "Amazon Elastic MapReduce cluster master nodes should not have public IP addresses",
                    "description": "Checks if master nodes on EMR clusters have public IP addresses.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EMR.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EMR.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G223",
                    "name": "OpenSearch domains should encrypt data sent between nodes",
                    "description": "Checks if Amazon OpenSearch domains have node-to-node encryption enabled. This check fails if node-to-node encryption is disabled on the domain.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G102",
                    "name": "Connections to Amazon Redshift clusters should be encrypted in transit",
                    "description": "Checks if connections to Amazon Redshift clusters are required to use encryption in transit. The check fails if the Amazon Redshift cluster parameter require_SSL is not set to 1.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Redshift.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G224",
                    "name": "OpenSearch domains should be in a VPC",
                    "description": "Checks Amazon OpenSearch Service domains are in an Amazon Virtual Private Cloud (VPC).<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G103",
                    "name": "Amazon Redshift clusters should prohibit public access",
                    "description": "Checks if Amazon Redshift clusters are publicly accessible. It evaluates the publiclyAccessible field in the cluster configuration item.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Redshift.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G225",
                    "name": "OpenSearch domains should have encryption at rest enabled",
                    "description": "Checks if Amazon OpenSearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G104",
                    "name": "Redshift clusters should use enhanced VPC routing",
                    "description": "Checks if a Redshift cluster has EnhancedVpcRouting enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Redshift.7<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G226",
                    "name": "Amazon EC2 instances launched using Auto Scaling group launch configurations should not have Public IP addresses",
                    "description": "Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled using launch configurations.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Autoscaling.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Autoscaling.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G105",
                    "name": "Amazon Redshift should have automatic upgrades to major versions enabled",
                    "description": "Checks if an Amazon Redshift cluster is configured with automatic upgrades to major versions.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Redshift.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G227",
                    "name": "CloudFront distributions should use custom SSL/TLS certificates",
                    "description": "Checks if CloudFront distributions are using the default SSL/TLS certificate CloudFront provides instead of a custom one. This check fails for a CloudFront distribution if it uses the default SSL/TLS certificate.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFront.7<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G106",
                    "name": "Amazon Redshift clusters should have audit logging enabled",
                    "description": "Checks if an Amazon Redshift cluster has audit logging enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: Redshift.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G228",
                    "name": "CloudFront distributions should use SNI to serve HTTPS requests",
                    "description": "Checks if Amazon CloudFront distributions are using a custom SSL/TLS certificate and are configured to use SNI to serve HTTPS requests as opposed to dedicated IP address.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CloudFront.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G107",
                    "name": "CloudFront distributions should require encryption in transit",
                    "description": "Checks if an Amazon CloudFront distribution requires viewers to use HTTPS directly, or if it uses redirection. The check fails if ViewerProtocolPolicy is set to allow-all for defaultCacheBehavior or for cacheBehaviors.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudFront.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G241",
                    "name": "Secrets should not be passed as container environment variable",
                    "description": "Checks if the container environment variables includes the following keys - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,  or ECS_ENGINE_AUTH_DATA.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECS.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G120",
                    "name": "Stopped EC2 instances should be removed after a specified time period",
                    "description": "Checks if any EC2 instances have been stopped for more than the allowed number of days. An EC2 instance fails this check if it is stopped for longer than the maximum allowed time period, which by default is 30 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G242",
                    "name": "Amazon ECR private repositories should have image scanning enabled",
                    "description": "Checks if a private ECR repository has image scanning enabled. This check fails if a private ECR repository has image scanning disabled. Amazon ECR image scanning helps in identifying software vulnerabilities in your container images. Amazon ECR uses the Common Vulnerabilities and Exposures (CVEs) database from the open-source Clair project and provides a list of scan findings. Enabling image scanning on ECR repositories adds a layer of verification for the integrity and safety of the images being stored.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECR.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECR.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G121",
                    "name": "EBS default encryption should be enabled",
                    "description": "Checks if Amazon Elastic Block Store (EBS) encryption is enabled by default. The check fails if EBS default encryption is not enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.7<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.7/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G119",
                    "name": "EBS volumes should be attached to EC2 instances",
                    "description": "Checks if EBS volumes are attached to EC2 instances.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G232",
                    "name": "RDS Database Clusters should use a custom administrator username",
                    "description": "Checks if an RDS database cluster has changed the admin username from its default value. This rule will fail if the admin username is set to the default value.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: RDS.24<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.24/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G111",
                    "name": "CloudTrail should be enabled and configured with at least one multi-region trail",
                    "description": "Checks that there is at least one multi-region AWS CloudTrail trail.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudTrail.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudTrail.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G233",
                    "name": "RDS database instances should use a custom administrator username",
                    "description": "Checks if an Amazon Relational Database Service (Amazon RDS) database instance has changed the admin username from its default value. This rule will only run on RDS database instances. The rule will fail if the admin username is set to the default value.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: RDS.25<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/RDS.25/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G112",
                    "name": "Secrets Manager secrets should be rotated within a specified number of days",
                    "description": "Checks if your secrets have rotated at least once within 90 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SecretsManager.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SecretsManager.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G234",
                    "name": "AWS CodeBuild S3 Logs should be encrypted",
                    "description": "Checks if a AWS CodeBuild project configured with Amazon S3 Logs has encryption enabled for its logs.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CodeBuild.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CodeBuild.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G113",
                    "name": "Secrets Manager secrets configured with automatic rotation should rotate successfully",
                    "description": "Checks if an AWS Secrets Manager secret rotated successfully based on the rotation schedule. The check fails if RotationOccurringAsScheduled is false. The check does not evaluate secrets that do not have rotation configured.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SecretsManager.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SecretsManager.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G235",
                    "name": "Amazon ECR private repositories should have tag immutability enabled",
                    "description": "Checks if a private ECR repository has tag immutability enabled. This check fails if a private ECR repository has tag immutability disabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECR.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECR.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G114",
                    "name": "Remove unused Secrets Manager secrets",
                    "description": "Checks if your secrets have been accessed within a specified number of days. The default value is 90 days. Secrets that have not been accessed even once within the number days you define, fail this check.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SecretsManager.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SecretsManager.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G236",
                    "name": "Amazon ECS Task Definitions should not share the host's process namespace",
                    "description": "Checks if Amazon ECS Task Definitions are configured to share a host's process namespace with its containers.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECS.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G115",
                    "name": "Secrets Manager secrets should have automatic rotation enabled",
                    "description": "Checks if a secret stored in AWS Secrets Manager is configured to rotate automatically.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: SecretsManager.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/SecretsManager.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G237",
                    "name": "Amazon ECS Containers should run as non-privileged",
                    "description": "Checks if the Privileged parameter in the container definition of Amazon ECS Task Definitions is set to 'true'.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECS.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G116",
                    "name": "EBS snapshots should not be public, determined by the ability to be restorable by anyone",
                    "description": "Checks if Amazon Elastic Block Store snapshots are not publicly restorable.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G238",
                    "name": "Amazon ECS Containers should only have read-only access to its root filesystems",
                    "description": "Checks if ECS Containers are limited to read-only access to its mounted root filesystems.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECS.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECS.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G117",
                    "name": "Attached EBS volumes should be encrypted at-rest",
                    "description": "Checks if the EBS volumes that are in an attached state are encrypted.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G118",
                    "name": "The VPC default security group should not allow inbound and outbound traffic",
                    "description": "Checks that the default security group of a VPC does not allow inbound or outbound traffic.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.2<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.2/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G207",
                    "name": "EC2 subnets should not automatically assign public IP addresses",
                    "description": "Checks if the assignment of public IPs in Amazon Virtual Private Cloud (VPC) subnets have the MapPublicIpOnLaunch set to FALSE. The check will pass if the flag is set to FALSE.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.15<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.15/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G208",
                    "name": "EC2 instances should not use multiple ENIs",
                    "description": "Checks to see if Amazon EC2 instance uses multiple ENI/EFA. This check will pass if single network adapters is used.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.17<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.17/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G209",
                    "name": "Unused Network Access Control Lists should be removed",
                    "description": "Checks to see if there are any NACLs (Network Access Control List) that are unused. The check will check the item configuration of the resource AWS::EC2::NetworkAcl and determine the relationships of the NACL.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.16<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.16/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G200",
                    "name": "CloudFront distributions should have a default root object configured",
                    "description": "Checks if an Amazon CloudFront distribution is configured to return a specific object that is the default root object. The check fails if the CloudFront distribution does not have a default root object configured.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudFront.1<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.1/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G201",
                    "name": "CloudFront distributions should have WAF enabled",
                    "description": "Checks to see if Amazon CloudFront distributions are associated with either WAF or WAFv2 web ACLs. The check fails if a CloudFront distribution is not associated with a web ACL.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudFront.6<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.6/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G202",
                    "name": "API Gateway REST API cache data should be encrypted at rest",
                    "description": "Checks if all methods in Amazon API Gateway REST API stages that have cache enabled are encrypted. The check fails if any method in API Gateway REST API stage is configured to cache and the cache is not encrypted.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: APIGateway.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/APIGateway.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G203",
                    "name": "Amazon Elasticsearch Service domains should have audit logging enabled",
                    "description": "This check checks whether Amazon Elasticsearch Service domains have audit logging enabled. This check fails if an Amazon Elasticsearch Service domain does not have audit logging enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ES.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ES.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G204",
                    "name": "Security groups should not allow unrestricted access to ports with high risk",
                    "description": "Checks if unrestricted incoming traffic for the security groups is accessible to the specified ports [3389, 20, 23, 110, 143, 3306, 8080, 1433, 9200, 9300, 25, 445, 135, 21, 1434, 4333, 5432, 5500, 5601, 22 ] that have the highest risk. This check passes when none of the rules in a security group allow ingress traffic from 0.0.0.0/0 for the listed ports.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.19<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.19/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G205",
                    "name": "Classic Load Balancers with HTTPS/SSL listeners should use a predefined security policy that has strong configuration",
                    "description": "Checks if your Classic Load Balancer SSL listeners use the predefined policy ELBSecurityPolicy-TLS-1-2-2017-01. The check fails if the Classic Load Balancer SSL listeners do not use the predefined policy ELBSecurityPolicy-TLS-1-2-2017-01.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: ELB.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ELB.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G206",
                    "name": "Amazon EC2 should be configured to use VPC endpoints that are created for the Amazon EC2 service",
                    "description": "Checks if a service endpoint for Amazon EC2 is created for each VPC. The check fails if a VPC does not have a VPC endpoint created for the Amazon EC2 service.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: EC2.10<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "zXCkfM1nI3",
                    "name": "IAM Use",
                    "description": "This check is intended to discourage the use of root access by checking for existence of at least one IAM user. You may ignore the alert if you are following the best practice of centralizing identities and configuring users in an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html\" target=\"_blank\">external identity provider</a> or <a href=\"https://aws.amazon.com/single-sign-on/\" target=\"_blank\">AWS Single Sign-On</a>. \n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: No IAM users have been created for this account.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nCreate an IAM user or use AWS Single Sign-On to create additional users whose permissions are limited to perform specific tasks in your AWS environment. \n<br><br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html\" target=\"_blank\" >What is AWS Single Sign-On?</a><br>\n<a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html\" target=\"_blank\">What Is IAM?</a>",
                    "category": "security",
                    "metadata": []
                },
                {
                    "id": "Hs4Ma3G220",
                    "name": "Connections to OpenSearch domains should be encrypted using TLS 1.2",
                    "description": "Checks if connections to OpenSearch domains are required to use TLS 1.2. The check fails if the OpenSearch domain TLSSecurityPolicy is not Policy-Min-TLS-1-2-2019-07.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Opensearch.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Opensearch.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G218",
                    "name": "CodeBuild project environments should not have privileged mode enabled",
                    "description": "Checks if an AWS CodeBuild project environment has privileged mode enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CodeBuild.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nRed: Critical or High Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CodeBuild.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Yw2K9puPzl",
                    "name": "IAM Password Policy",
                    "description": "Checks the password policy for your account and warns when a password policy is not enabled, or if password content requirements have not been enabled. Password content requirements increase the overall security of your AWS environment by enforcing the creation of strong user passwords. When you create or change a password policy, the change is enforced immediately for new users but does not require existing users to change their passwords. \n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: A password policy is enabled, but at least one content requirement is not enabled.  \n<br>\nRed: No password policy is enabled. \n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nIf some content requirements are not enabled, consider enabling them. If no password policy is enabled, create and configure one. See <a href=\"http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html\" target=\"_blank\">Setting an Account Password Policy for IAM Users</a>. \n<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"http://docs.aws.amazon.com/IAM/latest/UserGuide/Credentials-ManagingPasswords.html\" target=\"_blank\">Managing Passwords</a>",
                    "category": "security",
                    "metadata": [
                            "Password Policy",
                            "Uppercase",
                            "Lowercase",
                            "Number",
                            "Non-alphanumeric",
                            "Status",
                            "Reason"
                    ]
                },
                {
                    "id": "Hs4Ma3G219",
                    "name": "Amazon Redshift clusters should not use the default Admin username",
                    "description": "Checks if a Redshift cluster has changed the Admin username from its default value. This check will fail if the admin username for a Redshift cluster is set to 'awsuser'.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: Redshift.8<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/Redshift.8/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "c9D319e7sG",
                    "name": "Amazon Route 53 MX Resource Record Sets and Sender Policy Framework",
                    "description": "For each MX resource record set, checks that the TXT or SPF resource record set contains a valid SPF record. The record must start with \"v=spf1\". The SPF record specifies the servers that are authorized to send email for your domain, which helps detect and stop email address spoofing to reduce spam. Route 53 recommends that you use a TXT record instead of an SPF record. Trusted Advisor reports this check as green as long as each MX resource record set has at least one SPF or TXT record.\n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4>\n<br/>\nYellow: An MX resource record set doesn’t have a TXT or SPF resource record that contains a valid SPF value.\n<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br/>\nFor each MX resource record set, create a TXT resource record set that contains a valid SPF value. For more information, see <a href=\"http://www.open-spf.org/SPF_Record_Syntax\" target=\"_blank\">Sender Policy Framework: SPF Record Syntax</a> and <a href=\"http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RRSchanges_console.html\" target=\"_blank\">Creating Resource Record Sets By Using the Amazon Route 53 Console</a>.\n<br/><br/>\n<h4 class='headerBodyStyle'>Additional Information</h4>\n<br/>\n<a href=\"http://en.wikipedia.org/wiki/Sender_Policy_Framework\" target=\"_blank\">Sender Policy Framework</a> (Wikipedia)<br/>\n<a href=\"http://en.wikipedia.org/wiki/MX_record\" target=\"_blank\">MX record</a> (Wikipedia)",
                    "category": "security",
                    "metadata": [
                            "Hosted Zone Name",
                            "Hosted Zone ID",
                            "Resource Record Set Name",
                            "Status"
                    ]
                },
                {
                    "id": "Qsdfp3A4L4",
                    "name": "Amazon EC2 instances with Microsoft Windows Server end of support",
                    "description": "This check alerts you if the versions are near or have reached the end of support. Each Windows Server version offers 10 years of support, including 5 years of mainstream support and 5 years of extended support.  After the end of support, the Windows Server version won’t receive regular security updates. Running applications with unsupported Windows Server versions can bring security or compliance risks.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nRed: An EC2 instance has a Windows Server version that has reached end of support (Windows Server 2003, 2008, and 2008R2)<br/>\nYellow: An EC2 instance has a Windows Server version that will reach end of support in less than 18 months (Windows Server 2012 & 2012 R2)<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nConsider the following guidelines for end of support Windows Server EC2 instances:</br>\n<br/>\nTo modernize your Windows Server workloads, consider the various pathways available on the <a href=\"https://aws.amazon.com/windows/modernization/\" target=\"blank\">Modernize Windows Workloads with AWS</a> website.</br>\n<br/>\nTo upgrade your Windows Server workloads onto modern versions of Windows Server, consider using an automation runbook to simplify your upgrade. For more information, see the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/os-inplaceupgrade.html\" target=\"blank\">AWS Systems Manager documentation</a>.</br>\n<br/>\nIf you can’t upgrade your Windows Server workloads due to application incompatibilities, consider the End-of-Support Migration Program (EMP) for Windows Server. For more information on the program and tooling, see the <a href=\"https://aws.amazon.com/emp-windows-server/\" target=\"blank\">EMP website</a>. You can also purchase Extended Security Updates (ESU) from Microsoft for a maximum of 3 years after a product’s end of support date. <a href=\"https://aws.amazon.com/windows/faq/#eos-microsoft-products\" target=\"blank\">Learn more</a>.</br>\n",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Instance ID",
                            "Windows Server Version",
                            "Support Cycle",
                            "End of Support",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Qsdfp3A4L3",
                    "name": "Amazon EC2 instances with Microsoft SQL Server end of support",
                    "description": "Checks the SQL Server versions for Amazon Elastic Compute Cloud (Amazon EC2) instances running in the past 24 hours. This check alerts you if the versions are near or have reached the end of support. Each SQL Server version offers 10 years of support, including 5 years of mainstream support and 5 years of extended support. After the end of support, the SQL Server version won’t receive regular security updates. Running applications with unsupported SQL Server versions can bring security or compliance risks.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nRed: An EC2 instance has an SQL Server version that reached the end of support.<br/>\nYellow: An EC2 instance has an SQL Server version that will reach the end of support in 12 months.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nTo modernize your SQL Server workloads, consider refactoring to AWS Cloud native databases like Amazon Aurora. For more information, see <a href=\"https://aws.amazon.com/windows/modernization/\" target=\"blank\">Modernize Windows Workloads with AWS</a>.<br/>\nTo move to a fully managed database, consider replatforming to Amazon Relational Database Service (Amazon RDS). For more information, see <a href=\"https://aws.amazon.com/rds/sqlserver/\" target=\"blank\">RDS for SQL Server</a>.<br/>\nTo upgrade your SQL Server on EC2, consider using the automation runbook to simplify your upgrade. For more information, see the <a href=\"https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeSQLServer.html\" target=\"blank\">AWS Systems Manager documentation</a>.<br/>\nIf you can’t upgrade your SQL Server on EC2, consider the End-of-Support Migration Program (EMP) for Windows Server. For more information, see the <a href=\"https://aws.amazon.com/emp-windows-server/\" target=\"blank\">EMP Website</a><br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://aws.amazon.com/sql/sql2008-eos/\" target=\"blank\">Get ready for SQL Server end of support with AWS</a><br/>\n<a href=\"https://aws.amazon.com/sql/\" target=\"blank\">Microsoft SQL Server on AWS</a><br/>\n",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Instance ID",
                            "SQL Server Version",
                            "Support Cycle",
                            "End of Support",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G210",
                    "name": "CloudFront distributions should have logging enabled",
                    "description": "Checks to see if server access logging is enabled on Amazon CloudFront Distributions. The check will fail if access logging is not enabled for the distribution.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub control ID: CloudFront.5<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low. Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CloudFront.5/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G211",
                    "name": "S3 buckets with versioning enabled should have lifecycle policies configured",
                    "description": "Checks if Amazon Simple Storage Service (Amazon S3) version enabled buckets have lifecycle policy configured. This rule fails if Amazon S3 lifecycle policy is not enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: S3.10<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.10/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G212",
                    "name": "S3 buckets should have event notifications enabled",
                    "description": "Checks if S3 Event Notifications are enabled on an S3 bucket. This check fails if S3 Event Notifications are not enabled on a bucket.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: S3.11<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.11/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G213",
                    "name": "S3 access control lists (ACLs) should not be used to manage user access to buckets",
                    "description": "Checks if S3 buckets allow user permissions via access check lists (ACLs). This check fails if ACLs are configured for user access on S3 Bucket.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: S3.12<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/S3.12/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G214",
                    "name": "Network ACLs should not allow ingress from 0.0.0.0/0 to port 22 or port 3389",
                    "description": "Checks if a network access check list (NACL) allows unrestricted access to the default ports for SSH/RDP ingress traffic. The rule fails if a NACL inbound entry allows a source CIDR block of '0.0.0.0/0' or '::/0' for ports 22 or 3389<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EC2.21<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.21/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G215",
                    "name": "Unused EC2 security groups should be removed",
                    "description": "Checks that security groups are attached to Amazon EC2 instances or to an elastic network interface. The check will fail the security group is not associated with an Amazon EC2 instance or an elastic network interface.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: EC2.22<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/EC2.22/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G216",
                    "name": "ECR repositories should have at least one lifecycle policy configured",
                    "description": "Checks if an ECR repository has at least one lifecycle policy configured. This check fails if an ECR repository does not have any lifecycle policies configured.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: ECR.3<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/ECR.3/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Hs4Ma3G217",
                    "name": "CodeBuild project environments should have a logging configuration",
                    "description": "Checks if a CodeBuild project environment has at least one log option enabled.<br>\n<br>\n<h4 class='headerBodyStyle'>Source</h4><br>\n<a href=\"https://console.aws.amazon.com/securityhub/home\" target=\"_blank\">AWS Security Hub</a><br>\nSecurity Hub Control Id: CodeBuild.4<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Medium or Low Security Hub control failed.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nFollow the <a href=\"https://docs.aws.amazon.com/console/securityhub/CodeBuild.4/remediation\" target=\"_blank\">Security Hub documentation</a> to fix the issue.",
                    "category": "security",
                    "metadata": [
                            "Status",
                            "Region",
                            "Resource",
                            "Last Updated Time"
                    ]
                }
            ],
            "cost_optimizing": [
                {
                    "id": "COr6dfpM03",
                    "name": "Amazon EBS over-provisioned volumes",
                    "description": "Checks the Amazon Elastic Block Storage (Amazon EBS) volumes that were running at any time during the lookback period. This check alerts you if any EBS volumes were over-provisioned for your workloads. When you have over-provisioned volumes, you’re paying for unused resources. Although some scenarios can result in low optimization by design, you can often lower your costs by changing the configuration of your EBS volumes. Estimated monthly savings are calculated by using the current usage rate for EBS volumes. Actual savings will vary if the volume isn’t present for a full month.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Source</h4><br/>\nAWS Compute Optimizer<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: An EBS Volume that was over-provisioned during the lookback period. To determine if a volume is over-provisioned, we consider all default CloudWatch metrics (including IOPS and throughput). The algorithm used to identify over-provisioned EBS volumes follows AWS best practices. The algorithm is updated when a new pattern has been identified.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nConsider downsizing volumes that have low utilization.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\nFor more information about this recommendation, see the <a href=\"https://docs.aws.amazon.com/console/awssupport/trusted-advisor/compute-optimizer\" target=\"blank\">Trusted Advisor documentation.</a>.\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region/AZ",
                            "Volume ID",
                            "Volume Type",
                            "Volume Size(GB)",
                            "Volume Baseline IOPS",
                            "Volume Burst IOPS",
                            "Volume Baseline Throughput",
                            "Volume Burst Throughput",
                            "Recommended Volume Type",
                            "Recommended Volume Size(GB)",
                            "Recommended Volume Baseline IOPS",
                            "Recommended Volume Burst IOPS",
                            "Recommended Volume Baseline Throughput",
                            "Recommended Volume Burst Throughput",
                            "Lookback Period (days)",
                            "Savings Opportunity(%)",
                            "Estimated Monthly Savings",
                            "Estimated Monthly Savings Currency",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "COr6dfpM05",
                    "name": "AWS Lambda over-provisioned functions for memory size",
                    "description": "Checks the AWS Lambda functions that were invoked at least once during the lookback period. This check alerts you if any of your Lambda functions were over-provisioned for memory size. When you have Lambda functions that are over-provisioned for memory sizes, you’re paying for unused resources. Although some scenarios can result in low utilization by design, you can often lower your costs by changing the memory configuration of your Lambda functions. Estimated monthly savings are calculated by using the current usage rate for Lambda functions.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Source</h4><br/>\nAWS Compute Optimizer<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: A Lambda function that was over-provisioned for memory size during the lookback period. To determine if a Lambda function is over-provisioned, we consider all default CloudWatch metrics for that function. The algorithm used to identify over-provisioned Lambda functions for memory size follows AWS best practices. The algorithm is updated when a new pattern has been identified.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nConsider reducing the memory size of your Lambda functions.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\nFor more information about this recommendation, see the <a href=\"https://docs.aws.amazon.com/console/awssupport/trusted-advisor/compute-optimizer\" target=\"blank\">Trusted Advisor documentation page</a>.\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region/AZ",
                            "Function Name",
                            "Function Version",
                            "Memory Size(MB)",
                            "Recommended Memory Size(MB)",
                            "Lookback Period (days)",
                            "Savings Opportunity(%)",
                            "Estimated Monthly Savings",
                            "Estimated Monthly Savings Currency",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Wxdfp4B1L1",
                    "name": "AWS Well-Architected high risk issues for cost optimization",
                    "description": "Checks for high risk issues (HRIs) for your workloads in the cost optimization pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nRed: At least one active high risk issue was identified in the cost optimization pillar for AWS Well-Architected.<br>\nGreen: No active high risk issues were detected in the cost optimization pillar for AWS Well-Architected.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nAWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the <a href=\"https://console.aws.amazon.com/wellarchitected\" target=\"blank\">AWS Well-Architected</a> tool to review your answers and take action to resolve your active issues.",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Workload ARN",
                            "Workload Name",
                            "Reviewer Name",
                            "Workload Type",
                            "Workload Started Date",
                            "Workload Last Modified Date",
                            "Number of identified HRIs for Cost Optimization",
                            "Number of HRIs resolved for Cost Optimization",
                            "Number of questions answered for Cost Optimization",
                            "Total number of questions in Cost Optimization pillar",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "L4dfs2Q3C2",
                    "name": "AWS Lambda Functions with High Error Rates",
                    "description": "Checks for Lambda functions with high error rates that may result in high cost. Lambda charges based on the number of requests and aggregate execution time for your function. Function errors may cause retries that incur additional charges.<br/>\n<h4 class='headerBodyStyle'>Note:</h4> Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: Functions where > 10% of invocations end in error on any given day within the last 7 days.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br/>Consider the following guidelines to reduce errors. Function errors include errors returned by the function's code and errors returned by the function's runtime. To help you troubleshoot Lambda errors, Lambda integrates with services like Amazon CloudWatch and AWS X-Ray. You can use a combination of logs, metrics, alarms, and X-ray tracing to quickly detect and identify issues in your function code, API, or other resources that support your application. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html\" target=\"blank\">Monitoring and troubleshooting Lambda applications</a>. For more information on handling errors with specific runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html\" target=\"blank\">Error handling and automatic retries in AWS Lambda</a>. For additional troubleshooting, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html\" target=\"blank\">Troubleshooting issues in Lambda</a>.You can also choose from an ecosystem of monitoring and observability tools provided by AWS Lambda partners. For additional information about Partners, see <a href=\"https://aws.amazon.com/lambda/partners/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc\" target=\"blank\">AWS Lambda Partners</a>.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html\" target=\"blank\">Error Handling and Automatic  Retries in AWS Lambda</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html\" target=\"blank\">Monitoring and Troubleshooting Lambda applications</a><br/>\n<a href=\"https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-retry-timeout-sdk/\" target=\"blank\">Lambda Function Retry Timeout SDK</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html\" target=\"blank\">Troubleshooting  issues in Lambda</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_Errors\" target=\"blank\">API Invoke Errors</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/samples-errorprocessor.html\" target=\"blank\">Error Processor Sample Application for AWS Lambda</a><br/>\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Function ARN",
                            "Max Daily Error Rate",
                            "Date for Max Error Rate",
                            "Average Daily Error Rate",
                            "Lost Daily Compute Cost",
                            "Current Day Invokes",
                            "Current Day Error Rate",
                            "Average Daily Invokes",
                            "Last Refresh Time"
                    ]
                },
                {
                    "id": "L4dfs2Q3C3",
                    "name": "AWS Lambda Functions with Excessive Timeouts",
                    "description": "Checks for Lambda functions with high timeout rates that may result in high cost. Lambda charges based on execution time for your function and number of requests for your function. Function timeouts result in function errors that may cause retries that incur additional request and execution time charges.<br/>\n<h4 class='headerBodyStyle'>Note:</h4> Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: Functions where > 10% of invocations end in an error due to a timeout on any given day within the last 7 days.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nInspect function logging and X-ray traces to determine the contributor to the high function duration. Implement logging in your code at relevant parts, such as before or after API calls or database connections. By default, AWS SDK clients timeouts may be longer than the configured function duration. Adjust API and SDK connection clients to retry or fail within the function timeout. If the expected duration is longer than the configured timeout, you can increase the timeout setting for the function. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html\" target=\"blank\">Monitoring and troubleshooting Lambda applications</a>.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html\" target=\"blank\">Monitoring and troubleshooting Lambda applications</a><br/>\n<a href=\"https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-retry-timeout-sdk/\" target=\"blank\">Lambda Function Retry Timeout SDK</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\" target=\"blank\">Using AWS Lambda with AWS X-Ray</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html\" target=\"blank\">Accessing Amazon CloudWatch logs for AWS Lambda</a><br/>\n<a href=\"https://docs.aws.amazon.com/lambda/latest/dg/samples-errorprocessor.html\" target=\"blank\">Error Processor Sample Application for AWS Lambda</a><br/>\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Function ARN",
                            "Max Daily Timeout Rate",
                            "Date of Max Daily Timeout Rate",
                            "Average Daily Timeout Rate",
                            "Function Timeout Setting (millisecond)",
                            "Lost Daily Compute Cost",
                            "Average Daily Invokes",
                            "Current Day Invokes",
                            "Current Day Timeout Rate",
                            "Last Refresh Time"
                    ]
                },
                {
                    "id": "1e93e4c0b5",
                    "name": "Amazon EC2 Reserved Instance Lease Expiration",
                    "description": "Checks for Amazon EC2 Reserved Instances that are scheduled to expire within the next 30 days or have expired in the preceding 30 days. Reserved Instances do not renew automatically; you can continue using an EC2 instance covered by the reservation without interruption, but you will be charged On-Demand rates. New Reserved Instances can have the same parameters as the expired ones, or you can purchase Reserved Instances with different parameters.<br/>\r\nThe estimated monthly savings we show is the difference between the On-Demand and Reserved Instance rates for the same instance type.<br/><br/>\r\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\r\nYellow: The Reserved Instance lease expires in less than 30 days.<br/>\r\nYellow: The Reserved Instance lease expired in the preceding 30 days.<br/><br/>\r\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\r\nConsider purchasing a new Reserved Instance to replace the one that is nearing the end of its term. For more information, see <a href=\"https://aws.amazon.com/ec2/purchasing-options/reserved-instances/buyer/\" target=\"_blank\">How to Purchase Reserved Instances</a> and <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-concepts-buying.html\" target=\"_blank\">Buying Reserved Instances</a>.<br/><br/> \r\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\r\n<a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html\" target=\"_blank\">Reserved Instances</a><br/>\r\n<a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\" target=\"_blank\">Instance Types</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Zone",
                            "Instance Type",
                            "Platform",
                            "Instance Count",
                            "Current Monthly Cost",
                            "Estimated Monthly Savings",
                            "Expiration Date",
                            "Reserved Instance ID",
                            "Reason"
                    ]
                },
                {
                    "id": "DAvU99Dc4C",
                    "name": "Underutilized Amazon EBS Volumes",
                    "description": "Checks Amazon Elastic Block Store (Amazon EBS) volume configurations and warns when volumes appear to be underused. Charges begin when a volume is created. If a volume remains unattached or has very low write activity (excluding boot volumes) for a period of time, the volume is probably not being used.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: A volume is unattached or had less than 1 IOPS per day for the past 7 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nConsider creating a snapshot and deleting the volume to reduce costs. For more information, see <a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html\" target=\"_blank\">Creating an Amazon EBS Snapshot</a> and <a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-volume.html\" target=\"_blank\">Deleting an Amazon EBS Volume</a>.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html\" target=\"_blank\">Amazon Elastic Block Store (Amazon EBS)</a><br>\n<a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html\" target=\"_blank\">Monitoring the Status of Your Volumes</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Volume ID",
                            "Volume Name",
                            "Volume Type",
                            "Volume Size",
                            "Monthly Storage Cost",
                            "Snapshot ID",
                            "Snapshot Name",
                            "Snapshot Age"
                    ]
                },
                {
                    "id": "1qazXsw23e",
                    "name": "Amazon Relational Database Service (RDS) Reserved Instance Optimization",
                    "description": "Checks your usage of RDS and provides recommendations on purchase of Reserved Instances to help reduce costs incurred from using RDS On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Instance to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.<br/><br/>\r\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: Optimizing the purchase of RDS Reserved Instances can help reduce costs.<br/><br/>\r\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\r\nSee the <a href=\"http://console.aws.amazon.com/billing/home?/costexplorer#/costexplorer\" target=\"_blank\">Cost Explorer</a> page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase RDS Reserved Instances.\n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\nInformation on RDS Reserved Instances and how they can save you money can be found <a href=\"http://aws.amazon.com/rds/reserved-instances/\" target=\"_blank\">here</a>.<br>\nFor more information on this recommendation, see <a href=\"http://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/#Reserved_Instance_Optimization_Check_Questions\" target=\"_blank\">Reserved Instance Optimization Check Questions</a> in the Trusted Advisor FAQs.<br>\nFor more detailed description of fields, see <a href=\"http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationDetail.html#awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageUtilization\" target=\"_blank\">Cost Explorer documentation</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Family",
                            "Instance Type",
                            "License Model",
                            "Database Edition",
                            "Database Engine",
                            "Deployment Option",
                            "Recommended number of Reserved Instances to purchase",
                            "Expected Average Reserved Instance Utilization",
                            "Estimated Savings with Recommendation (monthly)",
                            "Upfront Cost of Reserved Instances",
                            "Estimated cost of Reserved Instances (monthly)",
                            "Estimated On-Demand Cost Post Recommended Reserved Instance Purchase (monthly)",
                            "Estimated Break Even (months)",
                            "Lookback Period (days)",
                            "Term (years)"
                    ]
                },
                {
                    "id": "hjLMh88uM8",
                    "name": "Idle Load Balancers",
                    "description": "Checks your Elastic Load Balancing configuration for load balancers that are not actively used. Any load balancer that is configured accrues charges. If a load balancer has no associated back-end instances or if network traffic is severely limited, the load balancer is not being used effectively.<br />\n<br />\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br />\nYellow: A load balancer has no active back-end instances.<br />\nYellow: A load balancer has no healthy back-end instances.<br />\nYellow: A load balancer has had less than 100 requests per day for the last 7 days.<br />\n<br />\n<h4 class='headerBodyStyle'>Recommended Action</h4><br />\nIf your load balancer has no active back-end instances, consider registering instances or deleting your load balancer. See <a href=\"http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/US_DeReg_Reg_Instances.html#RegisteringInstances\" target=\"_blank\">Registering Your Amazon EC2 Instances with Your Load Balancer</a> or <a href=\"http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html#delete-load-balancer\" target=\"_blank\">Delete Your Load Balancer</a>.<br />\nIf your load balancer has no healthy back-end instances, see <a href=\"http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ts-elb-healthcheck.html\" target=\"_blank\">Troubleshooting Elastic Load Balancing: Health Check Configuration</a>.<br />\nIf your load balancer has had a low request count, consider deleting your load balancer. See <a href=\"http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html#delete-load-balancer\" target=\"_blank\">Delete Your Load Balancer</a>.<br />\n<br />\n<h4 class='headerBodyStyle'>Additional Resources</h4><br />\n<a href=\"http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/UserScenarios.html\" target=\"_blank\">Managing Load Balancers</a><br />\n<a href=\"http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-troubleshooting.html\" target=\"_blank\">Troubleshoot Elastic Load Balancing</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Load Balancer Name",
                            "Reason",
                            "Estimated Monthly Savings"
                    ]
                },
                {
                    "id": "Ti39halfu8",
                    "name": "Amazon RDS Idle DB Instances",
                    "description": "Checks the configuration of your Amazon Relational Database Service (Amazon RDS) for any DB instances that appear to be idle. If a DB instance has not had a connection for a prolonged period of time, you can delete the instance to reduce costs. If persistent storage is needed for data on the instance, you can use lower-cost options such as taking and retaining a DB snapshot. Manually created DB snapshots are retained until you delete them.<br> \n<br> \n<h4 class='headerBodyStyle'>Alert Criteria</h4><br> \nYellow: An active DB instance has not had a connection in the last 7 days.<br> \n<br> \n<h4 class='headerBodyStyle'>Recommended Action</h4><br> \nConsider taking a snapshot of the idle DB instance and then either stopping it or deleting it. Stopping the DB instance removes some of the costs for it, but does not remove storage costs. A stopped instance keeps all automated backups based upon the configured retention period. Stopping a DB instance usually incurs additional costs when compared to deleting the instance and then retaining only the final snapshot. See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html\" target=\"_blank\">Stopping an Amazon RDS DB Instance Temporarily</a> and <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html\" target=\"_blank\">Deleting a DB Instance with a Final Snapshot</a>.<br> \n<br> \n<h4 class='headerBodyStyle'>Additional Resources</h4><br> \n<a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html\" target=\"_blank\">Back Up and Restore</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "DB Instance Name",
                            "Multi-AZ",
                            "Instance Type",
                            "Storage Provisioned (GB)",
                            "Days Since Last Connection",
                            "Estimated Monthly Savings (On Demand)"
                    ]
                },
                {
                    "id": "1qw23er45t",
                    "name": "Amazon Redshift Reserved Node Optimization",
                    "description": "Checks your usage of Redshift and provides recommendations on purchase of Reserved Nodes to help reduce costs incurred from using Redshift On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Nodes to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.<br/><br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>Yellow: Optimizing the purchase of Redshift Reserved Nodes can help reduce costs.<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>See the <a href=\"https://console.aws.amazon.com/billing/home?/costexplorer#/costexplorer\" target=\"_blank\">Cost Explorer</a> page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase Redshift Reserved Nodes.<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>Information on Redshift Reserved Nodes and how they can save you money can be found <a href=\"http://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html\" target=\"_blank\">here</a>.<br>\nFor more information on this recommendation, see <a href=\"http://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/#Reserved_Instance_Optimization_Check_Questions\" target=\"_blank\">Reserved Instance Optimization Check Questions</a> in the Trusted Advisor FAQs.<br/>\nFor more detailed description of fields, see <a href=\"http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationDetail.html#awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageUtilization\" target=\"_blank\">Cost Explorer documentation</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Family",
                            "Node Type",
                            "Recommended number of Reserved Nodes to purchase",
                            "Expected Average Reserved Node Utilization",
                            "Estimated Savings with Recommendation (monthly)",
                            "Upfront Cost of Reserved Nodes",
                            "Estimated cost of Reserved Nodes (monthly)",
                            "Estimated On-Demand Cost Post Recommended Reserved Nodes Purchase (monthly)",
                            "Estimated Break Even (months)",
                            "Lookback Period (days)",
                            "Term (years)"
                    ]
                },
                {
                    "id": "Cm24dfsM12",
                    "name": "Amazon Comprehend Underutilized Endpoints",
                    "description": "Checks the throughput configuration of your endpoints. This check alerts you when endpoints are not actively used for real-time inference requests. An endpoint that isn’t used for more than 15 consecutive days is considered underutilized. All endpoints accrue charges based on both the throughput set and the length of time that the endpoint is active.<br/>\n<h4 class='headerBodyStyle'>Note:</h4> This check is automatically refreshed once a day.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: The endpoint is active, but hasn’t been used for real-time inference requests in the past 15 days.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br/>If the endpoint hasn’t been used in the past 15 days, we recommend that you define a scaling policy for the resource by using <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-autoscaling.html\" target=\"blank\">Application Autoscaling.</a><br/>If the endpoint has a scaling policy defined and hasn’t been used in the past 30 days, consider deleting the endpoint and using asynchronous inference. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-delete.html\" target=\"blank\">Deleting an endpoint with Amazon Comprehend</a>.\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Endpoint ARN",
                            "Provisioned Inference Unit",
                            "AutoScaling Status",
                            "Reason",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "Z4AUBRNSmz",
                    "name": "Unassociated Elastic IP Addresses",
                    "description": "Checks for Elastic IP addresses (EIPs) that are not associated with a running Amazon Elastic Compute Cloud (Amazon EC2) instance. EIPs are static IP addresses designed for dynamic cloud computing. Unlike traditional static IP addresses, EIPs can mask the failure of an instance or Availability Zone by remapping a public IP address to another instance in your account. A nominal charge is imposed for an EIP that is not associated with a running instance.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: An allocated Elastic IP address (EIP) is not associated with a running Amazon EC2 instance.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nAssociate the EIP with a running active instance, or release the unassociated EIP. For more information, see <a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating-different\" target=\"_blank\">Associating an Elastic IP Address with a Different Running Instance</a> and <a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-releasing\" target=\"_blank\">Releasing an Elastic IP Address</a>.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html\" target=\"_blank\">Elastic IP Addresses</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "IP Address"
                    ]
                },
                {
                    "id": "7ujm6yhn5t",
                    "name": "Amazon OpenSearch Service Reserved Instance Optimization",
                    "description": "Checks your usage of Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) and provides recommendations on purchase of Reserved Instances to help reduce costs incurred from using Amazon OpenSearch Service On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Instance to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Optimizing the purchase of Amazon OpenSearch Service Reserved Instances can help reduce costs.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nSee the <a href=\"https://console.aws.amazon.com/billing/home?/costexplorer#/costexplorer\" target=\"_blank\">Cost Explorer</a> page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase Amazon OpenSearch Service Reserved Instances.<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\nInformation on Amazon OpenSearch Service Reserved Instances and how they can save you money can be found <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-ri.html\" target=\"_blank\">here</a>.<br>\nFor more information on this recommendation, see <a href=\"http://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/#Reserved_Instance_Optimization_Check_Questions\" target=\"_blank\">Reserved Instance Optimization Check Questions</a> in the Trusted Advisor FAQs.<br>\nFor more detailed description of fields, see <a href=\"http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationDetail.html#awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageUtilization\" target=\"_blank\">Cost Explorer documentation</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Instance Class",
                            "Instance Size",
                            "Recommended number of Reserved Instances to purchase",
                            "Expected Average Reserved Instance Utilization",
                            "Estimated Savings with Recommendation (monthly)",
                            "Upfront Cost of Reserved Instances",
                            "Estimated cost of Reserved Instances (monthly)",
                            "Estimated On-Demand Cost Post Recommended Reserved Instance Purchase (monthly)",
                            "Estimated Break Even (months)",
                            "Lookback Period (days)",
                            "Term (years)"
                    ]
                },
                {
                    "id": "Qch7DwouX1",
                    "name": "Low Utilization Amazon EC2 Instances",
                    "description": "Checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days and alerts you if the daily CPU utilization was 10% or less and network I/O was 5 MB or less on 4 or more days. Running instances generate hourly usage charges. Although some scenarios can result in low utilization by design, you can often lower your costs by managing the number and size of your instances.\n<br><br>\nEstimated monthly savings are calculated by using the current usage rate for On-Demand Instances and the estimated number of days the instance might be underutilized. Actual savings will vary if you are using Reserved Instances or Spot Instances, or if the instance is not running for a full day. To get daily utilization data, download the report for this check. \n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: An instance had 10% or less daily average CPU utilization and 5 MB or less network I/O on at least 4 of the previous 14 days.<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nConsider stopping or terminating instances that have low utilization, or scale the number of instances by using Auto Scaling. For more information, see <a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html\" target=\"_blank\">Stop and Start Your Instance</a>, <a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html\" target=\"_blank\">Terminate Your Instance</a>, and <a href=\"http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html\" target=\"_blank\">What is Auto Scaling?</a><br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br>\n<a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-monitoring.html\" target=\"_blank\">Monitoring Amazon EC2</a><br>\n<a href=\"http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html\" target=\"_blank\">Instance Metadata and User Data</a><br>\n<a href=\"http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/Welcome.html\" target=\"_blank\">Amazon CloudWatch Developer Guide</a><br>\n<a href=\"http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html\" target=\"_blank\">Auto Scaling Developer Guide</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region/AZ",
                            "Instance ID",
                            "Instance Name",
                            "Instance Type",
                            "Estimated Monthly Savings",
                            "Day 1",
                            "Day 2",
                            "Day 3",
                            "Day 4",
                            "Day 5",
                            "Day 6",
                            "Day 7",
                            "Day 8",
                            "Day 9",
                            "Day 10",
                            "Day 11",
                            "Day 12",
                            "Day 13",
                            "Day 14",
                            "14-Day Average CPU Utilization",
                            "14-Day Average Network I/O",
                            "Number of Days Low Utilization"
                    ]
                },
                {
                    "id": "G31sQ1E9U",
                    "name": "Underutilized Amazon Redshift Clusters",
                    "description": "Checks your Amazon Redshift configuration for clusters that appear to be underutilized. If an Amazon Redshift cluster has not had a connection for a prolonged period of time or is using a low amount of CPU, you can use lower-cost options such as downsizing the cluster or shutting down the cluster and taking a final snapshot. Final snapshots are retained even after you delete your cluster.<br/><br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: A running cluster has not had a connection in the last 7 days.<br/>\nYellow: A running cluster had less than 5% cluster-wide average CPU utilization for 99% of the last 7 days.<br/><br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nConsider shutting down the cluster and taking a final snapshot, or downsizing the cluster. See <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-mgmt-shutdown-delete-cluster\" target=\"_blank\">Shutting Down and Deleting Clusters</a> and <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-resize-intro\" target=\"_blank\">Resizing a Cluster</a>.<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/Welcome.html\" target=\"_blank\">Amazon CloudWatch Developer Guide</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Cluster",
                            "Instance Type",
                            "Reason",
                            "Estimated Monthly Savings"
                    ]
                },
                {
                    "id": "h3L1otH3re",
                    "name": "Amazon ElastiCache Reserved Node Optimization",
                    "description": "Checks your usage of ElastiCache and provides recommendations on purchase of Reserved Nodes to help reduce costs incurred from using ElastiCache On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Node to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br>\nYellow: Optimizing the purchase of ElastiCache Reserved Nodes can help reduce costs.\n<br><br>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br>\nSee the <a target=\"_blank\" href=\"http://console.aws.amazon.com/billing/home?/costexplorer#/costexplorer\">Cost Explorer</a> page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase ElastiCache Reserved Nodes.<br/><br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\nInformation on ElastiCache Reserved Nodes and how they can save you money can be found <a target=\"_blank\" href=\"http://aws.amazon.com/elasticache/reserved-cache-nodes/\">here</a>.<br>\nFor more information on this recommendation, see <a target=\"_blank\" href=\"http://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/#Reserved_Instance_Optimization_Check_Questions\">Reserved Instance Optimization Check Questions</a> in the Trusted Advisor FAQs.<br>\nFor more detailed description of fields, see <a target=\"_blank\" href=\"http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationDetail.html#awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageUtilization\">Cost Explorer documentation</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Family",
                            "Node Type",
                            "Product Description",
                            "Recommended number of Reserved Nodes to purchase",
                            "Expected Average Reserved Node Utilization",
                            "Estimated Savings with Recommendation (monthly)",
                            "Upfront Cost of Reserved Nodes",
                            "Estimated cost of Reserved Nodes (monthly)",
                            "Estimated On-Demand Cost Post Recommended Reserved Nodes Purchase (monthly)",
                            "Estimated Break Even (months)",
                            "Lookback Period (days)",
                            "Term (years)"
                    ]
                },
                {
                    "id": "vZ2c2W1srf",
                    "name": "Savings Plan",
                    "description": "Checks your usage of EC2, Fargate, and Lambda over the last 30 days and provides Savings Plan purchase recommendations, which allows you to commit to a consistent usage amount measured in $/hour for a one or three year term in exchange for discounted rates. These are sourced from AWS Cost Explorer which can be used to get more detailed recommendation information, or to purchase a savings plan. These recommendations should be considered an alternative to your RI recommendations and choosing to act fully on both sets of recommendations would likely lead to over commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account. \n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4>\n<br/>\nYellow: Optimizing the purchase of Savings Plans can help reduce costs.\n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br/>\nSee the <a href=\"https://console.aws.amazon.com/billing/home?/costexplorer#/costexplorer/\" target=\"_blank\">Cost Explorer</a> page for more detailed and customized recommendations and to purchase Savings Plans. \n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4>\n<br/>\nSavings Plan <a href=\"https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html\" target=\"_blank\">User Guide</a>\n<br/>\nSavings Plan <a href=\"https://aws.amazon.com/savingsplans/faq/\" target=\"_blank\">FAQ</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Savings Plan type",
                            "Payment option",
                            "Upfront cost",
                            "Hourly commitment to purchase",
                            "Estimated average utilization",
                            "Estimated Monthly Savings",
                            "Estimated savings percentage",
                            "Lookback Period (days)",
                            "Term (years)"
                    ]
                },
                {
                    "id": "Qsdfp3A4L1",
                    "name": "Amazon EC2 instances over-provisioned for Microsoft SQL Server",
                    "description": "Checks your Amazon Elastic Compute Cloud (Amazon EC2) instances that are running SQL Server in the past 24 hours. An SQL Server database has a compute capacity limit for each instance. An instance with SQL Server Standard edition can use up to 48 vCPUs. An instance with SQL Server Web can use up to 32 vCPUs. This check alerts you if an instance exceeds this vCPU limit.If your instance is over-provisioned, you pay full price without realizing an improvement in performance. You can manage the number and size of your instances to help lower costs. Estimated monthly savings are calculated by using the same instance family with the maximum number of vCPUs that an SQL Server instance can use and the On-Demand pricing. Actual savings will vary if you’re using Reserved Instances (RI) or if the instance isn’t running for a full day.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nRed: An instance with SQL Server Standard edition has more than 48 vCPUs.<br/>\nRed: An instance with SQL Server Web edition has more than 32 vCPUs.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nFor SQL Server Standard edition, consider changing to an instance in the same instance family with 48 vCPUs. For SQL Server Web edition, consider changing to an instance in the same instance family with 32 vCPUs. If it is memory intensive, consider changing to memory optimized R5 instances. For more information, see <a href=\"https://d1.awsstatic.com/whitepapers/best-practices-for-deploying-microsoft-sql-server-on-aws.pdf?did=wp_card&trk=wp_card\" target=\"blank\">Best Practices for Deploying Microsoft SQL Server on Amazon EC2.</a><br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://aws.amazon.com/sql/\" target=\"blank\">Microsoft SQL Server on AWS</a><br/>\nYou can use <a href=\"https://aws.amazon.com/launchwizard/\" target=\"blank\">Launch Wizard</a> to simplify your SQL Server deployment on EC2.<br/>\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Instance ID",
                            "Instance Type",
                            "vCPU",
                            "SQL Server Edition",
                            "Maximum vCPU",
                            "Recommended Instance Type",
                            "Estimated Monthly Savings",
                            "Last Updated Time"
                    ]
                },
                {
                    "id": "cX3c2R1chu",
                    "name": "Amazon EC2 Reserved Instances Optimization",
                    "description": "A significant part of using AWS involves balancing your Reserved Instance (RI) usage and your On-Demand instance usage. We provide recommendations on which RIs will help reduce costs incurred from using On-Demand instances.\n<br/>\nAWS generates these recommendations by analyzing your On-Demand usage for the past 30 days, and then categorizing the usage into eligible categories for reservations. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of RI to purchase to maximize your savings. This check covers recommendations based on Standard Reserved Instances with partial upfront payment option. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.\n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4>\n<br/>\nYellow: Optimizing the use of partial upfront RIs can help reduce costs.\n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br/>\nSee the <a href=\"https://aws.amazon.com/aws-cost-management/aws-cost-explorer/\" target=\"_blank\">Cost Explorer</a> page for more detailed and customized recommendations. Additionally, refer to the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html#ri-market-buying-guide\" target=\"_blank\">buying guide</a> to understand how to purchase RIs and the options available.\n<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4>\n<br/>\nInformation on RIs and how they can save you money can be found <a href=\"https://aws.amazon.com/ec2/pricing/reserved-instances/\" target=\"_blank\">here</a>.\n<br/>\nFor more information on this recommendation, see <a href=\"https://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/#Reserved_Instance_Optimization_Check_Questions\" target=\"_blank\">Reserved Instance Optimization Check Questions</a> in the Trusted Advisor FAQs.",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Region",
                            "Instance Type",
                            "Platform",
                            "Recommended Number of RIs to Purchase",
                            "Expected Average RI Utilization",
                            "Estimated Savings with Recommendation (monthly)",
                            "Upfront Cost of RIs",
                            "Estimated cost of RIs (monthly)",
                            "Estimated On-Demand Cost Post Recommended RI Purchase (monthly)",
                            "Estimated Break Even (months)",
                            "Lookback Period (days)",
                            "Term (years)"
                    ]
                },
                {
                    "id": "51fC20e7I2",
                    "name": "Amazon Route 53 Latency Resource Record Sets",
                    "description": "Checks for Amazon Route 53 latency record sets that are configured inefficiently. To allow Amazon Route 53 to route queries to the region with the lowest network latency, you should create latency resource record sets for a particular domain name (such as example.com) in different regions. If you create only one latency resource record set for a domain name, all queries are routed to one region, and you pay extra for latency-based routing without getting the benefits. Hosted zones created by AWS services won’t appear in your check results.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Alert Criteria</h4>\n<br>\nYellow: Only one latency resource record set is configured for a particular domain name.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Recommended Action</h4>\n<br>\nIf you have resources in multiple regions, be sure to define a latency resource record set for each region; see <a href=\"http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency\" target=\"_blank\">Latency-Based Routing</a>.<br>\nIf you have resources in only one region, consider creating resources in more than one region and define latency resource record sets for each; see <a href=\"http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency\" target=\"_blank\">Latency-Based Routing</a>.<br>\nIf you don't want to use multiple regions, you should use a simple resource record set; see  <a href=\"http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html\" target=\"_blank\">Working with Resource Record Sets</a>.\n<br>\n<br>\n<h4 class='headerBodyStyle'>Additional Resources</h4>\n<br>\n<a href=\"http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html\" target=\"_blank\">Amazon Route 53 Developer Guide</a><br>\n<a href=\"http://aws.amazon.com/route53/pricing/\" target=\"_blank\">Amazon Route 53 Pricing</a>",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Hosted Zone Name",
                            "Hosted Zone ID",
                            "Resource Record Set Name",
                            "Resource Record Set Type"
                    ]
                },
                {
                    "id": "Qsdfp3A4L2",
                    "name": "Amazon EC2 instances consolidation for Microsoft SQL Server",
                    "description": "Checks your Amazon Elastic Compute Cloud (Amazon EC2) instances that are running SQL Server in the past 24 hours. This check alerts you if your instance has less than the minimum number of SQL Server licenses. From the Microsoft SQL Server Licensing Guide, you are paying 4 vCPU licenses even if an instance has only 1 or 2 vCPUs. You can consolidate smaller SQL Server instances to help lower costs.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Alert Criteria</h4><br/>\nYellow: An instance with SQL Server has less than 4 vCPUs.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Recommended Action</h4><br/>\nConsider consolidating smaller SQL Server workloads into instances with at least 4 vCPUs.<br/>\n<br/>\n<h4 class='headerBodyStyle'>Additional Resources</h4><br/>\n<a href=\"https://aws.amazon.com/sql/\" target=\"blank\">Microsoft SQL Server on AWS</a><br/>\n<a href=\"https://aws.amazon.com/windows/resources/licensing/\" target=\"blank\">Microsoft Licensing on AWS</a><br/>\n<a href=\"https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing\" target=\"blank\">Microsoft SQL Server Licensing Guide</a><br/>\n",
                    "category": "cost_optimizing",
                    "metadata": [
                            "Status",
                            "Region",
                            "Instance ID",
                            "Instance Type",
                            "vCPU",
                            "Minimum vCPU",
                            "SQL Server Edition",
                            "Last Updated Time"
                    ]
                }
            ]
        }
    }
    return data


customer_ids = {
    "3dff95c1-12ff-48f9-9464-02e609bba998": "124dea25-9888-2123-9600-cvbcxb265676",
    "dde7e592-80a0-420a-ad82-df2dd6b6322b": "ac96551d-32ce-4010-ba1b-c86fc586c317",
    "602fbb3a-b688-4893-be3c-34bf26e80f8f": "bf3a79b1-9fa4-46ad-93e2-4d82912f281c",
    "7c2620c3-c1a3-484a-8f44-9298cd534d0d": "918ea26e-e482-428d-93b8-594f9c9f9038"
}

for customer_id, account_id in customer_ids.items():
    recommendation_data_list = []
    recommendation_data = generate_data_structure(account_id)
    recommendation_data_list.append(recommendation_data)

    insert_data_customer_db(customer_id, 'security_recommendations', recommendation_data_list)
