# 메인 = Main_Survey.py
from Func_Info import birth, sex, color, rp, ps
from Union_DB import create_table, save_data, show_statistics

create_table()

while True:     # 설문 참여 여부
    print("\n===== 개취 설문조사 =====")
    print()
    print("1. 설문 참여")
    print("2. 집계 현황 보기")
    print("0. 종료")
    print()

    menu = input(">> 선택 : ")
    print()

    if not menu.isdigit():
        print("==========================")
        print("숫자만 입력 가능합니다.")
        print("==========================")
        print()
        continue
    
    menu = int(menu)

    if menu == 1:
        print("==========================")
        print()
        print("$ 개인취향 설문조사를 시작합니다.")
        print()
        birth_data = birth()
        sex_data = sex()
        color_data = color()
        rp_data = rp()
        ps_data = ps()

        save_data(
            birth_data,
            sex_data,
            color_data,
            rp_data,
            ps_data
        )

        print("설문조사가 완료되었습니다.")

        show_statistics()

    elif menu == 2:
        show_statistics()

    elif menu == 0:
        print("==========================")
        print()
        print("프로그램을 종료합니다.")
        print()
        print("==========================")
        print()
        break

    else:
        print("==========================")
        print()
        print("1, 2, 0 중에서 선택하세요.")
        print()
        print("==========================")
        print()