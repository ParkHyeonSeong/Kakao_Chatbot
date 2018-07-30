from django.http import JsonResponse
from . import models
import random
import json

def recipe_new(content,user):

	try :
		user_command_2 = (user.COMMAND).split('#')[2]
	except:
		user_command_2 = '-1'

	if user_command_2 == "-1":
		return JsonResponse({
							"message":{
								"text" :
									"입력은 다음과 같습니다.\n\n"+
									"레시피 제목 : \n"+
									"요리 제목 : \n"+
									"아침,점심,저녁 : \n"+
									"재료 : \n"+
									"조리법 : \n\n"+
									"더 추가할 것들이 많습니다."

								},
							'keyboard': {
								'type': 'buttons',
								'buttons': add_menu
								}
						})


	return JsonResponse({
							"message":{
								"text" :
									"개발영역"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': home
								}
						})


add_menu = [
				'등록언제개발하냐...',
				'🔙 처음으로',
			]

home = ['🔙 처음으로']