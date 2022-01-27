
import csv
from datetime import datetime

if __name__ == '__main__':

    lista_clientes = [
        [1, "Maria", datetime.now().strftime("%Y%m%d%H%M%S%f")],
        [2, "Lorena", datetime.now().strftime("%Y%m%d%H%M%S%f")],
        [3, "Julia", datetime.now().strftime("%Y%m%d%H%M%S%f")]
    ]

    with open('clientes.csv', mode="w", newline='') as _file:
        writer = csv.writer(_file, delimiter=';')
        writer.writerows([["id", "nome", "timestamp"]])
        writer.writerows(lista_clientes)


    with open('clientes.csv', mode="w", newline='') as _file:
        headers = ["id", "nome", "timestamp"]

        writer = csv.DictWriter(_file, delimiter=';', fieldnames=headers)

        lista_clientes = [
            {
                "id": 1,
                "nome": "Maria",
                "timestamp": datetime.now().strftime("%Y%m%d%H%M%S%f")
            },
            {
                "id": 2,
                "nome": "Lorena",
                "timestamp": datetime.now().strftime("%Y%m%d%H%M%S%f")
            },
            {
                "id": 3,
                "nome": "Carla",
                "timestamp": datetime.now().strftime("%Y%m%d%H%M%S%f")
            }
        ]

        writer.writerows(lista_clientes)
        writer.writerow(
            {"id": 4, "nome": "Luana", "timestamp": datetime.now().strftime("%Y%m%d%H%M%S%f")}
        )
