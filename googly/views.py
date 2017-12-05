from django.shortcuts import render
import requests
from django.http import JsonResponse

def place_text_search(request):
	key = "AIzaSyArvJSCSnsJmO5W4SnPxO-l_fdoSlKGMPg"
	query = request.GET.get('query', 'coded')
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?region=kw&query=%s&key=%s"%(query, key)

	next_page = request.GET.get('nextpage')
	if next_page is not None:
		url += "&pagetoken="+next_page

	response = requests.get(url)

	context= {
		"response": response.json()
	}

	return render(request, 'place_search.html', context)

	# return JsonResponse(response.json(), safe=False)

def place_detail(request):
    key = "AIzaSyBXdd6MXVCHSKeEyYez9CweEgdH81KCsa4"
    place_id = request.GET.get('place_id', '')
    url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key, place_id)
    response = requests.get(url)
    map_key = "AIzaSyClI-mSeak0nzukHkc_yXAzLvsfr1fn6Ps"

    context = {
    	"response": response.json(),
    	"map": map_key, 
    }

    return render(request, "place_detail.html", context)
    # return JsonResponse(response.json(), safe=False)

	# Create your views here.
