import databases, sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "app_users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String, unique=True, nullable=False),
)

engine = sqlalchemy.create_engine(
    settings.db_url
)
metadata.create_all(engine)