import os
import time
import json
import requests
import django
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from backend.profesor.models import Profesor
from backend.utils.constants.constants import API_URL


def cargue():
    load_dotenv()
    try:
        url = API_URL + '/v1.0/profesores'
        headers = {
            'Authorization': os.environ.get('TOKEN')
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print(response.status_code)
            print(response.text)
            exit(1)
        else:
            count = 0
            profesores = json.loads(response.text)
            for profesor in profesores:
                try:
                    Profesor.objects.create(
                        nombre=profesor['Nomb_Prof'],
                        correo=profesor['Corr_Prof'],
                        telefono=profesor['Tele_Prof']
                    )
                    +(+count)
                except Exception as e:
                    print(f"Fallo Cargue {profesor['Nomb_Prof']} - {profesor['Corr_Prof']} - {profesor['Tele_Prof']}")
                    print(e)
            return count
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    print('Inicio Cargue de Profesores')
    start = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Inicio Cargue {start}')
    total = cargue()
    end = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Fin Cargue {end}')
    print(f'Profesores Cargados {total}')