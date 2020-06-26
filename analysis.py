import json 
import pandas as pd
import numpy as np
with open('tmp/space-invaders-1/openaigym.episode_batch.0.8049.stats.json') as json_file:
    data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')

best_episode = np.argmax(df.iloc[2].tolist()[0])
list_of_indexes = df.index.tolist()

for i in range(1,len(list_of_indexes)):
  item_index = df.index.tolist()[i]
  value = df.iloc[i][0][best_episode]
  print(item_index, (value))

  