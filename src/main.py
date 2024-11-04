import heapq

# Definición del grafo con las distancias en kilometros entre ciudades.
distancias = {
    'Logroño': {'Bilbao':136, 'Huesca':239, 'Burgos':132, 'Soria':100, 'Zaragoza':170},
    'Tarragona': {'Huesca':212, 'Zaragoza':236, 'Castellón':187},
    'Bilbao': {'Burgos':158, 'Logroño':136, 'Huesca':371},
    'Huesca': {'Bilbao':371, 'Logroño':239, 'Zaragoza':74, 'Tarragona':212},
    'Madrid': {'Burgos':249, 'Cuenca':165, 'Guadalajara':62, 'Soria':231},
    'Teruel': {'Zaragoza':170, 'Castellón':144, 'Guadalajara':244},
    'Guadalajara': {'Madrid':62, 'Soria':170, 'Zaragoza':256, 'Teruel':244, 'Cuenca':136},
    'Zaragoza': {'Huesca':74, 'Logroño':170, 'Tarragona':236, 'Teruel':170, 'Guadalajara':256},
    'Soria': {'Logroño':100, 'Guadalajara':170, 'Madrid':231},
    'Cuenca': {'Valencia':199, 'Guadalajara':136, 'Madrid':165},
    'Castellón': {'Teruel':144, 'Tarragona':187, 'Valencia':73},
    'Valencia': {'Castellón':73, 'Cuenca':199},
    'Burgos': {'Bilbao':158, 'Logroño':132, 'Madrid':249}
}

# Definición de las distancias aéreas (heurísticas).
heuristicas = {
    'Tarragona': {'Tarragona': 0, 'Bilbao': 419, 'Huesca': 177, 'Logroño': 340, 'Madrid': 424, 'Teruel': 216, 'Guadalajara': 374, 'Zaragoza': 187, 'Burgos': 432, 'Soria': 318, 'Cuenca': 308, 'Castellón': 167, 'Valencia': 229},
    'Bilbao': {'Bilbao': 0, 'Tarragona': 419, 'Huesca': 242, 'Logroño': 97, 'Madrid': 323, 'Teruel': 358, 'Guadalajara': 293, 'Zaragoza': 246, 'Burgos': 119, 'Soria': 171, 'Cuenca': 361, 'Castellón': 436, 'Valencia': 473},
    'Huesca': {'Huesca': 0, 'Tarragona': 177, 'Bilbao': 242, 'Logroño': 172, 'Madrid': 335, 'Teruel': 207, 'Guadalajara': 284, 'Zaragoza': 67, 'Burgos': 272, 'Soria': 176, 'Cuenca': 271, 'Castellón': 240, 'Valencia': 296},
    'Logroño': {'Logroño': 0, 'Tarragona': 340, 'Bilbao': 97, 'Huesca': 172, 'Madrid': 251, 'Teruel': 261, 'Guadalajara': 212, 'Zaragoza': 157, 'Burgos': 103, 'Soria': 77, 'Cuenca': 267, 'Castellón': 340, 'Valencia': 375},
    'Madrid': {'Madrid': 0, 'Tarragona': 424, 'Bilbao': 323, 'Huesca': 335, 'Logroño': 251, 'Teruel': 220, 'Guadalajara': 51, 'Zaragoza': 273, 'Burgos': 214, 'Soria': 182, 'Cuenca': 138, 'Castellón': 314, 'Valencia': 302},
    'Teruel': {'Teruel': 0, 'Tarragona': 216, 'Bilbao': 358, 'Huesca': 207, 'Logroño': 261, 'Madrid': 220, 'Guadalajara': 176, 'Zaragoza': 146, 'Burgos': 310, 'Soria': 195, 'Cuenca': 93, 'Castellón': 98, 'Valencia': 115},
    'Guadalajara': {'Guadalajara': 0, 'Tarragona': 374, 'Bilbao': 293, 'Huesca': 284, 'Logroño': 212, 'Madrid': 51, 'Teruel': 176, 'Zaragoza': 221, 'Burgos': 212, 'Soria': 138, 'Cuenca': 106, 'Castellón': 273, 'Valencia': 270},
    'Zaragoza': {'Zaragoza': 0, 'Tarragona': 187, 'Bilbao': 246, 'Huesca': 67, 'Logroño': 157, 'Madrid': 273, 'Teruel': 146, 'Guadalajara': 221, 'Burgos': 245, 'Soria': 133, 'Cuenca': 204, 'Castellón': 198, 'Valencia': 246},
    'Burgos': {'Burgos': 0, 'Tarragona': 432, 'Bilbao': 119, 'Huesca': 272, 'Logroño': 103, 'Madrid': 214, 'Teruel': 310, 'Guadalajara': 212, 'Zaragoza': 245, 'Soria': 119, 'Cuenca': 284, 'Castellón': 402, 'Valencia': 424},
    'Soria': {'Soria': 0, 'Tarragona': 318, 'Bilbao': 171, 'Huesca': 176, 'Logroño': 77, 'Madrid': 182, 'Teruel': 195, 'Guadalajara': 138, 'Zaragoza': 133, 'Burgos': 119, 'Cuenca': 191, 'Castellón': 284, 'Valencia': 311},
    'Cuenca': {'Cuenca': 0, 'Tarragona': 308, 'Bilbao': 361, 'Huesca': 271, 'Logroño': 267, 'Madrid': 138, 'Teruel': 93, 'Guadalajara': 106, 'Zaragoza': 204, 'Burgos': 284, 'Soria': 191, 'Castellón': 178, 'Valencia': 164},
    'Castellón': {'Castellón': 0, 'Tarragona': 167, 'Bilbao': 436, 'Huesca': 240, 'Logroño': 340, 'Madrid': 314, 'Teruel': 98, 'Guadalajara': 273, 'Zaragoza': 198, 'Burgos': 402, 'Soria': 284, 'Cuenca': 178, 'Valencia': 63},
    'Valencia': {'Valencia': 0, 'Tarragona': 229, 'Bilbao': 473, 'Huesca': 296, 'Logroño': 375, 'Madrid': 302, 'Teruel': 115, 'Guadalajara': 270, 'Zaragoza': 246, 'Burgos': 424, 'Soria': 311, 'Cuenca': 164, 'Castellón': 63}
}

# Función para la búsqueda avariciosa
def busqueda_avariciosa(inicio, objetivo):
    # Inicializa la lista de nodos abiertos con el costo heurístico del nodo inicial hacia el objetivo.
    abiertos = [(heuristicas[inicio][objetivo], inicio)]
    cerrados = set()  # Conjunto para rastrear nodos ya visitados.
    padres = {inicio: None}  # Diccionario para rastrear los padres de cada nodo.
    distancia_total = 0  # Inicializa la distancia total recorrida en 0.

    # Mientras haya nodos abiertos por explorar
    while abiertos:
        # Extrae el nodo con el costo más bajo de la cola de prioridad.
        _, actual = heapq.heappop(abiertos)
        
        # Si el nodo actual es el objetivo, construye el camino
        if actual == objetivo:
            camino = []  # Lista para almacenar el camino encontrado.
            while actual:
                camino.append(actual)  # Agrega el nodo actual al camino.
                actual = padres[actual]  # Retrocede al padre del nodo actual.
            camino = camino[::-1]  # Invierte el camino para que esté en orden desde inicio hasta objetivo.
            
            # Calcular la distancia total para el camino encontrado.
            for i in range(len(camino) - 1):
                distancia_total += distancias[camino[i]][camino[i+1]]
                
            return camino, distancia_total  # Devuelve el camino y la distancia total.
        
        cerrados.add(actual)  # Marca el nodo actual como visitado.
        
        # Explora los nodos vecinos del nodo actual.
        for vecino in distancias[actual]:
            if vecino not in cerrados:  # Si el vecino no ha sido visitado.
                padres[vecino] = actual  # Establece el padre del vecino como el nodo actual.
                heapq.heappush(abiertos, (heuristicas[vecino][objetivo], vecino))  # Agrega el vecino a la lista de abiertos con su costo heurístico.
    
    return [], 0  # Si no se encuentra un camino, devuelve una lista vacía y 0.

# Función para el algoritmo A*
def a_estrella(inicio, objetivo):
    # Inicializa la lista de nodos abiertos con el costo heurístico del nodo inicial hacia el objetivo.
    abiertos = [(heuristicas[inicio][objetivo], inicio)]
    cerrados = set()  # Conjunto para rastrear nodos ya visitados.
    padres = {inicio: None}  # Diccionario para rastrear los padres de cada nodo.
    g_costos = {inicio: 0}  # Diccionario para rastrear el costo acumulado desde el inicio.

    # Mientras haya nodos abiertos por explorar
    while abiertos:
        # Extrae el nodo con el costo total más bajo de la cola de prioridad.
        _, actual = heapq.heappop(abiertos)
        
        # Si el nodo actual es el objetivo, construye el camino
        if actual == objetivo:
            camino = []  # Lista para almacenar el camino encontrado.
            while actual:
                camino.append(actual)  # Agrega el nodo actual al camino.
                actual = padres[actual]  # Retrocede al padre del nodo actual.
            camino = camino[::-1]  # Invierte el camino para que esté en orden desde inicio hasta objetivo.
            
            # La distancia total es simplemente el costo acumulado hasta el objetivo.
            distancia_total = g_costos[objetivo]
            
            return camino, distancia_total  # Devuelve el camino y la distancia total.
        
        cerrados.add(actual)  # Marca el nodo actual como visitado.
        
        # Explora los nodos vecinos del nodo actual.
        for vecino in distancias[actual]:
            if vecino not in cerrados:  # Si el vecino no ha sido visitado.
                # Calcula el costo acumulado hasta el vecino.
                g_costo = g_costos[actual] + distancias[actual][vecino]

                # Si el vecino no está en g_costos o si se encuentra un camino más corto hacia el vecino.
                if vecino not in g_costos or g_costo < g_costos[vecino]:
                    g_costos[vecino] = g_costo  # Actualiza el costo acumulado.
                    f_costo = g_costo + heuristicas[vecino][objetivo]  # Calcula el costo total f.
                    padres[vecino] = actual  # Establece el padre del vecino como el nodo actual.
                    heapq.heappush(abiertos, (f_costo, vecino))  # Agrega el vecino a la lista de abiertos con su costo total.

    return [], 0  # Si no se encuentra un camino, devuelve una lista vacía y 0.


# Ejecución de los algoritmos
inicio = "Logroño"
objetivo = "Valencia"

camino_avariciosa, distancia_avariciosa = busqueda_avariciosa(inicio, objetivo)
camino_a_estrella, distancia_a_estrella = a_estrella(inicio, objetivo)
print("")
print("***Camino más corto mediante búsqueda informada | Por Jesus David Trujillo Teheran.***")
print("_________________________________________________________________________________________")
print("-> Búsqueda Avariciosa:", camino_avariciosa, f"Distancia total: {distancia_avariciosa} km")
print("-> Algoritmo A*:", camino_a_estrella, f"Distancia total: {distancia_a_estrella} km")