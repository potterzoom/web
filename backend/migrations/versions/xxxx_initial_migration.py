"""initial migration

Revision ID: 123456789abc
Revises: 
Create Date: 2024-10-05 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Tabla para almacenar información de usuarios
    op.create_table('usuario',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('contraseña', sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    
    # Tabla para almacenar datos de la red
    op.create_table('datos_red',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('carga', sa.Float(), nullable=False),
        sa.Column('latencia', sa.Float(), nullable=False),
        sa.Column('fecha', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Tabla para almacenar estadísticas de rendimiento del servidor
    op.create_table('estadisticas_servidor',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('servidor_id', sa.Integer(), nullable=False),  # Referencia a servidor
        sa.Column('carga_predicha', sa.Float(), nullable=False),
        sa.Column('latencia_predicha', sa.Float(), nullable=False),
        sa.Column('tiempo_respuesta', sa.Float(), nullable=False),
        sa.Column('p_perdidas_paquetes', sa.Float(), nullable=False),  # Corregido el nombre de la columna
        sa.Column('fecha', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Tabla para alertas predictivas
    op.create_table('alertas_predictivas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('usuario_id', sa.Integer(), nullable=False),  # Referencia al usuario
        sa.Column('mensaje', sa.String(length=200), nullable=False),
        sa.Column('nivel_riesgo', sa.String(length=20), nullable=False),  # Bajo, Medio, Alto
        sa.Column('fecha', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Eliminar tablas en orden inverso a su creación
    op.drop_table('alertas_predictivas')
    op.drop_table('estadisticas_servidor')
    op.drop_table('datos_red')
    op.drop_table('usuario')

