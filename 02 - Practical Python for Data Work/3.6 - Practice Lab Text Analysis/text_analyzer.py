# ===== Part A: Definisi string & class TextAnalyzer =====

givenstring = (
    "Lorem ipsum dolor! diam amet, consetetur Lorem magna. "
    "sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
)


class TextAnalyzer(object):
    def __init__(self, text):
        # hapus tanda baca (titik, seru, koma, tanya)
        formatted_text = (
            text.replace(".", "").replace("!", "").replace(",", "").replace("?", "")
        )
        # ubah jadi lowercase
        formatted_text = formatted_text.lower()

        self.fmtText = formatted_text

    def freq_all(self):
        # pecah teks jadi list kata
        word_list = self.fmtText.split()

        # buat dictionary frekuensi kata
        freq_map = {}
        for word in set(word_list):  # set -> tiap kata unik dicek sekali saja
            freq_map[word] = word_list.count(word)

        return freq_map

    def freq_of(self, word):
        freq_map = self.freq_all()

        if word in freq_map:
            return freq_map[word]
        else:
            return 0


# ===== Part B: Panggil method-method TextAnalyzer =====

# Step 1: buat instance TextAnalyzer
analyzed = TextAnalyzer(givenstring)

# Step 2: lihat teks yang sudah diformat (lowercase, tanpa tanda baca)
print("Formatted Text:", analyzed.fmtText)

# Step 3: hitung frekuensi SEMUA kata unik
freq_map = analyzed.freq_all()
print(freq_map)

# Step 4: hitung frekuensi kata tertentu ("lorem")
word = "lorem"
frequency = analyzed.freq_of(word)
print("The word", word, "appears", frequency, "times.")
