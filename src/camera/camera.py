from sqlalchemy import Table, Column, Integer, String, Boolean, Text
from sqlalchemy.orm import mapper
# from ...main import server

# class Camera(object):
#     query = server.db_session.query_property()

#     def __init__(self, name=None, url=None):
#         self.name=name
#         self.url=url

#     def __repr__(self):
#         return f'<Camera {self.name!r}>'

# camera = Table('camera', server.metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('name', String(50), unique=True),
#     Column('url', Text(), unique=True),
#     # Column('status', Boolean, default=False)
# )
# mapper(Camera, camera)