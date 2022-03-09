def register_routes(api, app, root="api"):
    from .controller import api as docuparser_api
    api.add_namespace(docuparser_api, path=f"/v1")
