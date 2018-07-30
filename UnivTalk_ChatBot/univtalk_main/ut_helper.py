from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from . import models
import json

def helper_init(user_key):

	# 현재 시각정보 받아오기
	today = datetime.today()
	today_info = today.strftime('%Y.%m.%d.%H.%M')
	today_year = today_info.split('.')[0] + "년 "
	today_month = today_info.split('.')[1] + "월 "
	today_day = today_info.split('.')[2] + "일  "
	today_hour = today_info.split('.')[3] + "시 "
	today_minute = today_info.split('.')[4] + "분"
	today_info = today_year + today_month + today_day + today_hour + today_minute

	# 요일 체크를 위한 변수
	t = ['월', '화', '수', '목', '금', '토', '일']
	r = datetime.today().weekday()

	# 사용자 정보 및 시간표 가져오기
	user = models.USER.objects.get(USER_KEY = user_key)
	user_s_1 = models.USER_SERVICE_1.objects.get(USER_KEY = user_key)

	# 등록된 수업이 있는지 확인
	if user_s_1.USER_CLASS_NUM != 0:

		class_list = []

		if user_s_1.USER_CLASS_1_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY : # 요일 확인
				class_list.append(user_s_1.USER_CLASS_1_START + "/" + user_s_1.USER_CLASS_1_END + "/" + user_s_1.USER_CLASS_1_NAME + "/" + user_s_1.USER_CLASS_1_ROOM + "/" + user_s_1.USER_CLASS_1_MASTER)
		if user_s_1.USER_CLASS_2_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_2_START + "/" + user_s_1.USER_CLASS_2_END + "/" + user_s_1.USER_CLASS_2_NAME + "/" + user_s_1.USER_CLASS_2_ROOM + "/" + user_s_1.USER_CLASS_2_MASTER)
		if user_s_1.USER_CLASS_3_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_3_START + "/" + user_s_1.USER_CLASS_3_END + "/" + user_s_1.USER_CLASS_3_NAME + "/" + user_s_1.USER_CLASS_3_ROOM + "/" + user_s_1.USER_CLASS_3_MASTER)
		if user_s_1.USER_CLASS_4_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_4_START + "/" + user_s_1.USER_CLASS_4_END + "/" + user_s_1.USER_CLASS_4_NAME + "/" + user_s_1.USER_CLASS_4_ROOM + "/" + user_s_1.USER_CLASS_4_MASTER)
		if user_s_1.USER_CLASS_5_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_5_START + "/" + user_s_1.USER_CLASS_5_END + "/" + user_s_1.USER_CLASS_5_NAME + "/" + user_s_1.USER_CLASS_5_ROOM + "/" + user_s_1.USER_CLASS_5_MASTER)
		if user_s_1.USER_CLASS_6_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_6_START + "/" + user_s_1.USER_CLASS_6_END + "/" + user_s_1.USER_CLASS_6_NAME + "/" + user_s_1.USER_CLASS_6_ROOM + "/" + user_s_1.USER_CLASS_6_MASTER)
		if user_s_1.USER_CLASS_7_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_7_START + "/" + user_s_1.USER_CLASS_7_END + "/" + user_s_1.USER_CLASS_7_NAME + "/" + user_s_1.USER_CLASS_7_ROOM + "/" + user_s_1.USER_CLASS_7_MASTER)
		if user_s_1.USER_CLASS_8_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_8_START + "/" + user_s_1.USER_CLASS_8_END + "/" + user_s_1.USER_CLASS_8_NAME + "/" + user_s_1.USER_CLASS_8_ROOM + "/" + user_s_1.USER_CLASS_8_MASTER)
		if user_s_1.USER_CLASS_9_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_9_START + "/" + user_s_1.USER_CLASS_9_END + "/" + user_s_1.USER_CLASS_9_NAME + "/" + user_s_1.USER_CLASS_9_ROOM + "/" + user_s_1.USER_CLASS_9_MASTER)
		if user_s_1.USER_CLASS_10_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_10_START + "/" + user_s_1.USER_CLASS_10_END + "/" + user_s_1.USER_CLASS_10_NAME + "/" + user_s_1.USER_CLASS_10_ROOM + "/" + user_s_1.USER_CLASS_10_MASTER)
		if user_s_1.USER_CLASS_11_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_11_START + "/" + user_s_1.USER_CLASS_11_END + "/" + user_s_1.USER_CLASS_11_NAME + "/" + user_s_1.USER_CLASS_11_ROOM + "/" + user_s_1.USER_CLASS_1_MASTER)
		if user_s_1.USER_CLASS_12_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_12_START + "/" + user_s_1.USER_CLASS_12_END + "/" + user_s_1.USER_CLASS_12_NAME + "/" + user_s_1.USER_CLASS_12_ROOM + "/" + user_s_1.USER_CLASS_12_MASTER)
		if user_s_1.USER_CLASS_13_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_13_START + "/" + user_s_1.USER_CLASS_13_END + "/" + user_s_1.USER_CLASS_13_NAME + "/" + user_s_1.USER_CLASS_13_ROOM + "/" + user_s_1.USER_CLASS_13_MASTER)
		if user_s_1.USER_CLASS_14_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_14_START + "/" + user_s_1.USER_CLASS_14_END + "/" + user_s_1.USER_CLASS_14_NAME + "/" + user_s_1.USER_CLASS_14_ROOM + "/" + user_s_1.USER_CLASS_14_MASTER)
		if user_s_1.USER_CLASS_15_TEMP != 0:
			if t[r] == user_s_1.USER_CLASS_1_DAY :
				class_list.append(user_s_1.USER_CLASS_15_START + "/" + user_s_1.USER_CLASS_15_END + "/" + user_s_1.USER_CLASS_15_NAME + "/" + user_s_1.USER_CLASS_15_ROOM + "/" + user_s_1.USER_CLASS_15_MASTER)




		# 당일 수업이 있을 때
		if len(class_list) != 0:
			return JsonResponse({
				"message":{
					"text" :
						"오늘 수업은 " + str(len(class_list)) + "개 있네요!"
					},
				'keyboard': {
							'type': 'buttons',
							'buttons': ['홈으로']
						}
				})

		else :
			return JsonResponse({
				"message":{
					"text" :
						"오늘은 수업이 없네요!\n공강 너무 좋다!!"
					},
				'keyboard': {
							'type': 'buttons',
							'buttons': ['홈으로']
						}
				})


	else: # 등록된 수업이 없으므로 시간표 등록 할 것을 추천
		return JsonResponse({
			"message":{
				"text" :
					"분석할 데이터가 없습니다!\n시간표를 등록해주세요!"
				},
			'keyboard': {
						'type': 'buttons',
						'buttons': ['홈으로']
					}
			})

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