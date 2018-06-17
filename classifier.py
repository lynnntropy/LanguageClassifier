from japanese_wordlist_builder import JapaneseWordListBuilder
from korean_wordlist_builder import KoreanWordListBuilder

japanese_wordlist_builder = JapaneseWordListBuilder()
japanese_wordlist = japanese_wordlist_builder.build()

# print(japanese_wordlist)

korean_wordlist_builder = KoreanWordListBuilder()
korean_wordlist = korean_wordlist_builder.build()

# print(korean_wordlist)