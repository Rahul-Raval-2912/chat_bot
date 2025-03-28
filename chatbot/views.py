import requests
from django.shortcuts import render

def chat(request):
    response_text = ""
    if request.method == "POST":
        user_input = request.POST.get("message")
        
        # Hugging Face API configuration
        API_URL = "https://transformer.huggingface.co/doc/gpt2-large"
        headers = {
            "Authorization": "Bearer YOUR_HUGGING_FACE_API_TOKEN"
        }
        
        # Make API request
        payload = {"inputs": user_input}
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            response_text = response.json()[0]["generated_text"]
        else:
            response_text = "Sorry, I couldn't process that. Try again!"

    return render(request, 'chatbot/chat.html', {'response': response_text})