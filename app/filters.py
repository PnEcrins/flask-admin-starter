
from flask_admin.contrib.sqla.filters import FilterEqual


class IlikeFilter(FilterEqual):
    def apply(self, query, value, alias=None):
        val = f"%{value}%"
        return query.filter(self.get_column(alias).ilike(val))
