# Imaging Project Mapping

Use this file when the user refers to a phone by marketing name, project code, project name, SW code name, or model code and you need to normalize it into query filters.

## Main Rule

For analytics queries:

- prefer `model_name` when the local SQLite table clearly uses marketing-facing project values such as `Frogger` / `FroggerPro`
- use `project_name` for Athena flows when that table stores SW code names
- refine with `model_code` when the user asks for a specific regional SKU

Do not guess blindly. Check which field actually exists in the current table.

## Mapping Table

| Marketing name | Project code | Project name | SW code name | Model code | Notes |
| --- | --- | --- | --- | --- | --- |
| Nothing Phone (1) | `20111` | `Abra` | `Spacewar` | `A063` | colors: white, black |
| Nothing Phone (2) | `22111` | `Alakazam` | `Pong` | Global/EU: `A065`; India: `AIN065` | |
| Nothing Phone (2a) | `23111` | `Aerodactyl` | `Pacman` | `A142` | |
| Nothing Phone (2a) Plus | `23113` | `Aerodactyl Plus` | `PacmanPro` | `A142P` | |
| CMF by Nothing Phone 1 | `23114` | `Beedrill` | `Tetris` | `A015` | |
| Nothing Phone (3) | `23112` | `Arbok` | `Metroid` | `A024` | |
| Nothing Phone (3a) | `24111` | `Arcanine` | `Asteroids` | `A059` | |
| Nothing Phone (3a) Pro | `24111` | `Arcanine Pro` | `Asteroids` | `A059P` | |
| CMF by Nothing Phone 2 Pro | `24121` | `Bulbasaur` | `Galaga` | `A001` | |
| CMF by Nothing Phone 2 Air | `24131` | `Bulbasaur Lite` | `Bomberman` | `A001L` | |
| Nothing Phone (3a) Lite | `24121T` | `Bulbasaur T` | `Galaxian` | `A001T` | |
| Nothing Phone (4a) | `25111` | `Bellsprout` | `Frogger` | `A069` | base |
| Nothing Phone (4a) Pro | `25111` | `Bellsprout` | `Frogger` | `A069P` | pro |
| Nothing Phone (4b) | `25131` | `Blastoise Pro` | `SuperContra` | `A009P` | |
| Nothing Phone (4a) Lite（暂定） | `25141` | `Blastoise` | `Contra` | `A009` | |
| CMF Phone 3 | `25151` | `Blastoise C` | `Arkanoid` | `A009C` | |

## Normalization Rules

### If the user says marketing name

Examples:

- `Nothing Phone (4a)` -> local `model_name='Frogger'`
- `Nothing Phone (4a) Pro` -> local `model_name='FroggerPro'`
- `Nothing Phone (2a)` -> local `model_name='Pacman'`

### If the user says SW code

Examples:

- `Frogger` -> Nothing Phone (4a) base
- `FroggerPro` -> Nothing Phone (4a) Pro
- `Pacman` -> Nothing Phone (2a)
- `PacmanPro` -> Nothing Phone (2a) Plus

### If the user says project name

Examples:

- `Bellsprout` usually maps to the Phone (4a) family, so refine with model code or base/pro if needed
- `Arcanine` / `Arcanine Pro` map to Phone (3a) / (3a) Pro

### If the user says model code

Examples:

- `A069` -> Nothing Phone (4a) / `Frogger`
- `A069P` -> Nothing Phone (4a) Pro / `FroggerPro`
- `AIN065` -> India SKU of Nothing Phone (2) / `Pong`

## Query Guidance

When the user asks by whole-device project:

1. identify what naming system they used
2. map it to the analytics-facing field
3. say the mapping briefly in the answer when useful
4. use the narrowest valid filter

Example answer pattern:

- 用户提到 `Nothing Phone (4a)`，本地库中对应 `model_name = 'Frogger'`
- 本次查询基于 `/Users/travis.zhao/imageProduct/outputs/local_analytics/india_4_1_4_7.db`

## Special Note

`Bellsprout` is a family-level project name while local analytics may separate it into:

- `Frogger`
- `FroggerPro`

So when the user says `4a 系列` or `Bellsprout`, consider whether the query should include both.
