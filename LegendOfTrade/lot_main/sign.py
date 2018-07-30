from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models,views

# 가입 전 가입 확인
def signcheck(request):
	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	# 가입 중복 방지
	if models.User.objects.filter(userkey = user_key).exists():
		user = models.User.objects.get(userkey = user_key)
		return JsonResponse({
			"message":{
				"text" :
					user.name + "님 이미 가입되어있습니다.\n"+
					"LOT에서 좋은 시간 보내세요."
					},
			'keyboard': {
	            'type': 'buttons',
	            'buttons' : [
	                		'시작하기',
	                		'가입하기',
	                		'개발자도구',
	                		'개발내역']
	                }
            })
	else:
		return JsonResponse({
			"message":{
				"text" :
					"다음과 같이 입력\n" +
					"다르게 입력시 가입 취소\n\n"+
					"→ [가입] [닉네임]\n" +
					"예시 : 가입 ABC\n\n" +
					"-----------------\n" +
					"[가입약관]\n"+
					"가입 시 사용자 인증을 위해 사용자자의 식별번호를 부여받습니다.\n"+
					"게임에 영향을 미치는 행동은 로그를 수집하여 차단 및 법적 처리합니다."

					},
			'keyboard': {
					'type': 'text'
					}
            })

# 가입
def sign(request):

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	name = content_name.split(' ')[1]

	if models.User.objects.filter(name = name).exists():
		return JsonResponse({
			"message":{
				"text" :
					"ERROR : 중복된 닉네임 입니다.\n"+
					"-----------------\n\n" +
					"다음과 같이 입력\n" +
					"다르게 입력시 가입 취소\n\n"+
					"→ [가입] [닉네임]\n" +
					"예시 : 가입 ABC\n\n" +
					"-----------------\n" +
					"[가입약관]\n"+
					"가입 시 사용자 인증을 위해 사용자자의 식별번호를 부여받습니다. "+
					"게임에 영향을 미치는 행동은 로그를 수집하여 차단 및 법적 처리합니다."

					},
			'keyboard': {
					'type': 'text'
					}
            })
	else :
		models.User.objects.create(userkey = user_key, name= name, )
		models.Box.objects.create(userkey = user_key, )

		return JsonResponse({
			"message":{
				"text" :
					name + "님 가입완료되었습니다!\n"+
					"LOT에서 좋은 시간 보내세요."
					},
				'keyboard': {
		            		'type': 'buttons',
		                    'buttons' : [
		                    	'시작하기',
		                    	'가입하기',
		                    	'개발자도구',
		                    	'개발내역']
		                }
		})

# 시작 전 가입 확인
def check(request):

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	if models.User.objects.filter(userkey = user_key).exists():
		return 100
	else:
		return 200