from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=255)),
    Column('username', String(length=255)),
    Column('password', String(length=255)),
    Column('active', Boolean),
    Column('confirmed_at', DateTime),
    Column('first_name', String(length=255)),
    Column('last_name', String(length=255)),
    Column('address', String(length=255)),
    Column('number', String(length=255)),
    Column('address2', String(length=255)),
    Column('neighbourhood', String(length=255)),
    Column('zipcode', String(length=255)),
    Column('city', String(length=255)),
    Column('state', String(length=255)),
    Column('birthday', String(length=255)),
    Column('cellphone', String(length=255)),
    Column('phone', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['username'].drop()
