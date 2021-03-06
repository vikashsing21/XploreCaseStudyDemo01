"""empty message

Revision ID: 234db526a925
Revises: 
Create Date: 2020-06-21 11:54:40.252979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234db526a925'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('ssnid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=300), nullable=False),
    sa.Column('state', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=60), nullable=False),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('cid')
    )
    op.create_index(op.f('ix_customers_ssnid'), 'customers', ['ssnid'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('login', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_role_id'), 'users', ['role_id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('accounts',
    sa.Column('accntid', sa.Integer(), nullable=False),
    sa.Column('customer_cid', sa.Integer(), nullable=True),
    sa.Column('accnt_type', sa.String(length=30), nullable=False),
    sa.Column('ammount', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['customer_cid'], ['customers.cid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('accntid')
    )
    op.create_table('cusotmer_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_cid', sa.Integer(), nullable=True),
    sa.Column('customer_ssnid', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=True),
    sa.Column('message', sa.String(length=100), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['customer_cid'], ['customers.cid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.Column('accnt_id', sa.Integer(), nullable=False),
    sa.Column('customer_cid', sa.Integer(), nullable=True),
    sa.Column('ammount', sa.Integer(), nullable=False),
    sa.Column('transaction_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('mode', sa.String(length=60), nullable=False),
    sa.Column('source_acc_type', sa.String(length=30), nullable=True),
    sa.Column('target_acc_type', sa.String(length=30), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_cid'], ['customers.cid'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    op.create_table('account_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_cid', sa.Integer(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('accnt_type', sa.String(length=30), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=True),
    sa.Column('message', sa.String(length=100), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.accntid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account_status')
    op.drop_table('transactions')
    op.drop_table('cusotmer_status')
    op.drop_table('accounts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_role_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_customers_ssnid'), table_name='customers')
    op.drop_table('customers')
    # ### end Alembic commands ###
