import matplotlib.pyplot as plt

def z_score_normalize(data):
    # Laske listan keskiarvo ja keskihajonta
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5

    # Sovella z-pistemääritystä jokaiseen arvoon
    normalized_data = [(x - mean_val) / std_dev for x in data]

    return normalized_data

# Alkuperäinen data
original_data = [10, 20, 15, 30, 25]

# Z-pistemääritys
normalized_data = z_score_normalize(original_data)

# Visualisointi
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
axs[1].set_title('Normalisoitu Data (Z-Score)')
axs[1].set_xticks(range(len(normalized_data)))
axs[1].set_xticklabels(range(len(normalized_data)))
axs[1].set_xlabel('Indeksi')
axs[1].set_ylabel('Arvo')

plt.tight_layout()
plt.show()
