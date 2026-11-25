"""Randomiza la indicación del comparador y, opcionalmente, la temperatura.

La indicación se genera como VP + U(0.000, 0.005) mm, es decir, un desvío
de 0 a 5 µm respecto del valor patrón. La temperatura se sortea en
U(21.3, 21.5) °C solo si se pasa --temp; por defecto se conserva.
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

CSV = Path(__file__).with_name("ascenso.csv")
BU = "BLOQUES UTILIZADOS (mm)"
VP = "VALOR PATRON (mm)"
IND = "INDICACION DEL COMPARADOR (mm)"
TEMP = "TEMPERATURA DEL BLOQUE (°C)"


def main(seed: int | None = None, temp: bool = False) -> None:
    rng = np.random.default_rng(seed)
    df = pd.read_csv(CSV)

    vp = df[VP].to_numpy(dtype=float)
    desvio = rng.uniform(0.000, 0.005, size=len(df))

    df[BU] = df[BU].astype(int)
    df[VP] = [f"{x:.3f}" for x in vp]
    df[IND] = [f"{x:.3f}" for x in vp + desvio]

    if temp:
        temperatura = rng.uniform(21.3, 21.5, size=len(df))
        df[TEMP] = [f"{x:.1f}" for x in temperatura]

    df.to_csv(CSV, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=None,
                        help="semilla opcional para reproducir el sorteo")
    parser.add_argument("--temp", action="store_true",
                        help="randomizar también la temperatura")
    args = parser.parse_args()
    main(args.seed, args.temp)
