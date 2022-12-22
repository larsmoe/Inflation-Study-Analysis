import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fs =20

otree_csv_path = 'Data/oTree_data.csv'
df_otree = pd.read_csv(otree_csv_path, sep= ',')
df_otree = df_otree[df_otree['session.code'] == '7ymv81x6']
df_otree = df_otree[df_otree['participant._current_page_name'].str.len() > 0]
simplify_dict = {'Closing_failed': 'Endseite - nicht bestanden', 'Closing_passed': 'Endseite - bestanden',
                 'Infl_calc_treatment': 'Inflationsrechner (Seite 4)', 'Infl_calc_control': 'Inflationsrechner (Seite 4)',
                 'Introduction': 'Einführung (Seite 1)', 'Demographics': 'Demographics (Seite 2)',
                 'attch': 'Attention Checks (Seite 6)', 'Likert1': 'Fragen (Seite 7)', 'Likert3': 'Fragen (Seite 9)',
                 'Likert5': 'Fragen (Seite 11)', 'Instructions': 'Instructions (Seite 3)'}
df_otree['endpage_simple'] = df_otree['participant._current_page_name'].map(simplify_dict)
#df_otree['participant._current_page_name'].value_counts().plot(kind='bar')
#df_otree['endpage_simple'].value_counts().plot(kind='bar')
df_failed_user = df_otree[df_otree['endpage_simple'] == 'Endseite - nicht bestanden']
print(df_failed_user)
yesno_questions = ['Persönliche Inflationsrate', 'Amtliche Inflationsrate', 'Inflationsvergleich zum Vorjahr', 'Leitzins',
                   'Spielzeug als Güterbereich', 'Nahrungsmittel als Güterbereich', 'Kaufempfehlungen']
all_questions = ['Persönliche Inflationsrate', 'Amtliche Inflationsrate', 'Inflationsvergleich zum Vorjahr', 'Leitzins',
                   'Spielzeug als Güterbereich', 'Nahrungsmittel als Güterbereich', 'Kaufempfehlungen',
                  'Leitzins verstehen', 'Berechnung Pers. Inflationsrate']
false_answer = [2, 2, 1, 1, 1, 2, 1]
for i, el in enumerate(yesno_questions):
    df_failed_user[el] = df_failed_user[f'survey_part_2.1.player.att{i+1}'] == false_answer[i]
df_failed_user['Leitzins verstehen'] = df_failed_user['survey_part_2.1.player.att8'] >= 4
df_failed_user['Berechnung Pers. Inflationsrate'] = df_failed_user['survey_part_2.1.player.att9'] <= 2
df_failed_user['num_of_false_yesno_questions'] = df_failed_user[yesno_questions].sum(axis=1)
df_failed_user['at_least_one_false_yes_no_question'] = df_failed_user['num_of_false_yesno_questions'] >= 1
df_failed_user['num_of_total_false_questions'] = df_failed_user[all_questions].sum(axis=1)
bins = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
df_failed_user['num_of_total_false_questions'].hist(bins=bins)
df_failed_user['at_least_one_false_yesno_question'] = df_failed_user['num_of_false_yesno_questions'] >=1
num_of_false_answered_questions = np.array(df_failed_user['num_of_total_false_questions'])
x = np.array(df_failed_user['num_of_false_yesno_questions'])
print(np.min(x), np.max(x))
fig1, ax1 = plt.subplots()
counts, edges, bars = plt.hist(num_of_false_answered_questions, bins=bins, rwidth=0.8, color='k')
#plt.xlabel('', size=fs)
plt.ylabel('Anzahl nicht bestande Attetion Checks', size=fs)
plt.xticks(np.arange(0, 11, 1.0))
ax1.tick_params(axis='both', labelsize=25)
plt.bar_label(bars, size=18)
plt.title(f'Anzahl der nicht bestandenen Attention Checks bei allen allen {np.sum(counts)} Teilnehmern, die nicht bestanden haben', size=fs)

####PLOT 2 - ANZAHL Personen die pro Kategorie rausgeflogen sind###

persons_failed_yesno_question = np.sum(np.array(df_failed_user['at_least_one_false_yesno_question']))
persons_failed_leitzins = np.sum(np.array(df_failed_user['Leitzins verstehen']))
persons_failed_calc_pers_infl = np.sum(np.array(df_failed_user['Berechnung Pers. Inflationsrate']))
height = np.array([persons_failed_yesno_question, persons_failed_leitzins, persons_failed_calc_pers_infl])



###PLOT 3 - Einzelne Fragen Personen durchgefallen###

height = np.zeros(len(all_questions))
for i in range(len(height)):
    height[i] = np.sum(np.array(df_failed_user[all_questions[i]]))

print(height)
fig3, ax3 = plt.subplots()
x_ticks = np.arange(0, len(height), 1.0)
plt.bar(x=x_ticks, height=height, width=0.8, color='k')
#plt.xlabel('', size=fs)
plt.ylabel('Anzahl Personen', size=fs)
plt.xticks(x_ticks, labels=all_questions, rotation=25,
           ha='right')
ax3.tick_params(axis='both', labelsize=18)
#ax2.bar_label(height, size=18)
plt.title(f'Anzahl der Personen, die durch einzelne Fragen geflogen sind', size=fs)
#print(df_failed_user)
plt.show()