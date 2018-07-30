from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from . import models
from datetime import datetime

def rank(user_key):
	# 사용자 커맨드 초기화
	user = models.User.objects.get(userkey = user_key)
	user.command = '1000'
	user.save()

	# 오늘
	today = datetime.today()
	today_info = today.strftime('%Y.%m.%d.%H.%M')
	today_year = today_info.split('.')[0] + "년 "
	today_month = today_info.split('.')[1] + "월 "
	today_day = today_info.split('.')[2] + "일  "
	today_hour = today_info.split('.')[3] + "시 "
	today_minute = today_info.split('.')[4] + "분"

	today_info = today_year + today_month + today_day + today_hour + today_minute

	ranklist = models.User.objects.all().order_by('-money')
	ranklist_count = models.User.objects.count()
	ex = []
	ex2 = []

	for ranklists in ranklist:
		try:
			ex.append(ranklists.name)
			ex2.append(ranklists.money)
		except:
			ex.append("없음")
			ex2.append("-")

	try:
		return JsonResponse({
					"message":{
						"text" :
							today_info + "\n" +
							"(축하)순자산 1위 : " + str(ex[0]) + 
							"\n        " +str(ex2[0]) + "원\n" +
							"(축하)순자산 2위 : " + str(ex[1]) + 
							"\n        " + str(ex2[1]) + "원\n" +
							"(축하)순자산 3위 : " + str(ex[2]) + 
							"\n        " + str(ex2[2]) + "원\n" +
							"(축하)순자산 4위 : " + str(ex[3]) + 
							"\n        " + str(ex2[3]) + "원\n" +
							"(축하)순자산 5위 : " + str(ex[4]) + 
							"\n        " + str(ex2[4]) + "원" 
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
	except:
		return JsonResponse({
					"message":{
						"text" :
							"랭크를 표시하기에는\n너무 적은 사용자입니다."
						},
					'keyboard': {
						'type': 'buttons',
						'buttons': [
								'$메인메뉴']
						}
					})