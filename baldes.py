# encoding: utf-8
# A linha anterior permite usar acentos no nosso programa.

def gerar_caminhos(grafo, caminho, final):
    """Enumera todos os caminhos no grafo `grafo` iniciados por `caminho` e que terminam no vértice `final`."""

    # Se o caminho de fato atingiu o vértice final, não há o que fazer.
    if caminho[-1] == final:
        yield caminho
        return

    # Procuramos todos os vértices para os quais podemos avançar…
    for vizinho in G[caminho[-1]]:
        # …mas não podemos visitar um vértice que já está no caminho.
        if vizinho in caminho:
            continue
        # Se você estiver usando python3, você pode substituir o for
        # pela linha "yield from gerar_caminhos(grafo, caminho + [vizinho], final)"
        for caminho_maior in gerar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior
        
# Exemplo de uso
G = {
  "00": ["40","03"],
  "40": ["13","43"],
  "13": ["03","10"],
  "03": ["30","43"],
  "43": ["40","03"],
  "10": ["01","00"],
  "01": ["41","00"],
  "41": ["23"],
  "30": ["33"],
  "33": ["42"],
  "42": [],
  "23": []
}
for caminho in gerar_caminhos(G, ['00'], '23'):
    # "print(caminho)" em python3
    print caminho

