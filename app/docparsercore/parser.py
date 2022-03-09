import fitz

class PdfExtractor:
	def __init__(self, urlpath):
		self.urlpath = urlpath		
		
	def extract_data_from_pdf(self):
		txt = []
		result_dict = {}
		keywords = ["Name", "Employee Code", "Designation", "PAN", "Basic Pay", "DA", 
			"Bonus", "House Rent", "Transport Allowance", "Performance Allowance", "Total Earnings",
			"Payslip"]
			
		with fitz.open(self.urlpath) as doc:        
			page = doc[0]
			text = page.get_text("text")
			text = text.split('\n')
			txt = list(text)
			for keyword in keywords:
				try:
					ix = txt.index(keyword)
				except:
					keyword = keyword + ":"
				ix = txt.index(keyword)
				ox = ix + 1
				result_dict.update({txt[ix].replace(":",""): txt[ox]})
				if 'Payslip' in result_dict:
					result_dict['Month and Year'] = result_dict.pop('Payslip')
			return result_dict

