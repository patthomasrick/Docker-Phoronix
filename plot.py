import matplotlib.pyplot as plt

data = {
    "QEMU": {
        "compression": 6117,
        "decompression": 6935,
    },
    "Rosetta": {
        "compression": 24944,
        "decompression": 16432,
    },
}

if __name__ == "__main__":
    # Show side-by-side bar plot with both compression and decompression times.
    fig, ax = plt.subplots()
    index = 0
    for name, times in data.items():
        for operation, mips in times.items():
            ax.bar(index, mips, label=operation)
            index += 1
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(["QEMU\ncompression", "QEMU\ndecompression", "Rosetta\ncompression", "Rosetta\ndecompression"])
    plt.title("Phoronix benchmark times")
    plt.ylabel("MIPS")
    plt.show()
