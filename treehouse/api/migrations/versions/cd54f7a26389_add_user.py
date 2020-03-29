"""Add user

Revision ID: cd54f7a26389
Revises: 
Create Date: 2020-03-23 14:00:47.757058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd54f7a26389'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    op.drop_table('availability')
    op.drop_table('room_has_amenities')
    op.drop_table('amenity')
    op.drop_table('room')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('Type', sa.VARCHAR(length=12), nullable=True),
    sa.Column('beds_num', sa.INTEGER(), nullable=False),
    sa.Column('baths_num', sa.INTEGER(), nullable=False),
    sa.Column('bedrooms_num', sa.INTEGER(), nullable=False),
    sa.Column('lounge', sa.BOOLEAN(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('smocking_allowed', sa.BOOLEAN(), nullable=False),
    sa.Column('pets_allowed', sa.BOOLEAN(), nullable=False),
    sa.Column('events_allowed', sa.BOOLEAN(), nullable=False),
    sa.Column('x_coordinate', sa.FLOAT(), nullable=False),
    sa.Column('y_coordinate', sa.FLOAT(), nullable=False),
    sa.Column('address', sa.VARCHAR(length=50), nullable=False),
    sa.Column('transport_info', sa.VARCHAR(length=100), nullable=True),
    sa.Column('persons_num', sa.INTEGER(), nullable=False),
    sa.Column('standard_cost', sa.FLOAT(), nullable=False),
    sa.Column('add_persons_cost', sa.FLOAT(), nullable=True),
    sa.CheckConstraint('"Type" IN (\'private_room\', \'shared_room\', \'house\')', name='roomtypes'),
    sa.CheckConstraint('events_allowed IN (0, 1)'),
    sa.CheckConstraint('lounge IN (0, 1)'),
    sa.CheckConstraint('pets_allowed IN (0, 1)'),
    sa.CheckConstraint('smocking_allowed IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('amenity',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('description', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id', 'description')
    )
    op.create_table('room_has_amenities',
    sa.Column('room_id', sa.INTEGER(), nullable=False),
    sa.Column('amenity_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['amenity_id'], ['amenity.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('room_id', 'amenity_id')
    )
    op.create_table('availability',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('room_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('source', sa.TEXT(), nullable=False),
    sa.Column('room_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id', 'source')
    )
    # ### end Alembic commands ###
