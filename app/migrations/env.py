# from logging.config import fileConfig
#
# from sqlalchemy import engine_from_config
# from sqlalchemy import pool
#
# from alembic import context
#
# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config
#
# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# fileConfig(config.config_file_name)
#
# # add your model's MetaData object here
# # for 'autogenerate' support
# # from myapp import mymodel
# # target_metadata = mymodel.Base.metadata
# target_metadata = None
#
# # other values from the config, defined by the needs of env.py,
# # can be acquired:
# # my_important_option = config.get_main_option("my_important_option")
# # ... etc.
#
#
# def run_migrations_offline():
#     """Run migrations in 'offline' mode.
#
#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.
#
#     Calls to context.execute() here emit the given string to the
#     script output.
#
#     """
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )
#
#     with context.begin_transaction():
#         context.run_migrations()
#
#
# def run_migrations_online():
#     """Run migrations in 'online' mode.
#
#     In this scenario we need to create an Engine
#     and associate a connection with the context.
#
#     """
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )
#
#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata
#         )
#
#         with context.begin_transaction():
#             context.run_migrations()
#
#
# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()


#
# import os
# import sys
# from logging.config import fileConfig
#
# from alembic import context
# from sqlalchemy import engine_from_config
# from sqlalchemy import pool
#
# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config
#
# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# fileConfig(config.config_file_name)
#
# # add your model's MetaData object here
# # for 'autogenerate' support
# from app.db import models
# target_metadata = models.Base.metadata
#
#
# def get_url():
#     """
#     Get postgres url from environment variables
#     :return: built string
#     """
#     user = os.getenv("POSTGRES_USER", "postgres")
#     password = os.getenv("POSTGRES_PASSWORD", "")
#     server = os.getenv("POSTGRES_SERVER", "postgres")
#     db = os.getenv("POSTGRES_DB", "ms")
#     return f"postgresql://{user}:{password}@{server}/{db}"
#
#
# def run_migrations_online():
#     """Run migrations in 'online' mode.
#
#     In this scenario we need to create an Engine
#     and associate a connection with the context.
#
#     """
#     configuration = config.get_section(config.config_ini_section)
#     configuration["sqlalchemy.url"] = get_url()
#
#     connectable = engine_from_config(
#         configuration,
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )
#
#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata
#         )
#
#         with context.begin_transaction():
#             context.run_migrations()
#
#
# run_migrations_online()


from __future__ import with_statement

import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
print(sys.path)

from app.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")

# Connect to to the database
db_string = f"postgres://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

config.set_main_option('sqlalchemy.url', db_string)
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    connectable = engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool,
    )

    print("Running migrations")
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()
#
# def run_migrations_online():
#     """Run migrations in 'online' mode.
#
#     In this scenario we need to create an Engine
#     and associate a connection with the context.
#
#     """
#
#     # this callback is used to prevent an auto-migration from being generated
#     # when there are no changes to the schema
#     # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
#     def process_revision_directives(context, revision, directives):
#         if getattr(config.cmd_opts, 'autogenerate', False):
#             script = directives[0]
#             if script.upgrade_ops.is_empty():
#                 directives[:] = []
#                 logger.info('No changes in schema detected.')
#
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix='sqlalchemy.',
#         poolclass=pool.NullPool,
#     )
#
#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=target_metadata,
#             process_revision_directives=process_revision_directives,
#             **current_app.extensions['migrate'].configure_args
#         )
#
#         with context.begin_transaction():
#             context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
