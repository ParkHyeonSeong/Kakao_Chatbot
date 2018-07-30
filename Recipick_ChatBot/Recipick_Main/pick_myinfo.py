from django.http import JsonResponse
from . import models
import json

def myinfo(content,user):

	try :
		user_command_2 = (user.COMMAND).split('#')[2]
	except:
		user_command_2 = '-1'

	if user_command_2 == '-1':
		return JsonResponse({
							"message":{
								"text" :
									"내 닉네임 : " + user.NAME
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': my_menu
								}
						})

	elif user_command_2 == '닉네임변경':

		try :
			user_command_3 = (user.COMMAND).split('#')[3]
		except:
			user_command_3 = '-1'

		if user_command_3 == '-1':
			return JsonResponse({
								"message":{
									"text" :
										"변경할 닉네임을 입력해주세요.\n(10글자 이내)"
									},
								'keyboard': {
									'type': 'text'
									}
							})
		else:
			if models.USER.objects.filter(NAME = user_command_3).exists():	# 중복된 닉네임
				user.COMMAND = user.HISTORY	 # 커맨드 돌려놓고
				user.save()
				return JsonResponse({
							"message":{
								"text" :
									"🤔중복된 닉네임입니다\n\n"
									"내 닉네임 : " + user.NAME
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': my_menu
								}
						})

			else :	# 중복 아니면 등록
				user.NAME = content
				user.save()
				return JsonResponse({
							"message":{
								"text" :
									"내 닉네임 : " + user.NAME
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': my_menu
								}
						})


my_menu = [
			'닉네임변경',
			'🔙 처음으로'
			]
home = ['🔙 처음으로']