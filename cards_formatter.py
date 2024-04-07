import json, re, sys

if len(sys.argv) != 3:
    raise ValueError(f"Expected two file names, got {len(sys.argv)-1}")
with open(sys.argv[1]) as fin:
    txt = re.sub(
        r"PvZCards\.Engine\.([A-Za-z]+)\.([A-Za-z]+), "
        r"EngineLib, Version=1\.0\.0\.0, Culture=neutral, PublicKeyToken=null",
        r"\1.\2", fin.read()
    )
    cards = json.loads(txt)
with open(sys.argv[2], "w") as fout:
    json.dump(cards, fout, indent=2)