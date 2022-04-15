# projekt_3_elections_scraper
Třetí projek Engeto Python Akademie.
## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb z let 2006 až 2021. Odkaz voleb 2017 k prohlédnutí [zde](https://volby.cz/pls/ps2017/ps3?xjazyk=CZ).
## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uloženy v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
$ pip --version
$ pip install -r requirements.txt
```
## Spouštění projektu
Spuštění souboru ```elections-scraper.py``` v rámci příkazového řádku požaduje dva povinné argumenty.

```python elections-scraper.py <odkaz-uzemniho-celku> <vysledny-soubor.csv>```

Následně se vám stáhnou výsledky jako soubor s příponou ```.csv```
## Ukázka projektu
Výsledky hlasování pro okres Uherské Hradiště:
  1. argument: ```https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202```
  2. argument: ```vysledky_uh_2017.csv```
### Spuštění programu:
```python elections_scraper.py "https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202" "vysledky_uh_2017.csv"```
### Průběh stahování:
```
STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202
UKLADAM DO SOUBORU: vysledky_uh_2017.csv
UKONCUJI elections_scraper
```
### Částečný výstup:
```
code,location,registered,envelopes,valid,...
592013,Babice,1452,873,866,79,0,0,60,0,55,66,5,6,3,0,2,74,0,23,254,1,0,95,5,1,0,133,4
592021,Bánov,1707,1070,1063,92,2,1,75,0,117,62,10,1,11,1,2,71,1,11,293,1,0,148,6,0,0,156,2
...
```
