from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    single_determiner = ["a", "one", "the"]
    for _ in range(4):
        determiner = get_determiner(1)
        assert determiner in single_determiner

    plural_determiner = ["two", "some", "many", "the"]
    for _ in range(4):
        determiner = get_determiner(2)
        assert determiner in plural_determiner

def test_get_noun():
    single_noun = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_noun
    
    plural_noun = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        noun = get_noun(2)
        assert noun in plural_noun

def test_get_verb():
    present_verb_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, "present")
        assert verb in present_verb_singular

    present_verb_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        verb = get_verb(2, "present")
        assert verb in present_verb_plural

    past_verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(any , "past")
        assert verb in past_verb

    future_verb = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(any, "future")
        assert verb in future_verb

def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(4):
        prepositions = get_preposition()
        assert prepositions in preposition

def test_get_prepositional_phrase(): 
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    single_noun = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_noun = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    single_determiner = ["a", "one", "the"]
    plural_determiner = ["two", "some", "many", "the"]
    #str.split(get_prepositional_phrase)
    for _ in range(4):
        prep_phrase = get_prepositional_phrase(1)   #"about a car"
        words = prep_phrase.split(" ")    # words = ["about", "a", "car"]
        preposition = words[0]
        determiner = words[1]
        noun = words[2]
        assert preposition in prepositions
        assert determiner in single_determiner
        assert noun in single_noun
    for _ in range(4):
        prep_phrase = get_prepositional_phrase(2)   #"about a car"
        words = prep_phrase.split(" ")    # words = ["about", "a", "car"]
        preposition = words[0]
        determiner = words[1]
        noun = words[2]
        assert preposition in prepositions
        assert determiner in plural_determiner
        assert noun in plural_noun
    #return (get_preposition, get_noun, get_noun)

pytest.main(["-v", "--tb=line", "-rN", __file__])