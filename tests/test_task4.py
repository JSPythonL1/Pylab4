from src.task4 import spam_generator

def test_spam_generator():
    assert list(spam_generator()) == ['s', 'sp', 'spa', 'spam']
