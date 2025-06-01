def summarize_issues(issue_list):
    from utils.ollama_wrapper import query_ollama
    import json
    from collections import Counter

    # Assume issue_list is a list of dicts with a 'status' key
    statuses = [issue['status'] for issue in issue_list]
    total = len(statuses)
    status_counts = Counter(statuses)
    percentage_breakdown = {
        status: round((count / total) * 100)
        for status, count in status_counts.items()
    }
    # Combine counts and percentages for display
    counts_and_percentages = {
        status: {"count": status_counts[status], "percent": percentage_breakdown[status]}
        for status in status_counts
    }

    prompt = f"""
You are an AI assistant helping to generate a "Monthly Project Status Report" based on Jira issue data.

Summarize the following:
- Current Status of the project (e.g., new issues, resolved, still open)
- Risks and challenges faced
- Blockers or dependencies that need attention
- Breakdown by status category (To Do, In Progress, Done, etc.)

Output should be structured in valid JSON with:
- title: "Monthly Project Status Report"
- bullets: main sections with sub-bullets
- chart: pie chart info (labels, values and legend with %)

Only use the data below to generate the report. Do not add unrelated details.
Respond ONLY in this JSON format:
Respond ONLY in this JSON format:
{{
  "title": "...",
  "bullets": {{
  "Current Status": [...],
  "Key Themes": [...],
  "Risks": [...],
  "Blockers": [...]
  }}
  "chart": {{
    "labels": [...],
    "values": [...]
  }}
}}
Do NOT wrap any objects or arrays in quotes.
Below is the breakdown of issues by their status (count and percentage):
{json.dumps(counts_and_percentages, indent=2)}
"""
    summary = query_ollama(model="granite3.3:2b", prompt=prompt)
    return summary