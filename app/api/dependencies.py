from app.infra.db.conn import get_pool


def get_database():
    return get_pool()
