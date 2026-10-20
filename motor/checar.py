"""Procura travessão (U+2014) e meia-risca (U+2013) nos arquivos passados. Sem saída = tudo certo.
Uso: python3 checar.py posts/p10_*.py posts/legendas_semana.py
"""
import sys
ruim = 0
for f in sys.argv[1:]:
    for n, l in enumerate(open(f, encoding='utf-8'), 1):
        if '–' in l or '—' in l:
            ruim += 1; print(f'{f}:{n}: {l.strip()[:120]}')
sys.exit(1 if ruim else 0)
