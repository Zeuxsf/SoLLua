import requests
import json
import os
import dotenv

#O .ENV vai proteger a KEY, para que ninguém além do dono do Código a use
dotenv.load_dotenv()
key = os.getenv('KEY')


def api():
    #A variável de chamada vai pegar as informações fornecidas pela API da meteor blue
    chamada = requests.get(f'https://my.meteoblue.com/packages/current_sunmoon?apikey={key}&lat=-22.7161&lon=-43.5553&asl=37&format=json')
    #A variável dados vai transformar a resposta da chamada em um json, para mais fácil acesso na hora de utilizar as informações recebidas
    dados = chamada.json()
    
    print(f'- PREVISÕES DO SOL E DA LUA PARA O DIA [{dados['data_day']['time'][1]}]')
    print(f'''
Pôr da Lua: {dados['data_day']['moonset'][1]}
Nascer do Sol: {dados['data_day']['sunrise'][1]}
Pôr do Sol: {dados['data_day']['sunset'][1]}
Nascer da Lua: {dados['data_day']['moonrise'][1]}
Fase da Lua: {dados['data_day']['moonphasename'][1]}
''')
    
if __name__ == '__main__':
    api()