# -*- encoding: utf-8 -*-

import re
import argparse
import source.crtsh as cr
import source.urlscan as us
import source.threatcrowd as tc
import source.dnsdumpster as dd
import source.certspotter as cs
import source.hackertarget as ht

from colorama import init, Fore, Back, Style
from tabulate import tabulate


from source.hostfind import HostfindParser
from source.hostcheck import check_domains

from utils import (polish_subdomain_strings,
                          remove_unrelated_domains,
                          clean_domain_strings,
                          sort_domains)

__all__ = ('main',)
init()
def agregar_codigo_respuesta(diccionario, matriz):
    for dominio, codigo_respuesta in diccionario.items():
        for entrada in matriz:
            if entrada[0] == dominio:
                entrada.append(codigo_respuesta)
                break
        else:
            matriz.append([dominio, '', '', codigo_respuesta])

def show_banner():
    print(Fore.GREEN + Style.BRIGHT +""" 
+--------------------------------------+----------+
|++++++++++++++++++++++++++++++++++++++|Shell Kr6 |
+--------------------------------------+----------+
|                                                 |
| > OddSubFinder                                  |
|                                                 |
| > OddSubFinder explora  el lado peculiar de los |
|   subdominios. Esta herramienta te permite      |
|   encontrar subdominios peculiares.             |
|                                                 |
| > comandos de ayuda                             |
+-------------------------------------------------+
|                                                 |
| > python OddSubFinder -u <subdomain> -p true    |
|   + Este comando hara una busqueda pasiva de    |
|   + subdominios y guardara el resultado         |
|                                                 |
| > python OddSubFinder -g true # inicia\\busqueda |
+-------------------------------------------------+
    """+Style.RESET_ALL)


def main():
    """Main routine of pdlist."""
    show_banner()
    parser = argparse.ArgumentParser(
        prog='OddSubFinder', description='A passive subdomain enumerator')

    parser.add_argument(
        "domains",
        help="Specify the domain to enumerate",
        default=[],
        type=str,
        nargs='+',
    )
    parser.add_argument(
        "-s", "--strict",
        dest='is_strict',
        action='store_true',
        help="Enables strict mode, where only proper (and not also related)\
        subdomains will be saved",
        default=False,
    )
    
    parser.add_argument(
        "-g", "--gravitiy",
        dest='is_scan',
        action='store_true',
        help="Full scan\
        Validator host",
        default=False,
    )
#    parser.add_argument(
#        "-o", "--output",
#        dest='outputfile',
#        help="Save results to the specified file",
#        default=args.domains[0],
#        nargs='?',
#        type=argparse.FileType(mode='wt',encoding='utf-8'),
#    )
    args = parser.parse_args()
    subdomains = []
    domains = clean_domain_strings(args.domains)

    print(
        f'{Fore.RED}{Style.BRIGHT}[*] {Fore.GREEN}The analyzed domains will be: {Fore.YELLOW}' +
        ' '.join(domains)+Style.RESET_ALL)

    sources = [tc, ht, us, dd, cr, cs]

    # inicia la busqueda
    if args.is_scan:
        headers = ["Dominio", "Direccion Ip", "Dominio NS"]
        
        hostifinder = HostfindParser()

        file_name = domains[0]+".txt"
        print(f"Escaneando posibles dominios {file_name}")
        hostifinder.process_ip_file(file_name)
        listMap = hostifinder.obtener_direcciones_ip()
        print(f"\n{Fore.RED}{Style.BRIGHT}[*] {Fore.GREEN} Extrayendo direcciones IP{Style.RESET_ALL}\n")
        alone_ip = []
        for domain, ip in listMap.items():
            print(f"Domain: {Fore.YELLOW}{domain}{Style.RESET_ALL} Internet protocol: {Fore.BLUE}{ip}{Style.RESET_ALL}")
            alone_ip.append(ip)
        print(f"\n{Fore.RED}{Style.BRIGHT}[*] {Fore.GREEN} Extrayendo registros SOA {Style.RESET_ALL}\n")  
        hostifinder.process_ip_available(alone_ip)
        h = hostifinder.get_ip_and_cdn
        
        matriz = [[dominio, direccion_ip, ns] for dominio, direccion_ip in listMap.items() if direccion_ip in h for direccion_ip2, ns in h.items() if direccion_ip2 == direccion_ip]
        
        print(f"{Fore.RED}{Style.BRIGHT}[+] {Fore.GREEN}Imprimiendo tabla{Style.RESET_ALL}")
        table = tabulate(matriz, headers, tablefmt="fancy_grid")
        print(Fore.GREEN+Style.BRIGHT+table+Style.RESET_ALL)
        # listMap tiene datos como dominio: direccion ip
        # hostifinder.get_ip_and_cdn extrae un diccionario con direccion ip: "ns domain"
        desicion = input(f"{Fore.RED}{Style.BRIGHT}[+]{Fore.GREEN} Desea ejecutar pruebas GET? Y/n: {Fore.RED}")
        if "y" == desicion.lower():
            
            f = hostifinder.get_ip_available
            domain_status = check_domains(f)
            # listMap = {dominio.com: "direccion ip"}
            # h = {direccion_ip: cdn}
            # domain_status = {dominio.com: "codigo de estado"}
            headers2 = ["Dominio", "Direccion Ip", "Dominio NS", "Cod Respuesta"]
            agregar_codigo_respuesta(domain_status, matriz)
            table2 = tabulate(matriz, headers2, tablefmt="fancy_grid")
            print(Fore.GREEN+Style.BRIGHT+table2+Style.RESET_ALL)
        
        else:
            # not requests
            print(f"[x] Programado por {Fore.GREEN}Krypton612")
        
    else:    
        for source in sources:
            name = re.sub(r' parser$', '', source.__doc__.strip().split('\n')[0])
            print('[+] Searching on {}...'.format(name))

            try:
                subdomains += source.parse(domains)
            except Exception:
                next

        print()
        print('[+] Printing domain list...')
        print()

        subdomains = polish_subdomain_strings(subdomains)

        if args.is_strict:
            subdomains = remove_unrelated_domains(subdomains, domains)
        
        # only get unique subdomains strings to avoid duplicates
        subdomains = list(set(subdomains))
        
        # sort subdomains
        subdomains = sort_domains(subdomains)

        print()
        
        file_d2 = args.domains

        
        for file_d in file_d2:
            # Verificar que file_d sea una cadena de texto
            if isinstance(file_d, str):
                # Crear variable FileType de tipo escritura y en utf-8
                file_d = file_d + ".txt"
                file = open(file_d, mode="w", encoding="utf-8")

                # Realizar operaciones de escritura en el archivo
                file.write('\n'.join(subdomains))

                # Cerrar el archivo
                file.close()
            else:
                print(f"La ruta del archivo {file_d} no es una cadena de texto valida.")
        
        for subdomain in subdomains:
            print(subdomain)