# 🛒 Steam Multisell Link-Generator

Ein einfaches, lokales Tool, mit dem du Steam-**Multisell-Links** erzeugst, um mehrere
Commodity-Items (Cases, Capsules, Sticker, Keys, Sammelkarten) gleichzeitig im Steam
Community Market zum Verkauf einzustellen.

Alles steckt in **einer einzigen `index.html`** – kein Server, kein Build, keine
Installation und **kein Steam-Login** in der App nötig. Einfach im Browser öffnen.

## Funktionen

- **3 Wege, Items hinzuzufügen**
  - 🔗 Steam-Market-Link(s) einfügen → App-ID & Item-Name werden automatisch ausgelesen
  - 📚 Aus kuratierter Item-Liste pro Spiel wählen (CS2, TF2, Dota 2, Steam-Karten)
  - ✏️ Manuell (App-ID, Context-ID, Name)
- **Warenkorb** mit beliebig vielen Items, gruppiert nach Spiel
- **Ein Multisell-Link pro Spiel** (Steam erlaubt nur ein Spiel pro Link)
- **Favoriten** und **Verlauf** – lokal im Browser gespeichert (`localStorage`)

## Nutzung

1. `index.html` im Browser öffnen (Doppelklick genügt).
2. Items über einen der drei Wege zum Warenkorb hinzufügen.
3. Den erzeugten Link „In Steam öffnen" – du musst im selben Browser bei Steam
   eingeloggt sein und die Items besitzen.
4. Auf der Steam-Seite Menge & Preis wählen und verkaufen.

## Wichtige Hinweise

- ⚠️ Funktioniert **nur für Commodity-Items**. Skins können über diese Methode nicht
  verkauft werden – Steam zeigt dann eine Fehlermeldung.
- Eine Stückzahl lässt sich nicht im Link festlegen; die wählst du auf der Steam-Seite.
- Das Tool ist **inoffiziell** und steht in keiner Verbindung zu Valve/Steam.
  Alle Daten bleiben lokal im Browser.

## App-IDs (häufig)

| Spiel    | App-ID | Context-ID | Eingebaute Liste |
|----------|--------|------------|------------------|
| CS2/CS:GO| 730    | 2          | ✅ voll (Live-Katalog, ~462 Container) |
| TF2      | 440    | 2          | ✅ Keys, Tickets, Tools, Crate-Serien |
| Dota 2   | 570    | 2          | Market-Link nutzen |
| Rust     | 252490 | 2          | Market-Link nutzen |
| PUBG     | 578080 | 2          | Market-Link nutzen |
| Steam (Karten) | 753 | 6      | Market-Link nutzen |

> Nur CS2 hat eine saubere, CORS-fähige Katalog-API ([ByMykel/CSGO-API](https://github.com/ByMykel/CSGO-API)).
> Für die übrigen Spiele ist das Einfügen des Market-Links der zuverlässige Weg – damit
> funktioniert jedes Commodity-Item exakt.

## Lizenz

MIT
