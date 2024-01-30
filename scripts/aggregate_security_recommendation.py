from app.db_utility import get_database, insert_data_customer_db
from bs4 import BeautifulSoup


def extract_alert_action(recommendation, type):
    extracted_recommendation = []
    if type in recommendation:
        for d in recommendation[type]:
            description = d['description']
            soup = BeautifulSoup(description, 'html.parser')

            # Extract Alert Criteria
            alert_criteria_element = soup.find(
                'h4', class_='headerBodyStyle', text='Alert Criteria')
            if not alert_criteria_element:
                alert_criteria_element = soup.find('b', text='Alert Criteria')

            # Extract text after Alert Criteria
            alert_criteria = ''
            if alert_criteria_element:
                next_element = alert_criteria_element.find_next_siblings()
                for element in next_element:
                    if element.name in ['h4', 'b']:
                        break
                    alert_criteria += str(element.next_sibling).strip()

            # Extract Recommended Action
            recommended_action_element = soup.find(
                'h4', class_='headerBodyStyle', text='Recommended Action')
            if not recommended_action_element:
                recommended_action_element = soup.find(
                    'b', text='Recommended Action')

            # Extract text after Recommended Action
            recommended_action = ''
            if recommended_action_element:
                next_elements = recommended_action_element.find_next_siblings()
                for element in next_elements:
                    if element.name in ['h4', 'b']:
                        break
                    recommended_action += str(
                        element.next_sibling) if element.name == 'br' and element.next_sibling else str(element)

            # Remove unwanted characters in order to reduce token size
            removable_char = ['\n', '\r', '<br>', '<br/>']
            for element in removable_char:
                alert_criteria = alert_criteria.replace(element, '').strip()
                recommended_action = recommended_action.replace(
                    element, '').strip()

            security = {}
            security = {
                "name": d['name'],
                "alert_criteria": alert_criteria,
                "recommended_action": recommended_action
            }
            extracted_recommendation.append(security)
    return extracted_recommendation


def aggregated_security_recommendation():
    admin_db = get_database('admin')
    customers = admin_db['customers'].find()
    try:
        for customer in customers:
            customer_id = customer['customer_id']
            customer_db = get_database(customer_id)
            security_recommendation_data = customer_db['security_recommendations']

            for account_data in security_recommendation_data.find():
                account_id = account_data['account_id']
                recommendation = account_data['recommendations']
                aggregated_data = []
                new_formatted_data = {
                    "account_id": account_id,
                    "security_recommendation": "",
                    "cost_optimizing": ""
                }

                new_formatted_data['security_recommendation'] = extract_alert_action(
                    recommendation, 'security')
                new_formatted_data['cost_optimizing'] = extract_alert_action(
                    recommendation, 'cost_optimizing')
                aggregated_data.append(new_formatted_data)
                insert_data_customer_db(customer_id, 'aggregate_security_recommendations', aggregated_data, {
                    'account_id': account_id})
    except Exception as e:
        print(f"An error occurred: {e}")
