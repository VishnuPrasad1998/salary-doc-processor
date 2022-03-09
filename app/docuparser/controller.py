import os, random
from flask import request
from flask import Response as flask_response
from flask import make_response
from app.response import Response
from app.status_constants import HttpStatusCode
from app.utils import file_service_util
from app.docuparser.delegates import DocuParserDelegate
from flask_restx import Namespace, Resource

api = Namespace("DocuParser", description="Namespace for Document Parser")

@api.route("/parse-data")
class DocuParserDetails(Resource):
    def post(self):
        payload = request.files
        if 'document_pdf' in payload:
            file = payload['document_pdf']
            data = DocuParserDelegate.parse_pdf_details(file)
            return Response.success(response_data=data,
                                    status_code=HttpStatusCode.OK, message="PDF details extracted and saved in DB")
