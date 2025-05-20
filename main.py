import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="스페인 여행 안내",
    page_icon="🇪🇸",
    layout="wide"
)

# --- 1. 사이드바 설정 ---
st.sidebar.title("🇪🇸 스페인 여행 가이드")
st.sidebar.markdown("꿈같은 스페인 여행을 시작해보세요!")

# --- 2. 메인 페이지 제목 및 소개 ---
st.title("🇪🇸 스페인으로 떠나는 여행")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sagrada_Fam%C3%ADlia_-_Barcelona.jpg/1920px-Sagrada_Fam%C3%ADlia_-_Barcelona.jpg",
         caption="바르셀로나의 사그라다 파밀리아",
         use_column_width=True)
st.markdown("""
스페인은 풍부한 역사, 활기찬 문화, 아름다운 자연경관, 그리고 맛있는 음식으로 가득한 나라입니다. 
이 앱은 여러분의 스페인 여행 계획을 돕기 위해 주요 도시 정보, 추천 활동, 그리고 유용한 팁을 제공합니다.
""")

# --- 3. 주요 도시 소개 ---
st.header("✨ 주요 도시 탐험")

# 도시 데이터
cities = {
    "마드리드": {
        "설명": "스페인의 수도이자 심장부인 마드리드는 왕궁, 프라도 미술관과 같은 세계적인 박물관, 그리고 활기찬 밤문화로 유명합니다.",
        "추천": ["프라도 미술관 방문", "레티로 공원에서 휴식", "마요르 광장과 산 미구엘 시장 탐방", "플라멩코 공연 관람"],
        "좌표": [40.4168, -3.7038]
    },
    "바르셀로나": {
        "설명": "가우디의 건축물로 유명한 바르셀로나는 현대적인 예술과 고딕 양식의 조화가 돋보이는 해변 도시입니다. 타파스와 카바를 즐기기에도 좋습니다.",
        "추천": ["사그라다 파밀리아", "구엘 공원", "고딕 지구", "람블라스 거리", "바르셀로네타 해변"],
        "좌표": [41.3851, 2.1734]
    },
    "세비야": {
        "설명": "안달루시아 지방의 수도인 세비야는 플라멩코의 발상지이자 스페인의 전통적인 매력을 느낄 수 있는 도시입니다. 알카사르 궁전과 세비야 대성당이 유명합니다.",
        "추천": ["세비야 대성당과 히랄다 탑", "알카사르 궁전", "스페인 광장", "트리아나 지구 탐방", "플라멩코 쇼 관람"],
        "좌표": [37.3887, -5.9829]
    }
}

selected_city = st.selectbox("어떤 도시를 탐험하고 싶으신가요?", list(cities.keys()))

if selected_city:
    st.subheader(f"📍 {selected_city}")
    st.write(cities[selected_city]["설명"])
    st.write("**추천 활동:**")
    for activity in cities[selected_city]["추천"]:
        st.markdown(f"- {activity}")

# --- 4. 스페인 지도 ---
st.header("🗺️ 스페인 주요 도시 지도")

# 지도 초기화 (스페인 중앙으로 설정)
m = folium.Map(location=[40.4168, -3.7038], zoom_start=6)

# 도시에 마커 추가
for city_name, city_data in cities.items():
    folium.Marker(
        location=city_data["좌표"],
        popup=city_name,
        tooltip=city_name
    ).add_to(m)

# Streamlit에 지도 표시
st_folium(m, width=800, height=500)

# --- 5. 나만의 여행 계획 도구 (간단한 예시) ---
st.header("🗓️ 나만의 스페인 여행 계획")
st.markdown("여행 기간을 입력하시면 간단한 추천 활동을 보여드립니다.")

travel_days = st.slider("여행 기간 (일)", 1, 14, 5)

if travel_days <= 3:
    st.info("짧은 여행을 위한 추천: 마드리드 또는 바르셀셀로나 한 도시에 집중하여 주요 명소를 방문하세요.")
elif 4 <= travel_days <= 7:
    st.info("중간 여행을 위한 추천: 마드리드와 바르셀로나 두 도시를 방문하거나, 세비야를 추가하여 안달루시아의 매력을 느껴보세요.")
else:
    st.info("긴 여행을 위한 추천: 스페인 전역을 여행하며 마드리드, 바르셀로나, 세비야 외에도 발렌시아, 그라나다, 빌바오 등 다양한 도시를 경험해보세요!")

# --- 6. 스페인 여행 팁 ---
st.header("💡 스페인 여행 팁")
st.markdown("""
* **언어**: 스페인어 (일부 관광지는 영어 소통 가능)
* **통화**: 유로 (EUR)
* **교통**: 고속철도 (AVE)가 잘 되어 있어 도시 간 이동이 편리합니다. 도시 내에서는 지하철, 버스를 이용하세요.
* **식사**: 점심은 14시 이후, 저녁은 21시 이후에 먹는 경우가 많습니다. 타파스와 상그리아를 꼭 즐겨보세요!
* **팁**: 식당에서는 보통 팁을 필수로 주지 않지만, 서비스가 좋았다면 5-10% 정도를 남길 수 있습니다.
* **시차**: 한국보다 8시간 느립니다. (서머타임 시 7시간)
* **안전**: 소매치기 등 경범죄에 유의하고, 특히 인파가 많은 곳에서는 소지품 관리에 신경 쓰세요.
""")

st.markdown("---")
st.caption("© 2025 스페인 여행 가이드. 즐거운 여행 되세요!")
