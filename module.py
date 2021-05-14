import os
import sys


class MModulo:
    def createDir(self, dir):
        try:
            os.mkdir(dir)
        except OSError as _err:
            print(f'Diretório já existe')
            raise _err


    def createArq(self, dir):
        try:
            arq = open(f'{dir}/__init__.py', 'w')
            arq.close()
            arq = open(f'{dir}/controller.py', 'w')
            arq.close()
            arq = open(f'{dir}/routes.py', 'w')
            arq.close()
            arq = open(f'{dir}/services.py', 'w')
            arq.close()
            arq = open(f'{dir}/models.py', 'w')
            arq.close()
        except Exception as _err:
            print(f'Erro na criação de arquivos')
            raise _err


    def criarModulo(self, nome):

        dir = f'{os.getcwd()}/app/{nome}'
        try:
            self.createDir(dir)
            self.createArq(dir)
        except OSError:
            print(f'Oops! Erro na criação do módulo {nome}')
        else:
            print(f'Blz! Módulo {nome} criado com sucesso')

        
def modulo():
    modMng = MModulo()
    modMng.criarModulo(sys.argv[2])


manager = {
    "modulo": modulo
}


manager[sys.argv[1]]()
