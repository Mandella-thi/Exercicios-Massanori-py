# M.Difícil: Fila de tijolos sem usar loops #
# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos
# é possível uma solução sem usar for ou while
# fila_tijolos(3, 1, 8) -> True
# fila_tijolos(3, 1, 9) -> False
# fila_tijolos(3, 2, 10) -> True
def fila_tijolos(n_peq, n_gra, meta):
    return n_peq>= meta%5 and (n_peq +(n_gra *5))>= meta:

print(fila_tijolos(3,2,8))