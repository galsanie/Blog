from django.shortcuts import render
import requests
from django.http import JsonResponse

def member_list(request):
	user = request.user
	social_account = user.socialaccount_set.get(user=user.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)
	token = social_token.token

	url ="https://api.github.com/user/repos"
	response = requests.get(url, headers={"Authorization": "token "+token})
	return JsonResponse(response.json(), safe=False)


# Create your views here.
