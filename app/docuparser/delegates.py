from app.docuparser.services import DocuParserService



class DocuParserDelegate:
    @staticmethod
    def parse_pdf_details(file):
        data = DocuParserService.parse_pdf_details(file)
        return data

       