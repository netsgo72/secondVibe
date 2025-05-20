import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="연령별 인구 현황 시각화", layout="wide")

# 데이터 불러오기
st.title("📊 연령별 인구 현황 시각화 (남녀/합계)")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="cp949")

    # 열 미리보기
    st.subheader("데이터 미리보기")
    st.dataframe(df.head())

    # 연도/월, 연령대, 성별 선택
    if "성별" in df.columns:
        sex_list = df["성별"].unique()
        selected_sex = st.selectbox("성별 선택", sex_list)

        filtered_df = df[df["성별"] == selected_sex]
    else:
        filtered_df = df.copy()

    # 연령대 기준으로 최신 월 선택
    filtered_df["기간"] = pd.to_datetime(filtered_df["기간"], errors="coerce")
    latest_date = filtered_df["기간"].max()
    df_latest = filtered_df[filtered_df["기간"] == latest_date]

    st.subheader(f"📈 {latest_date.date()} 기준 연령별 인구 분포")
    fig = px.bar(
        df_latest,
        x="연령별",
        y="총인구수 (명)",
        title=f"{latest_date.date()} 기준 연령별 인구수",
        labels={"연령별": "연령대", "총인구수 (명)": "인구수"},
        color="연령별"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📉 연령대별 인구 변화 (타임라인)")
    age_group = st.selectbox("연령대 선택", filtered_df["연령별"].unique())
    df_age = filtered_df[filtered_df["연령별"] == age_group]

    fig2 = px.line(
        df_age.sort_values("기간"),
        x="기간",
        y="총인구수 (명)",
        title=f"{age_group} 인구 변화 추이",
        labels={"총인구수 (명)": "인구수"},
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("CSV 파일을 업로드해 주세요. 예: 연령별인구현황_월간_남녀합계.csv")
