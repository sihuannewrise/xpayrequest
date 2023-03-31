"""First migration

Revision ID: 001
Revises: 
Create Date: 2023-03-30 16:07:34.202841

"""
from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank',
    sa.Column('bic', sa.String(length=9), nullable=False),
    sa.Column('correspondent_account', sa.String(length=20), nullable=True),
    sa.Column('payment_city', sa.String(length=50), nullable=True),
    sa.Column('swift', sa.String(length=11), nullable=True),
    sa.Column('registration_number', sa.String(length=20), nullable=True),
    sa.Column('treasury_accounts', sa.String(length=20), nullable=True),
    sa.Column('opf_type', sa.Enum('BANK', 'BANK_BRANCH', 'NKO', 'NKO_BRANCH', 'RKC', 'CBR', 'TREASURY', 'OTHER', name='bankopftype'), nullable=True),
    sa.Column('name', sa.String(length=160), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('status', sa.Enum('ACTIVE', 'LIQUIDATING', 'LIQUIDATED', 'BANKRUPT', 'REORGANIZING', name='entitystatus'), nullable=True),
    sa.Column('inn', sa.String(length=12), nullable=True),
    sa.Column('kpp', sa.String(length=9), nullable=True),
    sa.Column('actuality_date', sa.DateTime(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('liquidation_date', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('bic'),
    sa.UniqueConstraint('inn', 'kpp', name='_bank_inn_kpp_unique'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_bank_bic'), 'bank', ['bic'], unique=False)
    op.create_table('bankaccounttype',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_bankaccounttype_id'), 'bankaccounttype', ['id'], unique=False)
    op.create_table('counteragent',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=160), nullable=False),
    sa.Column('inn', sa.String(length=12), nullable=True),
    sa.Column('kpp', sa.String(length=9), nullable=True),
    sa.Column('ogrn', sa.String(length=20), nullable=True),
    sa.Column('ogrn_date', sa.DateTime(), nullable=True),
    sa.Column('ca_type', sa.Enum('LEGAL', 'INDIVIDUAL', name='counteragenttype'), nullable=True),
    sa.Column('opf_short', sa.String(length=10), nullable=True),
    sa.Column('name_short_with_opf', sa.String(length=150), nullable=True),
    sa.Column('ip_surname', sa.String(length=50), nullable=True),
    sa.Column('ip_name', sa.String(length=50), nullable=True),
    sa.Column('ip_patronymic', sa.String(length=50), nullable=True),
    sa.Column('management_post', sa.String(length=50), nullable=True),
    sa.Column('management_disqualified', sa.String(length=50), nullable=True),
    sa.Column('management_name', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('address_full', sa.String(length=150), nullable=True),
    sa.Column('status', sa.Enum('ACTIVE', 'LIQUIDATING', 'LIQUIDATED', 'BANKRUPT', 'REORGANIZING', name='entitystatus'), nullable=True),
    sa.Column('actuality_date', sa.DateTime(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('liquidation_date', sa.DateTime(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_counteragent_id'), 'counteragent', ['id'], unique=False)
    op.create_table('kbk',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_kbk_id'), 'kbk', ['id'], unique=False)
    op.create_table('kfp',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_kfp_id'), 'kfp', ['id'], unique=False)
    op.create_table('oktmo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_oktmo_id'), 'oktmo', ['id'], unique=False)
    op.create_table('payerstatus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_payerstatus_id'), 'payerstatus', ['id'], unique=False)
    op.create_table('paymentstatus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_paymentstatus_id'), 'paymentstatus', ['id'], unique=False)
    op.create_table('paymenttype',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_paymenttype_id'), 'paymenttype', ['id'], unique=False)
    op.create_table('paymentverdict',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_paymentverdict_id'), 'paymentverdict', ['id'], unique=False)
    op.create_table('prepayment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_prepayment_id'), 'prepayment', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('accesstoken',
    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('token', sa.String(length=43), nullable=False),
    sa.Column('created_at', fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('token')
    )
    op.create_index(op.f('ix_accesstoken_created_at'), 'accesstoken', ['created_at'], unique=False)
    op.create_table('bankaccount',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account', sa.String(length=20), nullable=False),
    sa.Column('currency', sa.String(length=20), nullable=True),
    sa.Column('bank_bic', sa.String(length=9), nullable=True),
    sa.Column('ca_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('is_default', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['bank_bic'], ['bank.bic'], ),
    sa.ForeignKeyConstraint(['ca_id'], ['counteragent.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['bankaccounttype.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account', 'bank_bic', name='_account_bank_unique')
    )
    op.create_index(op.f('ix_bankaccount_id'), 'bankaccount', ['id'], unique=False)
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['counteragent.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=300), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('patronymic_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('full_name', 'birthdate', name='_name_birth_unique')
    )
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=False)
    op.create_table('paymentrequest',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('payer_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=False),
    sa.Column('kfp_id', sa.Integer(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('purpose', sa.String(length=210), nullable=True),
    sa.Column('amount_netto', sa.Float(), nullable=True),
    sa.Column('amount_vat', sa.Float(), nullable=True),
    sa.Column('amount_total', sa.Float(), nullable=True),
    sa.Column('attach_url', sa.String(length=150), nullable=True),
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
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.ForeignKeyConstraint(['field_101_id'], ['payerstatus.id'], ),
    sa.ForeignKeyConstraint(['field_104_id'], ['kbk.id'], ),
    sa.ForeignKeyConstraint(['field_105_id'], ['oktmo.id'], ),
    sa.ForeignKeyConstraint(['kfp_id'], ['kfp.id'], ),
    sa.ForeignKeyConstraint(['payer_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['prepayment_id'], ['prepayment.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['counteragent.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['paymenttype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_paymentrequest_id'), 'paymentrequest', ['id'], unique=False)
    op.create_table('position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('employer_id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('full_stack', sa.Boolean(), server_default=sa.text('TRUE'), nullable=True),
    sa.Column('from_date', sa.Date(), nullable=True),
    sa.Column('till_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['employer_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_id'), 'position', ['id'], unique=False)
    op.create_table('paymentprocessing',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pr_id', sa.Integer(), nullable=False),
    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('verdict_id', sa.Integer(), nullable=True),
    sa.Column('processed_at', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['pr_id'], ['paymentrequest.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['verdict_id'], ['paymentverdict.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_paymentprocessing_id'), 'paymentprocessing', ['id'], unique=False)
    op.create_table('paymentregister',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fulfill_date', sa.DateTime(), nullable=True),
    sa.Column('pr_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['pr_id'], ['paymentrequest.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['paymentstatus.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_paymentregister_id'), 'paymentregister', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_paymentregister_id'), table_name='paymentregister')
    op.drop_table('paymentregister')
    op.drop_index(op.f('ix_paymentprocessing_id'), table_name='paymentprocessing')
    op.drop_table('paymentprocessing')
    op.drop_index(op.f('ix_position_id'), table_name='position')
    op.drop_table('position')
    op.drop_index(op.f('ix_paymentrequest_id'), table_name='paymentrequest')
    op.drop_table('paymentrequest')
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    op.drop_table('employee')
    op.drop_table('company')
    op.drop_index(op.f('ix_bankaccount_id'), table_name='bankaccount')
    op.drop_table('bankaccount')
    op.drop_index(op.f('ix_accesstoken_created_at'), table_name='accesstoken')
    op.drop_table('accesstoken')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_prepayment_id'), table_name='prepayment')
    op.drop_table('prepayment')
    op.drop_index(op.f('ix_paymentverdict_id'), table_name='paymentverdict')
    op.drop_table('paymentverdict')
    op.drop_index(op.f('ix_paymenttype_id'), table_name='paymenttype')
    op.drop_table('paymenttype')
    op.drop_index(op.f('ix_paymentstatus_id'), table_name='paymentstatus')
    op.drop_table('paymentstatus')
    op.drop_index(op.f('ix_payerstatus_id'), table_name='payerstatus')
    op.drop_table('payerstatus')
    op.drop_index(op.f('ix_oktmo_id'), table_name='oktmo')
    op.drop_table('oktmo')
    op.drop_index(op.f('ix_kfp_id'), table_name='kfp')
    op.drop_table('kfp')
    op.drop_index(op.f('ix_kbk_id'), table_name='kbk')
    op.drop_table('kbk')
    op.drop_index(op.f('ix_counteragent_id'), table_name='counteragent')
    op.drop_table('counteragent')
    op.drop_index(op.f('ix_bankaccounttype_id'), table_name='bankaccounttype')
    op.drop_table('bankaccounttype')
    op.drop_index(op.f('ix_bank_bic'), table_name='bank')
    op.drop_table('bank')
    # ### end Alembic commands ###
