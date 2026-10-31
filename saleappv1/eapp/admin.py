from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from unicodedata import category
from wtforms.fields.numeric import FloatField

from eapp import app, db
from flask_admin import Admin
from eapp.models import Category, Product

admin = Admin(app=app, name = "E-commerce'Admin")

class ProductView(ModelView):
    column_list ={'id', 'name', 'price', 'category_id'}
    column_searchable_list = ['name']
    can_export = True #xuat file
    edit_modal = True
    column_editable_list = ['name'] #chinh
    column_filters = ['name', 'price'] #loc theo ten va gia
    form_overrides ={
        'price':FloatField #them price
    }

class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(ModelView(Category,db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name = 'Thong Ke'))

