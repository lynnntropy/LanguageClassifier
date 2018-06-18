import xml.etree.ElementTree
import romkan
from tqdm import tqdm

class JapaneseWordListBuilder:
    DICTIONARY_LOCATION = 'dictionaries/JMdict_e'

    def build(self):

        word_list = []

        dictionary_root_node = xml.etree.ElementTree.parse(self.DICTIONARY_LOCATION).getroot()

        print('\nGenerating Japanese word list.')

        for entry in tqdm(dictionary_root_node.findall('entry'), ncols=75, unit='entries'):
            try: 
                reading = entry.find('.//r_ele/reb').text
                reading_romanized = romkan.to_hepburn(reading)
                word_list.append(reading_romanized)
            except AttributeError:
                pass

        return word_list