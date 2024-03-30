import requests
from django.http import JsonResponse
from collections import deque
from django.views.decorators.csrf import csrf_exempt

WINDOW_SIZE = 10

number_queue = deque(maxlen=WINDOW_SIZE)

@csrf_exempt
def number_average(request, number_id):
    if request.method == 'GET':
        # Fetch numbers from the test server
        try:
            response = requests.get(f'http://testserver/{number_id}')
            if response.status_code == 200:
                numbers = response.json().get('numbers', [])
                # Store unique numbers in the queue
                for num in numbers:
                    if num not in number_queue:
                        number_queue.append(num)
                # Calculate average of current window
                current_window = list(number_queue)
                if current_window:
                    average = sum(current_window) / len(current_window)
                else:
                    average = 0
                # Prepare response
                response_data = {
                    'numbers': numbers,
                    'windowPrevState': [],
                    'windowCurrState': current_window,
                    'avg': round(average, 2)
                }
                return JsonResponse(response_data, status=200)
            else:
                return JsonResponse({'error': 'Failed to fetch numbers from test server'}, status=500)
        except requests.RequestException:
            return JsonResponse({'error': 'Failed to connect to test server'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)