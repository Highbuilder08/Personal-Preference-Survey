# 함수정리 = Func_Info.py
from datetime import datetime

def choice_input(title, options):   # 설문 문항
    while True:
        print("==========================")
        print(title)

        for key, value in options.items():
            print(f"{key}. {value}")    # (문항 항목 번호 . 문항 항목 이름) 차례대로 출력
        
        print()
        answer = input(">> 입력 : ")
        
        if answer in options:
            print()
            print(f"$ 선택 확인 : {options[answer]}")     # 입력값 재확인
            print("==========================")
            return int(answer)      # 입력값 int 값으로 반환

        print()
        print("==========================")
        print("잘못된 입력입니다. 보기 중에서 선택하세요.")
        print("==========================")
        print()


def birth():
    current_year = datetime.now().year

    while True:
        print("==========================")
        print("1번 문항 : 생년월 입력")
        print("예시 : 199911, 200302")
        print()
        b = input(">> 입력 : ")
        print()
        print("==========================")

        if not b.isdigit():
            print("숫자만 입력하세요.")
            print("==========================")
            print()
            continue
        
        if len(b) != 6:
            print("YYYYMM 형식의 6자리를 입력하세요.")
            print("==========================")
            print()
            continue

        year = int(b[:4])   # 년도 저장
        month = int(b[4:6]) # 월 저장

        if year < 1900:     # 1900 미만 입력시 재입력
            print("1900년 이후만 입력 가능합니다.")
            print("==========================")
            print()
            continue

        if year > current_year:     # 현재년도(2026) 이상 입력시 재입력
            print("미래 연도는 입력할 수 없습니다.")
            print("==========================")
            print()
            continue

        if month < 1 or month > 12: # 1~12월 아니면 재입력
            print("월은 01~12만 가능합니다.")
            print("==========================")
            print()
            continue

        print(f"$ 입력 확인 : {year}년 {month:02d}월")    # 년도와 월 확인 출력
        print("==========================")
        print()
        return b


def sex():
    return choice_input("성별", {
        "1": "남",
        "2": "여",
        "3": "불명"
    })


def color():
    return choice_input("오방색", {
        "1": "흑",
        "2": "백",
        "3": "적",
        "4": "청",
        "5": "황"
    })


def rp():
    return choice_input("평면모양", {
        "1": "원",
        "2": "삼각",
        "3": "사각",
        "4": "오각",
        "5": "다각"
    })


def ps():
    return choice_input("입체모양", {
        "1": "구",
        "2": "정팔면체",
        "3": "정육면체",
        "4": "정십이면체",
        "5": "정이십면체"
    })
