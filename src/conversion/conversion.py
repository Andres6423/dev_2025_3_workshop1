class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        return(celsius * 9/5) + 32
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        
    
    def fahrenheit_a_celsius(self, fahrenheit):
        return(fahrenheit -32) * 5/9
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
       
    
    def metros_a_pies(self, metros):
        return metros * 3.281
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
    
    
    def pies_a_metros(self, pies):
        return pies * 0.3048
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        
    
    def decimal_a_binario(self, decimal):
        if decimal < 0>:
            raise ValueError("el numero debe de ser mayor a 0 o positivo")
        return bin(decimal)[2:]
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
      
    
    def binario_a_decimal(self, binario):
        if not set (binario) <={"0", "1"}:
            raise ValueError("El numero no es valido para binario")
            return int(binario, 2)
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
     
    
    def decimal_a_romano(self, numero):
        if not(1 <= numero <= 3999):
            raise ValueError("El numero debe ser mayor a 1 y debe estar entre 3999")

        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"), (1, "I") 
            
        ]

        RESULTADO = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                resultado -= valor
        return resultado

        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
    
    
    def romano_a_decimal(self, romano):
        valores = {
            "I": 1, "V": 1, "X": 1, "L": 1, 
            "C": 1, "D": 1, "M": 1
        }
        total= 0
        prev = 0
        for c in romano [::-1]:
            v = valores [c]
            if v < prev:
                total -= V
            else:
                    total += V
                prev = V
        return total
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        
    
    def texto_a_morse(self, texto):
        morse = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
            "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }
        text = texto.upper()
        return "".join(morse[c] for c in texto if c in morse)

        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        
    
    def morse_a_texto(self, morse):
        morse = {
             ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
            ".": "E", "..-.": "F", "--.": "G", "....": "H",
            "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
            "--": "M", "-.": "N", "---": "O", ".--.": "P",
            "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
            "-.--": "Y", "--..": "Z",
            "-----": "0", ".----": "1", "..---": "2", "...--": "3",
            "....-": "4", ".....": "5", "-....": "6", "--...": "7",
            "---..": "8", "----.": "9"
        }
        return "". join(morse[c] for c in codigo.split() if c in morse)
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        