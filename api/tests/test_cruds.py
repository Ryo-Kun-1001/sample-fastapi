from api import cruds
from api.models import User


def test_user_id_1_data(db_with_data):
    user = db_with_data.query(User).filter_by(user_id=1).one()
    assert user.user_name == 'ぽん'


def test_get_users(db_with_data):
    """ユーザーを取得するテスト関数"""
    user_objects = cruds.get_users(db=db_with_data)
    assert isinstance(user_objects, list)

    users = [{"user_name": user.user_name, "user_id": user.user_id}
             for user in user_objects]

    # 期待するユーザーデータ
    expected_users = [
        {"user_name": "ぽん", "user_id": 1},
        {"user_name": "ささかわ", "user_id": 2},
        {"user_name": "くらた", "user_id": 3},
        {"user_name": "ふじた", "user_id": 4},
    ]

    # 取得したユーザーデータが期待するデータと一致するかを確認
    assert users == expected_users
