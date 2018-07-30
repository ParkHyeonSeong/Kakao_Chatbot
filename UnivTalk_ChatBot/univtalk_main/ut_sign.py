from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import models
import random
import json

# 사용자 등록 기본
def sign_init(user_key):
	temp_name = random.choice(range(0,2100000000))
	models.USER.objects.create(USER_KEY = user_key, USER_NAME = temp_name, USER_COMMAND = "가입중복방지커맨드인데 뚫을까봐 길게해놈")
	models.USER_SERVICE_1.objects.create(USER_KEY = user_key, USER_NAME = temp_name,)

	return JsonResponse({
		"message":{
			"text" :
				"닉네임을 입력해주세요\n" +
				"(최소 3글자, 최대 5글자 예정)\n"+
				"-----------------\n" +
				"[가입약관]\n"+
				"1. 가입 시 사용자 인증을 위해 사용자의 식별번호를 부여받습니다.\n"+
				"2. 서버에 영향을 미치는 행동에 대해 로그를 수집하고 싶지만 아직 구현을 못했습니다ㅠㅠ."

				},
		'keyboard': {
				'type': 'text'
				}
		})

# 사용자 등록 중복
def sign_init_2():

	return JsonResponse({
		"message":{
			"text" :
				"(헉)ERROR : 중복된 닉네임 입니다\n"+
				"닉네임을 입력해주세요\n" +
				"(최소 3글자, 최대 5글자 예정)\n"+
				"-----------------\n" +
				"[가입약관]\n"+
				"1. 가입 시 사용자 인증을 위해 사용자의 식별번호를 부여받습니다.\n"+
				"2. 서버에 영향을 미치는 행동에 대해 로그를 수집하고 싶지만 아직 구현을 못했습니다ㅠㅠ."

				},
		'keyboard': {
				'type': 'text'
				}
		})


def sign_univ(user_key):

	# 사용자 정보 및 시간표 가져오기
	user = models.USER.objects.get(USER_KEY = user_key)

	# 나의 대학이 저장되어 있지 않은 경우
	if user.USER_UNIV != "-1":
		return JsonResponse({
					"message":{
						"text" :
							"대학목록이 추가될 예정입니다!\n가나다 순"
						},
					'keyboard': {
								'type': 'buttons',
								'buttons': [
								'고려대학교',
								'서울대학교',
								'순천향대학교',
								'연세대학교',
								'한양대학교'
								'홈으로']
							}
					})

	return JsonResponse({
				"message":{
					"text" :
						"대학이 등록되어 있습니다만\n구현을 안함ㅎ"
					},
				'keyboard': {
							'type': 'buttons',
							'buttons': [
							'홈으로']
						}
				})