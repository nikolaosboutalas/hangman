used_words = []
dictionary = ['Κρεμάλα','Μπουκάλι','Υπολογιστής','Ποντίκι','Πληκτρολόγιο','Καλώδιο','Εκτυπωτής','Βιβλίο','Τετράδιο','Αναπτήρας','Τσιγάρο','Κινητό','Άσπρο','Μαύρο','Πράσινο','Κόκκινο','Κίτρινο','Πόρτα','Παράθυρο','Γυαλιά','Μπλε','Πρόγραμμα','Τραπέζι','Καρέκλα','Κουζίνα','Σαλόνι','Υπνοδωμάτιο','Ψυγείο','Νεροχύτης','Κάδος','Σκουπίδια','Ανακύκλωση','Κοτόπουλο','Γουρούνι','Αρνί','Τσάι','Μήλο','Αχλάδι','Πορτοκάλι','Μανταρίνι','Ακουστικά','Μπαταρία','Φωτιστικό','Ζυγαριά','Μπλούζα','Παντελόνι','Παπούτσια','Κάλτσα','Ζακέτα','Κιθάρα']

def chooseWord(ls):
	"""Λαμβάνει για input μία λίστα και επιστρέφει τυχαία ένα στοιχείο της με τη χρήση της βιβλιοθήκης random."""
	import random
	index = random.randint(0,len(ls)-1)
	return ls[index] 

def startRound(names):
	"""Παίρνει ως όρισμα μία λίστα ονομάτων και καλεί την startGame για το κάθε όνομα μέχρι να βρεθεί νικητής ή να χάσουν όλοι.
	   Αν το μήκος της λίστας ειναι 0 τότε επιστρέφει None, αν το μήκος είναι 1 τότε επιστρέφει το μόνο όνομα στη λίστα,
	   αλλιώς καλεί την startRound με τους παίκτες που νίκησαν στον προηγούμενο γύρο.
	   Η λίστα used_words κάθε φορά που τελειώνει ο γύρος κρατάει τις λέξεις που χρησιμοποιήθηκαν σε αυτό τον γύρο."""
	global used_words
	if len(names) == 0:
		return None
	elif len(names) == 1:
		return names[0]
	else:
		next_names = []
		i=0
		while(i<len(names)):
			if(startGame(names[i])):
				next_names = next_names + [names[i]]
			i += 1
		while(len(used_words) - len(names) > 0):
			used_words.pop(0)
		return startRound(next_names)

def startGame(PlayerName):
	"""Λαμβάνει ως όρισμα το όνομα του παίκτη και επιστρέφει True αν ο παίκτης νικήσει και False αν όχι."""
	print('Όνομα Παίκτη: ' + PlayerName)
	lifes = choose_level()
	stages = draw(lifes)
	print('Υπενθύμιση: Έχεις περιθώριο να επιλέξεις μέχρι '+str(lifes - 1)+' λάθος γράμματα')
	print('            και το '+str(lifes)+'ο λάθος γράμμα σε βγάζει εκτός παιχνιδιού')
	global used_words
	Word = chooseWord(dictionary)
	while (Word in used_words):
		Word = chooseWord(dictionary)
	used_words += [Word]
	hidden_word = list(len(Word)*'_')
	win = False
	found_letters = 0
	found_letters_list = []
	while(lifes > 0 and win==False):
		print("")
		print('>Η λέξη που πρέπει να μαντέψεις είναι: ' + "".join(hidden_word))
		current_letter = input('> Δώσε γράμμα: ')
		while(isletter(current_letter.lower()) == False):
			print('Error - Δεν έδωσες γράμμα')
			current_letter = input('> Δώσε γράμμα: ')
		if((current_letter.lower() in Word) or (current_letter.upper() in Word)):
			if(not current_letter.lower() in found_letters_list):
				i=0
				while(i<len(Word)):
					if(Word[i] == current_letter.lower()):
						hidden_word[i] = current_letter.lower()
						found_letters += 1
					elif(Word[i] == current_letter.upper()):
						hidden_word[i] = current_letter.upper()
						found_letters += 1
					i += 1
				found_letters_list += [current_letter.lower()]
		else:
			lifes -= 1
			if(lifes > 0):
				print(stages.pop(0))
				print(">Έχεις ακόμα "+str(lifes)+" ζωές.")
			else:
				print(stages.pop(0))
				print("Η λέξη που ψάχναμε ήταν: “"+Word+"”")
		if(found_letters == len(Word)):
			win = True
	if win:
		print("Κέρδισες! Η λέξη ήταν: "+Word)
		return True
	else:
		return False


def isletter(letter):
	"""Ελέγχει εάν το γράμμα letter ανήκει στην Ελληνική αλφάβητο."""
	if letter in 'αβγδεζηθικλμνξοπρσςτυφχψωάέήίόύώ':
		return True
	else:
		return False

def choose_level():
	"""Ζητά ως είσοδο από τον χρήστη την επιλεγμένη του δυσκολία και επιστρέφει των αριθμό ζωών ανάλογα με την επιλογή του.
	Αν η είσοδος δεν είναι έγκυρη τότε ξανά καλεί τον εαυτό της."""
	choice = int(input("Διάλεξε δυσκολία: \n1. Αρχάριος \n2. Μέτριος \n3. Έμπειρος\n"))
	if choice == 1:
		return 8
	elif choice == 2:
		return 6
	elif choice == 3:
		return 4
	else:
		print("Error - Δεν έδωσες σωστή δυσκολία")
		return choose_level()

def draw(lives):
	"""Παίρνει ως όρισμα των αριθμό των ζωών του παίκτη και επιστρέφει μία λίστα με κάθε στοιχείο της το στάδιο της κρεμάλας που αντιστοιχεί στο επίπεδο δυσκολίας"""
	if(lives == 8):
		canvas = ['|---------|\n|         O\n|\n|\n|\n|\n|','|---------|\n|         O\n|         |\n|         |\n|\n|\n|','|---------|\n|         O\n|         |\\\n|         |\n|\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|         \\_\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|      ## ##\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|      ## ##\n|       fire']
	elif(lives == 6):
		canvas = ['|---------|\n|         O\n|\n|\n|\n|\n|','|---------|\n|         O\n|         |\n|         |\n|\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|      ## ##\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|      ## ##\n|       fire']
	else:
		canvas = ['|---------|\n|         O\n|         |\n|         |\n|\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|      ## ##\n|','|---------|\n|         O\n|        /|\\\n|         |\n|       _/\\_\n|      ## ##\n|       fire']
	return canvas

def Start():
	"""Εκκίνηση του παιχνιδιού"""
	print ("Εκκίνηση παιχνιδιού - Κρεμάλα")
	N = int(input('Αριθμός παικτών: '))
	i = 0
	names_list = []
	while(i<N):
		name = input(str(i+1) + ". Όνομα παίκτη: ")
		names_list = names_list + [name]
		i += 1
	winner = startRound(names_list)
	if winner:
		print("Το όνομα του νικητή είναι: " + winner)

Start()