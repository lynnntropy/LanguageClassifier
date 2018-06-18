from alphabet_to_feature import get_sample_from_string

class ClassifierWrapper:

    CLASS_NAMES = {
        0: 'Japanese',
        1: 'Korean'
    }

    def __init__(self, classifier):
        self.classifier = classifier

    def classify(self, string):
        sample = get_sample_from_string(string)

        prediction_set = []
        prediction_set.append(sample)

        prediction = self.classifier.predict(prediction_set)

        return (self.CLASS_NAMES[prediction[0]])
