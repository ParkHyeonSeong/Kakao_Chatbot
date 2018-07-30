from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from datetime import datetime

from . import models,lot_command_center
#from . import sales 2018.06.21 업데이트로 인해 제거됨

# 기본 인덱스 
def index(request):
	return HttpResponse("Welcome to Legend of Trade!")

# 처음 화면
def Keyboard(request):

	return JsonResponse({
		'type' : 'buttons',
		'buttons' : [
				'사용자인증']
		})

@csrf_exempt
def Message(request): # 기본 메시지 처리 및 인증
	
	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	# 사용자 정보가 등록되어 있을 때
	if models.User.objects.filter(userkey = user_key).exists():
		# 사용자 정보 가져오기
		user = models.User.objects.get(userkey = user_key)

		# 신규 커맨드 시
		if user.command == "100":
			# 닉네임 중복 시 에러
			if models.User.objects.filter(name = content_name).exists():
				return JsonResponse({
					"message":{
						"text" :
							"ERROR : 중복된 닉네임 입니다.\n"+
							"-----------------\n\n" +
							"게임에서 사용하실 닉네임을 입력해주세요\n" +
							"(최소 1글자 - 최대 5글자)\n\n"+
							"-----------------\n" +
							"[가입약관]\n"+
							"1. 가입 시 사용자 인증을 위해 사용자의 식별번호를 부여받습니다. "+
							"2. 게임에 영향을 미치는 행동에 대해 로그를 수집하고 싶지만 아직 구현을 못했습니다ㅠㅠ."

							},
					'keyboard': {
							'type': 'text'
							}
					})
			else : # 닉네임 성공
				# 사용자 창고 불러오기
				userbox = models.User_Box.objects.get(userkey = user_key)
				# 닉네임 할당
				user.name = content_name
				userbox.name = content_name
				# 접속 시작 인게임
				user.ingame = 1
				# 접속 시작 커맨드
				user.command = "$1000"
				user.save()
				userbox.save()
				return lot_command_center.Command_Center(request)

		# 신규 커맨드 외 모두
		else:
			'''
			# 패치중 접근 제한(#을 지우면 패치화면으로 넘어갑니다!)
			if user.level <= 5:
				return JsonResponse({
									"message":{
										"photo": {
											"url": "https://t1.daumcdn.net/cfile/tistory/99A0304B5B2CED8805",
											"width": 500,
											"height": 500
										},
										"text" :
											"※서버 패치중입니다※\n\n"+
											"[패치일정]\n"+
											"→ ~ 2018년 6월 23일 오전 2시\n\n"+
											"[패치내역]\n"+
											"→ 0.1.1버전에서 0.1.110버전으로 업데이트 및 본 서버 적용\n"	+
											"→ 새로운 버전업으로 인한 사용자 정보 초기화 예정\n"	
										},
										'keyboard': {
											'type': 'buttons',
											'buttons': [
											'사용자인증'
											]
										}
									})
			'''

			# 접속 시작 인게임
			user.ingame = 1
			# 접속 시작 커맨드
			user.save()
			return lot_command_center.Command_Center(request)

	# 사용자 정보가 없을 때
	else :
		temp_name = random.choice(range(0,2100000000))
		models.User.objects.create(userkey = user_key, name = temp_name, command = "100",)
		models.User_Bank.objects.create(userkey = user_key)
		models.User_Box.objects.create(userkey = user_key, name = temp_name,)


		return JsonResponse({
		"message":{
			"text" :
				"게임에서 사용하실 닉네임을 입력해주세요\n" +
				"(최소 1글자 - 최대 5글자)\n\n"+
				"-----------------\n" +
				"[가입약관]\n"+
				"1. 가입 시 사용자 인증을 위해 사용자의 식별번호를 부여받습니다. "+
				"2. 게임에 영향을 미치는 행동에 대해 로그를 수집하고 싶지만 아직 구현을 못했습니다ㅠㅠ."

				},
		'keyboard': {
				'type': 'text'
				}
		})

# 재화 업데이트 받기
@csrf_exempt
def update(request):

	message = request.body
	return_json_str = json.loads(message)
	G1_Update = return_json_str['G1']
	G3_Update = return_json_str['G3']
	G4_Update = return_json_str['G4']
	G5_Update = return_json_str['G5']

	# 업데이트 후 세이브
	G1 = models.Goods.objects.get(G_Code = "G1")
	G1.G_Price = G1_Update
	G1.save()

	G3 = models.Goods.objects.get(G_Code = "G3")
	G3.G_Price = G3_Update
	G3.save()

	G4 = models.Goods.objects.get(G_Code = "G4")
	G4.G_Price = G4_Update
	G4.save()

	G5 = models.Goods.objects.get(G_Code = "G5")
	G5.G_Price = G5_Update
	G5.save()



	print("G1 업데이트 값 변경함 : " + str(G1_Update))
	print("G3 업데이트 값 받음 : " + str(G3_Update))
	print("G4 업데이트 값 받음 : " + str(G4_Update))
	print("G5 업데이트 값 받음 : " + str(G5_Update))
	return JsonResponse({
				"message": "100"
	            })

























'''

	# 가입 커맨드 확인
	content_name_split = content_name.split(' ')[0]
	if content_name_split == "가입":
		# 리턴으로 함수호출안하면 오류납니다.
		return sign.sign(request)

	# 거래 시스템
	elif content_name_split == "거래":
		return sale.salemenu(request)

	elif content_name_split == "시세갱신":
		return sale.salerefresh(request)

	elif content_name_split == "매수":
		return sale.buy(request)

	elif content_name_split == "매도":
		return sale.sell(request)

	# 은행 시스템
	elif content_name_split == "은행":
		return bank.bank_init(request)

	# 랭킹 시스템
	elif content_name_split == "랭크":
		return rank.rank()

	else:

		# 오늘
		today = datetime.today()
		today_info = today.strftime('%Y-%m-%d, %H:%M:%S')

		# 처음화면으로
		if content_name == '처음으로':
			return JsonResponse({
				"message":{
				"text" : "처음으로 돌아갑니다."
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

		# 시작 관련
		elif (content_name == '시작하기') or (content_name == "돌아가기") or (content_name == "c") or (content_name == "ㅊ"):
			# 가입확인
			if sign.check(request) == 200:
				return JsonResponse({
				"message":{
				"text" : "가입된 사용자가 아닙니다."
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
				user = models.User.objects.get(userkey = user_key)
				return JsonResponse({
					"message":{
						"text" :
							 user.name + "님 접속을 환영합니다.\n"+
							"게임을 시작합니다."
						},
					'keyboard': {
		                        'type': 'buttons',
		                        'buttons': [
		                        '거래 TRADE',
		                        '은행 BANK',
		                        '뉴스 NEWS',
		                        '랭크 RANK',
		                        '처음으로']
		                }
					})

		# 거래 시스템 -> 2018.06.20 sale.py로 이전

		# 은행 관련 -> 2018.06.21 bank.py로 이전

		# 가입 관련

		elif content_name == '가입하기':
			return sign.signcheck(request)

		# 개발 관련

		elif content_name == "개발자도구":
			return JsonResponse({
				"message":{
					"text" :
						"개발자도구입니다."
					},
				'keyboard': {
					'type': 'text'
					}
				})

		elif content_name == '개발내역':
			return JsonResponse({
				"message":{
					"text" :
						"1인 개발자 : 박현성\n"+
						"개발시작 : 2018.06.19\n"+
						"버전 : 0.1v",
					"message_button":{
						"label": "개발자 페이스북",
						"url": "https://www.facebook.com/yolo.xsha"
						}
					},
				'keyboard': {
	                        'type': 'buttons',
	                        'buttons': ['처음으로']
	                }
				})

		else:
			return JsonResponse({
				"message":{
				"text" :
					"허용되지않은 접근입니다.\n"+
					"처음으로 돌아갑니다."
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


'''	