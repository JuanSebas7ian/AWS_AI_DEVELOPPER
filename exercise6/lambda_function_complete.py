import os
import json
import shutil
import sqlite3
from datetime import datetime

def get_available_vacations_days(employee_id):
    conn = sqlite3.connect('/tmp/employee_database.db')
    c = conn.cursor()

    if employee_id:
        c.execute("""
            SELECT employee_vacation_days_available
            FROM vacations
            WHERE employee_id = ?
            ORDER BY year DESC
            LIMIT 1
        """, (employee_id,))

        available_vacation_days = c.fetchone()

        if available_vacation_days:
            available_vacation_days = available_vacation_days[0]
            conn.close()
            return available_vacation_days
        else:
            conn.close()
            return f"No vacation data found for employee_id {employee_id}"
    else:
        conn.close()
        raise Exception("No employee id provided")

def lambda_handler(event, context):
    # Copy database to /tmp if it doesn't exist
    if not os.path.exists('/tmp/employee_database.db'):
        shutil.copy('employee_database.db', '/tmp/employee_database.db')
    
    agent = event['agent']
    action_group = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    
    # Convert parameters to dict
    params = {param['name']: param['value'] for param in parameters}
    
    if function == 'get_available_vacations_days':
        employee_id = params.get('employee_id')
        result = get_available_vacations_days(employee_id)
        
        return {
            'response': {
                'actionGroup': action_group,
                'function': function,
                'functionResponse': {
                    'responseBody': {
                        'TEXT': {
                            'body': str(result)
                        }
                    }
                }
            }
        }
    
    return {
        'response': {
            'actionGroup': action_group,
            'function': function,
            'functionResponse': {
                'responseBody': {
                    'TEXT': {
                        'body': f"Unknown function: {function}"
                    }
                }
            }
        }
    }