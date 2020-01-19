from dataclasses import dataclass

from app.main import db

@dataclass
class DataFetcher:
    # db fetching layer
    resource: db.Model

    def all(self):
        return self.resource.query.all()
    
    def first(self, **filters):
        data = self.resource.query.filter_by(**filters)
        return data.first()
    
    def filter(self, **filters):
        return self.resource.query.filter_by(**filters)