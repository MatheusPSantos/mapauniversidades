import requests
from bs4 import BeautifulSoup

url = "https://www.pebsp.com/lista-de-universidade-federais-do-brasil-2020"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tables = soup.find_all("table", {"width": "1168"})
contador_regiao = 0

regioes = []
universidades = []

for table in tables:
    tbody = table.find("tbody")
    primeiro_tr = tbody.find("tr")
    nome_regiao = primeiro_tr.find("td").find("h3").string

    regiao = {
        "regiao": nome_regiao,
        "cod": contador_regiao
    }

    regioes.append(regiao)

    linhas = tbody.find_all("tr")
    primeira_linha_valida = tbody.find_all("tr")[2]
    contador_linha = 0

    for linha in linhas:
        if contador_linha >= len(linhas):
            break
        if contador_linha > 2:
          td_elements = linha.find_all("td")

          region = td_elements[0].text.strip()
          state = td_elements[1].text.strip()
          university = td_elements[2].text.strip()
          acronym = td_elements[3].text.strip()
          link = td_elements[3].find("a")

          if link:
            link = link.get("href")
          else:
            link = ""

          universidade = {
            "regiao": region,
            "cod_regiao": contador_regiao,
            "uf": state,
            "nome": university,
            "sigla": acronym,
            "link": link
          }
          universidades.append(universidade)
        contador_linha += 1

    contador_regiao += 1
