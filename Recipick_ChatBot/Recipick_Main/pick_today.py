from django.http import JsonResponse
from . import models
import random
import json

def today_pick(content,user):
	
	return JsonResponse({
							"message":{
								"text" :
									"개발중이므로 이용하실 수 없습니다."
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': home
								}
						})

home = ['🔙 처음으로']