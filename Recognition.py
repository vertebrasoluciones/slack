import time
import json
import os
import shutil
import PySimpleGUI as sg

layout=[
    [sg.Text("Seleccione factura:"), sg.FileBrowse(file_types=[("PDF files", "*.pdf")])]
]

window = sg.Window('Facturacion - Vertebra', size=(800,550)).Layout(layout)




def init():
    
    # event, values = window.read()

    # # if event in (None, 'Cancel'):   # if user closes window or clicks cancel
    # #     break
    # print(event, values)
    # print('You entered ', values[0])
    
    print("Obteniendo información de la factura...")
    time.sleep(5)
    print("Generando archivo de imagen desde pdf...")
    time.sleep(5)
    shutil.copy("archivos davivienda/Factura Davivienda 04-2019.png", "Factura Davivienda 04-2019.png")

    print("Obteniendo datos...")
    time.sleep(5)

    print({
        "NIU": 17109493,
        "NIC": 2292254,
        "Usuario o suscriptor": "DAVIVIENDA S.A",
        "Energía": 419910,
        "Total a pagar": 530610
    })

    print("Cargando informacion a software...")
    time.sleep(3)
    print("Información cargada")
    


    # print("Resultado:", {
    #     "titular_pago": "BANCO DAVIVIENDA S.A",
    #     # "usuario_suscriptor": "BANCO DAVIVIENDA S.A",
    #     "codigo_niu": "17109493",
    #     "energia": "419910",
    #     "total_pagar_mes": "530610"
    # })


def select_facturas():
    path = "/home/wilson/Escritorio/text-recognition/"
    # for a in os.listdir(path):
    #     if "Factura Davivienda Factura Davivienda" in a:
    #         # os.rename(path + "/" + a, path + "/" + "Factura Davivienda " + a.replace("Factura Davivienda ", ""))