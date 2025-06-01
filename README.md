# agentic_status_report
# :brain: AI-Based Jira Project Status Reporter
This project uses AI agents to automate the generation of a monthly **executive status report** from Jira issues. The output is a visually formatted PowerPoint slide with summary bullets, a pie chart of issue breakdown, and a color-coded RAG status.

## :rocket: Features
- :mag: **Jira JQL Agent**: Determines the best JQL to query issues using a language model.
- :bar_chart: **Summary Agent**: Summarizes the Jira issues using LLM (Granite model).
- :art: **PowerPoint Agent**: Generates a one-slide `.pptx` with:
  - Bullets & sub-bullets
  - Pie chart for status category
    
## :bricks: Modular Agent Architecture
| Agent         | Description                             | Model Used          |
|---------------|-----------------------------------------|---------------------|
| `jql_agent.py`       | Infers JQL query for given context     | `granite3.3b` via Ollama |
| `summary_agent.py`   | Summarizes Jira issue data            | `granite3:3b` via Ollama` |
| `ppt_agent.py`       | Creates the PowerPoint slide          | Uses Python-pptx     |

## :open_file_folder: Project Structure
Here's a complete README.md for your modular AI-powered project that pulls Jira data, summarizes it, and generates a PowerPoint with an executive summary and RAG status:
# :brain: AI-Based Jira Project Status Reporter
This project uses AI agents to automate the generation of a monthly **executive status report** from Jira issues. The output is a visually formatted PowerPoint slide with summary bullets, a pie chart of issue breakdown, and a color-coded RAG status.

## :rocket: Features
- :mag: **Jira JQL Agent**: Determines the best JQL to query issues using a language model.
- :bar_chart: **Executive Summary Agent**: Summarizes the Jira issues using LLM (Granite model).
- :art: **PowerPoint Agent**: Generates a one-slide `.pptx` with:
  - Bullets & sub-bullets
  - Pie chart for status category

## :open_file_folder: Project Structure
. ├── main.py ├── jql_agent.py ├── summary_agent.py ├── ppt_agent.py ├── rag_agent.py ├── ollama_wrapper.py ├── summary.json ├── template.pptx ├── output.pptx ├── .env └── README.md
---
## :gear: Setup Instructions
1. **Install Dependencies**
```bash
pip install python-dotenv python-pptx openai requests
2. Configure Environment
Create a .env file:
JIRA_URL=https://yourdomain.atlassian.net
JIRA_TOKEN=your_jira_token
JIRA_USER=your_email@company.com
3. Provide the PowerPoint Template
Create template.pptx with a slide having:
A title
A content placeholder for bullets
Space for pie chart and RAG status (can be placed using fixed coordinates)

:arrow_forward: Run the Project
python main.py
This will:
1. Generate JQL.
2. Fetch Jira issues.
3. Summarize the data and infer RAG.
4. Create output.pptx.
---
:pushpin: Output Slide Content
:memo: Executive Summary (with bullets and sub-points)
:bar_chart: Pie Chart: Status Category Breakdown
