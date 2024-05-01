from api import cruds
from api.models import User


def test_user_id_1_data(db_with_data):
    user = db_with_data.query(User).filter_by(user_id=1).one()
    assert user.user_name == 'ぽん'


def test_get_users(db_session):
    """ユーザーを取得するテスト関数"""
    users = cruds.get_users(db=db_session)
    assert isinstance(users, list)
