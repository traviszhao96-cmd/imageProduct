# Model Mapping

Use analytics-facing SW code in `project_name`.

## Main Mappings

| project_name | marketing_name | internal project name | model_code | notes |
| --- | --- | --- | --- | --- |
| `Spacewar` | Nothing Phone (1) | `Abra` | `A063` | single SKU |
| `Pong` | Nothing Phone (2) | `Alakazam` | Global/EU: `A065`; India: `AIN065` | refine by `model_code` if region matters |
| `Pacman` | Nothing Phone (2a) | `Aerodactyl` | `A142` | single SKU |
| `PacmanPro` | Nothing Phone (2a) Plus | `Aerodactyl Plus` | `A142P` | single SKU |
| `Tetris` | CMF by Nothing Phone 1 | `Beedrill` | `A015` | |
| `Metroid` | Nothing Phone (3) | `Arbok` | `A024` | |
| `Asteroids` | Nothing Phone (3a) / (3a) Pro family | `Arcanine` / `Arcanine Pro` | `A059`, `A059P` | refine with `model_code` when needed |
| `Galaga` | CMF by Nothing Phone 2 Pro | `Bulbasaur` | `A001` | |
| `Bomberman` | CMF by Nothing Phone 2 Air | `Bulbasaur Lite` | `A001L` | |
| `Galaxian` | Nothing Phone (3a) Lite | `Bulbasaur T` | `A001T` | |
| `Frogger` | Nothing Phone (4a) | `Bellsprout` | `A069` | base |
| `FroggerPro` | Nothing Phone (4a) Pro | `Bellsprout` | `A069P` | pro |
| `SuperContra` | Nothing Phone (4b) | `Blastoise Pro` | `A009P` | |
| `Contra` | Nothing Phone (4a) Lite（暂定） | `Blastoise` | `A009` | |
| `Arkanoid` | CMF Phone 3 | `Blastoise C` | `A009C` | |

## Rule

- If the user says a marketing or internal project name, convert it to the SW code in `project_name` before writing SQL.
- If the source row groups multiple SKUs under one family, refine with `model_code` when needed.
- Prefer `project_name IN (...)` when the user asks for a whole family.
- For `Bellsprout`, do not stop at the family name; decide whether the request means `Frogger`, `FroggerPro`, or both.
