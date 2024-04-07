import json, re, sys

if len(sys.argv) != 3:
    raise ValueError(f"Expected two file names, got {len(sys.argv)-1}")
with open(sys.argv[1]) as fin:
    cards = json.load(fin)
    txt = json.dumps(cards, indent=None, separators=(",", ":"))
    txt = re.sub(
        r"(Components|Effects|Queries)\.[A-Za-z]+",
        lambda match: f"PvZCards.Engine.{match.group(0)}, "
                       "EngineLib, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null",
        txt
    )
with open(sys.argv[2], "w") as fout:
    fout.write(txt)