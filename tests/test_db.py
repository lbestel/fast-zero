from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='dunossauro',
        email='duno@sauro.com',
        password='minhasenha',
    )

    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'duno@sauro.com'))

    assert result.id == 1
