from statistics import stdev
import matplotlib.pyplot as plt

TIMES_APPLE = (
    26.233,
    26.36,
    27.966,
    27.008,
    26.007,
    25.978,
    26.062,
    26.198,
    26.468,
)
TIMES_ROSETTA = (32.155, 32.447, 32.226)
TIMES_QEMU = (253.824, 253.897, 253.233)

TIME_APPLE = sum(TIMES_APPLE) / len(TIMES_APPLE)
TIME_ROSETTA = sum(TIMES_ROSETTA) / len(TIMES_ROSETTA)
TIME_QEMU = sum(TIMES_QEMU) / len(TIMES_QEMU)
STDEV_APPLE = stdev(TIMES_APPLE)
STDEV_ROSETTA = stdev(TIMES_ROSETTA)
STDEV_QEMU = stdev(TIMES_QEMU)
DATA = (
    ("Apple M1", TIME_APPLE, STDEV_APPLE),
    ("Rosetta 2", TIME_ROSETTA, STDEV_ROSETTA),
    ("QEMU", TIME_QEMU, STDEV_QEMU),
)


def plot_1():
    # Show side-by-side bar plot with all times with uncertainty.
    plt.bar(
        ["Apple Silicon", "Rosetta 2", "QEMU"],
        [TIME_APPLE, TIME_ROSETTA, TIME_QEMU],
        yerr=[STDEV_APPLE, STDEV_ROSETTA, STDEV_QEMU],
    )
    plt.title("Phoronix benchmark times - Prime Sieve")
    plt.ylabel("Execution time (seconds)")
    plt.show()


def plot_2():
    # Compare to % difference from Apple M1.
    plt.bar(
        ["Apple Silicon", "Rosetta 2", "QEMU"],
        [
            100,
            TIME_APPLE / TIME_ROSETTA * 100,
            TIME_APPLE / TIME_QEMU * 100,
        ],
    )
    plt.title("Phoronix benchmark times - Prime Sieve")
    plt.ylabel("Performance compared to native (%)")
    plt.show()


if __name__ == "__main__":
    for label, time_mean, time_stdev in DATA:
        print(f"{label}: {time_mean:.3f} ± {time_stdev:.3f}")

    plot_1()
    plot_2()
