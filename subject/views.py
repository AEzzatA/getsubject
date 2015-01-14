from django.http import HttpResponse
from django.shortcuts import render
from .analyzer import POSTagger
from .models import Text

def search(request):
	output = []
	if request.method == 'POST':
		form = request.POST['item_text']
		#Save the sentence to the model for future test data
		s = Text.objects.create(text=form)
		s.save()
		sentence = POSTagger(form)
		sentence.processText()
		output = sentence.getSubject()
		output = [str(x) for x in output]
		return render(request, 'subject/home.html',
			{'text': form, 'output': output})

	else:
		return render(request, 'subject/home.html',
			{'output': output,})

def about(request):
	return render(request, 'subject/about.html')
