# DB 쿼리 + 집계 = Union_DB.py
import pymysql


def get_connection():   # DB 접속
    return pymysql.connect(
        host='192.168.32.39',
        user='testuser',
        password='test1234',
        database='testdb'
    )


def create_table():     # 테이블이 없으면 생성
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Survey_INFO (
                    NO INT AUTO_INCREMENT PRIMARY KEY,
                    BIRTH VARCHAR(6) NOT NULL,
                    SEX TINYINT NOT NULL,
                    FIVECOLOR TINYINT NOT NULL,
                    RP TINYINT NOT NULL,
                    PS TINYINT NOT NULL,
                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    finally:
        conn.close()


def save_data(birth, sex, color, rp, ps):   # 설문 정보 저장
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            sql = """
            INSERT INTO Survey_INFO
            (BIRTH, SEX, FIVECOLOR, RP, PS)
            VALUES (%s, %s, %s, %s, %s)
            """

            cur.execute(sql, (birth, sex, color, rp, ps))
            conn.commit()

    finally:
        conn.close()


def show_statistics():      # 집계
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            stats = {
                "성별": ("SEX", {1: "남", 2: "여", 3: "불명"}),
                "오방색": ("FIVECOLOR", {1: "흑", 2: "백", 3: "적", 4: "청", 5: "황"}),
                "평면모양": ("RP", {1: "원", 2: "삼각", 3: "사각", 4: "오각", 5: "다각"}),
                "입체모양": ("PS", {1: "구", 2: "정팔면체", 3: "정육면체", 4: "정십이면체", 5: "정이십면체"})
            }
            
            cur.execute("SELECT COUNT(*) FROM Survey_INFO")     # 테이블 모든 설문 참여자 집계
            total_count = cur.fetchone()[0]         # 설문 참여자 집계 내역 저장

            print()
            print("===== 설문 집계 현황 =====")
            print()
            print(f"전체 응답 수 : {total_count}명")      # 설문 참여자 집계 출력

            for title, data in stats.items():
                column = data[0]        # 설문 문항 이름
                options = data[1]       # 문항 항목 내용
                
                print()
                print(f"[{title}]")   # 설문 문항별 항목 차례대로 출력

                sql = f"""
                SELECT {column}, COUNT(*)
                FROM Survey_INFO
                GROUP BY {column}
                ORDER BY {column}
                """
                                
                cur.execute(sql)
                result = cur.fetchall()     # 문항별 인원 집계 
                count_dict = dict(result)   # 문항별 집계 내역 저장
                
                for key, value in options.items():
                    
                    count = count_dict.get(key, 0)
                    
                    if total_count > 0:
                        percent = (count / total_count) * 100       # 백분율 계산
                    else:
                        percent = 0
                    
                    print(f"{value} : {count}명 ({percent:.1f}%)")  # 문항 항목별 인원 확인 + 백분율 분포 집계

            print("==========================")
            print()

    finally:
        conn.close()