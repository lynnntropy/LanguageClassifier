import json
from korean_romanizer.romanizer import Romanizer
from tqdm import tqdm

class KoreanWordListBuilder:
    DICTIONARY_LOCATION = 'dictionaries/kdict_dump.json'

    def build(self):

        word_list = []
        
        with open(self.DICTIONARY_LOCATION, encoding="utf-8") as f:
            data = json.load(f)

            print('Generating Korean word list.')
            
            for entry in tqdm(data, ncols=75, unit='entries'):
                try:
                    word_list.append(Romanizer(entry['word']).romanize())
                except TypeError:
                    pass
                except KeyError:
                    pass
                except AttributeError:
                    pass


        return word_list