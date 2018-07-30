from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from ipware.ip import get_ip
from . import pick_recipe
from . import pick_search
from . import pick_myinfo
from . import pick_today
from . import pick_new
from . import models
import random
import json

def index(request):	# 아이피 수집하기 주섬주섬
	ip = get_ip(request)
	if ip is not None:
	    print("잡았다 ip")
	    print("IP : " + ip)
	else:
	    print ("못찾았다")
	return render(request, 'Recipick_Main/index.html')


@csrf_exempt
def Keyboard(request):	# 카카오톡 서버 인증

	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['👋 레시픽, 오늘은 무얼 만들까?']
		})

@csrf_exempt
def Message(request):	# 메시지 처리

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	if models.USER.objects.filter(KEY = user_key).exists():	# 사용자 정보 확인
	
		user = models.USER.objects.get(KEY = user_key)	# 사용자 정보 받아옴

		if content == '👋 레시픽, 오늘은 무얼 만들까?' or content == "요리계속하기":

			if user.COOK == 1:
				user.COOK = 0
				if content == "요리계속하기" :
					user.COOK = 1
					return pick_recipe.recipe("하던중임을표시함", user)
				else :
					return JsonResponse({
									"message":{
										"text" :
											"만들던 요리가 있습니다!\n계속하시겠습니까?"
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': ['요리계속하기','🔙 처음으로']
										}
								})

				return JsonResponse({
									"message":{
										"text" :
											"🤗" + user.NAME + "님 반갑습니다🤗\n\n" +
											"📢 7월29일 1차 런칭에서 만나요~\n"
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': intro
										}
								})

		elif content == "🔙 처음으로":
			user.COMMAND = ""
			user.HISTORY = ""
			user.COOK = 0
			user.save()
			return JsonResponse({
							"message":{
								"text" :
										"🤗" + user.NAME + "님 반갑습니다🤗\n\n" +
										"📢 7월29일 1차 런칭에서 만나요~\n"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': intro
								}
						})


		# Depth 1
		if content == "🔥 오늘의 요리":
			user.COMMAND = "#" + content
			user.save()
			return pick_today.today_pick(content,user)

		elif content == "🔍 레시피 검색":
			user.COMMAND = "#" + content
			user.save()
			return pick_search.recipe_search(content,user)

		elif content == "📝 레시피 등록":

			if user.LEVEL < 11:	# 개발 중 접근 제한
				return JsonResponse({
							"message":{
								"photo": {
									"url": "https://t1.daumcdn.net/cfile/tistory/99F45D3F5B45E4C029",
									"width": 500,
									"height": 500
								},
								"text" :
									"레시피 등록은 금지💦\n" +
									"🤗정식 런칭을 기다려주세요🤗"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': intro
								}
						})

			user.COMMAND = "#" + content
			user.save()
			return pick_new.recipe_new(content,user)

		elif content == "🔑 내정보 관리":
			user.COMMAND = "#" + content
			user.save()
			return pick_myinfo.myinfo(content,user)


		elif content == "🚨 버그신고&개발내역":
			return JsonResponse({
							"message":{
								"photo": {
									"url": "https://t1.daumcdn.net/cfile/tistory/9955644B5B46034116",
									"width": 500,
									"height": 500
								},
								"text" :
									"개발자 : 박현성\n" +
									"개발버전 : 알파 버전\n" +
									"개발시작 : 2018년 7월 11일\n" +
									"업데이트 : 2018년 7월 20일\n" +
									"후원 : 신한은행 110-454-684364\n" +
									"광고문의 : yolo.xsha@gmail.com\n" +
									"개발자프로필 : https://github.com/ParkHyeonSeong"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': intro
								}
						})

		else :
			user.HISTORY = user.COMMAND
			user.COMMAND = user.COMMAND + "#" + content
			user.save()

			try :
				user_command_1 = (user.COMMAND).split('#')[1]
			except:
				user_command_1 = '-1'

			# Depth 2
			if user_command_1 == "🔥 오늘의 요리":
				return pick_today.today_pick(content,user)
			elif user_command_1 == "🔍 레시피 검색":
				return pick_search.recipe_search(content,user)
			elif user_command_1 == "📝 레시피 등록":
				return pick_new.recipe_new(content,user)
			elif user_command_1 == "🔑 내정보 관리":
				return pick_myinfo.myinfo(content,user)
			elif user_command_1 == "리딩중":
				return pick_recipe.recipe(content,user)
			else :
				return JsonResponse({
								"message":{
									"text" :
										"미구현 뎁스"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': intro
									}
							})

	else:	# 첫 사용자 정보 생성
		temp_name = random.choice(range(0,10000))
		while models.USER.objects.filter(CHECK = temp_name).exists():
			temp_name = random.choice(range(0,10000))

		models.USER.objects.create(KEY = user_key, NAME = temp_name)

		user = models.USER.objects.get(KEY = user_key)	# 사용자 정보 받아옴
		
		return JsonResponse({
						"message":{
							"text" :
								"👋첫 방문이시군요!\n" +
								"계정을 생성해드렸습니다!\n\n" +
								"임시 닉네임 : " + user.NAME + "\n" +
								"※ [내정보 관리]를 눌러 정보 변경을 해주세요!"

							},
						'keyboard': {
							'type': 'buttons',
							'buttons': intro
							}
					})



intro = [
			'🔥 오늘의 요리',
			'🔍 레시피 검색',
			'🎉 공지&이벤트',
			#'📝레시피 등록',
			'🔑 내정보 관리',
			'🚨 버그신고&개발내역'
		]

home = ['🔙 처음으로']