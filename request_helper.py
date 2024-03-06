import requests
from errors import BairroNotFoundError

def get_bairro(cep):
    url = f'https://viacep.com.br/ws/{cep}/json'
    resp = requests.get(url)
    resp_dict = resp.json()
    bairro = resp_dict.get('bairro')

    if bairro is None:
        raise BairroNotFoundError('bairro não encontrado')
    
    return bairro