import matplotlib.pyplot as plt

def min_max_normalize(data):
    # Laske listan minimi- ja maksimiarvot
    min_val = min(data)
    max_val = max(data)

    # Sovella min-max-normalisointia jokaiseen arvoon
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]

    return normalized_data

# Alkuperäinen data
original_data = [10, 15, 20, 30, 40]

# Min-max-normalisointi
normalized_data = min_max_normalize(original_data)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))


# Alkuperäinen data
axs[0].bar(range(len(original_data)), original_data, color='black')
axs[0].set_title('Alkuperäinen Data')
axs[0].set_xticks(range(len(original_data)))
axs[0].set_xticklabels(range(len(original_data)))
axs[0].set_xlabel('Indeksi')
axs[0].set_ylabel('Arvo')

# Normalisoitu data
axs[1].bar(range(len(normalized_data)), normalized_data, color='black')
axs[1].set_title('Normalisoitu Data')
axs[1].set_xticks(range(len(normalized_data)))
axs[1].set_xticklabels(range(len(normalized_data)))
axs[1].set_xlabel('Indeksi')
axs[1].set_ylabel('Arvo')

plt.tight_layout()
plt.show()
