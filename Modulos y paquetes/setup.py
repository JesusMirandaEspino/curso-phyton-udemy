from struct import pack
from setuptools import setup

setup(
    name='Mensajes',
    version='2.0',
    description='Un paquete para saludar y despedir',
    author='Héctor Costa Guzmán',
    author_email='hola@hektor.dev',
    url='https://www.hektor.dev',
    packages=['mensajes', 'mensajes.hola', 'mensajes.adios'],
    scripts=['test.py']
)
