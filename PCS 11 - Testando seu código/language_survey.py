from survey import AnonymousSurvey

# Define uma pergunta e faz uma pesquisa
question = f"What language do you speak?"
language_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena respostas
language_survey.show_question()
print(f"Enter 'q' any time to quit.\n")
while True:
    response = input(f"Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Mostra os resultados da pesquisa
print(f"\nThnak you to everyone who participated at the survey!")
language_survey.show_results()