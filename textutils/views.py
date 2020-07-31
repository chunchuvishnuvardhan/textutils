#vishnu
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse(home page)
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover=request.POST.get('spaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    #check with checkbox is on
    if removepunc=="on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
            'purpose': 'remove punctuations',
            'analyzed_text': analyzed
                 }
    #analyze the text
        return render(request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {
            'purpose': 'changed to UPPERCASE',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
             analyzed = analyzed + char
        params = {
            'purpose': 'removed new lines',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    if(spaceremover=='on'):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {
            'purpose': 'removed spaces',
            'analyzed_text': analyzed
        }
        return render(request,'analyze.html',params)
    if (charactercounter == 'on'):
      for char in djtext:
        analyzed =len(djtext)
        params = {
            'purpose': 'number of characetrs',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)



    else:
        return HttpResponse("error")

