from getpass import getpass
import paramiko
import time
ip = input("Ingrese IP del dispositivo: ")
usuario = input("Ingrese usuario: ")
password = getpass("Ingrese contraseña: ")
print ("Conectando con el dispositivo......")
cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cliente.connect(hostname=ip,username=usuario,password=password)
devices_access = cliente.invoke_shell()
devices_access.send(b"conf t\n")