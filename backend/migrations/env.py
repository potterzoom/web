from __future__ import with_statement
from logging import getLogger
from logging.config import fileConfig  # Importar fileConfig aquí
from flask import current_app
from alembic import context
from backend import db

# Configuración de logging para Alembic
config = context.config
fileConfig(config.config_file_name)

logger = getLogger('alembic.env')

def run_migrations_offline():
    """Ejecutar migraciones en modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=db.metadata,  # Meta datos de la base de datos
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    # Ejecutar las migraciones en transacción
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecutar migraciones en modo 'online'."""
    connectable = db.engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=db.metadata,  # Asegúrate de que los modelos reflejen las métricas de red
            compare_type=True,  # Comparar tipos para asegurar integridad de datos
        )

        # Ejecutar las migraciones en transacción
        with context.begin_transaction():
            context.run_migrations()


# Decidir el modo de ejecución de migraciones
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
