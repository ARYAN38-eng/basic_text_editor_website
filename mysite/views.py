# I have created this file - Aryan Raina 
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={"name":"Aryan Raina","place":"India"}
    return render(request,'index.html',params)
# def about(request):
#     return HttpResponse("Hello Aryan Raina! This is your about page!")

# def removepunc(request):
#     djtext=request.GET.get("text","default")
#     print(djtext)
#     return HttpResponse("remove punc")

def analyze(request):
    # Get the text
    djtext = request.GET.get("text", "default")
    
    # Get the checkbox values
    removepunc = request.GET.get("removepunc", "off")
    fullcaps = request.GET.get("fullcaps", "off")
    newlineremover = request.GET.get("newlineremover", "off")
    extraspaceremover = request.GET.get("extraspaceremover", "off")
    charcounter = request.GET.get("charcounter", "off")
    
    if djtext == "default":
        return HttpResponse("Error: Please enter text to analyze.")
    
    analyzed = djtext
    purpose = []

    # Perform tasks based on checkboxes
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"/\,<>.?@#$%^&*-_~`'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        purpose.append("Removed Punctuation")
    
    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose.append("Converted to Uppercase")
    
    if newlineremover == "on":
        analyzed = analyzed.replace("\n", "").replace("\r", "")
        purpose.append("Removed Newlines")
    
    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        purpose.append("Removed Extra Spaces")
    
    if charcounter == "on":
        char_count = len(analyzed.replace(" ", ""))
        purpose.append(f"Character Count: {char_count}")
    
    # If no options are selected
    if not purpose:
        return HttpResponse("Error: No actions selected!")

    # Prepare parameters for rendering
    params = {
        "purpose": ", ".join(purpose),
        "analyzed_text": analyzed
    }

    # Return the response
    return render(request, "analyze.html", params)

    
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("capitalize first")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount ")