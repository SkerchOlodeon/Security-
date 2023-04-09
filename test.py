print("Bienvenue au quizz des ports pour Security +!!")
print('Bonne chance!...tu vas en avoir de besoin :)')
score = 0
question_no = 0
playing = input('Es-tu pret? Oui ou non?').lower()
if playing == 'oui':
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du POP3?').lower()
    if ques == '110':
        score += 1
        print('Bien joué!')

    else:
        print('Mmmm tu dois réviser encore un peu plus...')
        print(f'La réponse est --> 110')

    # ------1
    question_no += 1
    ques = input(f'\n{question_no}. Quels sont les 2 ports du FTP? Syntaxe: X et Y').lower()

    if ques == '20 et 21':
        score += 1
        print('Bien joué!')

    else:
        print('Mmmm tu dois réviser encore un peu plus...')
        print(f'La réponse est --> 20 et 21')

    # -----2
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du SNMP et SNMP Trap? Syntaxe: X et Y ').lower()

    if ques == '161 et 162':
        score += 1
        print('Bien joué!')

    else:
        print('Mmmm tu dois réviser encore un peu plus...')
        print(f'La réponse est --> 161 et 162')

    # -----3
    question_no += 1
    ques = input(f'\n{question_no}. Quel sont les ports du LDAP et LDAPS? Syntaxe: X et Y ').lower()

    if ques == '389 et 636':
        score += 1
        print('Bien joué!')

    else:
        print('Mmmm tu dois réviser encore un peu plus...')
        print(f'La réponse est --> 389 et 636')

    # -----4
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du syslog? ').lower()

    if ques == '514':
        score += 1
        print('Bien joué!')

    else:
        print('Mmmm tu dois réviser encore un peu plus...')
        print(f'La réponse est --> 514')
        # -----5
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du L2TP? ').lower()

    if ques == '1701':
            score += 1
            print('Bien joué!')

    else:
            print('Mmmm tu dois réviser encore un peu plus...')
            print(f'La réponse est --> 1701')
            # -----6
            question_no += 1
            ques = input(f'\n{question_no}. Quels sont les ports du HTTP et HTTPS? Syntaxe: X et Y ').lower()

    if ques == '80 et 443':
                score += 1
                print('Bien joué!')

    else:
                print('Mmmm tu dois réviser encore un peu plus...')
                print(f'La réponse est --> 80 et 443')
                # -----7
    question_no += 1
    ques = input(f'\n{question_no}. Quels sont les ports du DHCP? ').lower()

    if ques == '67 et 68':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 67 et 68')
                # -----8
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du SSH? ').lower()

    if ques == '22':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 2')

                # -----9
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du SMTP? ').lower()

    if ques == '25':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 25')
                    # -----10
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du TACACS? ').lower()

    if ques == '49':
        score += 1
        print('Bien joué!')

    else:
        print('Mmmm tu dois réviser encore un peu plus...')
        print(f'La réponse est --> 49')
        # -----11
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du TELNET? ').lower()

    if ques == '23':
            score += 1
            print('Bien joué!')

    else:
            print('Mmmm tu dois réviser encore un peu plus...')
            print(f'La réponse est --> 23')

                # -----12
    question_no += 1
    ques = input(f'\n{question_no}. Quels sont les ports du DNS et DNSSEC? Syntaxe: X et Y ').lower()

    if ques == '53 et 53':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 53 et 53...ils utilisent les memes!')
                # -----13
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du Kerberos? ').lower()

    if ques == '88':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 88')
                # -----14
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du SCP? ').lower()

    if ques == '22':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 22')
                # -----15
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du RDP? ').lower()

    if ques == '3389':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 3389')
                # -----16
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du IPSec? ').lower()

    if ques == '500':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 500')
                # -----17
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du SFTP? ').lower()

    if ques == '22':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 22')
                # -----18
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du IMAP4 et IMAP4 Secure? Syntaxe X et Y ').lower()

    if ques == '143 et 993':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 143 et 993')
                # -----19
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du S/MIME? ').lower()

    if ques == '993':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 993')
                # -----20
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du SNMPV3 ').lower()

    if ques == '162':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 162')
                # -----21
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du PPTP? ').lower()

    if ques == '1723':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 1723')
                # -----22
    question_no += 1
    ques = input(f'\n{question_no}. Quel est le port du TFTP? ').lower()

    if ques == '69':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 69')
                # -----23
    question_no += 1
    ques = input(f'\n{question_no}. Quels sont les ports du POP 3 et POP3 Secure? Syntaxe: X et Y ').lower()

    if ques == '110 et 995':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 110 et 995')
                # -----24
    question_no += 1
    ques = input(f'\n{question_no}. Quels sont les ports du FTPS? ').lower()

    if ques == '989 et 990':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 989 et 990')
                # -----25
    question_no += 1
    ques = input(f'\n{question_no}. Quels sont les ports du SIP et SRTP? ').lower()

    if ques == '5060 et 5061':
                    score += 1
                    print('Bien joué!')

    else:
                    print('Mmmm tu dois réviser encore un peu plus...')
                    print(f'La réponse est --> 5060 et 5061')




else:
    print(f'Jai déja hate que tu sois pret...')
    quit()

print(f'\nLe nombre de question est {question_no}')
print(f'Ton score est {score}')
try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print('0% des questions sont bonnes')

print(f'{percentage}% des questions sont bonnes.')