from survey import AnonymousSurvey

def test_store_single_response():
    """Testa se uma única resposta está devidamente armazenada"""
    question = f"What language do you speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    question = f"What languages do you speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses