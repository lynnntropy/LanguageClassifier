from japanese_wordlist_builder import JapaneseWordListBuilder
from korean_wordlist_builder import KoreanWordListBuilder
from alphabet_to_feature import get_sample_from_string
from tqdm import tqdm

from sklearn import svm
from sklearn.externals import joblib

import os.path

class ClassifierManager:
    
    TRAINING_SET_SIZE = 10000

    PERSISTED_CLASSIFIER_FILENAME = 'classifier.pkl'


    def build_new_classifier(self):

        japanese_wordlist_builder = JapaneseWordListBuilder()
        japanese_wordlist = japanese_wordlist_builder.build()

        korean_wordlist_builder = KoreanWordListBuilder()
        korean_wordlist = korean_wordlist_builder.build()
        
        japanese_training_set = japanese_wordlist[:self.TRAINING_SET_SIZE]
        korean_training_set = korean_wordlist[:self.TRAINING_SET_SIZE]

        training_samples = []
        training_labels = []

        print('\nGenerating training data.')

        for word in tqdm(japanese_training_set, ncols=75, unit='samples', desc='Japanese'):
            training_samples.append(get_sample_from_string(word))
            training_labels.append(0)

        for word in tqdm(korean_training_set, ncols=75, unit='samples', desc='Korean'):
            training_samples.append(get_sample_from_string(word))
            training_labels.append(1)

        print('\nTraining model.')

        classifier = svm.SVC(verbose=True)
        classifier.fit(training_samples, training_labels)

        self.persist_classifier(classifier)

        return classifier


    def persist_classifier(self, classifier):
        joblib.dump(classifier, self.PERSISTED_CLASSIFIER_FILENAME)


    def persisted_classifier_exists(self):  
        return os.path.isfile(self.PERSISTED_CLASSIFIER_FILENAME)


    def get_persisted_classifier(self):
        return joblib.load(self.PERSISTED_CLASSIFIER_FILENAME)