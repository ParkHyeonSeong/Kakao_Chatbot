from django.db import models

# Create your models here.
class USER(models.Model):										# 사용자 정보
	
	CHECK = models.IntegerField(default = 0)					## 사용자 인덱스
	KEY = models.CharField(max_length = 50, default = "`")		## 사용자 식별 번호
	NAME = models.CharField(max_length = 50, default = "`")		## 사용자 닉네임
	COMMAND = models.CharField(max_length = 500, default = "`")	## 사용자 커맨드
	HISTORY = models.CharField(max_length = 500, default = "`")	## 사용자 히스토리
	LEVEL = models.IntegerField(default = 5)					## 사용자 접근 권한
	COOK = models.IntegerField(default = 0)						## 요리중인지 확인

	def __str__(self):
		return self.NAME

class RECIPE(models.Model):										# 레시피 데이터베이스

	CHECK = models.IntegerField(default = 0)					## 레시피 인덱스
	USER_KEY = models.CharField(max_length=50,default="`")		## 사용자 식별 번호
	USER_NAME = models.CharField(max_length=50,default="`")		## 사용자 닉네임
	R_NAME = models.CharField(max_length=100,default="`")		## 레시피 이름
	F_NAME = models.CharField(max_length=100,default="`")		## 요리 이름
	INGRED = models.CharField(max_length=1000,default="`")		## 재료
	ORDER_1 = models.CharField(max_length=10000,default="`")	## 조리 순서
	PICK = models.IntegerField(default = 0)						## 레시피 추천
	DATE = models.CharField(max_length=100,default="`")			## 레시피 등록 및 업데이트 날짜
	DAY = models.CharField(max_length=50,default="`")			## 아침, 점심, 저녁 중 선택


	def __str__(self):
		return str(self.CHECK) + ":" + self.R_NAME