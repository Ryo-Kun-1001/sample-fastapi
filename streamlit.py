import streamlit as st
import random
import requests
import json
import datetime
import pandas as pd

page = st.sidebar.selectbox('Choose your page', ['users', 'rooms', 'bookings'])

if page == 'users':
    st.title('ユーザー登録画面')

    with st.form(key='user'):
        user_name: str = st.text_input('ユーザー名', max_chars=12)
        data = {
            'user_name': user_name,
        }
        submit_button = st.form_submit_button(label='登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('ユーザー登録完了')
        st.write(res.status_code)
        st.json(res.json())

elif page == 'rooms':
    st.title('会議室登録画面')

    with st.form(key='room'):
        room_name: str = st.text_input('会議室名', max_chars=12)
        capacity: int = st.number_input('定員', step=1, min_value=1)
        data = {
            'room_name': room_name,
            'capacity': capacity,
        }
        submit_button = st.form_submit_button(label='登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('会議室登録完了')
        st.write(res.status_code)
        st.json(res.json())

elif page == 'bookings':
    st.title('会議室予約画面')

    # ユーザー一覧取得
    url_users = 'http://127.0.0.1:8000/users'
    res = requests.get(url_users)
    users = res.json()
    users_dict = {}
    for user in users:
        users_dict[user['user_name']] = user

    # 会議室一覧取得
    url_rooms = 'http://127.0.0.1:8000/rooms'
    res = requests.get(url_rooms)
    rooms = res.json()
    rooms_dict = {}
    for room in rooms:
        rooms_dict[room['room_name']] = room

    st.write('### 会議室一覧')
    df_rooms = pd.DataFrame(rooms)
    df_rooms.columns = ['会議室名', '定員', '会議室ID']
    st.table(df_rooms)

    # 予約一覧取得
    url_bookings = 'http://127.0.0.1:8000/bookings'
    res = requests.get(url_bookings)
    bookings = res.json()

    st.write('### 予約一覧')
    df_bookings = pd.DataFrame(bookings)
    st.table(df_bookings)

    with st.form(key='booking'):
        user_name: str = st.selectbox('予約者名', users_dict.keys())
        room_name: str = st.selectbox('会議室名', rooms_dict.keys())
        booked_num: int = st.number_input('予約人数', step=1, min_value=1)
        target_date = st.date_input('日付:', min_value=datetime.date.today())
        start_time = st.time_input(
            '開始時刻:', value=datetime.time(hour=9, minute=0))
        end_time = st.time_input(
            '終了時刻:', value=datetime.time(hour=20, minute=0))

        submit_button = st.form_submit_button(label='予約')

    if submit_button:

        user_id: int = users_dict[user['user_name']]['user_id']
        room_id: int = rooms_dict[room['room_name']]['room_id']
        capacity: int = rooms_dict[room['room_name']]['capacity']

        data = {
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(year=target_date.year, month=target_date.month, day=target_date.day, hour=start_time.hour, minute=start_time.minute).isoformat(),
            'end_datetime': datetime.datetime(year=target_date.year, month=target_date.month, day=target_date.day, hour=end_time.hour, minute=end_time.minute).isoformat(),
        }

        st.write(data)

        # 定員以下の予約の場合、会議室の予約を行う
        if booked_num <= capacity:

            url = 'http://127.0.0.1:8000/bookings'
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('予約完了')
            st.write(res.status_code)
            st.write(res.json())

        else:
            st.error(f'{room_name}の定員は、{capacity}名です。')
