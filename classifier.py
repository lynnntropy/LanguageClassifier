from classifier_manager import ClassifierManager
from classifier_wrapper import ClassifierWrapper

classifier_manager = ClassifierManager()

if classifier_manager.persisted_classifier_exists():

    print('An existing classifier is available. Load it (y/n)?')
    answer = input('> ')

    if answer == 'y':
        classifier = classifier_manager.get_persisted_classifier()
    else: 
        classifier = classifier_manager.build_new_classifier()
else:
    classifier = classifier_manager.build_new_classifier()

classifier_wrapper = ClassifierWrapper(classifier)

print('Enter a word in romanized form to guess the language.')

while True:
    word = input('> ')
    print(classifier_wrapper.classify(word))
