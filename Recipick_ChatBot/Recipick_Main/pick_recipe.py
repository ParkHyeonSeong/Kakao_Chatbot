from django.http import JsonResponse
from . import models
import json

def recipe(content,user):

	try :
		user_command_2 = (user.COMMAND).split('#')[2]
	except:
		user_command_2 = '-1'

	try :
		user_command_3 = (user.COMMAND).split('#')[3]
	except:
		user_command_3 = '-1'

	try :
		user_command_4 = (user.COMMAND).split('#')[4]
	except:
		user_command_4 = '-1'

	recipe_info = models.RECIPE.objects.get(CHECK = int(user_command_2))
	recipe_list = []


	for i in range(1,21):
		try:
			recipe_list.append((recipe_info.ORDER_1).split("#")[i])
		except:
			recipe_list.append("-")



	if content == "다음으로":	# 레시피 이동
		user_command_3 = str(int(user_command_3) + 1)
		user.COMMAND = "#리딩중#" + user_command_2 + "#" + user_command_3
		user_command_4 = '-1'
		user.save()

	if content == "이전으로":	# 레시피 이동
		user_command_3 = str(int(user_command_3) - 1)
		user.COMMAND = "#리딩중#" + user_command_2 + "#" + user_command_3
		user_command_4 = '-1'
		user.save()

	if user_command_4 == "-1" :	# 레시피 정보를 표시합니다 

		if recipe_list[int(user_command_3)-1] != "-":	# 조리순서가 존재할 경우

			return JsonResponse({
									"message":{
										"text" : "맛있는 요리 만드는중...\n" + 
										"["+ user_command_3 +"] : " + recipe_list[int(user_command_3)-1]
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': [
													'다음으로',
													'이전으로',
													'🔙 처음으로'
													]
										}
								})
		else :	# 존재하지 않으면
			return JsonResponse({
								"message":{
									"text" :
										"요리가 완성되었다!"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': ['🔙 처음으로']
									}
							})



	return JsonResponse({
								"message":{
									"text" :
										"미구현 뎁스"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': ['🔙 처음으로']
									}
							})