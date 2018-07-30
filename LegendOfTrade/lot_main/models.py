from django.db import models

# Create your models here.

# 기본 사용자 정보
class User(models.Model):
	# 사용자 식별 번호
	userkey = models.CharField(max_length = 50)
	# 사용자 닉네임
	name = models.CharField(max_length = 20)
	# 사용자 보유 머니(디폴트 = 100만원)
	money = models.IntegerField(default = 1000000)
	# 사용자 커맨드
	command = models.CharField(max_length = 100, default = "")
	# 사용자 권한(0:일반, 10:관리자)
	level = models.IntegerField(default = 0)
	# 사용자 인게임 확인(0:로그아웃 1:인게임)
	ingame = models.IntegerField(default = 0)
	# 사용자 최근 접속 시간
	recent = models.CharField(max_length = 30, default = '1')

	def __str__(self):
		return self.name
# 사용자 창고 정보
class User_Box(models.Model):
	# 사용자 식별 번호 
	userkey = models.CharField(max_length = 50)
	# 사용자 닉네임
	name = models.CharField(max_length = 20)
	# 쌀
	G1 = models.IntegerField(default = 0)
	G1_M = models.IntegerField(default = 0)
	# 금
	G3 = models.IntegerField(default = 0)
	G3_M = models.IntegerField(default = 0)
	# 가상화폐
	G4 = models.IntegerField(default = 0)
	G4_M = models.IntegerField(default = 0)
	# 국보책
	G5 = models.IntegerField(default = 0)
	G5_M = models.IntegerField(default = 0)

	def __str__(self):
		return self.name
# 사용자 은행 정보 2018.06.22 추가
class User_Bank(models.Model):
	# 사용자 식별 번호
	userkey = models.CharField(max_length = 50)
	# 사용자 예금
	money = models.IntegerField(default = 0)
	# 럭키박스 연속 횟수
	lucky_chance = models.IntegerField(default = 0)

	def __str__(self):
		return self.userkey
# 재화 정보
class Goods(models.Model):
	# 재화 식별번호
	G_Code = models.CharField(max_length = 5)
	# 재화 이름
	G_Name = models.CharField(max_length = 20)
	# 재화 가격
	G_Price = models.IntegerField(default = 10000)
	# 재화 량
	G_Amount = models.IntegerField(default = 1000000)

	def __str__(self):
		return self.G_Name