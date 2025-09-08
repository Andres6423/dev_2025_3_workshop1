import pytest
from games import Games

class TestGames:
    def setup_method(self):
        self.games = Games()

    def test_piedra_papel_tijera(self):
        assert self.games.piedra_papel_tijera("piedra", "tijera") == "jugador1"
        assert self.games.piedra_papel_tijera("papel", "piedra") == "jugador1"
        assert self.games.piedra_papel_tijera("tijera", "papel") == "jugador1"
        assert self.games.piedra_papel_tijera("tijera", "piedra") == "jugador2"
        assert self.games.piedra_papel_tijera("piedra", "papel") == "jugador2"
        assert self.games.piedra_papel_tijera("papel", "tijera") == "jugador2"
        assert self.games.piedra_papel_tijera("piedra", "piedra") == "empate"

    def test_adivinar_numero_pista(self):
        assert self.games.adivinar_numero_pista(10, 10) == "correcto"
        assert self.games.adivinar_numero_pista(10, 15) == "muy alto"
        assert self.games.adivinar_numero_pista(10, 5) == "muy bajo"

    def test_ta_te_ti_ganador(self):
        
        tablero_fila1 = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila1) == "X"

        tablero_fila2 = [[" ", " ", " "], ["O", "O", "O"], ["X", "X", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila2) == "O"

        tablero_fila3 = [["O", "X", "O"], ["X", "O", "X"], ["X", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_fila3) == "X"

       
        tablero_col1 = [["X", "O", "O"], ["X", "O", "X"], ["X", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col1) == "X"

        tablero_col2 = [["X", "O", "X"], [" ", "O", "X"], ["X", "O", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col2) == "O"

        tablero_col3 = [["X", "O", "O"], ["X", "X", "O"], [" ", " ", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_col3) == "O"

       
        tablero_diag1 = [["X", "O", "O"], ["O", "X", "O"], ["X", "O", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag1) == "X"

        
        tablero_diag2 = [["X", "O", "O"], ["X", "O", "X"], ["O", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag2) == "O"

        
        tablero_empate = [["X", "O", "X"], ["O", "O", "X"], ["O", "X", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_empate) == "empate"

       
        tablero_continua = [["X", "O", " "],
                            [" ", "O", "X"],
                            ["O", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_continua) == "continua"

    def test_generar_combinacion_mastermind(self):
        colores = ["rojo", "azul", "verde"]
        combinacion = self.games.generar_combinacion_mastermind(4, colores)
        assert len(combinacion) == 4
        for c in combinacion:
            assert c in colores

    def test_validar_movimiento_torre_ajedrez(self):
        tablero = [[" " for _ in range(8)] for _ in range(8)]
        tablero[0][0] = "T"
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 7, tablero)
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 7, 0, tablero)
        assert not self.games.validar_movimiento_torre_ajedrez(0, 0, 7, 7, tablero)

        tablero[0][3] = "P"  # pieza bloqueando
        assert not self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 7, tablero)
