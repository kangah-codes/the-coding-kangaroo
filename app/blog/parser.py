"""
Parser for taking text and returning html

So for instance a text like:
	!h1{Hello world} will return <h1>Hello world</>
	!img{hello.png} will return <img src="hello.png">

"""
import re
from re import split

class Parser:
	"""
	Class for all objects to be oarsed
	"""
	def __init__(self, text):
		self.text = text
		self.length = len(self.text)

	def parse_headings(self, text):
		#return re.sub(r'!(h\d){(.+)}', r'<\1>\2</\1>', text)
		try:
			# replacing all text with this pattern in the main string
			self.text = re.sub(r'!(h\d){(.+)}', r'<\1>\2</\1>', text)
		except Exception as e:
			return False
		else:
			return True

	def parse_paragraphs(self, text):
		#return re.sub(r'!p{(.+)}', r'<p>\1</p>', text)
		try:
			# replacing all text with this pattern in the main string
			self.text = re.sub(r'!p{(.+)}', r'<p>\1</p>', text)
		except Exception as e:
			return False
		else:
			return True


	def parse_quotes(self, text):
		#return re.sub(r'!quote_(h\d){(.+)}', r'<blockquote><\1>\2</\1></blockquote>', text)
		try:
			# replacing all text with this pattern in the main string
			self.text = re.sub(r'!quote_(h\d){(.+)}', r'<blockquote><\1>\2</\1></blockquote>', text)
		except Exception as e:
			return False
		else:
			return True

	def parse_tables(self, text):
		#return re.sub(r'!table_(th{.*}){.}', r'lol', text)
		try:
			# replacing all text with this pattern in the main string
			self.text = re.sub(r'!table_(th{.*}){.}', r'lol', text)
		except Exception as e:
			return False
		else:
			return True

	def parse_lists(self, text, typeof):
		pass

	def parse_images(self, text):
		#return re.sub(r'!img{(.+)}', r'<img src="\1">', text)
		try:
			# replacing all text with this pattern in the main string
			self.text = re.sub(r'!img{(.+)}', r'<img src="\1">', text)
		except Exception as e:
			return False
		else:
			return True

	def parse_links(self, text, make_bold=True):
		try:
			# replacing all text with this pattern in the main string
			if make_bold:
				self.text = re.sub(r'!link{(.+)}{(.+)}', r'<b><a href="\1">\2</a></b>', text)
			else:
				self.text = re.sub(r'!link{(.+)}{(.+)}', r'<a href="\1">\2</a>', text)
		except Exception as e:
			return False
		else:
			return True

	def __repr__(self):
		return f"""
			Parser object with text {self.text}
			Parsed headings {self.parse_headings(self.text)}
			Parsed Paragraphs {self.parse_paragraphs(self.text)}
			Parsed quotes {self.parse_quotes(self.text)}
		"""
							
