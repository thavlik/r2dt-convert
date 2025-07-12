import json
import sys

path = sys.argv[1]
with open(path, "r") as f:
    m = json.loads(f.read())
seq = m['rnaComplexes'][0]['rnaMolecules'][0]['sequence']
for bp in seq:
    resi = bp['residueName']
    if resi not in ['A', 'C', 'G', 'U']:
        continue
    print(resi, bp['x'], bp['y'])