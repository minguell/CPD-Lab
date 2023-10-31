def radix_sort_msd(arr):
    if len(arr) <= 1:
        return arr

    def key_at(s, d):
        if d < len(s):
            return ord(s[d])
        return -1


def counting_sort(arr, d):
    max_key = max(key_at(s, d) for s in arr)
    count = [0] * (max_key + 2)
    output = [""] * len(arr)

    for s in arr:
        count[key_at(s, d) + 1] += 1

    for i in range(1, max_key + 2):
        count[i] += count[i - 1]

    for s in arr:
        output[count[key_at(s, d)]] = s
        count[key_at(s, d)] += 1

    return output

    def sort(arr, lo, hi, d):
        if hi <= lo:
            return
        aux = counting_sort(arr[lo:hi], d)
        arr[lo:hi] = aux

        for i in range(1, len(aux)):
            if key_at(aux[i], d) == key_at(aux[i - 1], d):
                continue
            sort(arr, lo + i, lo + i + (hi - lo), d + 1)

    sort(arr, 0, len(arr), 0)


# Função para ler um arquivo de texto e retornar uma lista de strings
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().split()


# Função para contar as ocorrências de palavras em uma lista de strings
def count_words(strings):
    word_count = {}
    for word in strings:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


# Função para gerar arquivos de texto a partir de um dicionário de palavras e contagens
def write_word_counts(word_count, output_file):
    with open(output_file, "w") as file:
        for word, count in word_count.items():
            file.write(f"{word} {count}\n")


# Leitura do arquivo de entrada
input_file = "frankenstein.txt"
words = read_file(input_file)

# Ordenação das palavras usando Radix Sort MSD
radix_sort_msd(words)

# Geração do arquivo de palavras ordenadas
output_file = "frankenstein_sorted.txt"
with open(output_file, "w") as file:
    for word in words:
        file.write(f"{word}\n")

# Contagem das palavras
word_count = count_words(words)

# Geração do arquivo de contagem das palavras
count_file = "frankenstein_counted.txt"
write_word_counts(word_count, count_file)
