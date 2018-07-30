from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from . import models
from datetime import datetime


def market_init(user_key,user_command_2,user_command_3,user_command_4,user_command_5,user_command_6):
	# 시장 기본 메뉴
	if user_command_2 == "-1":
		return JsonResponse({
								"message":{
									"text" :
										 "시장에 진입하셨습니다.\n\n"+
										 "무역소 -> 물건의 가격이 변하는 거래소\n" +
										 "아이템상점(준비중) -> 개인아이템 상점"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'$무역소',
										'$아이템상점',
										'$메인메뉴']
									}
							})

	# 무역소 진입
	elif user_command_2 == "무역소":

		# 오늘
		today = datetime.today()
		today_info = today.strftime('%Y-%m-%d, %H:%M:%S')

		# 무역소 기본 메뉴
		if user_command_3 == '-1':
			return JsonResponse({
							"message":{
								"text" :
									 "무역소에서 판매중인 물품들\n\n" +
									 "쌀 : 1분마다 가격변동\n가격변동 0원~500원\n±확률 50%\n\n" +
									 "금 : 1분마다 가격변동\n가격변동 0원~500원\n±확률 50%\n\n" +
									 "가상화폐 : 1분마다 가격변동\n가격변동 0원~5000원\n±확률 50%\n\n" +
									 "국보책 : 1분마다 가격변동\n가격변동 0원~1000원\n±확률 50%"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'$쌀',
										'$금',
										'$가상화폐',
										'$국보책',
										'$메인메뉴']
								}
					})

		# G1-쌀
		elif user_command_3 == "쌀":

			# 재화별 기본 메뉴
			if user_command_4 == '-1':

				goods = models.Goods.objects.get(G_Code = "G1")
				userbox = models.User_Box.objects.get(userkey = user_key)

				return JsonResponse({
								"message":{
									"text" :
										 today_info + "\n"+
										"현재가 : " + str(goods.G_Price) +"원\n"+
										"매물 수량 : " + str(goods.G_Amount) +"개\n"+
										"나의 보유량 : " + str(userbox.G1) + "개\n" +
										"-------------------------\n"+
										"매도 및 매수는 현재가 기준입니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': [
											'$시세갱신',
											'$매수',
											'$매도',
											'$메인메뉴']
									}
						})

			# 매수 진입
			elif user_command_4 == "매수":
				return G1_Buy(user_key,user_command_5)
			# 매도 진입
			elif user_command_4 == "매도":
				return G1_Sell(user_key,user_command_5)
			# 시세갱신
			#elif user_command_4 == "시세갱신->쌀":
			#	return G1_Refresh(user_key)
		# G3-금
		elif user_command_3 == "금":

			# 재화별 기본 메뉴
			if user_command_4 == '-1':

				goods = models.Goods.objects.get(G_Code = "G3")
				userbox = models.User_Box.objects.get(userkey = user_key)

				return JsonResponse({
								"message":{
									"text" :
										 today_info + "\n"+
										"현재가 : " + str(goods.G_Price) +"원\n"+
										"현재 수량 : " + str(goods.G_Amount) +"개\n"+
										"보유 수량 : " + str(userbox.G3) + "개\n" +
										"-------------------------\n"+
										"매도 및 매수는 현재가 기준입니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': [
											'$시세갱신',
											'$매수',
											'$매도',
											'$메인메뉴']
									}
						})

			# 매수 진입
			elif user_command_4 == "매수":
				return G3_Buy(user_key,user_command_5)
			# 매도 진입
			elif user_command_4 == "매도":
				return G3_Sell(user_key,user_command_5)
			# 시세갱신
			#elif user_command_4 == "시세갱신->":
			#	return G3_Refresh(user_key,user_command_2,user_command_3,user_command_4,user_command_5,user_command_6)
		# G4-가상화폐
		elif user_command_3 == "가상화폐":

			# 재화별 기본 메뉴
			if user_command_4 == '-1':

				goods = models.Goods.objects.get(G_Code = "G4")
				userbox = models.User_Box.objects.get(userkey = user_key)

				return JsonResponse({
								"message":{
									"text" :
										 today_info + "\n"+
										"현재가 : " + str(goods.G_Price) +"원\n"+
										"현재 수량 : " + str(goods.G_Amount) +"개\n"+
										"보유 수량 : " + str(userbox.G4) + "개\n" +
										"-------------------------\n"+
										"매도 및 매수는 현재가 기준입니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': [
											'$시세갱신',
											'$매수',
											'$매도',
											'$메인메뉴']
									}
						})

			# 매수 진입
			elif user_command_4 == "매수":
				return G4_Buy(user_key,user_command_5)
			# 매도 진입
			elif user_command_4 == "매도":
				return G4_Sell(user_key,user_command_5)
			# 시세갱신
			#elif user_command_4 == "시세갱신":
			#	return G4_Refresh(user_key,user_command_2,user_command_3,user_command_4,user_command_5,user_command_6)
		# G5-국보책
		elif user_command_3 == "국보책":

			# 재화별 기본 메뉴
			if user_command_4 == '-1':

				goods = models.Goods.objects.get(G_Code = "G5")
				userbox = models.User_Box.objects.get(userkey = user_key)

				return JsonResponse({
								"message":{
									"text" :
										 today_info + "\n"+
										"현재가 : " + str(goods.G_Price) +"원\n"+
										"현재 수량 : " + str(goods.G_Amount) +"개\n"+
										"보유 수량 : " + str(userbox.G5) + "개\n" +
										"-------------------------\n"+
										"매도 및 매수는 현재가 기준입니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': [
											'$시세갱신',
											'$매수',
											'$매도',
											'$메인메뉴']
									}
						})

			# 매수 진입
			elif user_command_4 == "매수":
				return G5_Buy(user_key,user_command_5)
			# 매도 진입
			elif user_command_4 == "매도":
				return G5_Sell(user_key,user_command_5)
			# 시세갱신
			#elif user_command_4 == "시세갱신":
			#	return G5_Refresh(user_key,user_command_2,user_command_3,user_command_4,user_command_5,user_command_6)
 
 	# 새로운 컨텐츠
	elif user_command_2 == "아이템상점":

		if user_command_3 == '-1':
			return JsonResponse({
							"message":{
								"text" :
									 "새로운 컨텐츠를 준비하기 위해 아이템상점이 열렸습니다.\n업데이트를 기다려주세요"
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': [
										'$시장',
										'$메인메뉴'
										]
								}
					})

def G1_Buy(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G1")
		user = models.User.objects.get(userkey = user_key)
		userbox = models.User_Box.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$쌀$매수$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"현재가 : " + str(goods.G_Price) + "원\n"+
							"매물 수량 : " + str(goods.G_Amount) + "개\n"+
							"나의 보유량 : " + str(userbox.G1) + "개\n"+
							"MAX 구매가능량 : " + str(int(user.money/goods.G_Price)) + "\n" +
							"수량을 입력해 주세요(숫자만)\n※ 0을 입력하시면 취소됩니다."

						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if(int(user_command_5)*goods.G_Price) <= user.money and int(user_command_5) <= goods.G_Amount:

				# 지불 단계
				goods.G_Amount = goods.G_Amount - int(user_command_5)
				user.money = user.money - (int(user_command_5)*goods.G_Price)
				userbox.G1 = userbox.G1 + int(user_command_5)
				userbox.G1_M = goods.G_Price
				user.save()
				userbox.save()
				goods.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"남은 돈 : " + str(user.money) + "원\n" +
							"보유량 : " + str(userbox.G1) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재산 또는 남은 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
def G1_Sell(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G1")
		user = models.User.objects.get(userkey = user_key)
		userbox = models.User_Box.objects.get(userkey = user_key)

		# 매도 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$쌀$매도$"
			user.save()

			# 차액 확인

			return JsonResponse({
					"message":{
						"text" :
							"나의 보유량 : " + str(userbox.G1) + "개\n\n" +
							"매수 평균 단가 : " + str(userbox.G1_M) + "\n\n" +
							"현재 단가 : " + str(goods.G_Price) + "\n\n" +
							"개당 손익 분석 : " + str(userbox.G1_M-goods.G_Price) + "\n\n" +
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if int(user_command_5) <= userbox.G1:

				# 지불 단계
				goods.G_Amount = goods.G_Amount + int(user_command_5)
				user.money = user.money + (int(user_command_5)*goods.G_Price)
				userbox.G1 = userbox.G1 - int(user_command_5)
				# 모두 팔아져서 평균낼 필요가 없을 때 초기화
				if userbox.G1 == 0:
					userbox.G1_M = 0
				user.save()
				userbox.save()
				goods.save()

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
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

def G3_Buy(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G3")
		user = models.User.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$금$매수$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if(int(user_command_5)*goods.G_Price) <= user.money and int(user_command_5) <= goods.G_Amount:
				# 사용자 박스 불러오기
				userbox = models.User_Box.objects.get(userkey = user_key)

				# 지불 단계
				goods.G_Amount = goods.G_Amount - int(user_command_5)
				goods.save()
				user.money = user.money - (int(user_command_5)*goods.G_Price)
				user.save()
				userbox.G3 = userbox.G3 + int(user_command_5)
				userbox.G3_M = goods.G_Price
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"남은 돈 : " + str(user.money) + "원\n" +
							"보유량 : " + str(userbox.G3) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재산 또는 남은 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
def G3_Sell(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G3")
		user = models.User.objects.get(userkey = user_key)
		userbox = models.User_Box.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$금$매도$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"나의 보유량 : " + str(userbox.G3) + "개\n\n" +
							"매수 평균 단가 : " + str(userbox.G1_M) + "\n\n" +
							"현재 단가 : " + str(goods.G_Price) + "\n\n" +
							"개당 손익 분석 : " + str(userbox.G3_M-goods.G_Price) + "\n\n" +
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if int(user_command_5) <= userbox.G3:

				# 지불 단계
				goods.G_Amount = goods.G_Amount + int(user_command_5)
				goods.save()
				user.money = user.money + (int(user_command_5)*goods.G_Price)
				user.save()
				userbox.G3 = userbox.G3 - int(user_command_5)
				# 모두 팔아져서 평균낼 필요가 없을 때 초기화
				if userbox.G3 == 0:
					userbox.G3_M = 0
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"정산 후 보유자산 : " + str(user.money) + "원\n" +
							"정산 후 금 수량 : " + str(userbox.G3) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

def G4_Buy(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G4")
		user = models.User.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$가상화폐$매수$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if(int(user_command_5)*goods.G_Price) <= user.money and int(user_command_5) <= goods.G_Amount:
				# 사용자 박스 불러오기
				userbox = models.User_Box.objects.get(userkey = user_key)

				# 지불 단계
				goods.G_Amount = goods.G_Amount - int(user_command_5)
				goods.save()
				user.money = user.money - (int(user_command_5)*goods.G_Price)
				user.save()
				userbox.G4 = userbox.G4 + int(user_command_5)
				userbox.G4_M = goods.G_Price
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"남은 돈 : " + str(user.money) + "원\n" +
							"보유량 : " + str(userbox.G4) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재산 또는 남은 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
def G4_Sell(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G4")
		user = models.User.objects.get(userkey = user_key)
		userbox = models.User_Box.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$가상화폐$매도$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"나의 보유량 : " + str(userbox.G4) + "개\n\n" +
							"매수 평균 단가 : " + str(userbox.G1_M) + "\n\n" +
							"현재 단가 : " + str(goods.G_Price) + "\n\n" +
							"개당 손익 분석 : " + str(userbox.G4_M-goods.G_Price) + "\n\n" +
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if int(user_command_5) <= userbox.G4:

				# 지불 단계
				goods.G_Amount = goods.G_Amount + int(user_command_5)
				goods.save()
				user.money = user.money + (int(user_command_5)*goods.G_Price)
				user.save()
				userbox.G4 = userbox.G4 - int(user_command_5)
				# 모두 팔아져서 평균낼 필요가 없을 때 초기화
				if userbox.G4 == 0:
					userbox.G4_M = 0
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"정산 후 보유자산 : " + str(user.money) + "원\n" +
							"정산 후 가상화폐 수량 : " + str(userbox.G4) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

def G5_Buy(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G5")
		user = models.User.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$금$매수$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if(int(user_command_5)*goods.G_Price) <= user.money and int(user_command_5) <= goods.G_Amount:
				# 사용자 박스 불러오기
				userbox = models.User_Box.objects.get(userkey = user_key)

				# 지불 단계
				goods.G_Amount = goods.G_Amount - int(user_command_5)
				goods.save()
				user.money = user.money - (int(user_command_5)*goods.G_Price)
				user.save()
				userbox.G5 = userbox.G5 + int(user_command_5)
				userbox.G5_M = goods.G_Price
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"남은 돈 : " + str(user.money) + "원\n" +
							"보유량 : " + str(userbox.G5) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재산 또는 남은 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
def G5_Sell(user_key,user_command_5):
	try : 
		goods = models.Goods.objects.get(G_Code = "G5")
		user = models.User.objects.get(userkey = user_key)
		userbox = models.User_Box.objects.get(userkey = user_key)

		# 매수 기본 메뉴
		if int(user_command_5) == -1:
			# 커맨드 대기
			user.command = "$시장$무역소$국보책$매도$"
			user.save()

			return JsonResponse({
					"message":{
						"text" :
							"나의 보유량 : " + str(userbox.G5) + "개\n\n" +
							"매수 평균 단가 : " + str(userbox.G1_M) + "\n\n" +
							"현재 단가 : " + str(goods.G_Price) + "\n\n" +
							"개당 손익 분석 : " + str(userbox.G5_M-goods.G_Price) + "\n\n" +
							"수량을 입력해 주세요(숫자만)"
						},
					'keyboard': {
						'type': 'text'
						}
					})

		# 매수 시작
		if int(user_command_5) >= 0:
			# 보유 돈 확인
			if int(user_command_5) <= userbox.G5:

				# 지불 단계
				goods.G_Amount = goods.G_Amount + int(user_command_5)
				goods.save()
				user.money = user.money + (int(user_command_5)*goods.G_Price)
				user.save()
				userbox.G5 = userbox.G5 - int(user_command_5)
				# 모두 팔아져서 평균낼 필요가 없을 때 초기화
				if userbox.G5 == 0:
					userbox.G5_M = 0
				userbox.save()

				# 구매 내역 확인
				return JsonResponse({
					"message":{
						"text" :
							"정산 후 보유자산 : " + str(user.money) + "원\n" +
							"정산 후 국보책 수량 : " + str(userbox.G5) + "개"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})

			else:

				# 커맨드 초기화
				user.command = "$시장"
				user.save()

				return JsonResponse({
					"message":{
						"text" :
							"보유 재화가 부족합니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
		else:
			return JsonResponse({
					"message":{
						"text" :
							"정상적인 범위가 아닙니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})
	except:
		return JsonResponse({
					"message":{
						"text" :
							"[WARNING]\n" +
							"불법적인 접근"
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
							'$메인메뉴'
							]
					}
				})