import re
txt = 'I love to teach python and javaScript'
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
match = re.match('I love to teach python',txt,re.I)
print(match)
span = match.span()
start,end = span
substring = txt[start:end]
print(substring)

txt_1 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_1 = re.search('first',txt_1,re.I)
span_1 = match_1.span()
start_1,end_1 = span_1
substring_1 = txt_1[start_1:end_1]
print(substring_1)
matches = re.findall('language',txt_1,re.I)
print(matches)

txt_2 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_2 = re.findall('python',txt_2,re.I)
print(match_2)

txt_3 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_3 = re.findall('python|Python',txt_3)
print(match_3)

txt_4 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_4 = re.findall('[pP]ython',txt_4)
print(match_4)

txt_5 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_5 = re.sub('[pP]ython','Javscript',txt_5)
print(match_5)

txt_6 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
match_6 = re.sub('%','',txt_6)
print(match_6)

# Writing RegEx Patterns
regex_pattern_1 = r'[Aa]pple|[Bb]anana'
txt_8 = '''Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'''
match_8 = re.findall(regex_pattern_1,txt_8)
print(match_8)

# Writing RegEx Patterns
regex_pattern_2 = r'\d'
txt_9 = '''AThis regular expression example was made on December 6,  2019 and revised on July 8, 2021'''
match_9 = re.findall(regex_pattern_2,txt_9)
print(match_9)

# Writing RegEx Patterns
regex_pattern_3 = r'\d+'
txt_10 = '''AThis regular expression example was made on December 6,  2019 and revised on July 8, 2021'''
match_10 = re.findall(regex_pattern_3,txt_10)
print(match_10)

# Writing RegEx Patterns
regex_pattern_4 = r'[Ee]-?mail'
txt_11 = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
match_11 = re.findall(regex_pattern_4,txt_11)
print(match_11)

# Writing RegEx Patterns
regex_pattern_5 = r'\d{4}'
txt_12 = '''A This regular expression example was made on December 6,  2019 and revised on July 8, 2021'''
match_12 = re.findall(regex_pattern_5,txt_12)
print(match_12)

# Writing RegEx Patterns
regex_pattern_6 = r'\d{1,4}'
txt_13 = '''A This regular expression example was made on December 6,  2019 and revised on July 8, 2021'''
match_14 = re.findall(regex_pattern_6,txt_12)
print(match_14)

# Writing RegEx Patterns
regex_pattern_7 = r'^This'
txt_14 = '''This regular expression example was made on December 6,  2019 and revised on July 8, 2021'''
match_15 = re.findall(regex_pattern_7,txt_14)
print(match_15)