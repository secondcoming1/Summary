from nlplogic.corenlp import get_phrases, get_text_blob, search_wikipedia, summarize_wikipedia

def test_get_phrases():
    assert 'golden state' in get_phrases('golden state warriors')
