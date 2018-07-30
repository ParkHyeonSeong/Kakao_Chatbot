from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from . import models,views
from datetime import datetime

def salemenu(request):

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

	if content_name_split == "TRADE":
		return JsonResponse({
				"message":{
					"text" :
						"현재 수도권지역에서만 거래가 가능합니다.\n"
						"(타 지역 개발 상태)"
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'거래 수도권',
						'돌아가기'
						]
					}
				})

	elif content_name_split == "수도권":
		return JsonResponse({
				"message":{
					"text" :
						"가격변동간격 : 1분\n" +
						"가격변동률 : 2단계" 
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'거래 쌀',
						'돌아가기'
						]
					}
				})

	elif content_name_split == "쌀":
		# 재화 정보 받아오기
		goods = models.Goods.objects.get(G_Code = "G1")
		return JsonResponse({
			"message":{
				"text" :
					today_info + "\n\n"+
					"현재가 : " + str(goods.G_Price) +"원\n\n"+
					"최대 매도수량 : " + str(goods.G_Amount) +"개\n\n"+
					"-------------------------\n"+
					"매도 및 매수는 현재가 기준입니다."
				},
			'keyboard': {
				'type': 'buttons',
				'buttons': [
					'시세갱신 쌀',
					'매수 쌀',
					'매도 쌀',
					'돌아가기'
					]
				}
			})

def buy(request):

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

	# 주문 커맨드확인
	if content_name_split == "쌀":
		if content_name_split_n == "-1":
			# 재화 정보 받아오기
			goods = models.Goods.objects.get(G_Code = "G1")
			return JsonResponse({
				"message":{
					"text" :
						"☆주문방식☆\n\n"+
						"→ 매수 쌀 수량\n\n"+
						"예시 : 매수 쌀 100\n\n"+
						"-------------------------\n\n"+
						today_info + "\n"+
						"현재가 : " + str(goods.G_Price) +"원\n"+
						"최대 매수 가능 수량 : " + str(goods.G_Amount) +"개\n\n"+
						"-------------------------\n\n"+
						"매도 및 매수는 현재가 기준입니다.\n"+
						"방식이 틀리면 취소됩니다.\n"+
						"'ㅊ'또는'c' 입력 시 이전단계로"
					},
				'keyboard': {
					'type': 'text'
					}
				})

		#직접 매수
		elif int(content_name_split_n) >= 0:
			goods = models.Goods.objects.get(G_Code = "G1")
			user = models.User.objects.get(userkey = user_key)

			if (int(content_name_split_n)*goods.G_Price) <= user.money and int(content_name_split_n) <= goods.G_Amount:
				userbox = models.Box.objects.get(userkey = user_key)

				# 지불 단계
				goods.G_Amount = goods.G_Amount - int(content_name_split_n)
				goods.save()
				user.money = user.money - (int(content_name_split_n)*goods.G_Price)
				user.save()
				userbox.G1 = userbox.G1 + int(content_name_split_n)
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"남은 돈 : " + str(user.money)
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'돌아가기'
							]
					}
				})

			else:
				return JsonResponse({
					"message":{
						"text" :
							"보유 재산 또는 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'돌아가기'
							]
					}
				})

		else:
			return JsonResponse({
					"message":{
						"text" :
							"수량 오류입니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'돌아가기'
							]
					}
				})
	else:
		return test()


def sell(request):
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

	# 주문 커맨드확인
	if content_name_split == "쌀":

		# 재화 정보 받아오기
		goods = models.Goods.objects.get(G_Code = "G1")
		# 사용자 정보 받아오기
		user = models.User.objects.get(userkey = user_key)
		userbox = models.Box.objects.get(userkey = user_key)
		
		if content_name_split_n == "-1":
			return JsonResponse({
				"message":{
					"text" :
						"☆주문방식☆\n\n"+
						"→ 매도 재화 수량\n\n"+
						"예시 : \"매도 쌀 100\"\n\n"+
						"-------------------------\n\n"+
						"현재가 : " + str(goods.G_Price) +"원\n"+
						"최대 매도 가능 수량 : " + str(userbox.G1) +"개\n\n"+
						"-------------------------\n\n"+
						"매도 및 매수는 현재가 기준입니다.\n"+
						"방식이 틀리면 취소됩니다.\n"+
						"'ㅊ'또는'c' 입력 시 이전단계로"
					},
				'keyboard': {
					'type': 'text'
					}
				})

		#직접 매도
		elif int(content_name_split_n) >= 0:

			if int(content_name_split_n) <= userbox.G1:
				userbox = models.Box.objects.get(userkey = user_key)

				# 지불 단계
				goods.G_Amount = goods.G_Amount + int(content_name_split_n)
				goods.save()
				user.money = user.money + (int(content_name_split_n)*goods.G_Price)
				user.save()
				userbox.G1 = userbox.G1 - int(content_name_split_n)
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"정산 후 보유자산 : " + str(user.money) + "원\n" +
							"정산 후 쌀 수량 : " + str(userbox.G1) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'돌아가기'
							]
					}
				})

			else:
				return JsonResponse({
					"message":{
						"text" :
							"보유 재화가 모자랍니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'돌아가기'
							]
					}
				})

		else:
			return JsonResponse({
					"message":{
						"text" :
							"수량 오류입니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'돌아가기'
							]
					}
				})

	else:
		return test()


def salerefresh(request):

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
	except:
		content_name_split = "-1"

	# 주문 커맨드확인
	if content_name_split == "쌀":
		# 재화 정보 받아오기
		goods = models.Goods.objects.get(G_Code = "G1")
		return JsonResponse({
			"message":{
				"text" :
					today_info + "\n\n"+
					"현재가 : " + str(goods.G_Price) +"원\n\n"+
					"최대 매수 가능 수량 : " + str(goods.G_Amount) +"개\n\n"+
					"-------------------------\n"+
					"매도 및 매수는 현재가 기준입니다."
				},
			'keyboard': {
				'type': 'buttons',
				'buttons': [
					'시세갱신 쌀',
					'매수 쌀',
					'매도 쌀',
					'돌아가기'
					]
				}
			})

	else:
		return test()

def test():
	return JsonResponse({
				"message":{
					"text" :
						"분류되지 않은 sale 오류입니다."
					},
				'keyboard': {
					'type': 'buttons',
					'buttons': [
						'돌아가기'
						]
					}
				})