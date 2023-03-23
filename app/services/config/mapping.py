# dadata mapping table
BANK = {
    'name': data['value'],
    'bic': data['data']['bic'],
    'address': data['data']['address']['value'],
    'status': data['data']['state']['status'],
    'inn': data['data']['inn'],
    'kpp': data['data']['kpp'],
    'actuality_date': data['data']['state']['actuality_date'],
    'registration_date': data['data']['state']['registration_date'],
    'liquidation_date': data['data']['state']['liquidation_date'],
    'correspondent_account': data['data']['correspondent_account'],
    'payment_city': data['data']['payment_city'],
    'swift': data['data']['swift'],
    'registration_number': data['data']['registration_number'],
    'treasury_accounts': data['data']['treasury_accounts'],
    'opf_type': data['data']['opf']['type'],
}
