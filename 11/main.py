NO_OF_CHARS = 256

def getNextState(pat, M, state, x):
	# Если символ c совпадает с следующим символом в образце,
	# просто увеличиваем состояние

	if state < M and x == ord(pat[state]):
		return state+1

	i=0
	# ns хранит результат, который является следующим состоянием

	# ns наконец содержит самый длинный префикс,
	# который также является суффиксом в "pat[0..state-1]c"

	# Начинаем с самого большого возможного значения и
	# останавливаемся, когда найдем префикс, который также является суффиксом
	for ns in range(state,0,-1):
		if ord(pat[ns-1]) == x:
			while(i<ns-1):
				if pat[i] != pat[state-ns+1+i]:
					break
				i+=1
			if i == ns-1:
				return ns 
	return 0

def computeTF(pat, M):
	global NO_OF_CHARS

	TF = [[0 for i in range(NO_OF_CHARS)]\
		for _ in range(M+1)]

	for state in range(M+1):
		for x in range(NO_OF_CHARS):
			z = getNextState(pat, M, state, x)
			TF[state][x] = z

	return TF

def search(pat, txt):
	global NO_OF_CHARS
	M = len(pat)
	N = len(txt)
	TF = computeTF(pat, M) 

	# Обрабатываем текст по конечному автомату.
	state=0
	for i in range(N):
		state = TF[state][ord(txt[i])]
		if state == M:
			print("Образец найден по индексу: {}".\
				format(i-M+1))


with open('input.txt', 'r', encoding='utf-8') as file:
    txt = file.read().strip()
pat = input("Введите строку поиска: ")
search(pat, txt)
