from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import models
from . import ut_sign, ut_helper,ut_service_1
import json


# 처음 화면
def Keyboard(request):

	return JsonResponse({
		'type' : 'buttons',
		'buttons' : [
				'로그인']
		})

# 기본 메뉴 리스트 전역 변수
basic_list = ['대학톡 헬퍼',
			'나의 시간표',
			'학점 계산기',
			'나의 대학정보',
			'버그신고 & 개발 내역',
			'홈으로']


@csrf_exempt
def Message(request): # 기본 메시지 처리 및 인증

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	# 인증된 사용자인지 확인
	if models.USER.objects.filter(USER_KEY = user_key).exists():

		# 사용자 정보 받아오기
		user = models.USER.objects.get(USER_KEY = user_key)
		user_s_1 = models.USER_SERVICE_1.objects.get(USER_KEY = user_key)

		# 가입 커맨드 처리 단계
		if user.USER_COMMAND == "가입중복방지커맨드인데 뚫을까봐 길게해놈":
			if models.USER.objects.filter(USER_NAME = content_name).exists():
				return ut_sign.sign_init_2()
			else :
				user.USER_NAME = content_name
				user.USER_COMMAND = "가입완료커멘드인데 이것도 뚫을까봐 길게해놈"
				user_s_1.USER_NAME = content_name
				user.save()
				user_s_1.save()
		# 사용자 인증을 받은 사람들은 무시하고 아래단계 진행 가능
		# 개발 중 접근 제한
		if user.USER_LEVEL < 10:
			return JsonResponse({
						"message":{
							"photo": {
								"url": "https://t1.daumcdn.net/cfile/tistory/9990A43E5B30D1A514",
								"width": 500,
								"height": 500
							},
							"text" :
								 "개발 중이므로 이용하실 수 없습니다."
							},
						'keyboard': {
							'type': 'buttons',
							'buttons': [
								'홈으로'
								]
							}
					})

		# 가장 먼저 입력값처리
		# Depth 1
		if user.USER_COMMAND == "가입완료커멘드인데 이것도 뚫을까봐 길게해놈" or content_name == "홈으로" or content_name == "버그신고 & 개발 내역":
			user.USER_COMMAND = "$홈으로"
			user.save()
		# Depth 2
		if content_name == "대학톡 헬퍼" or content_name == "나의 시간표" or content_name == "나의 대학정보":
			user.USER_COMMAND  = "$" + content_name
			user.save()
		# Depth Extra
		else :
			user.USER_COMMAND  = user.USER_COMMAND + "$" + content_name
			user.save()

		# 그 다음 사용자 입력 커맨딩
		try :
			user_command_1 = (user.USER_COMMAND).split('$')[1]
		except:
			user_command_1 = '-1'

		try :
			user_command_2 = (user.USER_COMMAND).split('$')[2]
		except:
			user_command_2 = '-1'

		try :
			user_command_3 = (user.USER_COMMAND).split('$')[3]
		except:
			user_command_3 = '-1'

		# 커맨드 처리 단계
		if user_command_1 == "홈으로":
			# 커맨드 초기화
			user.USER_COMMAND = ""
			user.save()

			return JsonResponse({
						"message":{
							"text" :
								 "대학톡 OPEN!"
							},
						'keyboard': {
							'type': 'buttons',
							'buttons': basic_list
							}
					})

		elif user_command_1 == "대학톡 헬퍼":
			return ut_helper.helper_init(user_key)

		elif user_command_1 == "나의 시간표":
			return ut_service_1.service_1_init(user_key)

		elif user_command_1 == "나의 대학정보":
			return ut_sign.sign_univ(user_key)

		elif user_command_1 == "버그신고 & 개발 내역":
			return JsonResponse({
				"message":{
					"text" :
						"1인 개발자 : 박현성\n"+
						"개발시작 : 2018.06.25\n"+
						"최근업데이트 : 2018.06.25\n"+
						"버전 : 0.0.1 Beta Version",
					"message_button":{
						"label": "개발자 페이스북",
						"url": "https://www.facebook.com/yolo.xsha"
						}
					},
				'keyboard': {
						'type': 'buttons',
						'buttons': ['홈으로']
						}
				})
		else : # Depth1 예외값 처리
			return JsonResponse({
						"message":{
							"text" :
								"[ " + user.USER_NAME + "님 환영합니다]"
							},
						'keyboard': {
							'type': 'buttons',
							'buttons': basic_list
							}
					})

	# 인증되지 않은 사용자 처리
	else :
		return ut_sign.sign_init(user_key)