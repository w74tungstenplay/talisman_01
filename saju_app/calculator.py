# calculator.py

def calculate_five_elements(birth_date, birth_time):
    """
    생년월일과 출생시간을 바탕으로 오행 구성 비율 계산 (간단한 임의 예시).
    실제 사주명리학 로직이 필요한 경우 외부 사주 API 또는 사주 알고리즘이 필요함.
    """
    # 생일 정보를 문자열로 변환
    birth_str = birth_date.strftime("%Y%m%d") + birth_time.strftime("%H%M")
    seed = sum([int(char) for char in birth_str if char.isdigit()])

    # 5로 나눈 나머지를 기준으로 간단한 분포 생성
    five_elements = {
        "목": (seed + 0) % 3,
        "화": (seed + 1) % 3,
        "토": (seed + 2) % 3,
        "금": (seed + 3) % 3,
        "수": (seed + 4) % 3,
    }

    return five_elements


def recommend(five_elements):
    """
    부족한 오행에 대해 오방색과 숫자를 추천합니다.
    부족 기준: count < 2
    """
    result = []

    for element, count in five_elements.items():
        if count < 2:
            result.append({
                "오행": element,
                "오방색": element_to_color(element),
                "추천 숫자": element_to_number(element)
            })

    return {"추천": result}


def element_to_color(element):
    """
    오행에 해당하는 오방색을 반환
    """
    color_map = {
        "목": "청색",
        "화": "적색",
        "토": "황색",
        "금": "백색",
        "수": "흑색"
    }
    return color_map.get(element, "무색")


def element_to_number(element):
    """
    오행에 해당하는 길한 숫자를 반환
    """
    number_map = {
        "목": [3, 8],
        "화": [2, 7],
        "토": [5, 10],
        "금": [4, 9],
        "수": [1, 6]
    }
    return number_map.get(element, [])
from calculator import calculate_five_elements, recommend

