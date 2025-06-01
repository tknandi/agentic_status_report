def fetch_jira_issues(jql):
    import os
    import requests
    import re

    fields_to_quote = ["Epic Link", "Sprint Name"]
    JIRA_URL = os.getenv("JIRA_URL")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

    headers = { 
        "Authorization": f"Bearer {JIRA_API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(JIRA_URL, headers=headers)

    #print("Status Code:", response.status_code)
    #print("Response Body:", response.text)
    for field in fields_to_quote:
        if field in jql and f'"{field}"' not in jql:
            jql = jql.replace(field,f'"{field}"')
    response = requests.get(
        f"{JIRA_URL}rest/api/2/search?jql={jql}",
        headers=headers
    )

    response.raise_for_status()
    data = response.json()
    return data.get("issues",[])
