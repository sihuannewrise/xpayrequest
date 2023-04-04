# dadata mapping table
# BANK = {
#     'name': data['value'],
#     'bic': data['data']['bic'],
#     'address': data['data']['address']['value'],
#     'status': data['data']['state']['status'],
#     'inn': data['data']['inn'],
#     'kpp': data['data']['kpp'],
#     'actuality_date': data['data']['state']['actuality_date'],
#     'registration_date': data['data']['state']['registration_date'],
#     'liquidation_date': data['data']['state']['liquidation_date'],
#     'correspondent_account': data['data']['correspondent_account'],
#     'payment_city': data['data']['payment_city'],
#     'swift': data['data']['swift'],
#     'registration_number': data['data']['registration_number'],
#     'treasury_accounts': data['data']['treasury_accounts'],
#     'opf_type': data['data']['opf']['type'],
# }
DATE_FIELDS = ('actuality_date', 'registration_date', 'liquidation_date')

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
}
