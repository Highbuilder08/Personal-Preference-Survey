# 메인 = Main_Survey.py
from Func_Info import birth, sex, color, rp, ps
from Union_DB import create_table, save_data, show_statistics

create_table()

while True:     # 설문 참여 여부
    print("\n===== 개취 설문조사 =====")
    print("1. 설문 참여")
    print("2. 집계 현황 보기")
    print("0. 종료")
    print()

    menu = input("선택 : ")

    if menu == "1":     # 설문 참여 = Func_Info 모듈에서 함수 호출 및 정보 입력
        birth_data = birth()
        sex_data = sex()
        color_data = color()
        rp_data = rp()
        ps_data = ps()

        save_data(      # 입력값들을 튜플로 고정해서 조합
            birth_data,
            sex_data,
            color_data,
            rp_data,
            ps_data
        )

        print("설문조사가 완료되었습니다.")

        show_statistics()

    elif menu == "2":       # 설문 집계 출력 = Union_DB 모듈에서 조회
        show_statistics()

    elif menu == "0":       # 강제종료
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 선택하세요.")
    print()