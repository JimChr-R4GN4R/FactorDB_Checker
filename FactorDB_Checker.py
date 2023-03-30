from requests import get
import re
def factordb(n: int):
	"""
	n (int) - required: Number to be factored.
	"""
	
	try:
		int(n)
	except ValueError:
		return ValueError("n must be integer.")

	def FindNumberById(id):
		try:
			res = get(f'http://factordb.com/index.php?id={str(id)}').text
		except Exception as e:
			return e

		try:
			return int(re.findall(r'<input type="text" size=100 name="query" value="(.*)">\n<input type="submit" value="Factorize!">', res)[0])
		except ValueError:
			try:
				return simple_eval(re.findall(r'<input type="text" size=100 name="query" value="(.*)">\n<input type="submit" value="Factorize!">', res)[0].replace('^','**').replace('/','//'))
			except SyntaxError:
				return None
		return None
	
	try:
		res = get(f'http://factordb.com/index.php?query={str(n)}').text
	except Exception as e:
		return e

	factors = re.findall(r'"index\.php\?id=([0-9]*)">', res)

	if len(factors) == 0:
		return None
	elif (factors[0] == factors[1]):
		return [1,n]
	else:
		factors.pop(0)
		for i in range(len(factors)):
			factors[i] = FindNumberById(factors[i])
		return factors

while 1:
	n = input("Number: ")
	if n == "":
		break
	else:
		print(factordb(n))
