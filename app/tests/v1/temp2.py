mappingproxy({
    '__module__': 'app.core.models.counteragent',
    '__annotations__': {
        'id': sqlalchemy.orm.base.Mapped[int],
        'name': sqlalchemy.orm.base.Mapped[str],
        'opf_short': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'name_full_with_opf': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'ca_type': sqlalchemy.orm.base.Mapped[typing.Optional[app.core.models._selectchoice.CounterAgentType]],
        'group_id': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'branch_type': sqlalchemy.orm.base.Mapped[typing.Optional[app.core.models._selectchoice.CounterAgentBranch]],
        'ogrn': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'ogrn_date': sqlalchemy.orm.base.Mapped[typing.Optional[datetime.datetime]],
        'fio_surname': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'fio_name': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'fio_patronymic': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'management_post': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'management_disqualified': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'management_name': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'email': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'address_full': sqlalchemy.orm.base.Mapped[typing.Optional[str]],
        'bank_accounts': sqlalchemy.orm.base.Mapped[typing.List[ForwardRef('BankAccount')]],
        'payments': sqlalchemy.orm.base.Mapped[typing.List[ForwardRef('PaymentRequest')]],
        'kpp_list': sqlalchemy.orm.base.Mapped[typing.List[ForwardRef('CaKppMapping')]]},
    'id': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FEC0>,
    'name': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FF60>,
    'opf_short': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FD80>,
    'name_full_with_opf': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850040>,
    'group_id': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FE20>,
    'ogrn': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850220>,
    'fio_surname': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850360>, 
    'fio_name': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850400>,
    'fio_patronymic': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD8504A0>,
    'management_post': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850540>,
    'management_disqualified': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD8505E0>,
    'management_name': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850680>,
    'email': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850720>,
    'address_full': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD8507C0>,
    'bank_accounts': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FBA0>,
    'payments': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FC40>,
    'kpp_list': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD82FCE0>,
    '__doc__': None,
    '_sa_class_manager': <ClassManager of <class 'app.core.models.counteragent.CounterAgent'> at 1b8dd838650>,
    'inn': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850860>,
    'address': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850900>,
    'status': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD8509A0>,
    'actuality_date': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850A40>,
    'registration_date': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850AE0>,
    'liquidation_date': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850B80>,
    'is_archived': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850C20>,
    'description': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850CC0>,
    '__table__': Table(
        'counteragent', MetaData(),
        Column('id', Integer(), table=<counteragent>, primary_key=True, nullable=False),
        Column('inn', String(length=12), table=<counteragent>),
        Column('name', String(length=160), table=<counteragent>, nullable=False),
        Column('opf_short', String(length=10), table=<counteragent>),
        Column('name_full_with_opf', String(length=300), table=<counteragent>),
        Column('ca_type', Enum('LEGAL', 'INDIVIDUAL', name='counteragenttype'), table=<counteragent>),
        Column('group_id', Integer(), ForeignKey('counteragentgroup.id'), table=<counteragent>),
        Column('branch_type', Enum('MAIN', 'BRANCH', name='counteragentbranch'), table=<counteragent>),
        Column('ogrn', String(length=20), table=<counteragent>),
        Column('ogrn_date', DateTime(), table=<counteragent>),
        Column('fio_surname', String(length=50), table=<counteragent>),
        Column('fio_name', String(length=50), table=<counteragent>),
        Column('fio_patronymic', String(length=50), table=<counteragent>),
        Column('management_post', String(length=50), table=<counteragent>),
        Column('management_disqualified', String(length=50), table=<counteragent>),
        Column('management_name', String(length=150), table=<counteragent>),
        Column('email', String(length=150), table=<counteragent>),
        Column('address_full', String(length=150), table=<counteragent>),
        Column('address', String(length=200), table=<counteragent>),
        Column('status', Enum('ACTIVE', 'LIQUIDATING', 'LIQUIDATED', 'BANKRUPT', 'REORGANIZING', name='entitystatus'), table=<counteragent>),
        Column('actuality_date', DateTime(), table=<counteragent>),
        Column('registration_date', DateTime(), table=<counteragent>),
        Column('liquidation_date', DateTime(), table=<counteragent>),
        Column('is_archived', Boolean(), table=<counteragent>, server_default=DefaultClause(<sqlalchemy.sql.elements.TextClause object at 0x000001B8DD7A0A50>, for_update=False)),
        Column('description', String(length=150), table=<counteragent>), schema=None),
    '__init__': <function __init__ at 0x000001B8DD82FA60>,
    'ca_type': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD8500E0>,
    'branch_type': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD850180>,
    'ogrn_date': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x000001B8DD8502C0>,
    '__mapper__': <Mapper at 0x1b8dbc31d90; CounterAgent>,
    '__parameters__': ()
})
