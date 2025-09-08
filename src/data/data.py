class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        nueva = []
        for i in range(len(lista)-1, -1, -1):
            nueva.append(lista[i])
        return nueva
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        nueva = []
        for elem in lista:
            encontrado = False
            for existente in nueva:
                if existente == elem and type(existente) == type(elem):
                    encontrado = True
                    break
            if not encontrado:
                nueva.append(elem)
        return nueva
    
    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado
    
    def rotar_lista(self, lista, k):
        if not lista:
            return []
        n = len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_actual = 0
        for num in lista:
            suma_actual += num
        return suma_esperada - suma_actual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            encontrado = False
            for elem2 in conjunto2:
                if elem == elem2:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }
    
    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }
    
    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)
        return transpuesta
