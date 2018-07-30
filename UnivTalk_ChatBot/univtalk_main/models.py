from django.db import models

# 기본 사용자 정보
class USER(models.Model):
	# 사용자 식별 번호
	USER_KEY = models.CharField(max_length = 50, default = "-1")
	# 사용자 이름 or 닉네임
	USER_NAME = models.CharField(max_length = 20, default = "-1")
	# 사용자 대학교
	USER_UNIV = models.CharField(max_length = 40, default = "-1")
	# 사용자 커맨드
	USER_COMMAND = models.CharField(max_length = 100, default = "-1")
	# 관리자 권한 체크(0: 차단 / 5: 기본사용자 / 10: 관리자)
	USER_LEVEL = models.IntegerField(default = 5)

	def __str__(self):
		return self.USER_NAME

# 사용자 서비스 1 - 시간표 저장
class USER_SERVICE_1(models.Model):
	# 사용자 식별 번호
	USER_KEY = models.CharField(max_length = 50)
	# 사용자 이름 or 닉네임
	USER_NAME = models.CharField(max_length = 20)
	# 시간표 이름
	USER_CLASS_NAME = models.CharField(max_length = 20)
	# 수업 갯수 확인
	USER_CLASS_NUM = models.IntegerField(default = 0)
	# 수업 1
	USER_CLASS_1_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_1_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_1_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_1_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_1_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_1_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_1_TEMP = models.IntegerField(default = 0)
	# 수업 2
	USER_CLASS_2_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_2_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_2_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_2_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_2_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_2_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_2_TEMP = models.IntegerField(default = 0)
	# 수업 3
	USER_CLASS_3_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_3_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_3_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_3_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_3_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_3_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_3_TEMP = models.IntegerField(default = 0)
	# 수업 4
	USER_CLASS_4_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_4_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_4_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_4_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_4_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_4_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_4_TEMP = models.IntegerField(default = 0)
	# 수업 5
	USER_CLASS_5_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_5_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_5_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_5_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_5_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_5_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_5_TEMP = models.IntegerField(default = 0)
	# 수업 6
	USER_CLASS_6_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_6_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_6_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_6_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_6_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_6_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_6_TEMP = models.IntegerField(default = 0)
	# 수업 7
	USER_CLASS_7_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_7_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_7_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_7_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_7_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_7_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_7_TEMP = models.IntegerField(default = 0)
	# 수업 8
	USER_CLASS_8_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_8_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_8_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_8_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_8_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_8_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_8_TEMP = models.IntegerField(default = 0)
	# 수업 9
	USER_CLASS_9_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_9_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_9_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_9_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_9_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_9_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_9_TEMP = models.IntegerField(default = 0)
	# 수업 10
	USER_CLASS_10_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_10_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_10_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_10_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_10_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_10_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_10_TEMP = models.IntegerField(default = 0)
	# 수업 11
	USER_CLASS_11_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_11_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_11_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_11_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_11_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_11_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_11_TEMP = models.IntegerField(default = 0)
	# 수업 12
	USER_CLASS_12_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_12_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_12_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_12_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_12_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_12_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_12_TEMP = models.IntegerField(default = 0)
	# 수업 13
	USER_CLASS_13_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_13_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_13_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_13_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_13_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_13_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_13_TEMP = models.IntegerField(default = 0)
	# 수업 14
	USER_CLASS_14_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_14_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_14_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_14_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_14_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_14_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_14_TEMP = models.IntegerField(default = 0)
	# 수업 15
	USER_CLASS_15_DAY = models.CharField(max_length = 5, default = "-1")
	USER_CLASS_15_START = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_15_END = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_15_NAME = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_15_ROOM = models.CharField(max_length = 50, default = "-1")
	USER_CLASS_15_MASTER = models.CharField(max_length = 20, default = "-1")
	USER_CLASS_15_TEMP = models.IntegerField(default = 0)

	def __str__(self):
		return self.USER_NAME