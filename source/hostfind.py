# -*- encoding: utf-8 -*-
"""
Hostfind parser

:Copyright: Â© 2023, Krypton612.
:License: BSD (see /LICENSE).
"""
from sty import fg, bg, rs
import threading
from ping3 import ping
import socket
from colorama import init, Fore, Back, Style
init()


class HostfindParser:
    def __init__(self):
        self.ip_available = []
        self.cdn_service = None
        self.ip_with_cdn = []
        self.ip_not_cdn = []
        self.ip_and_cdn = {}
        

    def get_cdn_service(self, ip):
        try:
            hostnames = socket.gethostbyaddr(ip)
            if hostnames:
                self.cdn_service = hostnames[0]
        except socket.herror:
            pass

        if self.cdn_service:
            print(f"La direccion IP {Fore.BLUE}{ip} {Style.RESET_ALL}utiliza el servicio CDN: {Fore.GREEN}{self.cdn_service}{Style.RESET_ALL}")
            self.ip_and_cdn[ip] = self.cdn_service
            self.cdn_service = None
            self.ip_with_cdn.append(ip)
        else:
            self.ip_not_cdn.append(ip)
            self.ip_and_cdn[ip] = None
            print(f"No se encontro informacion de servicio CDN para la direccion IP {Fore.RED}{ip}{Style.RESET_ALL}")

    def send_ping(self, destination):
        result = ping(destination)
        if result is not None:
            if result == False:
                pass
            else:    
                print(f"Response was received from x {Fore.BLUE}{destination}: {Fore.GREEN }{result} ms{Style.RESET_ALL}")
                self.ip_available.append(destination)
        else:
            pass

    def process_ip_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                ips = file.readlines()
        except Exception:
            print(f"{Style.BRIGHT}{Fore.RED}[!] Porfavor haga un reconocimiento pasivo o agregue de forma manual el archivo {file_path}")
            exit(1)
        threads = []
        for ip in ips:
            ip = ip.strip()  # Eliminar espacios en blanco y saltos de l¡nea

            t = threading.Thread(target=self.send_ping, args=(ip,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def process_ip_available(self, alone_ip):
        threads = []
        for ip in alone_ip:
            ip = ip.strip()  # Eliminar espacios en blanco y saltos de l¡nea

            t = threading.Thread(target=self.get_cdn_service, args=(ip,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def obtener_direcciones_ip(self):
        resultados = {}

        def obtener_ip(dominio):
            try:
                ip = socket.gethostbyname(dominio)
                resultados[dominio] = ip
            except socket.gaierror:
                resultados[dominio] = None

        hilos = []

        for dominio in self.ip_available:
            hilo = threading.Thread(target=obtener_ip, args=(dominio,))
            hilo.start()
            hilos.append(hilo)

        for hilo in hilos:
            hilo.join()

        return resultados
    
    @property
    def get_ip_with_cdn(self):
        return self.ip_with_cdn
    @property
    def get_ip_not_cdn(self):
        return self.ip_not_cdn
    
    @property
    def get_ip_and_cdn(self):
        return self.ip_and_cdn
    
    @property
    def get_ip_available(self):
        return self.ip_available 