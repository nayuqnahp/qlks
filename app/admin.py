from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db, dao
from app.models import TypeRoom, Room, RoomForm, Regulation, User
from flask_login import logout_user, current_user
from flask import redirect, request
from app.models import UserRoleEnum
import hashlib
admin = Admin(app=app, name='OU HOTEL', template_mode='bootstrap4')


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class MyRoomView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'description', 'image', 'typeroom']
    column_searchable_list = ['name']
    column_filters = ['name']
    can_export = True
    can_view_details = True

class MyRoomFormView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'check_in', 'check_out', 'count', 'typeroom']
    column_searchable_list = ['name']
    column_filters = ['name']
    can_export = True
    can_view_details = True

class MyRegulationView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'number', 'note']
    column_searchable_list = ['name']
    column_filters = ['name']
    can_export = True
    can_view_details = True

class MyTypeRoomView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'rooms','price']





class MyStatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        kw = request.args.get("kw")
        return self.render('admin/stats.html', stats=dao.revenue_stats(kw))





class MyUserView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'username', 'password', 'user_role']
    column_searchable_list = ['name']
    column_filters = ['name']
    can_export = True
    can_view_details = True

    def on_model_change(self, form, model, is_created=True):
        if 'password' in form:
            model.password = str(hashlib.md5(form.password.data.encode('utf-8')).hexdigest())


class MyLogOutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyTypeRoomView(TypeRoom, db.session))
admin.add_view(MyRoomView(Room, db.session))
admin.add_view(MyRoomFormView(RoomForm, db.session))
admin.add_view(MyRegulationView(Regulation, db.session))
admin.add_view(MyUserView(User, db.session))
admin.add_view(MyStatsView(name='Báo cáo doanh thu'))
admin.add_view(MyLogOutView(name='Đăng xuất'))
