from agents.jql_agent import generate_jql
from agents.summary_agent import summarize_issues
from agents.ppt_agent import update_template
from utils.jira_api import fetch_jira_issues
import re
import json
from dotenv import load_dotenv

load_dotenv()

def main():
    task_description = (
        "Find all Stories only in projects AIWA, AIWB and AIWC that are linked to Epic Link AIWA-4388 and AIWC-10474."
    )
        
    # Agent 1 : JQL Generation
    jql = generate_jql(task_description)
    jql = re.sub("`","",jql)
    print("Generated JQL:", jql)

    # Fetch issues from Jira
    issues = fetch_jira_issues(jql)
    print(f"Fetched {len(issues)} issues from Jira")

    # Extract only key and status for summarization
    filtered_issues = [
        {"key": issue["key"], "status": issue["fields"]["status"]["name"]}
        for issue in issues
    ]

    # Agent 2 : Summarize the information
    summary = summarize_issues(filtered_issues)  # This is a string (JSON)
    print(summary)
    if isinstance(summary, str):
        summary = json.loads(summary)  # Convert string to dict

    # Save to JSON for later use
    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=2)



    # Agent 3 : Build PowerPoint presentation
    with open("summary.json", "r") as f:
        summary_data = json.load(f)  # This will be a dict, not a string
    result = update_template(summary_data, "template.pptx")
    if result["success"]:
        print("PowerPoint presentation created successfully.")
    else:
        print("Failed to create PowerPoint presentation:", result["error"])
    
if __name__ == "__main__":
    main()