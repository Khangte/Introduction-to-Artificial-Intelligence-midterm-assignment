import random

def choose_word(words_list):
    # 랜덤 단어 선택
    word = random.choice(words_list)
    word = word.lower()  # 단어를 소문자로 변환
    return word

def display_start():
    # 게임 시작 문구 출력
    print("--------------------")
    print("[ 행맨 게임 (동물 이름 맞추기) ]")
    print("게임 시작!!!")
    print("--------------------")

def display_word(word, correct_letter_list, attempts):
    # 게임 문구 출력
    display = ""
    for letter in word:
        if letter in correct_letter_list:
            display += letter
        else:
            display += "_"
    print("남은 시도: " + str(attempts))
    print("글자 개수: " + str(len(word)))
    print("현재 단어: " + display)

def count_attempts(attempts):
    # 남은 시도 회수 세기
    if attempts > 0:
        return 1
    elif attempts == 0:
        print("모든 시도를 사용하였습니다.")
        return 0
    try:
        if attempts < 0:
            raise ValueError("시도 횟수 오류")
    except ValueError as e:
        print(e)

def input_word():
    # 문자 입력 후 소문자로 변환
    guess = input("문자 입력: ").lower()
    print("--------------------")
    return guess

def except_handling_guess(guess, correct_letter_list):
    # 예외 처리
    try:
        if not guess.isalpha():
            raise ValueError("올바른 알파벳을 입력하세요.")
    except ValueError as e:
        print(e)
        print("--------------------")
        return 1
    try:
        if len(guess) != 1:
            raise ValueError("하나의 알파벳만 입력하세요")
    except ValueError as e:
        print(e)
        print("--------------------")
        return 1
    try:
        if guess in correct_letter_list:
            raise ValueError("이미 일치한 문자입니다.")
    except ValueError as e:
        print(e)
        print("--------------------")
        return 1

def check_correct_guess(word, guess, correct_letter_list):
    # 입력된 문자가 정답에 있는지 확인
    if guess in word:
        correct_letter_list.append(guess)
    else:
        print("아닙니다!\n시도 1회가 감소합니다.")
        print("--------------------")
        return 1

def decrease_attempts(attempts):
    # 시도 회수 감소
    attempts -= 1
    return attempts

def check_correct_letter(word, correct_letter_list):
    # 입력된 단어가 정답과 일치하는지 확인
    if set(correct_letter_list) == set(word):
        return 1

def is_game_over(word, correct_letter_list, attempts):
    # 게임 결과 확인 및 출력
    if set(correct_letter_list) == set(word):
        print(f'축하합니다! 정답은 {word}입니다.')
    if attempts == 0:
        print(f'아쉽습니다. 정답은 {word}이었습니다.')
