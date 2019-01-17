#LEARN THE COUNTRIES AND CAPITALS OF THE WORLD
#TRISTAN PRICE COPYRIGHT 2019 PYTHON 2.7.15
import random
from colors import *
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Democratic Republic of the Congo',
    'Republic of the Congo',
    'Costa Rica',
    'Cote d\'Ivoire',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Kosovo',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Korea',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Korea',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States of America',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
answers = {
    'Afghanistan':'Kabul',
    'Albania':'Tirana',
    'Algeria':'Algiers',
    'Andorra':'Andorra la Vella',
    'Angola':'Luanda',
    'Antigua and Barbuda':'Saint John\'s',
    'Argentina':'Buenos Aires',
    'Armenia':'Yerevan',
    'Australia':'Canberra',
    'Austria':'Vienna',
    'Azerbaijan':'Baku',
    'Bahamas':'Nassau',
    'Bahrain':'Manama',
    'Bangladesh':'Dhaka',
    'Barbados':'Bridgetown',
    'Belarus':'Minsk',
    'Belgium':'Brussels',
    'Belize':'Belmopan',
    'Benin':'Porto-Novo',
    'Bhutan':'Thimphu',
    'Bolivia':'Sucre',
    'Bosnia and Herzegovina':'Sarajevo',
    'Botswana':'Gaborone',
    'Brazil':'Brasilia',
    'Brunei':'Bandar Seri Begawan',
    'Bulgaria':'Sofia',
    'Burkina Faso':'Ouagadougou',
    'Burundi':'Bujumbura',
    'Cabo Verde':'Praia',
    'Cambodia':'Phnom Penh',
    'Cameroon':'Yaounde',
    'Canada':'Ottawa',
    'Central African Republic':'Bangui',
    'Chad':'N\'Djamena',
    'Chile':'Santiago',
    'China':'Beijing',
    'Colombia':'Bogota',
    'Comoros':'Moroni',
    'Democratic Republic of the Congo':'Kinshasa',
    'Republic of the Congo':'Brazzaville',
    'Costa Rica':'San Jose',
    'Cote d\'Ivoire':'Yamoussoukro',
    'Croatia':'Zagreb',
    'Cuba':'Havana',
    'Cyprus':'Nicosia',
    'Czech Republic':'Prague',
    'Denmark':'Copenhagen',
    'Djibouti':'Djibouti',
    'Dominica':'Roseau',
    'Dominican Republic':'Santo Domingo',
    'Ecuador':'Quito',
    'Egypt':'Cairo',
    'El Salvador':'San Salvador',
    'Equatorial Guinea':'Malabo',
    'Eritrea':'Asmara',
    'Estonia':'Tallinn',
    'Eswatini':'Mbabane',
    'Ethiopia':'Addis Ababa',
    'Fiji':'Suva',
    'Finland':'Helsinki',
    'France':'Paris',
    'Gabon':'Libreville',
    'Gambia':'Banjul',
    'Georgia':'Tbilisi',
    'Germany':'Berlin',
    'Ghana':'Accra',
    'Greece':'Athens',
    'Grenada':'Saint George\'s',
    'Guatemala':'Guatemala City',
    'Guinea':'Conakry',
    'Guinea-Bissau':'Bissau',
    'Guyana':'Georgetown',
    'Haiti':'Port-au-Prince',
    'Honduras':'Tegucigalpa',
    'Hungary':'Budapest',
    'Iceland':'Reykjavik',
    'India':'New Delhi',
    'Indonesia':'Jakarta',
    'Iran':'Tehran',
    'Iraq':'Baghdad',
    'Ireland':'Dublin',
    'Israel':'Jerusalem',
    'Italy':'Rome',
    'Jamaica':'Kingston',
    'Japan':'Tokyo',
    'Jordan':'Amman',
    'Kazakhstan':'Astana',
    'Kenya':'Nairobi',
    'Kiribati':'Tarawa',
    'Kosovo':'Pristina',
    'Kuwait':'Kuwait City',
    'Kyrgyzstan':'Bishkek',
    'Laos':'Vientiane',
    'Latvia':'Riga',
    'Lebanon':'Beirut',
    'Lesotho':'Maseru',
    'Liberia':'Monrovia',
    'Libya':'Tripoli',
    'Liechtenstein':'Vaduz',
    'Lithuania':'Vilnius',
    'Luxembourg':'Luxembourg',
    'Macedonia':'Skopje',
    'Madagascar':'Antananarivo',
    'Malawi':'Lilongwe',
    'Malaysia':'Kuala Lumpur',
    'Maldives':'Male',
    'Mali':'Bamako',
    'Malta':'Valletta',
    'Marshall Islands':'Majuro',
    'Mauritania':'Nouakchott',
    'Mauritius':'Port Louis',
    'Mexico':'Mexico City',
    'Micronesia':'Palikir',
    'Moldova':'Chisinau',
    'Monaco':'Monaco',
    'Mongolia':'Ulaanbaatar',
    'Montenegro':'Podgorica',
    'Morocco':'Rabat',
    'Mozambique':'Maputo',
    'Myanmar':'Naypyidaw',
    'Namibia':'Windhoek',
    'Nauru':'Yaren District',
    'Nepal':'Kathmandu',
    'Netherlands':'Amsterdam',
    'New Zealand':'Wellington',
    'Nicaragua':'Managua',
    'Niger':'Niamey',
    'Nigeria':'Abuja',
    'North Korea':'Pyongyang',
    'Norway':'Oslo',
    'Oman':'Muscat',
    'Pakistan':'Islamabad',
    'Palau':'Ngerulmud',
    'Palestine':'East Jerusalem',
    'Panama':'Panama City',
    'Papua New Guinea':'Port Moresby',
    'Paraguay':'Asuncion',
    'Peru':'Lima',
    'Philippines':'Manila',
    'Poland':'Warsaw',
    'Portugal':'Lisbon',
    'Qatar':'Doha',
    'Romania':'Bucharest',
    'Russia':'Moscow',
    'Rwanda':'Kigali',
    'Saint Kitts and Nevis':'Basseterre',
    'Saint Lucia':'Castries',
    'Saint Vincent and the Grenadines':'Kingstown',
    'Samoa':'Apia',
    'San Marino':'San Marino',
    'Sao Tome and Principe':'Sao Tome',
    'Saudi Arabia':'Riyadh',
    'Senegal':'Dakar',
    'Serbia':'Belgrade',
    'Seychelles':'Victoria',
    'Sierra Leone':'Freetown',
    'Singapore':'Singapore',
    'Slovakia':'Bratislava',
    'Slovenia':'Ljubljana',
    'Solomon Islands':'Honiara',
    'Somalia':'Mogadishu',
    'South Africa':'Pretoria',
    'South Korea':'Seoul',
    'South Sudan':'Juba',
    'Spain':'Madrid',
    'Sri Lanka':'Sri Jayawardenepura Kotte',
    'Sudan':'Khartoum',
    'Suriname':'Paramaribo',
    'Sweden':'Stockholm',
    'Switzerland':'Bern',
    'Syria':'Damascus',
    'Taiwan':'Taipei',
    'Tajikistan':'Dushanbe',
    'Tanzania':'Dodoma',
    'Thailand':'Bangkok',
    'Timor-Leste':'Dili',
    'Togo':'Lome',
    'Tonga':'Nuku\'alofa',
    'Trinidad and Tobago':'Port of Spain',
    'Tunisia':'Tunis',
    'Turkey':'Ankara',
    'Turkmenistan':'Ashgabat',
    'Tuvalu':'Funafuti',
    'Uganda':'Kampala',
    'Ukraine':'Kiev',
    'United Arab Emirates':'Abu Dhabi',
    'United Kingdom':'London',
    'United States of America':'Washington, D.C.',
    'Uruguay':'Montevideo',
    'Uzbekistan':'Tashkent',
    'Vanuatu':'Port Vila',
    'Vatican City':'Vatican City',
    'Venezuela':'Caracas',
    'Vietnam':'Hanoi',
    'Yemen':'Sana\'a',
    'Zambia':'Lusaka',
    'Zimbabwe':'Harare',
}
versioning = ['1.6.2.032.190116-ANSI.0']
build = ['007']
date = ['190117']
print '\nWelcome to LEARN.PY. Here you can learn the countries and capitals of the world! Type \'end\' to end the program. Type \'all\' to see the technical data for this program. Let\s get started.\n'
right = 0
wrong = 0
total = right + wrong
def get_key(val):
    for key, value in answers.items():
        if val == value:
            return key
def c_w_r(right, wrong):
    return green('%s/%s' % (right, wrong))
def c_w_w(right, wrong):
    return red('%s/%s' % (right, wrong))
def perc(right, wrong):
    return '%.2f' % (100.00 / float(total) * float(right))
choose = raw_input('Answer with the countries or capitals? (1 or 2): ')
if choose == 'all':
    print '\nVersion %s.%s.%s' % (versioning[-1], build[-1], date[-1])
    print 'Tristan Price and Gabriel Swan.'
    print 'Copyright 2019 Apache 2.0 license.'
    print 'Python 2.7.15'
elif choose == '2':
	while True:
		n = random.randint(0, 196)
		print '\n\n'
		print 'What is the capital of the country %s?' % blue((get_key(answers.get(countries[n]))))
		ans = raw_input()
		if ans.lower() == 'end':
			exit()
		elif ans.lower() == answers.get(countries[n]).lower():
			print green('\nCORRECT')
			right += 1
			total = right + wrong
			print c_w_r(right, total)
			print blue('%s' % (str(perc(right, wrong))) + '%\n')
		else:
			print red('\nWRONG. ' + answers.get(countries[n]))
			wrong += 1
			total = right + wrong
			print c_w_w(right, total)
			print blue('%s' % (str(perc(right, wrong))) + '%\n')
elif choose == '1':
	while True:
		n = random.randint(0, 196)
		print '\n\n'
		print 'Which country has the capital %s?\n\n' % blue((answers.get(countries[n])))
		ans = raw_input()
		if ans.lower() == 'end':
			exit()
		elif ans.lower() == get_key(answers.get(countries[n])).lower():
			print green('\nCORRECT')
			right += 1
			total = right + wrong
			print c_w_r(right, total)
			print blue('%s' % (str(perc(right, wrong))) + '%\n')
		else:
			print red('\nWRONG. ' + get_key(answers.get(countries[n])))
			wrong += 1
			total = right + wrong
			print c_w_w(right, total)
			print blue('%s' % (str(perc(right, wrong))) + '%\n')
else:
	print 'Um'
	exit()
