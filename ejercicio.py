from typing import Dict, Any


class AnalizadorLogs:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:

        total_solicitudes = 0
        solicitudes_por_metodo = {}
        solicitudes_por_codigo = {}
        tamano_total_respuesta = 0
        solicitudes_por_url = {}


        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:

                campos = linea.strip().split()
                direccion_ip = campos[0].split(':')[1]
                fecha_hora = ' '.join(campos[1:3])
                metodo = campos[3].replace('"', '')
                url = campos[4]
                codigo_respuesta = int(campos[5])
                tamano_respuesta = int(campos[6])


                total_solicitudes += 1
                if metodo in solicitudes_por_metodo:
                    solicitudes_por_metodo[metodo] += 1
                else:
                    solicitudes_por_metodo[metodo] = 1
                if codigo_respuesta in solicitudes_por_codigo:
                    solicitudes_por_codigo[codigo_respuesta] += 1
                else:
                    solicitudes_por_codigo[codigo_respuesta] = 1
                tamano_total_respuesta += tamano_respuesta
                if url in solicitudes_por_url:
                    solicitudes_por_url[url] += 1
                else:
                    solicitudes_por_url[url] = 1


        tamano_promedio_respuesta = tamano_total_respuesta / total_solicitudes
        urls_mas_solicitadas = sorted(solicitudes_por_url.items(), key=lambda x: x[1], reverse=True)[:10]


        estadisticas = {
            "total_solicitudes": total_solicitudes,
            "solicitudes_por_metodo": solicitudes_por_metodo,
            "solicitudes_por_codigo": solicitudes_por_codigo,
            "tamano_total_respuesta": tamano_total_respuesta,
            "tamano_promedio_respuesta": tamano_promedio_respuesta,
            "urls_mas_solicitadas": urls_mas_solicitadas
        }

        return estadisticas



prueba = AnalizadorLogs("archivo_logs.txt")
estadisticas = prueba.procesar_logs()
print(estadisticas)
