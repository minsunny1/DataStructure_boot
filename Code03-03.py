def delete_data(idx) :
	if idx < 0 or idx > len(pokemons) :
		print("Out of range!")
		return

	len_pokemons = len(pokemons)
	pokemons[idx] = None	# 데이터 삭제

	for i in range(idx + 1, len_pokemons) :
		# pokemons[i - 1] = pokemons[i]
		# pokemons[i] = None	# 배열의 맨 마지막 위치 삭제
		pokemons[i] = None  # [1]이후의 값 모두 삭제
	# pokemons.pop()

	for i in range(idx, 5):  # [1]이후의 값 모두 삭제
		pokemons.pop()


	# del pokemons[len_pokemons - 1]


if __name__ == "__main__":  # main 함수처럼 동작
	pokemons = ["피카츄", "라이츄", "원츄", "꼬부기", "이상해"]
	print(pokemons)
	# delete_data(2)
	# print(pokemons)
	# delete_data(3)
	# print(pokemons)
	delete_data(1)  # [1]이후의 값 모두 삭제
	print(pokemons)


# pokemons = ['다현', '정연', '쯔위', '사나', '지효']
#
#
# def delete_data(position):
# 	if position < 0 or position > len(pokemons):
# 		print("데이터를 삭제할 범위를 벗어났습니다.")
# 		return
#
# 	kLen = len(pokemons)
# 	pokemons[position] = None  # 데이터 삭제
#
# 	for i in range(position + 1, kLen):
# 		pokemons[i - 1] = pokemons[i]
# 		pokemons[i] = None  # 배열의 맨 마지막 위치 삭제
#
# 	del (pokemons[kLen - 1])
#
#
# delete_data(1)
# print(pokemons)
# delete_data(3)
# print(pokemons)