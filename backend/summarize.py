import requests
OLLAMA_URL = "http://ollama:11434/api/generate"
MODEL_NAME = "mistral"  # Change this to the desired model name [mistral, lamda2, etc.]

# System prompt for summarization context
system_prompt = """ 
You are an assistant that analyzes tax-related documents and generates a short summary.
Your goal is to:
- Keep the summary concise, focusing on the most important details.
- Highlight the most crucial points.
- If the document contains unclear information, highlight it without making assumptions.
- Respond in markdown format.
"""

# User prompt for summarizing document
user_prompt = """
You are looking at the following document. Please provide a short and clear summary:
"""

def generate_summary(input_text):
    """Generates a summary based on either plain text (chat) or PDF content."""
    try:
        # Generate the combined prompt based on the system and user instructions
        prompt = f"{system_prompt}\n\n{user_prompt}\n\n{input_text}\n\nSummary:"

        # Make the request to Ollama for summarization
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        if response.status_code == 200:
            # Check the response and get the summary
            result = response.json()
            summary = result.get("response", "No summary generated.")
            return summary
        else:
            return f"Error from Ollama API: {response.text}"

    except requests.exceptions.RequestException as e:
        # Handle any network issues or request errors
        return f"Request failed: {str(e)}"

    except Exception as e:
        # Handle any other exceptions that might arise
        return f"Error generating summary: {str(e)}"
