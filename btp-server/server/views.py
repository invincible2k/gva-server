# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithFileField

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_geek (request) :

	# This will return Hello Geeks
	# string as HttpResponse
	return HttpResponse("Welcome")



def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})
