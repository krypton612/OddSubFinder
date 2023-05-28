# OddSubFinder
Otro buscador de subdominios

```
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
| > python OddSubFinder -g true # inicia\busqueda |
+-------------------------------------------------+
```
#
```
usage: OddSubFinder [-h] [-s] [-g] domains [domains ...]

A passive subdomain enumerator

positional arguments:
  domains         Specify the domain to enumerate

options:
  -h, --help      show this help message and exit
  -s, --strict    Enables strict mode, where only proper (and not also related) subdomains will be saved
  -g, --gravitiy  Full scan Validator host
 ```
