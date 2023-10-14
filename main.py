# 행맨 게임
# 동물 이름 맞추기

import hangman_function
import words_list
def main():
    # 단어 랜덤 선택
    word = hangman_function.choose_word(words_list.words)
    
    # 정답 단어와 일치하는 문자를 저장할 리스트
    correct_letter_list = []

    # 입력 시도 회수
    attempts = 6

    hangman_function.display_start()
    # 게임 루프
    while hangman_function.count_attempts(attempts):
        hangman_function.display_word(word, correct_letter_list, attempts)
        guess = hangman_function.input_word()
        if hangman_function.except_handling_guess(guess, correct_letter_list):
            continue
        if hangman_function.check_correct_guess(word, guess, correct_letter_list):
            attempts = hangman_function.decrease_attempts(attempts)
        if hangman_function.check_correct_letter(word, correct_letter_list):
            break

    # 게임 결과 확인
    hangman_function.is_game_over(word, correct_letter_list, attempts)

if __name__ == '__main__':
    main()
