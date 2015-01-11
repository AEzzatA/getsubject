from django.http import HttpResponse
from django.shortcuts import render
from .analyzer import POSTagger

def search(request):
	output = []
	if request.method == 'POST':
		form = request.POST['item_text']
		sentence = POSTagger(form)
		sentence.processText()
		output = sentence.getSubject()
		output = [str(x) for x in output]
		return render(request, 'subject/home.html',
			{'text': form, 'output': output})

	else:
		return render(request, 'subject/home.html',
			{'output': output,})

