import sys
import os

global WordlistName
clear = lambda: os.system('cls')
pause = lambda: os.system('pause')
SetColorGreen = lambda: os.system('color 0a')
WordlistName = 'brazilian.txt'

class caesar():
	def encode(string, key):
		string = string.lower()
		alf = 'abcdefghijklmnopqrstuvwxyz'
		out = ''
		for char in string:
			if alf.find(char) == -1:
				out += char
				continue
			pos = alf.find(char)+key
			if pos > 25:
				pos = pos - 26
			out += alf[pos]
		return out

	def decode(string, key):
		string = string.lower()
		alf = 'abcdefghijklmnopqrstuvwxyz'
		out = ''
		for char in string:
			if alf.find(char) == -1:
				out += char
				continue
			pos = alf.find(char)-key
			if pos < 0:
				pos += 26
			out += alf[pos]
		return out

	def find_words(wordsVector):
		counter = 0
		for word in wordsVector:
			counter += 1
			wordlist = open(WordlistName, 'r')
			for line in wordlist:
				ln = line.split()
				ln = caesar.filter(ln)
				if ln == word:
					return counter
			wordlist.close()
		return False

	def filter(strLine):
		line = ''
		for char in strLine:
			if char != "'" and char != '[' and char != ']':
				line += char
		return line

	def getFirst(phrase):
		space = False
		for char in phrase:
			if char == ' ':
				space = True
				break
		if space:
			word = ''
			for char in phrase:
				if char != ' ':
					word += char
				else:
					return word
		else:
			return phrase

	def brute_force(string):
		string = string.lower()
		wordsVector = []
		alf = 'abcdefghijklmnopqrstuvwxyz'
		for key in range(1,26):
			out = ''
			for char in string:
				if alf.find(char) == -1:
					out += char
					continue
				pos = alf.find(char)-key
				if pos < 0:
					pos += 26
				out += alf[pos]
			wordsVector.append(caesar.getFirst(out))
			if key > 9: 
				print('KEY{} - {}'.format(key, out))
			else:
				print('KEY0{} - {}'.format(key, out))
		print('\nBrute forcing...\n')
		flag = caesar.find_words(wordsVector)
		if flag != False:
			if flag > 9:
				print('Most likely match: KEY{} - '.format(flag), end='')
				print(caesar.decode(string, flag) + '\n\n')
			else:
				print('Most likely match: KEY0{} - '.format(flag), end='')
				print(caesar.decode(string, flag) + '\n\n')
		else:
			print('No Match! Try another wordlist...\n\n')

class limit():
	def key_verify(key):
		if key < 1 or key > 25:
			print('\nInvalid key!\n\n')
			pause()
			clear()
			limit.menu()
		else: pass

	def menu():
		print('\t Caesar Cipher Hack v2.0 by Cripto S.a\n')
		print(' [1] Encode\n [2] Decode\n [3] Brute Force\n [4] Exit\n')
		op = int(input(' Option: '))
		if op < 1 or op > 4:
			clear()
			limit.menu()
		if op == 1:
			clear()
			print('\t Encode\n')
			key = int(input('Key: '))
			limit.key_verify(key)
			ent = input('Input: ')
			encoded = caesar.encode(ent, key)
			clear()
			print('Encoded text:\n')
			print(encoded + '\n\n')
			pause()
			clear()
			limit.menu()
		elif op == 2:
			clear()
			print('\t Decode\n')
			key = int(input('Key: '))
			limit.key_verify(key)
			ent = input('Input: ')
			decoded = caesar.decode(ent, key)
			clear()
			print('Decoded text:\n')
			print(decoded + '\n\n')
			pause()
			clear()
			limit.menu()
		elif op == 3:
			clear()
			print('\t Brute Force\n')
			ent = input('Input: ')
			print('')
			caesar.brute_force(ent)
			pause()
			clear()
			limit.menu()
		elif op == 4:
			sys.exit()

SetColorGreen()
limit.menu()