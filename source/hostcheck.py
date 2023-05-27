import threading
import requests
from requests.exceptions import Timeout
from fake_useragent import UserAgent
import concurrent.futures

testing_domain_list = {}

def check_domains(domains):
    req = requests.Session()

    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white

    def check_domain(subdomain):
        ua = UserAgent()
        headers = {'User-Agent': str(ua.random)}

        try:
            reque = req.get("https://" + subdomain, headers=headers, timeout=2)
            
            if reque.status_code == 200:
                print(f"{subdomain} codigo {Y}{reque.status_code}{W} \u26A1\uFE0F")
            elif reque.status_code == 100:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 101:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2b50\ufe0f")
            elif reque.status_code == 502:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 503:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 1002:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 1003:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 404:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \N{FIRE}")
            else:
                print(f"{subdomain} codigo {B}{reque.status_code}{W} \u26A0\uFE0F")
            testing_domain_list[subdomain] = reque.status_code
        except requests.exceptions.ConnectionError:
            reque = requests.get("http://" + subdomain, headers=headers, verify=False, timeout=2)

            if reque.status_code == 200:
                print(f"{subdomain} codigo {Y}{reque.status_code}{W} \u26A1\uFE0F")
            elif reque.status_code == 100:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 101:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 502:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 503:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 1002:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 1003:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \u2B50\uFE0F")
            elif reque.status_code == 404:
                print(f"{subdomain} codigo {G}{reque.status_code}{W} \N{FIRE}")
            else:
                print(f"{subdomain} codigo {B}{reque.status_code}{W} \u26A0\uFE0F")
            testing_domain_list[subdomain] = reque.status_code
        except requests.exceptions.HTTPError as errh:
            print(subdomain, end=" ")
            print(f"Codigo {R}-1{W} \u274C\uFE0F")
            testing_domain_list[subdomain] = "-1"
        except requests.exceptions.ConnectionError as errc:
            print(subdomain, end=" ")
            print(f"Codigo {R}-1{W} \u274C\uFE0F")
            testing_domain_list[subdomain] = reque.status_code
        except requests.exceptions.Timeout as errt:
            print(subdomain, end=" ")
            print(f"Codigo {R}-1{W} \u274C\uFE0F")
            testing_domain_list[subdomain] = reque.status_code
        except requests.exceptions.RequestException as err:
            print(subdomain, end=" ")
            print(f"Codigo {R}-1{W} \u274C\uFE0F")
            testing_domain_list[subdomain] = reque.status_code
        except (requests.RequestException, KeyError) as e:
            print(f"Error al procesar el dominio {subdomain}")
            testing_domain_list[subdomain] = reque.status_code
        except Exception as e:
            print("error 1")
            print("=================================================")
            testing_domain_list[subdomain] = reque.status_code
        except Timeout as tim:
            print("error")

    # Crear un ThreadPoolExecutor con 10 trabajadores
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Enviar cada dominio al executor para su procesamiento
        futures = [executor.submit(check_domain, domain) for domain in domains]

        # Esperar a que todas las tareas se completen
        concurrent.futures.wait(futures)
    
    return testing_domain_list
