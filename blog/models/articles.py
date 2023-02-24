from sqlalchemy import Column, Integer, String
from blog.models.database import db


class Articles(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    author = Column(String(50), nullable=False)
    text = Column(String(150))

    def __repr__(self):
        return f'<Articles #{self.id} {self.name}>'
