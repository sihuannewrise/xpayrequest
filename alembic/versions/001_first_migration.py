"""First migration

Revision ID: 001
Revises: 
Create Date: 2023-03-03 20:11:56.607102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank',
    sa.Column('bic', sa.Integer(), nullable=False),
    sa.Column('correspondent_account', sa.String(length=20), nullable=True),
    sa.Column('payment_city', sa.String(length=50), nullable=False),
    sa.Column('swift', sa.String(length=11), nullable=True),
    sa.Column('registration_number', sa.Integer(), nullable=True),
    sa.Column('treasury_account', sa.String(length=20), nullable=True),
    sa.Column('opf_type', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('inn', sa.Integer(), nullable=True),
    sa.Column('kpp', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('actuality_date', sa.DateTime(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('liquidation_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bic'),
    sa.UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bankaccounttype',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('counteragent',
    sa.Column('on_behalf', sa.Boolean(), nullable=True),
    sa.Column('ogrn', sa.String(length=20), nullable=True),
    sa.Column('ogrn_date', sa.DateTime(), nullable=True),
    sa.Column('counteragent_type', sa.String(length=50), nullable=True),
    sa.Column('opf_short', sa.String(length=10), nullable=True),
    sa.Column('name_short_with_opf', sa.String(length=150), nullable=True),
    sa.Column('ip_surname', sa.String(length=100), nullable=True),
    sa.Column('ip_name', sa.String(length=100), nullable=True),
    sa.Column('ip_patronymic', sa.String(length=100), nullable=True),
    sa.Column('management_name', sa.String(length=300), nullable=True),
    sa.Column('management_post', sa.String(length=100), nullable=True),
    sa.Column('address_full_with_index', sa.String(length=300), nullable=True),
    sa.Column('address_egrul', sa.String(length=300), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('inn', sa.Integer(), nullable=True),
    sa.Column('kpp', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('actuality_date', sa.DateTime(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('liquidation_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),
    sa.UniqueConstraint('name')
    )
    op.create_table('kbk',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kfp',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oktmo',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payerstatus',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paymentstatus',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paymenttype',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prepayment',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bankaccount',
    sa.Column('account', sa.String(length=20), nullable=False),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.Column('ca_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('is_default', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['bank_id'], ['bank.id'], ),
    sa.ForeignKeyConstraint(['ca_id'], ['counteragent.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['bankaccounttype.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account', 'bank_id', name='_account_bank_unique')
    )
    op.create_table('paymentrequest',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('payer_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('kfp_id', sa.Integer(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('purpose', sa.String(length=50), nullable=False),
    sa.Column('amount_netto', sa.Float(), nullable=True),
    sa.Column('amount_vat', sa.Float(), nullable=True),
    sa.Column('amount_total', sa.Float(), nullable=False),
    sa.Column('attachement', sa.String(length=150), nullable=True),
    sa.Column('field_101_id', sa.Integer(), nullable=True),
    sa.Column('field_104_id', sa.Integer(), nullable=True),
    sa.Column('field_105_id', sa.Integer(), nullable=True),
    sa.Column('field_106', sa.String(length=20), nullable=True),
    sa.Column('field_107', sa.String(length=20), nullable=True),
    sa.Column('field_108', sa.String(length=20), nullable=True),
    sa.Column('field_109', sa.String(length=20), nullable=True),
    sa.Column('project', sa.String(length=50), nullable=True),
    sa.Column('contract', sa.String(length=50), nullable=True),
    sa.Column('contract_date', sa.DateTime(), nullable=True),
    sa.Column('sub_contract', sa.String(length=50), nullable=True),
    sa.Column('sub_contract_date', sa.DateTime(), nullable=True),
    sa.Column('prepayment_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['field_101_id'], ['payerstatus.id'], ),
    sa.ForeignKeyConstraint(['field_104_id'], ['kbk.id'], ),
    sa.ForeignKeyConstraint(['field_105_id'], ['oktmo.id'], ),
    sa.ForeignKeyConstraint(['kfp_id'], ['kfp.id'], ),
    sa.ForeignKeyConstraint(['payer_id'], ['counteragent.id'], ),
    sa.ForeignKeyConstraint(['prepayment_id'], ['prepayment.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['counteragent.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['paymenttype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paymentregister',
    sa.Column('pr_id', sa.Integer(), nullable=False),
    sa.Column('payment_status', sa.Integer(), nullable=False),
    sa.Column('fulfilled_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['payment_status'], ['paymentstatus.id'], ),
    sa.ForeignKeyConstraint(['pr_id'], ['paymentrequest.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('paymentregister')
    op.drop_table('paymentrequest')
    op.drop_table('bankaccount')
    op.drop_table('prepayment')
    op.drop_table('paymenttype')
    op.drop_table('paymentstatus')
    op.drop_table('payerstatus')
    op.drop_table('oktmo')
    op.drop_table('kfp')
    op.drop_table('kbk')
    op.drop_table('counteragent')
    op.drop_table('bankaccounttype')
    op.drop_table('bank')
    # ### end Alembic commands ###