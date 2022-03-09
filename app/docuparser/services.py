from app import response, mongo_db
from werkzeug.utils import secure_filename
import fitz
import random
import os
import json
import re
import pytz
from app.docparsercore.parser import PdfExtractor
from app.utils.mongo_encoder import format_cursor_obj
from bson.objectid import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from pymongo.message import query

class DocuParserService:
    @staticmethod
    def parse_pdf_details(file):
        file_name = 'sample{0}.pdf'.format(random.randint(1,5000))
        file.save(os.path.join('app/document-storage', file_name))
        pdf = PdfExtractor('app/document-storage/'+ file_name)
        val = pdf.extract_data_from_pdf()
        mongo_db.db.Docs.insert_one(val)
        bs = dumps(val, json_options=RELAXED_JSON_OPTIONS)
        response_data = format_cursor_obj(json.loads(bs))
        return response_data

    