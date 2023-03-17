import wikipedia, re
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

def wikiped(request: HttpRequest) -> HttpResponse:
    result = str()
    if request.POST:
        s = request.POST["i"]
        try:
            ny = wikipedia.page(s)
            wikitext = ny.content[:1000]
            wikimas = wikitext.split('.')
            wikimas = wikimas[:-1]
            wikitext2 = ''
            for x in wikimas:
                if not ('==' in x):
                    if (len((x.strip())) > 3):
                        wikitext2 = wikitext2 + x + '.'
                else:
                    break
            wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
            wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
            wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
            result = wikitext2
        except Exception as e:
            result = "No info"
            return render(request, "wik.html", {"result": result})
    return render(request, "wik.html", {"result": result})



