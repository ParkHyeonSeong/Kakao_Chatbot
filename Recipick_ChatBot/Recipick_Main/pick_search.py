from django.http import JsonResponse
from . import pick_recipe
from . import models
import json

def recipe_search(content,user):

	if models.RECIPE.objects.count() == 0:	# 등록된 레시피가 없다면 🔙 처음으로 돌아갑니다.
		return JsonResponse({
							"message":{
								"text" :
									"등록된 레시피가 없습니다."
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': home
								}
						})

	try :
		user_command_2 = (user.COMMAND).split('#')[2]
	except:
		user_command_2 = '-1'

	if user_command_2 == '-1':
		return JsonResponse({
							"message":{
								"text" :
									user_command_2
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': [
												'🆕 새로운 레시피',
												'📕 음식 이름 검색',
												#'📗 레시피 이름 검색',
												#'📘 레시피 작성자 검색',
												'🔙 처음으로'
											]
								}
						})

	elif user_command_2 == '🆕 새로운 레시피':

		try :
			user_command_3 = (user.COMMAND).split('#')[3]
		except:
			user_command_3 = '-1'

		if user_command_3 == '-1':	# 검색창
			searchs = models.RECIPE.objects.all().order_by('-CHECK')
			search = []
			search.append('🔙 처음으로')
			for temp in searchs:
				search.append("[" + str(temp.CHECK) + "] " +temp.R_NAME + "-" + temp.USER_NAME + "-👍:" + str(temp.PICK))

			return JsonResponse({
								"message":{
									"text" :
										"모든 레시피를 받아옵니다."
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': search
									}
							})
		else :
			try :
				user_command_4 = (user.COMMAND).split('#')[4]
			except:
				user_command_4 = '-1'

			if user_command_4 == "-1":	# 요리시작전

				recipe_number = content.split("]")[0].split("[")[1]
				recipe_info = models.RECIPE.objects.get(CHECK = recipe_number)
				return JsonResponse({
								"message":{
									"text" :
										"레시피 이름 : " + recipe_info.R_NAME + "\n" +
										"요리 이름 : " + recipe_info.F_NAME + "\n" +
										"재료 : " + recipe_info.INGRED
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': ["1단계씩보기","🔙 처음으로"]
									}
							})
			elif user_command_4 == "1단계씩보기":
				user_command_3 = (user.COMMAND).split('#')[3]
				user.COMMAND = "#리딩중#" + (user_command_3.split("]")[0]).split("[")[1] + "#1"	# 리딩중 커맨드와 레시피 번호 넣기
				user.HISTORY = "#리딩중#" + (user_command_3.split("]")[0]).split("[")[1]
				user.COOK = 1
				user.save()
				return pick_recipe.recipe(0, user)

	elif user_command_2 == '📕 음식 이름 검색':

		try :
			user_command_3 = (user.COMMAND).split('#')[3]
		except:
			user_command_3 = '-1'
		
		if user_command_3 == '-1':	# 검색창

			return JsonResponse({
						"message":{
							"text" :
								"음식 이름으로 검색합니다.\n\n"+
								"예 : 부대찌개"

							},
						'keyboard': {
							'type': 'text'
							}
						})
		else :
			try :
				user_command_4 = (user.COMMAND).split('#')[4]
			except:
				user_command_4 = '-1'

			if user_command_4 == '-1' :	# 검색 기본

				if models.RECIPE.objects.filter(F_NAME = user_command_3).exists():
					searchs = models.RECIPE.objects.filter(F_NAME = user_command_3).order_by('USER_NAME')
					search = []
					for temp in searchs:
						search.append("[" + str(temp.CHECK) + "] " +temp.R_NAME + "-" + temp.USER_NAME + "-👍:" + str(temp.PICK))

					search.append('🔙 처음으로')

					return JsonResponse({
								"message":{
									"text" :
										content +"로 검색을 완료하였습니다.\n"+
										"레시피를 눌러주시면 자세한 정보를 보여드립니다."
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': search
									}
							})

				else:
					return JsonResponse({
									"message":{
										"text" :
											"검색된 레시피가 없습니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': home
										}
								})
			else :

				try :
					user_command_5 = (user.COMMAND).split('#')[5]
				except:
					user_command_5 = '-1'

				if user_command_5 == "-1":	# 요리시작전
					recipe_number = content.split("]")[0].split("[")[1]
					recipe_info = models.RECIPE.objects.get(CHECK = recipe_number)
					return JsonResponse({
									"message":{
										"text" :
											"레시피 정보를 받아옵니다.\n" +
											str(recipe_info.CHECK)
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': ["요리시작하기","🔙 처음으로"]
										}
								})
				elif user_command_5 == "요리시작하기":
					user_command_4 = (user.COMMAND).split('#')[4]
					user.COMMAND = "#리딩중#" + (user_command_4.split("]")[0]).split("[")[1] + "#1"	# 리딩중 커맨드와 레시피 번호 넣기
					user.HISTORY = "#리딩중#" + (user_command_4.split("]")[0]).split("[")[1]
					user.COOK = 1
					user.save()
					return pick_recipe.recipe(0, user)

# 미완성 메뉴
	elif user_command_2 == '📗 레시피 이름 검색':

		try :
			user_command_3 = (user.COMMAND).split('#')[3]
		except:
			user_command_3 = '-1'
		
		if user_command_3 == '-1':	# 검색창

			return JsonResponse({
						"message":{
							"text" :
								"레시피 이름으로 검색합니다.\n\n"+
								"예 : 단짠 치킨만들기"

							},
						'keyboard': {
							'type': 'text'
							}
						})

		else :
			try :
				user_command_4 = (user.COMMAND).split('#')[4]
			except:
				user_command_4 = '-1'

			if user_command_4 == '-1' :	# 검색 기본

				if models.RECIPE.objects.filter(R_NAME = user_command_3).exists():

					if models.RECIPE.objects.filter(R_NAME = user_command_3).count() < 2 :	# 검색된 레시피가 중복된 경우
						search = models.RECIPE.objects.get(R_NAME = user_command_3)
						return JsonResponse({
										"message":{
											"text" :
												"레시피 이름 : " + search.R_NAME + "\n" +
												"음식 이름 : " + search.F_NAME
											},
										'keyboard': {
											'type': 'buttons',
											'buttons': ['레시피 검색']
											}
									})

					else :
						searchs = models.RECIPE.objects.filter(R_NAME = user_command_3).order_by('USER_NAME')
						search = []
						for temp in searchs:
							search.append(temp.R_NAME + "-" + temp.USER_NAME)

						search.append('🔙 처음으로')

						return JsonResponse({
									"message":{
										"text" :
											"검색된 레시피가 여러개 존재합니다.\n"+
											"찾으시는 레시피를 선택해주세요!"
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': search
										}
								})

				else:
					return JsonResponse({
									"message":{
										"text" :
											"검색된 레시피가 없습니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': home
										}
								})
			elif user_command_4 == '조리 시작':	# 이제 조리시작들어갔을 경우
				return JsonResponse({
									"message":{
										"text" :
											"조리시작이 불가능합니다"
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': home
										}
								})

			else :	# 다중 리스트 중 선택했을 경우
				user.COMMAND = user.HISTORY	# 이전 입력으로 미리 돌아가 놓고 조리시작 대기
				user.save()
				search = models.RECIPE.objects.filter(USER_NAME = user_command_4.split("-")[1]).get(R_NAME = user_command_4.split('-')[0])
				return JsonResponse({
								"message":{
									"text" :
										"레시피 이름 : " + search.R_NAME + "\n" +
										"음식 이름 : " + search.F_NAME
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': ['조리 시작','레시피 검색','🔙 처음으로']
									}
							})

	elif user_command_2 == '📘 레시피 작성자 검색':

		try :
			user_command_3 = (user.COMMAND).split('#')[3]
		except:
			user_command_3 = '-1'
		
		if user_command_3 == '-1':	# 검색창

			return JsonResponse({
						"message":{
							"text" :
								"레시피 작성자이름으로 검색합니다.\n\n"+
								"예 : 닉네임"

							},
						'keyboard': {
							'type': 'text'
							}
						})

		else :
			try :
				user_command_4 = (user.COMMAND).split('#')[4]
			except:
				user_command_4 = '-1'

			if user_command_4 == '-1' :	# 검색 기본

				if models.RECIPE.objects.filter(USER_NAME = user_command_3).exists():

					if models.RECIPE.objects.filter(USER_NAME = user_command_3).count() == 1 :	# 닉네임에 의한 레시피가 한개인 경우
						search = models.RECIPE.objects.get(USER_NAME = user_command_3)
						return JsonResponse({
										"message":{
											"text" :
												"레시피 이름 : " + search.R_NAME + "\n" +
												"음식 이름 : " + search.F_NAME
											},
										'keyboard': {
											'type': 'buttons',
											'buttons': ['🔙 처음으로']
											}
									})
					else :
						searchs = models.RECIPE.objects.filter(USER_NAME = user_command_3).order_by('R_NAME')
						search = []
						for temp in searchs:
							search.append(temp.R_NAME + "-" + temp.USER_NAME)

						search.append('🔙 처음으로')

						return JsonResponse({
									"message":{
										"text" :
											"검색된 레시피가 여러개 존재합니다.\n"+
											"찾으시는 레시피를 선택해주세요!"
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': search
										}
								})
				else :
					return JsonResponse({
									"message":{
										"text" :
											"검색된 레시피가 없습니다."
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': home
										}
								})
			elif user_command_4 == '조리 시작':	# 이제 조리시작들어갔을 경우
				return JsonResponse({
									"message":{
										"text" :
											"조리시작이 불가능합니다"
										},
									'keyboard': {
										'type': 'buttons',
										'buttons': home
										}
								})

			else :	# 다중 리스트 중 선택했을 경우
				user.COMMAND = user.HISTORY	# 이전 입력으로 미리 돌아가 놓고 조리시작 대기
				user.save()
				search = models.RECIPE.objects.filter(USER_NAME = user_command_4.split("-")[1]).get(R_NAME = user_command_4.split('-')[0])
				return JsonResponse({
								"message":{
									"text" :
										"레시피 이름 : " + search.R_NAME + "\n" +
										"음식 이름 : " + search.F_NAME
									},
								'keyboard': {
									'type': 'buttons',
									'buttons': ['조리 시작','레시피 검색','🔙 처음으로']
									}
							})

	else :
		return JsonResponse({
							"message":{
								"text" :
									"개발영역"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': home
								}
						})


	return JsonResponse({
							"message":{
								"text" :
									"개발영역"
								},
							'keyboard': {
								'type': 'buttons',
								'buttons': home
								}
						})

home = ['🔙 처음으로']