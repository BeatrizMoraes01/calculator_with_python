from cx_Freeze import setup, Executable

setup(name='Calculadora',
      version='0.1',
      description='Calculadora com Python',
      executables=[Executable('main.py')])
