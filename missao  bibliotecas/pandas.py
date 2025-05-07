import pandas as pd

df = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [23, 35, 29]
})
print(df.describe())

#saida caso não rode
#|       | idade |
#| ----- | ----: |
#| count |   3.0 |
#| mean  |  29.0 |
#| min   |  23.0 |
#| 50%   |  29.0 |
#| 75%   |  32.0 |
#| max   |  35.0 |
#