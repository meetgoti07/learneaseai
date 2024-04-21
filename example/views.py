from django.http import JsonResponse
import datetime
from .transcript import give_transscript
from .quiz import generate_quiz

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

# Add the csrf_exempt decorator if you're not including the CSRF token in your requests
@csrf_exempt
def transcript_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        video_path = data.get('url')
        if video_path:
            response = {}
            transcript = give_transscript(video_path)
            response['transcript'] = transcript
            quiz = generate_quiz(transcript)
            response['quiz'] = quiz
            return JsonResponse({'response': response})
        else:
            return HttpResponseBadRequest("URL not provided")
    else:
        return HttpResponseBadRequest("Invalid request method")