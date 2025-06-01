def generate_jql(task_description):
    from utils.ibm_watsonx_wrapper import query_ibm_watsonx
    from openai import OpenAI
    print(task_description)
    prompt = f"""
    You are a JQL expert assistant. Based on the following Task, generate only the correct Jira JQL.
    
    Guidelines:
    - To reference an Epic, use: "Epic Link" = EPIC-123
    - If filtering by multiple projects, use project in (ABC,XYZ)
    - Use double quotes around custom field names like "Epic Link"

    Do not use: issuelinkedto, epickey, Epic LinkedIn
    Do not include explanations - only return the JQL query string.
    Task: {task_description}
    JQL:
    """
    
    response = query_ibm_watsonx(prompt)
    return response
