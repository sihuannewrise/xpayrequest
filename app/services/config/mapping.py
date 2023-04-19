# dadata mapping table
DD_SEARCH_SUBJECT = {
    'bank': 'bank',
    'counteragent': 'party',
}
DATE_FIELDS = (
    'actuality_date', 'registration_date', 'liquidation_date', 'ogrn_date',
)

# our companies
COMPANIES = {
    '7706295292': 'КНХ',
    '7708395493': 'ЛУНИ',
    '7708412886': 'СГ',
    '7708405825': 'ЮНП-Инвест',
    '7708414379': 'ИНВЕСТ',
}
RUBLE_CODE = '810'

# supplementry tables info
BankAccountType = {
    'main': 'основной',
    'invest': 'инвестиционный',
    'special': 'специальный',
}

PaymentType = {
    'to_counteragent': 'контрагенту',
    'to_budget': 'в бюджет',
    'to_invest': 'инвест счёт',
}

KFP = {
    '12102': 'Закупка газа',
    '12104': 'Закупка газопродуктов',
    '12106': 'Закупка теплоэнергии и ХОВ',
    '12107': 'Закупка электроэнергии и мощности',
    '12109': 'Закупка прочих сырья, материалов и товаров',

    '1228': 'Услуги, связанные продажами и закупками',
    '1229019': 'Прочие структурные подразделения (управленческие и общехозяйственные расходы)',

    '123': 'оплата труда',
    '1240001': 'Налог на добавленную стоимость',
    '1240009': 'Налог на прибыль',
    '1240019': 'Прочие налоги и сборы',

    '1290002': 'Расчеты за третьих  лиц',
    '1290005': 'Возмещение расходов по налогу на прибыль КГН',
    '1290018': 'Выплаты по Margin Call',
    '1290019': 'Прочие выплаты',

    '221': 'Направление средств на капитальные вложения',
    '22901': 'Приобретение ценных бумаг, привлечение депозитов',
    '22909': 'Прочие выплаты по ИД',

    '32301': 'Выплаты доходов участникам (учредителям)',
    '3230501': 'Обязательства по аренде МСФО 16 облагаемой НДС',
    '3230502': 'Обязательства по аренде МСФО 16 не облагаемой НДС',
    '32309': 'Прочие выплаты по финансовым операциям',

    '62': 'Выплаты по внутренним операциям',
}

PayerStatus = {
    '01': 'Организация и ИП перечисляют налоги, сборы или взносы, администрируемые ФНС (налогоплательщики, налоговые агенты, плательщики сборов и взносов)',
    '02': 'Организации и ИП перечисляют налоги и взносы платежкой, которая заменяет уведомление об исчисленных суммах налогов и страховых взносов',
}

KBK = {
    '182 0 10 61201 01 0000 510': 'ЕНП',
    '797 1 02 12000 06 1000 160': 'уплата взносов на травматизм с выплат работникам',
    '182 1 01 01011 01 1000 110': 'Налог на прибыль организаций (кроме КГН): в федеральный бюджет (ставка – 3%)',
    '182 1 01 01012 02 1000 110': 'Налог на прибыль организаций (кроме КГН): в региональный бюджет (ставка от 12,5% до 17%)',
    '182 1 03 01000 01 1000 110': 'НДС',
    '182 1 06 02010 02 1000 110': 'Налог на имущество',
}

OKTMO = {
    '45382000': 'Москва, мун. округ Тверской',
}

Prepayment = {
    'in_advance': 'аванс',
    'fact': 'по факту',
}

PaymentStatus = {
    'project': 'проект',
    'signing': 'на подписании',
    'on_approval': 'на утверждении',
    'processing': 'в работе',
    'finished': 'завершен',
}

PaymentVerdict = {
    'declined': 'отклонено',
    'accepted': 'одобрено',
}

KPP = {
    # '770701001': 'по месту нахождения организации',
    # '770801001': 'по месту нахождения организации',
    # '110208001': 'по месту нахождения земельного участка',
    # '231508001': 'по месту нахождения земельного участка',
}

KPP_LIST = {
    '543301001', '526201001', '507401001', '771001001', '594706001',
    '772543001', '526043001', '667101001', '344501001', '772601001',
    '344601001', '772201001', '771701001', '770901001', '771501001',
    '775050001', '298301001', '502901001', '540101001', '500901001',
    '110101001', '770501001', '770601001', '862101001', '997650001',
    '773001001', '774850001', '770143001', '773101001', '345901001',
    '500301001', '772701001', '166001001', '772043001', '772101001',
    '502401001', '344401001', '346008001', '595901001', '997950001',
    '121501001', '773601001', '997350001', '774301001', '772401001',
    '290101001', '631701001', '302501001', '860743001', '997250001',
    '402301001', '773851001', '594801001', '771401001', '890101001',
    '345308001', '231501001', '010501001', '230801001', '771901001',
    '770701001', '593301001', '504701001', '773301001', '810701001',
    '997750001', '997150001', '366301001', '343601001', '775101001',
    '301502001', '504201001', '110201001', '590501001', '110208001',
    '773401001', '772301001', '771601001', '301901001', '771301001',
    '503243001', '770401001', '860701001', '110143001', '340702001',
    '770301001', '771801001', '231508001', '860201001', '301501001',
    '595706001', '785150001', '667901001', '773501001', '772843001',
    '760401001', '770801001', '860101001', '772801001', '745601001',
    '770101001', '772501001', '772001001', '502701001', '591401001',
    '231543001', '770201001', '668601001', '110801001',
}

CounterAgentGroup = {
    'ЛУКОЙЛ': 'Группа ЛУКОЙЛ',
    'Госорганы': 'Государственные органы',
}

Currency = {
    '810': 'Российский рубль',
    '840': 'доллар США',
    '978': 'евро',
}

# Don't forget update this dictionary in app.services.supplementarycreate file
SUPPLEMENTARY_SCHEMAS = {
    'BankAccountType': BankAccountType,
    'PaymentType': PaymentType,
    'KFP': KFP,
    'PayerStatus': PayerStatus,
    'KBK': KBK,
    'OKTMO': OKTMO,
    'Prepayment': Prepayment,
    'PaymentStatus': PaymentStatus,
    'PaymentVerdict': PaymentVerdict,
    'KPP': KPP,
    'CounterAgentGroup': CounterAgentGroup,
    'Currency': Currency,
}
