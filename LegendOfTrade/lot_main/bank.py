from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

from . import models,views
from datetime import datetime

def bank_init(request):

	# 오늘
	today = datetime.today()
	today_info = today.strftime('%Y-%m-%d, %H:%M:%S')

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	try:
		content_name_split = content_name.split(' ')[1]
		content_name_split_n = content_name.split(' ')[2]
	except:
		content_name_split_n = "-1"


	if content_name_split == "BANK":
		user = models.User.objects.get(userkey = user_key)
		return JsonResponse({
				"message":{
					"text" :
						user.name + "님 어서오세요.\n" +
						"LOT BANK입니다."
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'은행 나의재산',
						'은행 나의창고',
						'은행 럭키박스',
						#'은행 로또',
						'돌아가기'
						]
					}
				})

	elif content_name_split == "나의재산":
		user = models.User.objects.get(userkey = user_key)
		return JsonResponse({
				"message":{
					"text" :
						user.name + "님의 재산\n" +
						str(user.money) +"원 입니다."
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'돌아가기'
						]
					}
				})

	elif content_name_split == "나의창고":
		user = models.User.objects.get(userkey = user_key)
		userbox = models.Box.objects.get(userkey = user_key)
		return JsonResponse({
				"message":{
					"text" :
						user.name + "님의 창고입니다.\n\n" +
						"쌀 : " + str(userbox.G1) + "개"
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'돌아가기'
						]
					}
				})

	elif content_name_split == "럭키박스":
		if content_name_split_n == '-1' or content_name_split_n == "돌아가기" :
			user = models.User.objects.get(userkey = user_key)
			return JsonResponse({
					"message":{
						"text" :
							"럭키박스 [일반] 10000원\n" +
							"최소 5000 ~ 최대 100만원\n\n" +
							"럭키박스 [고급] 100000원\n" +
							"-구현되지 않음-"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'은행 럭키박스 [일반]',
							'은행 럭키박스 [고급]',
							'은행 BANK 돌아가기'
							]
						}
					})
		elif content_name_split_n == "[일반]":
			return luckybox_1(request)
		elif content_name_split_n == "[고급]":
			return luckybox_2(request)

	else:
		return JsonResponse({
				"message":{
					"text" :
						"죄송합니다.\n"+
						"개발중인 기능입니다.\n"
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'돌아가기'
						]
					}
				})

def luckybox_1(request):

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']

	# 사용자 정보 가져오기
	user = models.User.objects.get(userkey = user_key)
	if user.money <= 10000:
		return JsonResponse({
					"message":{
						"text" :
							"소지금이 부족합니다.\n" +
							"현재 잔액 : " + str(user.money) + "원"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'은행 럭키박스 돌아가기'
							]
						}
					})

	# 사용자 지불 단계
	user.money = user.money - 10000
	user.save()

	# 확률 설정
	# 1등확률 0.01%
	# 2등확률 0.1%
	luckymoney = random.choice(range(0,1000001))
	if luckymoney > 999900 :

		#당첨금 지급
		user.money = user.money + 1000000
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[일확천금]\n럭키박스 [일반]에서 100만원에 당첨되셨습니다!\n축하드립니다!"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'은행 럭키박스 돌아가기'
							]
						}
					})

	elif luckymoney >= 990000 and luckymoney <=999900:

		#당첨금 지급
		luckymoney = int(luckymoney / 9)
		user.money = user.money + luckymoney
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[아쉽지만 돈벌었다!]\n럭키박스 [일반]에서 " + str(luckymoney) + "원에 당첨되셨습니다!\n축하드립니다!"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'은행 럭키박스 돌아가기'
							]
						}
					})

	else:

		#당첨금 지급
		user.money = user.money + 7000
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[꽝이네요...]\n럭키박스 [일반]에서 7000원에 당첨되셨습니다!"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'은행 럭키박스 돌아가기'
							]
						}
					})

	

def luckybox_2(request):

	message = (request.body).decode('utf-8')
	return_json_str = json.loads(message)
	content_name = return_json_str['content']
	type_name = return_json_str['type']
	user_key = return_json_str['user_key']
		
	return JsonResponse({
					"message":{
						"text" :
							"잉 아직 미구현~"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'은행 BANK 돌아가기'
							]
						}
					})