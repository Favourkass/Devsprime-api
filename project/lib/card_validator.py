from django.conf import settings
import requests
from lib.response import Response


def card_validator(self, learner_profile, serializer):
    access_token = settings.PAYSTACK_PUBLIC_KEY
    acc_num = serializer.validated_data.get('account_number')
    get_bank_info = requests.get('https://api.paystack.co/bank',
        headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'})
    get_bank_code=None
    bank_list= {}
    for bank in get_bank_info.json()['data']:
        bank_list.setdefault('list of valid banks', [])
        bank_list['list of valid banks'].append(bank.get('name'))
        if bank.get('name') == serializer.validated_data.get('bank_name'):
            get_bank_code = bank.get('code')
            break
    if not get_bank_code:
        return Response(None, {'Bank Name Error': bank_list})

    result = requests.get(
        f'https://api.paystack.co/bank/resolve?account_number={acc_num}&bank_code={get_bank_code}',
        headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'})
    if result.json()['status']: 
        learner_profile.account_name = result.json()['data'].get('account_name')
        learner_profile.account_number= acc_num
        learner_profile.bank_name= serializer.validated_data.get('bank_name')
        learner_profile.save()
        response = {
            'account_name': result.json()['data'].get('account_name'),
            'account_number': result.json()['data'].get('account_number'),
            'bank_name': serializer.validated_data.get('bank_name')
        }
        return Response(response)
    return Response(None, {'Invalid credentials': 'One or more data are incorrect'})
