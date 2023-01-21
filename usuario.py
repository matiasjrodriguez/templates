class Usuario:
    def __init__(self):
        self._usuario = None
        self._crear_archivo()

    @staticmethod
    def _crear_archivo():
        import os
        import json
        if not os.path.exists('usuarios.json') or os.path.getsize('usuarios.json') == 0:
            data = {'usuarios': []}
            with open('usuarios.json', 'w') as archivo:
                json.dump(data, archivo)

    def login(self, usuario_cliente, clave_cliente):
        import json

        try:
            with open('usuarios.json') as archivo:
                data = json.load(archivo)

                encontrado = False

                for usuario in data['usuarios']:
                    if usuario['usuario'] == usuario_cliente and usuario['clave'] == clave_cliente:
                        self._usuario = usuario_cliente
                        encontrado = True
                        break

                if encontrado:
                    print('Login correcto')
                else:
                    print('Login incorrecto')

        except FileNotFoundError:
            print('No existe el registro de usuarios "Usuarios"')

    @staticmethod
    def sign_up(usuario, clave):
        import json

        try:
            with open('usuarios.json', 'r') as archivo:
                data = json.load(archivo)

            data['usuarios'].append({
                'usuario': usuario,
                'clave': clave
            })

            with open('usuarios.json', 'w') as archivo:
                json.dump(data, archivo)

        except FileNotFoundError:
            print('No existe el registro de usuarios "Usuarios"')
