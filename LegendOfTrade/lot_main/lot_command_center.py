from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from datetime import datetime

from . import models,lot_rank,lot_bank,lot_market

@csrf_exempt
def Command_Center(request):

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	# 사용자 정보 가져오기
	user = models.User.objects.get(userkey = user_key)
	# 사용자 입력 -> 사용자 커맨드 저장
	# 사용자 커맨드 분리
	# 1레벨
	if content_name == '사용자인증' or content_name == '$메인메뉴'  or content_name == '$시작하기':
		user.command = '$1000'
		user.save()
	# 2레벨
	elif content_name == "$시장" or content_name == "$은행" or content_name == "$뉴스" or content_name == "$랭크" or content_name == '$버그신고&개발내역':
		user.command = content_name
		user.save()
	# 3레벨
	elif content_name == "$무역소" or content_name == "$아이템상점" :
		user.command = user.command + content_name
		user.save()
	# 4레벨
	elif content_name == "$시세갱신":
		# 시세갱신할 재화 저장
		temp = (user.command).split('$')[3]
		user.command = "$시장$무역소$" + temp
		user.save()
	# 입력레벨
	else :
		user.command = user.command + content_name
		user.save()

	# 커맨드 정보 스플릿
	try :
		user_command_1 = (user.command).split('$')[1]
	except:
		user_command_1 = '-1'

	try :
		user_command_2 = (user.command).split('$')[2]
	except:
		user_command_2 = '-1'

	try :
		user_command_3 = (user.command).split('$')[3]
	except:
		user_command_3 = '-1'


	# 사용자 정상 인게임 확인
	if user.ingame == 1:
		# 사용자 커맨드 확인
		if user_command_1 == "1000":
			user_total = models.User.objects.count()

			return JsonResponse({
							"message":{
								"photo": {
									"url": "https://t1.daumcdn.net/cfile/tistory/99094E445B2CC18F23",
									"width": 500,
									"height": 500
								},
								"text" :
									 "[" + user.name + "님 접속을 환영합니다]\n"+
									 "현재 유저수 : " + str(user_total) + "\n\n"
									"[새로운 소식]\n"+
									"☞ [NEW] 무역소 거래 시 손익분석이 가능합니다!\n"+
									"☞ [WAIT] 럭키박스 횟수가 제한될 예정입니다!\n"+
									"☞ [WAIT] 사용자 아이템 상점이 오픈될 예정입니다!\n"+
									"☞ 시세변동이 실시간을 가능합니다!\n"+
									"☞ 럭키박스 고급이 오픈되었습니다!\n"+
									"☞ 모든 스크립트가 개선되었습니다!\n"+
									"☞ 개인회생이 가능합니다!(은행)\n"+
									"\n"+
									"[게임 소식]\n"+
									"☞ 0.1.110버전으로 업데이트되었습니다.\n"+
									"☞ 새로운 기능을 적용하기 위해 사용자 정보차 초기화되었습니다(흑흑)\n"+
									"☞ 버그 발견 카카오톡 : HyeonE723"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': [
									'$시장',
									'$은행',
									#'$뉴스',
									'$랭크',
									'$버그신고&개발내역']
								}
						})

		# 시장 메뉴 진입
		elif user_command_1 == "시장":
			try :
				user_command_4 = (user.command).split('$')[4]
			except:
				user_command_4 = '-1'
			try :
				user_command_5 = (user.command).split('$')[5]
			except:
				user_command_5 = '-1'
			try :
				user_command_6 = (user.command).split('$')[6]
			except:
				user_command_6 = '-1'

			return lot_market.market_init(user_key,user_command_2,user_command_3,user_command_4,user_command_5,user_command_6)
		
		# 은행 메뉴 진입
		elif user_command_1 == "은행":
			return lot_bank.bank_init(user_key,user_command_2,user_command_3)

		elif user_command_1 == "뉴스":
			return lot_rank.rank(user_key)

		# 랭크 매뉴 진입
		elif user_command_1 == "랭크":
			return lot_rank.rank(user_key)

		# 개발내역 표시
		elif user_command_1 == '버그신고&개발내역':
			return JsonResponse({
				"message":{
					"text" :
						"1인 개발자 : 박현성\n"+
						"개발시작 : 2018.06.19\n"+
						"최근업데이트 : 2018.06.23\n"+
						"버전 : 0.1.110 Version",
					"message_button":{
						"label": "개발자 페이스북",
						"url": "https://www.facebook.com/yolo.xsha"
						}
					},
				'keyboard': {
	                        'type': 'buttons',
	                        'buttons': ['$메인메뉴']
	                }
				})

		else:
			return JsonResponse({
							"message":{
								"text" :
									"사용자인증에 성공하였습니다!"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': [
									'$시작하기']
								}
						})

	#기본 인게임 메뉴
	