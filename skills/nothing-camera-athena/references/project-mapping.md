# Nothing / CMF Project Mapping

## How To Use This Reference

For analytics, prefer the SW code / analytics-facing `project_name` alias. Internal project names such as `Abra` or `Bellsprout` are useful for cross-checking source material, but reporting should usually map to marketing names through the SW code.

If one SW code row represents multiple SKUs, refine with `model_code`.

## Analytics Alias Table

| project_name / SW code | model_code | marketing_name | project_code | internal_project_name | notes |
| --- | --- | --- | --- | --- | --- |
| `Spacewar` | `A063` | Nothing Phone (1) | `20111` | `Abra` | single SKU |
| `Pong` | `A065` / `AIN065` | Nothing Phone (2) | `22111` | `Alakazam` | India variant uses `AIN065` |
| `Pacman` | `A142` | Nothing Phone (2a) | `23111` | `Aerodactyl` | single SKU |
| `Tetris` | `A015` | CMF by Nothing Phone 1 | `23114` | `Beedrill` | single SKU |
| `PacmanPro` | `A142P` | Nothing Phone (2a) Plus | `23113` | `Aerodactyl Plus` | single SKU |
| `Asteroids` | `A059` | Nothing Phone (3a) | `24111` | `Arcanine` | base / pro row grouped in source table |
| `Asteroids` | `A059P` | Nothing Phone (3a) Pro | `24111` | `Arcanine Pro` | split by `model_code` |
| `Galaga` | `A001` | CMF by Nothing Phone 2 Pro | `24121` | `Bulbasaur` | single SKU |
| `Metroid` | `A024` | Nothing Phone (3) | `23112` | `Arbok` | single SKU |
| `Bomberman` | `A001L` | CMF by Nothing Phone 2 Air | `24131` | `Bulbasaur Lite` | source row lacks color/resolution details |
| `Galaxian` | `A001T` | Nothing Phone (3a) Lite | `24121T` | `Bulbasaur T` | single SKU |
| `Frogger` | `A069` | Nothing Phone (4a) | `25111` | `Bellsprout` | user explicitly cited `Frogger` for 4a |
| `FroggerPro` | `A069P` | Nothing Phone (4a) Pro | `25111` | `Bellsprout` | user explicitly cited `FroggerPro` for 4a Pro |
| `SuperContra` | `A009P` | Nothing Phone 4(b) | `25131` | `Blastoise Pro` | single SKU |
| `Contra` | `A009` | Nothing Phone (4a) Lite（暂定） | `25141` | `Blastoise` | tentative marketing name |
| `Arkanoid` | `A009C` | CMF Phone 3 | `25151` | `Blastoise C` | source row lacks color/resolution details |

## Full Source Table (Normalized)

| marketing_name | project_code | internal_project_name | sw_code_name | model_code | colour_id | resolution | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nothing Phone (1) | `20111` | `Abra` | `Spacewar` | `A063` | white, black | 1080 x 2400 |  |
| Nothing Phone (2) | `22111` | `Alakazam` | `Pong` | Global/EU: `A065`; India: `AIN065` | white, gray | 1080 x 2412 |  |
| Nothing Phone (2a) | `23111` | `Aerodactyl` | `Pacman` | `A142` | white, black, milk, blue, Community Edition | 1084 x 2412 |  |
| CMF by Nothing Phone 1 | `23114` | `Beedrill` | `Tetris` | `A015` | black, light green, blue, orange | 1080 x 2400 |  |
| Nothing Phone (2a) Plus | `23113` | `Aerodactyl Plus` | `PacmanPro` | `A142P` | grey, black, Community Edition | 1084 x 2412 |  |
| Nothing Phone (3a) | `24111` | `Arcanine` | `Asteroids` | `A059` | Black, White, Blue, Community Edition | 1080 x 2392 | source row grouped with 3a Pro |
| Nothing Phone (3a) Pro | `24111` | `Arcanine Pro` | `Asteroids` | `A059P` | Black, Grey | 1080 x 2392 | source row grouped with 3a |
| CMF by Nothing Phone 2 Pro | `24121` | `Bulbasaur` | `Galaga` | `A001` | black, light green, orange, white | 1080 x 2392 |  |
| Nothing Phone (3) | `23112` | `Arbok` | `Metroid` | `A024` | White, Black | 1260 x 2800 |  |
| CMF by Nothing Phone 2 Air | `24131` | `Bulbasaur Lite` | `Bomberman` | `A001L` |  |  | source row incomplete |
| Nothing Phone (3a) Lite | `24121T` | `Bulbasaur T` | `Galaxian` | `A001T` | Black, White | 1080 x 2392 |  |
| Nothing Phone (4a) | `25111` | `Bellsprout` | `Frogger` | `A069` | Base: Black / White / Pink / Blue | 1224 x 2720 | 6.78" |
| Nothing Phone (4a) Pro | `25111` | `Bellsprout` | `FroggerPro` | `A069P` | Pro: Black / White / Pink | 1260 x 2800 | 6.83" |
| Nothing Phone 4(b) | `25131` | `Blastoise Pro` | `SuperContra` | `A009P` |  | 1080 x 2344 | 6.77" |
| Nothing Phone (4a) Lite（暂定） | `25141` | `Blastoise` | `Contra` | `A009` |  | 1080 x 2344 | 6.77" |
| CMF Phone 3 | `25151` | `Blastoise C` | `Arkanoid` | `A009C` |  |  | source row incomplete |

## Unresolved / Incomplete Entries

- `Caterpie` appears in the provided mapping block without a complete row. Do not infer a marketing mapping from that fragment alone.
- The source table groups some SKUs under one project row. When exact base/pro attribution matters, include both `project_name` and `model_code` in SQL.
