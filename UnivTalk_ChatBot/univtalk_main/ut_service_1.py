from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import models
import json

def service_1_init(user_key):

	# 사용자 정보 가져오기
	user = models.USER.objects.get(USER_KEY = user_key)
	user_s_1 = models.USER_SERVICE_1.objects.get(USER_KEY = user_key)

	# 커맨드 스플릿
	try :
		user_command_2 = (user.USER_COMMAND).split('$')[2]
	except:
		user_command_2 = '-1'

	try :
		user_command_3 = (user.USER_COMMAND).split('$')[3]
	except:
		user_command_3 = '-1'

	# 기본 메뉴 출력
	if user_command_2 == '-1':
		# 시간표를 1개라도 등록했는지 확인
		if user_s_1.USER_CLASS_NUM != 0:

			# 시간표 정보를 분석하여 표시해야함

			return JsonResponse({
								"message":{
									"text" :
										 "시간표 정보가 떠야하는데 개발아직 덜함"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'시간표 등록',
										'시간표 삭제',
										'시간표 수정[미구현]',
										'홈으로',
										]
									}
							})

		else: # 등록하지 않았다면 필수 등록 메뉴 호출

			return JsonResponse({
							"message":{
								"text" :
									 "시간표가 등록되지 않았습니다\n신규등록이 필요합니다!"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': [
									'시간표 등록',
									'홈으로',
									]
								}
						})

	elif user_command_2 == '시간표 등록':
		return service_1_add(user_key)
	elif user_command_2 == '시간표 삭제':
		return service_1_del(user_key)

def service_1_add(user_key):

	# 사용자 정보 가져오기
	user = models.USER.objects.get(USER_KEY = user_key)
	user_s_1 = models.USER_SERVICE_1.objects.get(USER_KEY = user_key)

	try :
		user_command_3 = (user.USER_COMMAND).split('$')[3]
	except:
		user_command_3 = '-1'

	try :
		user_command_4 = (user.USER_COMMAND).split('$')[4]
	except:
		user_command_4 = '-1'

	try :
		user_command_5 = (user.USER_COMMAND).split('$')[5]
	except:
		user_command_5 = '-1'

	try :
		user_command_6 = (user.USER_COMMAND).split('$')[6]
	except:
		user_command_6 = '-1'

	try :
		user_command_7 = (user.USER_COMMAND).split('$')[7]
	except:
		user_command_7 = '-1'

	try :
		user_command_8 = (user.USER_COMMAND).split('$')[8]
	except:
		user_command_8 = '-1'

	# 요일 설정
	if user_command_3 == '-1':
		return JsonResponse({
								"message":{
									"text" :
										 "요일 설정"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'월',
										'화',
										'수',
										'목',
										'금',
										'홈으로'
										]
									}
							})

	else :
		# 시작 시간 설정
		if user_command_4 == '-1':
			return JsonResponse({
								"message":{
									"text" :
										 "시작 시간을 선택해주세요"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'1) 오전 9시 00분',
										'2) 오전 9시 30분',
										'3) 오전 10시 00분',
										'4) 오전 10시 30분',
										'5) 오전 11시 00분',
										'6) 오전 11시 30분',
										'7) 오전 12시 00분',
										'8) 오전 12시 30분',
										'9) 오후 1시 00분',
										'10) 오후 1시 30분',
										'11) 오후 2시 00분',
										'12) 오후 2시 30분',
										'13) 오후 3시 00분',
										'14) 오후 3시 30분',
										'15) 오후 4시 00분',
										'16) 오후 4시 30분',
										'17) 오후 5시 00분',
										'18) 오후 5시 30분',
										'19) 오후 6시 00분',
										'20) 오후 6시 30분',
										'21) 오후 7시 00분',
										'22) 오후 7시 30분',
										'홈으로'
										]
									}
							})

		else :
			# 끝나는 시간 설정
			if user_command_5 == '-1':
				return JsonResponse({
								"message":{
									"text" :
										 "종료 시간을 선택해주세요"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'1) 오전 9시 00분',
										'2) 오전 9시 30분',
										'3) 오전 10시 00분',
										'4) 오전 10시 30분',
										'5) 오전 11시 00분',
										'6) 오전 11시 30분',
										'7) 오전 12시 00분',
										'8) 오전 12시 30분',
										'9) 오후 1시 00분',
										'10) 오후 1시 30분',
										'11) 오후 2시 00분',
										'12) 오후 2시 30분',
										'13) 오후 3시 00분',
										'14) 오후 3시 30분',
										'15) 오후 4시 00분',
										'16) 오후 4시 30분',
										'17) 오후 5시 00분',
										'18) 오후 5시 30분',
										'19) 오후 6시 00분',
										'20) 오후 6시 30분',
										'21) 오후 7시 00분',
										'22) 오후 7시 30분',
										'홈으로'
										]
									}
							})

			else :
				# 시작시간과 끝나는 시간의 차이가 올바른지 확인
				if int(user_command_4.split(')')[0]) < int(user_command_5.split(')')[0]):

					# 강의이름을 등록
					if user_command_6 == "-1":
						return JsonResponse({
						"message":{
							"text" :
								"강의 이름을 적어주세요"

							},
						'keyboard': {
							'type': 'text'
							}
						})

					else :
						# 강의 교실 설정
						if user_command_7 == "-1":
							return JsonResponse({
								"message":{
									"text" :
										"강의 교실을 적어주세요"

									},
								'keyboard': {
									'type': 'text'
									}
								})

						else :
							# 교수님 이름
							if user_command_8 == "-1":
								return JsonResponse({
									"message":{
										"text" :
											"교수님 성함"

										},
									'keyboard': {
										'type': 'text'
										}
									})
							else :
								# 저장 단계
								# 3 요일
								# 4 시작 5 끝
								# 6 강의 이름
								# 7 강의 교실
								# 8 교수 성함
								user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM + 1
								# 순서대로 채워넣기 위해서... 효율성이 딸림
								if user_s_1.USER_CLASS_1_TEMP == 0:
									user_s_1.USER_CLASS_1_DAY = user_command_3
									user_s_1.USER_CLASS_1_START = user_command_4
									user_s_1.USER_CLASS_1_END = user_command_5
									user_s_1.USER_CLASS_1_NAME = user_command_6
									user_s_1.USER_CLASS_1_ROOM = user_command_7
									user_s_1.USER_CLASS_1_MASTER = user_command_8
									user_s_1.USER_CLASS_1_TEMP = 1
								elif user_s_1.USER_CLASS_2_TEMP == 0:
									user_s_1.USER_CLASS_2_DAY = user_command_3
									user_s_1.USER_CLASS_2_START = user_command_4
									user_s_1.USER_CLASS_2_END = user_command_5
									user_s_1.USER_CLASS_2_NAME = user_command_6
									user_s_1.USER_CLASS_2_ROOM = user_command_7
									user_s_1.USER_CLASS_2_MASTER = user_command_8
									user_s_1.USER_CLASS_2_TEMP = 1
								elif user_s_1.USER_CLASS_3_TEMP == 0:
									user_s_1.USER_CLASS_3_DAY = user_command_3
									user_s_1.USER_CLASS_3_START = user_command_4
									user_s_1.USER_CLASS_3_END = user_command_5
									user_s_1.USER_CLASS_3_NAME = user_command_6
									user_s_1.USER_CLASS_3_ROOM = user_command_7
									user_s_1.USER_CLASS_3_MASTER = user_command_8
									user_s_1.USER_CLASS_3_TEMP = 1 
								elif user_s_1.USER_CLASS_4_TEMP == 0:
									user_s_1.USER_CLASS_4_DAY = user_command_3
									user_s_1.USER_CLASS_4_START = user_command_4
									user_s_1.USER_CLASS_4_END = user_command_5
									user_s_1.USER_CLASS_4_NAME = user_command_6
									user_s_1.USER_CLASS_4_ROOM = user_command_7
									user_s_1.USER_CLASS_4_MASTER = user_command_8
									user_s_1.USER_CLASS_4_TEMP = 1
								elif user_s_1.USER_CLASS_5_TEMP == 0:
									user_s_1.USER_CLASS_5_DAY = user_command_3
									user_s_1.USER_CLASS_5_START = user_command_4
									user_s_1.USER_CLASS_5_END = user_command_5
									user_s_1.USER_CLASS_5_NAME = user_command_6
									user_s_1.USER_CLASS_5_ROOM = user_command_7
									user_s_1.USER_CLASS_5_MASTER = user_command_8
									user_s_1.USER_CLASS_5_TEMP = 1
								elif user_s_1.USER_CLASS_6_TEMP == 0:
									user_s_1.USER_CLASS_6_DAY = user_command_3
									user_s_1.USER_CLASS_6_START = user_command_4
									user_s_1.USER_CLASS_6_END = user_command_5
									user_s_1.USER_CLASS_6_NAME = user_command_6
									user_s_1.USER_CLASS_6_ROOM = user_command_7
									user_s_1.USER_CLASS_6_MASTER = user_command_8
									user_s_1.USER_CLASS_6_TEMP = 1 
								elif user_s_1.USER_CLASS_7_TEMP == 0:
									user_s_1.USER_CLASS_7_DAY = user_command_3
									user_s_1.USER_CLASS_7_START = user_command_4
									user_s_1.USER_CLASS_7_END = user_command_5
									user_s_1.USER_CLASS_7_NAME = user_command_6
									user_s_1.USER_CLASS_7_ROOM = user_command_7
									user_s_1.USER_CLASS_7_MASTER = user_command_8
									user_s_1.USER_CLASS_7_TEMP = 1 
								elif user_s_1.USER_CLASS_8_TEMP == 0:
									user_s_1.USER_CLASS_8_DAY = user_command_3
									user_s_1.USER_CLASS_8_START = user_command_4
									user_s_1.USER_CLASS_8_END = user_command_5
									user_s_1.USER_CLASS_8_NAME = user_command_6
									user_s_1.USER_CLASS_8_ROOM = user_command_7
									user_s_1.USER_CLASS_8_MASTER = user_command_8
									user_s_1.USER_CLASS_8_TEMP = 1 
								elif user_s_1.USER_CLASS_9_TEMP == 0:
									user_s_1.USER_CLASS_9_DAY = user_command_3
									user_s_1.USER_CLASS_9_START = user_command_4
									user_s_1.USER_CLASS_9_END = user_command_5
									user_s_1.USER_CLASS_9_NAME = user_command_6
									user_s_1.USER_CLASS_9_ROOM = user_command_7
									user_s_1.USER_CLASS_9_MASTER = user_command_8
									user_s_1.USER_CLASS_9_TEMP = 1 
								elif user_s_1.USER_CLASS_9_TEMP == 0:
									user_s_1.USER_CLASS_9_DAY = user_command_3
									user_s_1.USER_CLASS_9_START = user_command_4
									user_s_1.USER_CLASS_9_END = user_command_5
									user_s_1.USER_CLASS_9_NAME = user_command_6
									user_s_1.USER_CLASS_9_ROOM = user_command_7
									user_s_1.USER_CLASS_9_MASTER = user_command_8
									user_s_1.USER_CLASS_9_TEMP = 1 
								elif user_s_1.USER_CLASS_10_TEMP == 0:
									user_s_1.USER_CLASS_10_DAY = user_command_3
									user_s_1.USER_CLASS_10_START = user_command_4
									user_s_1.USER_CLASS_10_END = user_command_5
									user_s_1.USER_CLASS_10_NAME = user_command_6
									user_s_1.USER_CLASS_10_ROOM = user_command_7
									user_s_1.USER_CLASS_10_MASTER = user_command_8
									user_s_1.USER_CLASS_10_TEMP = 1 
								elif user_s_1.USER_CLASS_11_TEMP == 0:
									user_s_1.USER_CLASS_11_DAY = user_command_3
									user_s_1.USER_CLASS_11_START = user_command_4
									user_s_1.USER_CLASS_11_END = user_command_5
									user_s_1.USER_CLASS_11_NAME = user_command_6
									user_s_1.USER_CLASS_11_ROOM = user_command_7
									user_s_1.USER_CLASS_11_MASTER = user_command_8
									user_s_1.USER_CLASS_11_TEMP = 1 
								elif user_s_1.USER_CLASS_12_TEMP == 0:
									user_s_1.USER_CLASS_12_DAY = user_command_3
									user_s_1.USER_CLASS_12_START = user_command_4
									user_s_1.USER_CLASS_12_END = user_command_5
									user_s_1.USER_CLASS_12_NAME = user_command_6
									user_s_1.USER_CLASS_12_ROOM = user_command_7
									user_s_1.USER_CLASS_12_MASTER = user_command_8
									user_s_1.USER_CLASS_12_TEMP = 1 
								elif user_s_1.USER_CLASS_13_TEMP == 0:
									user_s_1.USER_CLASS_13_DAY = user_command_3
									user_s_1.USER_CLASS_13_START = user_command_4
									user_s_1.USER_CLASS_13_END = user_command_5
									user_s_1.USER_CLASS_13_NAME = user_command_6
									user_s_1.USER_CLASS_13_ROOM = user_command_7
									user_s_1.USER_CLASS_13_MASTER = user_command_8
									user_s_1.USER_CLASS_13_TEMP = 1 
								elif user_s_1.USER_CLASS_14_TEMP == 0:
									user_s_1.USER_CLASS_14_DAY = user_command_3
									user_s_1.USER_CLASS_14_START = user_command_4
									user_s_1.USER_CLASS_14_END = user_command_5
									user_s_1.USER_CLASS_14_NAME = user_command_6
									user_s_1.USER_CLASS_14_ROOM = user_command_7
									user_s_1.USER_CLASS_14_MASTER = user_command_8
									user_s_1.USER_CLASS_14_TEMP = 1 
								elif user_s_1.USER_CLASS_15_TEMP == 0:
									user_s_1.USER_CLASS_15_DAY = user_command_3
									user_s_1.USER_CLASS_15_START = user_command_4
									user_s_1.USER_CLASS_15_END = user_command_5
									user_s_1.USER_CLASS_15_NAME = user_command_6
									user_s_1.USER_CLASS_15_ROOM = user_command_7
									user_s_1.USER_CLASS_15_MASTER = user_command_8
									user_s_1.USER_CLASS_15_TEMP = 1 
								

								user_s_1.save()


								return JsonResponse({
										"message":{
											"text" :
												 "시간표가 추가되었습니다!"
											},
										'keyboard': {
											'type': 'buttons',
											'buttons': [
												'홈으로'
												]
											}
									})


				else: # 시간 설정 오류뜨면 리턴
					return JsonResponse({
								"message":{
									"text" :
										 "시간이 올바르지 않습니다."
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'홈으로'
										]
									}
							})




	return JsonResponse({
							"message":{
								"text" :
									 "시간표 등록 함수입니다."
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': [
									'홈으로',
									]
								}
						})

def service_1_del(user_key):

	# 사용자 정보 가져오기
	user = models.USER.objects.get(USER_KEY = user_key)
	user_s_1 = models.USER_SERVICE_1.objects.get(USER_KEY = user_key)

	try :
		user_command_3 = (user.USER_COMMAND).split('$')[3]
	except:
		user_command_3 = '-1'

	try :
		user_command_4 = (user.USER_COMMAND).split('$')[4]
	except:
		user_command_4 = '-1'

	class_list = []
	class_index = []
	i = 1
	if user_s_1.USER_CLASS_1_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_1_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_2_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_2_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_3_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_3_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_4_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_4_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_5_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_5_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_6_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_6_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_7_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_7_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_8_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_8_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_9_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_9_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_10_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_10_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_11_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_11_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_12_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_12_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_13_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_13_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_14_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_14_NAME)
		i = i + 1
	if user_s_1.USER_CLASS_15_TEMP != 0:
		class_list.append( str(i) + ") " + user_s_1.USER_CLASS_15_NAME)
		i = i + 1
	class_list.append('홈으로')

	# 시간표 삭제 기본 메뉴
	if user_command_3 == '-1':
		return JsonResponse({
							"message":{
								"text" :
									 "삭제할 시간표를 선택해주세요"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': class_list
								}
						})

	else : 
		
		del_list = user_command_3.split(') ')[1]

		# 순서대로 검사 소스가 너무 길다는 단점
		if user_s_1.USER_CLASS_1_NAME == del_list:
			user_s_1.USER_CLASS_1_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_2_NAME == del_list:
			user_s_1.USER_CLASS_2_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_3_NAME == del_list:
			user_s_1.USER_CLASS_3_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_4_NAME == del_list:
			user_s_1.USER_CLASS_4_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_5_NAME == del_list:
			user_s_1.USER_CLASS_5_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_6_NAME == del_list:
			user_s_1.USER_CLASS_6_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_7_NAME == del_list:
			user_s_1.USER_CLASS_7_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_8_NAME == del_list:
			user_s_1.USER_CLASS_8_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_9_NAME == del_list:
			user_s_1.USER_CLASS_9_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_10_NAME == del_list:
			user_s_1.USER_CLASS_10_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_11_NAME == del_list:
			user_s_1.USER_CLASS_11_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_12_NAME == del_list:
			user_s_1.USER_CLASS_12_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_13_NAME == del_list:
			user_s_1.USER_CLASS_13_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_14_NAME == del_list:
			user_s_1.USER_CLASS_14_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()
		if user_s_1.USER_CLASS_15_NAME == del_list:
			user_s_1.USER_CLASS_15_TEMP = 0
			user_s_1.USER_CLASS_NUM = user_s_1.USER_CLASS_NUM - 1
			user_s_1.save()

		
		return JsonResponse({
							"message":{
								"text" :
									 "선택된 시간표가 삭제되었습니다."
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': [
									'홈으로'
									]
								}
						})
