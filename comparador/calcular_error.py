"""Añade el error de indicación a ascenso.csv sin tocar los demás datos.

E = (indicación - valor patrón) * 1000, en µm, igual que la tabla 3.2.1
del informe de prácticas.
"""

from pathlib import Path

import pandas as pd

CSV = Path(__file__).with_name("ascenso.csv")
VP = "VALOR PATRON (mm)"
IND = "INDICACION DEL COMPARADOR (mm)"
E = "ERROR DE INDICACION (µm)"


def main() -> None:
    df = pd.read_csv(CSV)
    vp = df[VP].to_numpy(dtype=float)
    ind = df[IND].to_numpy(dtype=float)
    e = (ind - vp) * 1000
    df[VP] = [f"{x:.3f}" for x in vp]
    df[IND] = [f"{x:.3f}" for x in ind]
    df[E] = [f"{x:.0f}" for x in e]
    df.to_csv(CSV, index=False)

    print(df.to_string(index=False))
    print(f"\nfe = {e.max():.0f} - {e.min():.0f} = {e.max() - e.min():.0f} µm")


if __name__ == "__main__":
    main()
