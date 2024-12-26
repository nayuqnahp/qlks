from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    ADMIN = 1
    STAFF = 2
    CUSTOMER = 3

    def __str__(self):
        return self.name

class UserRoleCustomer(enum.Enum):
    DOMESTIC = 1
    Foreign = 2

    def __str__(self):
        return self.name
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(200), default='https://s.net.vn/UqTC')
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.CUSTOMER)

    def __str__(self):
        return self.name




class TypeRoom(db.Model):
    __tablename__ = 'typeroom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    rooms = relationship('Room', backref='typeroom', lazy=True)
    price = Column(Float, default=0)

    def __str__(self):
        return self.name


class Room(db.Model):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(200), nullable=False)
    image = Column(String(200), nullable=False)
    price = Column(Float, default=0)
    typeroom_id = Column(Integer, ForeignKey(TypeRoom.id), nullable=False)


    def __str__(self):
        return self.name

class RoomForm(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100),nullable=False)
    check_in = Column(db.Date, nullable=False)
    check_out = Column(db.Date, nullable=False)
    count = Column(Integer,nullable=False)
    typeroom= Column(String(100), nullable=False)
    def __str__(self):
        return self.name
class Regulation(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    note = Column(String(100), nullable=False)
    def __str__(self):
        return self.name

class Bill(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    check_in = Column(db.Date, nullable=False)
    check_out = Column(db.Date, nullable=False)
    count = Column(Integer, nullable=False)
    typeroom = Column(String(100), nullable=False)
    total = Column(Float, nullable=False)
    create_date = Column(db.Date, nullable=False)

if __name__ == '__main__':
    from app import app
    with app.app_context():
        import hashlib

        # user1 = User(username='admin',
        #              password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #              name='Admin',
        #              address='HCM',
        #              phone='0849165932',
        #              user_role=UserRoleEnum.ADMIN)
        # user2 = User(username='quyan',
        #              password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #              name='QuyAn',
        #              address='Hoc Mon',
        #              phone='0392995499',
        #              user_role=UserRoleEnum.STAFF)
        # user3 = User(username='nguyentuyen',
        #              password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #              name='NguyenTuyen',
        #              address='Vung Tau',
        #              phone='0775438606',
        #              user_role=UserRoleEnum.STAFF)
        # user4 = User(username='thienan',
        #              password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #              name='ThienAn',
        #              address='Go Vap',
        #              phone='0977751951',
        #              user_role=UserRoleEnum.STAFF)
        # db.session.add_all([user1, user2, user3, user4])
        # db.session.commit()

        # type1 = TypeRoom(name='Phòng President', price=5000000)
        # type2 = TypeRoom(name='Phòng Premium', price=3000000)
        # type3 = TypeRoom(name='Phòng Luxury', price=2000000)
        # type4 = TypeRoom(name='Phòng Studio', price=1500000)
        # type5 = TypeRoom(name='Phòng Executive', price=1000000)
        # db.session.add_all([type1, type2, type3, type4, type5])
        # db.session.commit()

        # room1 = Room(name='Phòng President Suite Hướng biển',
        #              description='THE ROOM FOR THE PRESIDENT, THE HEADS OF STATE',
        #              image='https://rosaalbaresort.com/wp-content/uploads/2023/10/RAS3-2048x1365.jpg',
        #              price=5000000,
        #              typeroom_id=1)
        # room2 = Room(name='Phòng Premium Deluxe Hướng Biển',
        #              description='A DISTINGUISHED YET COMFORTABLE AMBIENCE',
        #              image='https://rosaalbaresort.com/wp-content/uploads/2023/10/PDT11-scaled.jpg',
        #              price=3000000,
        #              typeroom_id=2)
        # room3 = Room(name='Phòng Luxury Deluxe Hướng Biển',
        #              description='INSPIRE ROMANTIC MEMORIES WITH A TRULY CHARMING RETREAT',
        #              image='https://rosaalbaresort.com/wp-content/uploads/2023/10/SD5-2048x1365.jpg',
        #              price=2000000,
        #              typeroom_id=3)
        # room4 = Room(name='Phòng Studio Deluxe Hướng Biển',
        #              description='INSPIRE ROMANTIC MEMORIES WITH A TRULY CHARMING RETREAT',
        #              image='https://rosaalbaresort.com/wp-content/uploads/2023/10/ST4-2048x1365.jpg',
        #              price=1500000,
        #              typeroom_id=4)
        # room5 = Room(name='Phòng Executive Deluxe Hướng Biển',
        #              description='THE TASTEFULLY DECORATED OFFER A HIGH LEVEL OF LUXURY',
        #              image='https://rosaalbaresort.com/wp-content/uploads/2023/10/ES3-2048x1365.jpg',
        #              price=1000000,
        #              typeroom_id=5)
        # db.session.add_all([room1, room2, room3, room4, room5])
        # db.session.commit()
        # db.create_all()

