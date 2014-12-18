from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .forms import SubjectForm
from .analyzer import POSTagger

def search(request):
	output = []
	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			sentence = POSTagger(form.cleaned_data['sentence'])
			sentence.processText()
			output = sentence.getSubject()
			return render(request, 'subject/hello.html', {'form': form, 'output': output})
		else:
			#return with *this field is required error
			return render(request, 'subject/hello.html', {'form': form, 'output': output})
	else:
		form = SubjectForm()
		return render(request, 'subject/hello.html', {'form': form, 'output': output})



'''
def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else: 
			message = 'You have searched for {0}'.format(request.GET['q'])
			return render(request, 'subject/hello.html', {'output': message})
	else:
		message = 'You have submitted an empty form'
		return render(request, 'subject/hello.html', {'output': message, 'error': error})
'''