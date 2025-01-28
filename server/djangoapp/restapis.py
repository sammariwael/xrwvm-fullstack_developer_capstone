# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv
import requests
from urllib.parse import urlencode

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    # Ensure the backend URL is correctly set
    #backend_url = "https://waelsammari2-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
    
    # Build the full request URL
    params = urlencode(kwargs)  # Safely encode query parameters
    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url += f"?{params}"
    
    print(f"GET from {request_url}")  # Debugging
    
    try:
        # Send GET request with a timeout
        response = requests.get(request_url, timeout=10)
        
        # Check if the request was successful
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 4xx, 5xx)
        
        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")  # Print detailed error
        return None

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
# Add code for retrieving sentiments

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
