#! python3
#randomQuizGenerator.py create quiz with question and answers in
# random order, along with the answer key

import random

capitals = { 'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#generate 35 quiz flies

for quizNum in range(35):
       #create the quiz and answer keys
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open ('captitalsquiz_aswers%s.txt' % (quizNum + 1) ,"w")

    #write out the header for the quiz
    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Forms %s)' % (quizNum + 1))
    quizFile.write('\n\n')


    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    #get right and wrong answers
    correctAnswer = capitals[states[quizNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    #write the question and the answer options to the quiz quiz file
    quizFile.write('{} What is the capital of {}?\n'.format( (quizNum + 1), (states[quizNum])))
    for i in range(4):
       quizFile.write('{}{}'.format('ABCD'[i], answerOptions[i]))

       quizFile.write("\n")

    # wite the answer key to a file
    answerKeyFile.write('{}{}\n'.format(quizNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
