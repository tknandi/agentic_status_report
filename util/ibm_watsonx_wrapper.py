def query_ibm_watsonx(prompt):
    import os
    from ibm_watsonx_ai import Credentials, APIClient
    from ibm_watsonx_ai.foundation_models import ModelInference
    from langchain_ibm import WatsonxLLM

    # Check required environment variables
    WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
    WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
    WATSONX_URL = os.getenv("WATSONX_URL")
    MODEL = os.getenv("MODEL")
    if not all([WATSONX_PROJECT_ID, WATSONX_API_KEY, WATSONX_URL, MODEL]):
        raise EnvironmentError("Missing one or more required WatsonX environment variables.")

    credentials = Credentials(
        url=WATSONX_URL,
        api_key=WATSONX_API_KEY
    )
    client = APIClient(credentials)

    model = ModelInference(
        model_id=MODEL,
        api_client=client,
        project_id=WATSONX_PROJECT_ID,
        params={
            "max_new_tokens": 500,
            "temperature": 0.2,
            "decoding_method": "greedy",
            "top_p": 0.9,
            "stop_sequences": []
        }
    )
    llm = WatsonxLLM(watsonx_model=model)
    try:
        response = llm.invoke(prompt)
        # Return the first non-empty line, or the whole response if empty
        for line in response.strip().split('\n'):
            if line.strip():
                return line.strip()
        return response.strip()
    except Exception as e:
        raise RuntimeError(f"WatsonX API call failed: {e}")
