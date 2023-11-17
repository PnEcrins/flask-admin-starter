
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.env import db
from app.models import Foo
from app.filters import IlikeFilter


admin = Admin(
    name="Admin", template_mode="bootstrap4", base_template="layout.html",
)


class FooAdmin(ModelView):
    can_delete = False
    column_sortable_list = ["name"]
    column_list = ["name"]

    column_searchable_list = ["name"]

    column_filters = [
        IlikeFilter(column=Foo.name, name="Name"),
    ]


admin.add_view(
    FooAdmin(Foo, db.session, name='foo', endpoint='foo', url='/foo')
)
