def shellSort(arr, sequence, sequence_name):
    n = len(arr)
    for gap in sequence:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        print("SEQ=" + sequence_name)
        print(" ".join(map(str, arr)))
        print("INCR=" + str(gap))


def main():
    with open("entrada2.txt", "r") as input_file, open(
        "saida2.txt", "w"
    ) as output_file:
        for line in input_file:
            numbers = list(map(int, line.strip().split()))
            n = numbers[0]
            arr = numbers[1:]

            # Sequência SHELL(potências de 2)
            shell_sequence = [
                1,
                2,
                4,
                8,
                16,
                32,
                64,
                128,
                256,
                512,
                1024,
                2048,
                4096,
                8192,
                16384,
                32768,
                65536,
                131072,
                262144,
                524288,
                1048576,
            ]
            shellSort(arr, shell_sequence, "SHELL")

            # Sequência KNUTH
            knuth_sequence = [
                1,
                4,
                13,
                40,
                121,
                364,
                1093,
                3280,
                9841,
                29524,
                88573,
                265720,
                797161,
                2391484,
            ]
            shellSort(arr, knuth_sequence, "KNUTH")

            # Sequência CIURA
            ciura_sequence = [
                1,
                4,
                10,
                23,
                57,
                132,
                301,
                701,
                1577,
                3548,
                7983,
                17961,
                40412,
                90927,
                204585,
                460316,
                1035711,
            ]
            shellSort(arr, ciura_sequence, "CIURA")

            output_file.write(f"{n} {' '.join(map(str, arr))}\n")


if __name__ == "__main__":
    main()
