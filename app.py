import pandas as pd
import streamlit as st

st.set_page_config(page_title='보상질문톡')

st.header("보상질문을 검색해보세요 - 메리츠")

password = st.text_input("비밀번호를 입력해주세요")

if password=='1003':

    @st.cache()
    def read_pickle():
        df = pd.read_pickle(r'1.pkl')
        return df

    df = read_pickle()

    search_keyword = st.text_input('검색어를 입력해주세요')

    if search_keyword:

        search_1 = search_keyword.split(" ")

        search_title = []
        search_question = []
        search_contents = []

        for i in search_1:
            search_title.append(df[df['제목'].str.contains(i)].index.tolist())
            search_question.append(df[df['질문'].str.contains(i)].index.tolist())
            search_contents.append(df[df['답변'].str.contains(i)].index.tolist())

        def make_intersection(list_):
            base_list = list_[0]
            for i in range(len(list_)-1):
                temp = list(set(base_list).intersection(list_[i+1]))
                base_list = temp
            return base_list

        def flatten(lst):
            result = []
            for item in lst:
                if type(item) == list:
                    result += flatten(item)
                else:
                    result +=[item]
            return result

        a1 = make_intersection(search_title)
        a2 = make_intersection(search_question)
        a3 = make_intersection(search_contents)
        a_all = [a1, a2, a3]
        a_all = flatten(a_all)
        a_all = list(set(a_all))

        a_all.sort()

        for i in a_all:
            title = df.loc[i].제목
            question = df.loc[i].질문
            answer = df.loc[i].답변
            date1 = df.loc[i].일자
            msg = str(date1)+"\n"+title+"\n"+question+"\n"+answer
            print(msg)
            if len(msg)>0:
                st.info(msg)
