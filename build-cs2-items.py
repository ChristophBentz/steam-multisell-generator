#!/usr/bin/env python3
"""Erzeugt cs2-items.json (schlanke Namensliste aller CS2-Container).

Quelle: ByMykel/CSGO-API (frei, Community-gepflegt).
Ausführen, wenn Valve neue Cases/Capsules veröffentlicht:

    python3 build-cs2-items.py
"""
import json
import urllib.request

URL = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/crates.json"

def main():
    with urllib.request.urlopen(URL) as r:
        data = json.load(r)
    # Alle Container mit Marktnamen aufnehmen. NICHT nach "type" filtern:
    # brandneue Container (z.B. "Sealed Genesis Terminal") haben type=null und
    # würden sonst fehlen. Ein paar nicht-handelbare Geschenk-Items sind harmlos.
    names = sorted({c["market_hash_name"] for c in data if c.get("market_hash_name")})
    with open("cs2-items.json", "w", encoding="utf-8") as f:
        json.dump(names, f, ensure_ascii=False, indent=0)
    print(f"cs2-items.json geschrieben: {len(names)} Items")

if __name__ == "__main__":
    main()
