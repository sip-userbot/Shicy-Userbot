from sqlalchemy import Column, String

from ShicyXd.modules.sql_helper import BASE, SESSION


class GBan(BASE):
    __tablename__ = "gban"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason


GBan.__table__.create(checkfirst=True)


def is_gbanned(chat_id):
    try:
        return SESSION.query(GBan).filter(GBan.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_gbanuser(chat_id):
    try:
        return SESSION.query(GBan).get(str(chat_id))
    finally:
        SESSION.close()


def freakgban(chat_id, reason):
    adder = GBan(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def freakungban(chat_id):
    rem = SESSION.query(GBan).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_gbanned():
    rem = SESSION.query(GBan).all()
    SESSION.close()
    return rem
