from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reverse_text = user_text[::-1]
	user_text_list = user_text.split()
	number_words = len(user_text_list)
	if number_words == 1:
		s = ''
	else:
		s = 's'
	return render(request, 'reverse.html', {'usertext':user_text, 'reversetext':reverse_text, 'numberwords':number_words, 's':s})