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
# Preview
![](img/img1.png?raw=true)
# Instalacion
```console
krypton612@localhost:~$ git clone https://github.com/krypton612/OddSubFinder.git
Cloning into 'oddsubfinder'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (39/39), done.
Receiving objects:  72% (36/50)
Receiving objects: 100% (50/50), 153.13 KiB | 507.00 KiB/s, done.
Resolving deltas: 100% (6/6), done.
krypton612@localhost:~$ cd OddSubFinder
krypton612@localhost:~$ git checkout master
Switched to a new branch 'master'
branch 'master' set up to track 'origin/master'.
krypton612@localhost:~$ pip install virtualenv
Requirement already satisfied: virtualenv in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (20.16.3)
Requirement already satisfied: filelock<4,>=3.4.1 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (3.8.0)
Requirement already satisfied: distlib<1,>=0.3.5 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (0.3.5)
Requirement already satisfied: platformdirs<3,>=2.4 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (2.5.2)

[notice] A new release of pip is available: 23.0 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
krypton612@localhost:~$ python -m virtualenv venv
created virtual environment CPython3.10.5.final.0-64 in 1964ms
  creator CPython3Windows(dest=C:\Users\krypton612\OddSubFinder\oddsubfinder\venv2, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\krypton612\AppData\Local\pypa\virtualenv)
    added seed packages: pip==23.1, setuptools==67.6.1, wheel==0.40.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
krypton612@localhost:~$ source venv/bin/activate
(venv) krypton612@localhost:~$ pip install -r requirements.txt
Requirement already satisfied: requests in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from -r .\requirements.txt (line 1)) (2.28.0)
Collecting dnsdumpster
  Using cached dnsdumpster-0.8.tar.gz (6.8 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: BeautifulSoup4 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from -r .\requirements.txt (line 3)) (4.11.1)
Collecting ping3
  Using cached ping3-4.0.4-py3-none-any.whl (13 kB)
Requirement already satisfied: colorama in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from -r .\requirements.txt (line 5)) (0.4.5)
Collecting sty
  Using cached sty-1.0.4-py3-none-any.whl (11 kB)
Collecting tabulate
  Using cached tabulate-0.9.0-py3-none-any.whl (35 kB)
Requirement already satisfied: fake_useragent in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from -r .\requirements.txt (line 8)) (0.1.11)
Requirement already satisfied: idna<4,>=2.5 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from requests->-r .\requirements.txt (line 1)) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from requests->-r .\requirements.txt (line 1)) (1.26.9)
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from requests->-r .\requirements.txt (line 1)) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from requests->-r .\requirements.txt (line 1)) (2022.6.15)
Requirement already satisfied: bs4 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from dnsdumpster->-r .\requirements.txt (line 2)) (0.0.1)
Requirement already satisfied: soupsieve>1.2 in c:\users\krypton612\appdata\local\programs\python\python310\lib\site-packages (from BeautifulSoup4->-r .\requirements.txt (line 3)) (2.3.2.post1)
Installing collected packages: sty, tabulate, ping3, dnsdumpster
  DEPRECATION: dnsdumpster is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
  Running setup.py install for dnsdumpster ... done
Successfully installed dnsdumpster-0.8 ping3-4.0.4 sty-1.0.4 tabulate-0.9.0

[notice] A new release of pip is available: 23.0 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
krypton612@localhost:~$ python __main__.py -h
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

usage: OddSubFinder [-h] [-s] [-g] domains [domains ...]

A passive subdomain enumerator

positional arguments:
  domains         Specify the domain to enumerate

options:
  -h, --help      show this help message and exit
  -s, --strict    Enables strict mode, where only proper (and not also related) subdomains will be saved
  -g, --gravitiy  Full scan Validator host
```
