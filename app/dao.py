from app.models import TypeRoom, Room, User, RoomForm, Bill, db
import hashlib
from sqlalchemy import func

def load_typeroom():
    return TypeRoom.query.all()

def load_rooms(kw=None, type_id=None, pricefrom=None, priceto=None):
    rooms = Room.query
    if kw:
        rooms = rooms.filter(Room.name.contains(kw))
    if type_id:
        rooms = rooms.filter(Room.typeroom_id.__eq__(type_id))
    if pricefrom:
        rooms = rooms.filter(Room.price.__gt__(pricefrom))
    if pricefrom and priceto:
        rooms = rooms.filter(Room.price.__gt__(pricefrom),
                             Room.price.__lt__(priceto))
    return rooms.all()

def load_bookrooms(kw=None):
    rooms = Room.query
    if kw:
        rooms = rooms.filter(Room.name.contains(kw))
    return rooms.all()

def load_roomform():
    roomform = RoomForm.query

    return roomform.all()
def get_user_by_id(id):
    return User.query.get(id)

def get_room_by_id(id):
    return Room.query.get(id)

def get_typeroom_by_id(id):
    return TypeRoom.query.get(id)



def get_roomform_by_id(id):
    return RoomForm.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()

def revenue_stats(kw=None):

    query = db.session.query(TypeRoom.id, TypeRoom.name, func.sum(Room.price))\
                     .join(Room, Room.typeroom_id == TypeRoom.id).group_by(TypeRoom.id)

    return query