from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
# 딜레이 API
import time

from . import models
from datetime import datetime

bank_menu =  [
			'$나의재산',
			'$나의창고',
			'$럭키박스',
			'$개인회생',
			'$메인메뉴']

def bank_init(user_key,user_command_2,user_command_3):

	# 은행 기본 메뉴
	if user_command_2 == "-1":
		return JsonResponse({
								"message":{
									"text" :
										 "LOT은행에 오신것을 환영합니다.\n\n" +
										 "(돈)나의재산 -> 보유머니 확인\n" +
										 "(돈)나의창고 -> 보유재화 확인\n" +
										 "(돈)럭키박스 -> 확률상자 게임"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': bank_menu
									}
							})

	# 나의 재산 메뉴
	elif user_command_2 == "나의재산":
		user = models.User.objects.get(userkey = user_key)
		user.command = "$은행"
		user.save()
		return JsonResponse({
				"message":{
					"text" :
						user.name + "님의 재산\n" +
						str(user.money) +"원 입니다."
					},
				'keyboard': {
						'type': 'buttons',
						'buttons': [
								'$나의재산',
								'$나의창고',
								'$럭키박스',
								'$개인회생',
								'$메인메뉴']
					}
				})

	# 나의 창고 메뉴
	elif user_command_2 == "나의창고":
		user = models.User.objects.get(userkey = user_key)
		userbox = models.User_Box.objects.get(userkey = user_key)
		user.command = "$은행"
		user.save()
		return JsonResponse({
				"message":{
					"text" :
						user.name + "님의 창고입니다.\n\n" +
						"쌀 : " + str(userbox.G1) + "개\n" +
						"금 : " + str(userbox.G3) + "개\n" +
						"가상화폐 : " + str(userbox.G4) + "개\n" +
						"국보책 : " + str(userbox.G5) + "개\n"
					},
				'keyboard': {
						'type': 'buttons',
						'buttons': [
								'$나의재산',
								'$나의창고',
								'$럭키박스',
								'$메인메뉴']
					}
				})

	# 럭키박스 메뉴
	elif user_command_2 == "럭키박스":

		# 럭키박스 메뉴 진입
		if user_command_3 == '-1':
			return JsonResponse({
					"message":{
						"photo": {
							"url": "https://t1.daumcdn.net/cfile/tistory/999684455B2BB8391F",
							"width": 500,
							"height": 500
						},
						"text" :
							"럭키박스(선물) [일반] 1만원\n" +
							"최소 5,000 ~ 최대 100만원\n\n" +
							"럭키박스(선물) [고급] 10만원\n" +
							"최소 10,000 ~ 최대 100만원"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})
		elif user_command_3 == '일반':
			return luckybox_1(user_key)

		elif user_command_3 == '고급':
			return luckybox_2(user_key)

	# 개인회생 메뉴
	elif user_command_2 == "개인회생":
		user = models.User.objects.get(userkey = user_key)
		user.command = "$은행"
		user.save()

		if user.money <= 50000:
			user.money = 500000
			user.save()
			return JsonResponse({
				"message":{
					"text" :
						user.name + "님(흑흑)\n" + 
						"소지금이 5만원 이하이므로\n" +
						"개인회생에 성공하셨습니다!\n\n" +
						"소지금 : 50만원"
					},
				'keyboard': {
						'type': 'buttons',
						'buttons': bank_menu
					}
				})

		else:
			return JsonResponse({
					"message":{
						"text" :
							"소지금이 너무 많습니다!"
						},
					'keyboard': {
							'type': 'buttons',
							'buttons': bank_menu
						}
					})

# 럭키박스 일반
def luckybox_1(user_key):
	user = models.User.objects.get(userkey = user_key)
	user.command = "$은행$럭키박스"
	user.save()
	if user.money < 10000:
		return JsonResponse({
					"message":{
						"text" :
							"소지금이 부족합니다.\n" +
							"현재 잔액 : " + str(user.money) + "원"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$은행'
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
							"[일확천금]\n럭키박스 [일반]에서 100만원에 당첨되셨습니다!\n축하드립니다!"+
							"\n\n나의 재산 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})

	elif luckymoney >= 998900 and luckymoney <=999900:

		#당첨금 지급
		luckymoney = int(luckymoney / 9)
		user.money = user.money + luckymoney
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[아쉽지만 돈벌었다!]\n럭키박스 [고급]에서 " + str(luckymoney) + "원에 당첨되셨습니다!\n축하드립니다!"+
							"\n\n나의 재산 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})

	else:

		#당첨금 지급
		user.money = user.money + 5000
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[꽝이네요...]\n럭키박스 [일반]에서 5000원에 당첨되셨습니다!"+
							"\n\n나의 재산 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})
# 럭키박스 고급
def luckybox_2(user_key):
	user = models.User.objects.get(userkey = user_key)
	user.command = "$은행$럭키박스"
	user.save()
	if user.money <= 100000:
		return JsonResponse({
					"message":{
						"text" :
							"소지금이 부족합니다.\n" +
							"현재 잔액 : " + str(user.money) + "원"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$은행'
							]
						}
					})

	# 사용자 지불 단계
	user.money = user.money - 100000
	user.save()

	# 확률 설정
	# 1등확률 1%
	# 2등확률 10%
	luckymoney = random.choice(range(0,1000001))
	if luckymoney > 990000 :

		#당첨금 지급
		user.money = user.money + 1000000
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[일확천금]\n럭키박스 [고급]에서 100만원에 당첨되셨습니다!\n축하드립니다!"+
							"\n\n나의 재산 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})

	elif luckymoney >= 900000 and luckymoney <= 990000:

		#당첨금 지급
		luckymoney = int(luckymoney / 9 * 2)
		user.money = user.money + luckymoney
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[아쉽지만 돈벌었다!]\n럭키박스 [고급]에서 " + str(luckymoney) + "원에 당첨되셨습니다!\n축하드립니다!"+
							"\n\n나의 재산 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})

	else:

		#당첨금 지급
		user.money = user.money + 10000
		user.save()

		return JsonResponse({
					"message":{
						"text" :
							"[꽝이네요...]\n럭키박스 [고급]에서 10,000원에 당첨되셨습니다!"+
							"\n\n나의 재산 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$일반',
							'$고급',
							'$은행'
							]
						}
					})