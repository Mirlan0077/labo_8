from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def validate_numbers(a, b):
    try:
        a = float(a)
        b = float(b)
        return a, b
    except ValueError:
        return None

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a, b = data.get('A'), data.get('B')
            numbers = validate_numbers(a, b)
            if numbers:
                a, b = numbers
                return JsonResponse({"answer": a + b})
            else:
                return JsonResponse({"error": "Invalid input!"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON!"}, status=400)
    return JsonResponse({"error": "Invalid request method!"}, status=405)

@csrf_exempt
def subtract(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a, b = data.get('A'), data.get('B')
            numbers = validate_numbers(a, b)
            if numbers:
                a, b = numbers
                return JsonResponse({"answer": a - b})
            else:
                return JsonResponse({"error": "Invalid input!"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON!"}, status=400)
    return JsonResponse({"error": "Invalid request method!"}, status=405)

@csrf_exempt
def multiply(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a, b = data.get('A'), data.get('B')
            numbers = validate_numbers(a, b)
            if numbers:
                a, b = numbers
                return JsonResponse({"answer": a * b})
            else:
                return JsonResponse({"error": "Invalid input!"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON!"}, status=400)
    return JsonResponse({"error": "Invalid request method!"}, status=405)

@csrf_exempt
def divide(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a, b = data.get('A'), data.get('B')
            numbers = validate_numbers(a, b)
            if numbers:
                a, b = numbers
                if b == 0:
                    return JsonResponse({"error": "Division by zero!"}, status=400)
                return JsonResponse({"answer": a / b})
            else:
                return JsonResponse({"error": "Invalid input!"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON!"}, status=400)
    return JsonResponse({"error": "Invalid request method!"}, status=405)

def index(request):
    return render(request, 'index.html')
