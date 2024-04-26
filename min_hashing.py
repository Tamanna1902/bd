import pandas as pd
import numpy as np
import random

def shinglewithoutsepr(doc, kval):
    """
    Function to generate shingles without separator
    """
    text = doc.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(";", "").replace(":", "")
    shingles = [text[i:i+kval] for i in range(len(text)-kval+1)]
    return shingles

with open("1.txt", "r") as file:
    doc1 = file.read()
print("Document 1:")
print(doc1)
with open("2.txt", "r") as file:
    doc2 = file.read()
print("Document 2:")
print(doc2)

kval = 2
shingle1 = shinglewithoutsepr(doc1, kval)
shingle2 = shinglewithoutsepr(doc2, kval)
all_shingles = list(set(shingle1 + shingle2))
print("\nShingle 1:", shingle1)
print("Shingle 2:", shingle2)
print("All shingles:", all_shingles)

df = pd.DataFrame(columns=["Shingle", "doc1", "doc2"])
df["Shingle"] = all_shingles
df.fillna(0, inplace=True)

for i in range(len(shingle1)):
    df.loc[df["Shingle"] == shingle1[i], "doc1"] = 1
for i in range(len(shingle2)):
    df.loc[df["Shingle"] == shingle2[i], "doc2"] = 1

df["Hash1"] = df.index.map(lambda x: (17 * int(x) + 5) % len(df))
df["Hash2"] = df.index.map(lambda x: (11 * int(x) + 3) % len(df))

print("\nDataFrame:")
print(df)