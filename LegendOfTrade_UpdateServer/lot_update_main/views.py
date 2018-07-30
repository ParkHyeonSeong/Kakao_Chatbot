from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import threading
import random
import requests
import json

# db임포트
from . import models

# Create your views here.
Set_time = 60

def update_main():

	#자동 재시작 끔
	#timer = threading.Timer(60, update_main)
	#timer.start()

	# 현재시각 표시
	today = datetime.today()
	today_info = today.strftime('%Y-%m-%d, %H:%M:%S')

	print( today_info +"\n업데이트를 시작합니다.")

	G1 = update_G1()
	print( "변경된 쌀의 가격 : " + str(G1) + "원")

	# POST 전송
	data = {'G1' : G1, 'G2' : 'TEST'}
	r = requests.post('http://127.0.0.1:723/update', data=json.dumps(data))
	print(r.status_code)

def update_main_auto():

	timer = threading.Timer(Set_time, update_main_auto)
	timer.start()

	# 현재시각 표시
	today = datetime.today()
	today_info = today.strftime('%Y-%m-%d, %H:%M:%S')

	print( today_info +"\n업데이트를 시작합니다.")

	G1 = update_G1()
	print( "변경된 쌀의 가격 : " + str(G1) + "원")

	# POST 전송
	data = {'G1' : G1, 'G2' : 'TEST'}
	r = requests.post('http://127.0.0.1:723/update', data=json.dumps(data))
	print("서버 응답 확인 코드 : " + str(r.status_code))
	print("업데이트를 성공적으로 마쳤습니다.")


def update_G1():
	# 업데이트 재화 정보 가져오기
	goods = models.Goods.objects.get(G_Code = "G1")

	# 변동범위 및 레이트 설정
	Level = Price_Level(goods.G_Level)
	EventRate = goods.G_Rate

	if random.choice(range(1,101)) >= EventRate:
		# 최대 범위 설정
		if (goods.G_Price + Level) >= 100000:
			goods.G_Price = 100000
		else:
			goods.G_Price = goods.G_Price + Level
	else:
		#최소 범위 설정
		if (goods.G_Price - Level) <= 2000:
			goods.G_Price = 2000
		else:
			goods.G_Price = goods.G_Price - Level

	goods.save()
	return goods.G_Price

def Price_Level(level):
	if level == 1:
		Price = random.choice(range(0,50)) * 1

	elif level == 2:
		Price = random.choice(range(0,50)) * 10

	elif level == 3:
		Price = random.choice(range(0,50)) * 20
		return Price

	elif level == 4:
		Price = random.choice(range(0,50)) * 100

	elif level == 5:
		Price = random.choice(range(0,50)) * 1000

	else:
		Price = 0

	return Price

# 2018.06.21 삭제된 기능
# update_main()

while 1 :
	print(" 1 -> 수동 재시작")
	print(" 2 -> 자동 재시작")
	command = input('  > ')
	if command == "1":
		update_main()

	elif command == "2":
		print('  자동 재시작 주기(s) >', end = ' ')
		command_sec = input()

		if command_sec == "":
			update_main_auto()
		else:
			Set_time = int(command_sec)
			update_main_auto()
	
		break

	else:
		print("개발 중 입니다.")