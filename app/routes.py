def register_routes(api, app, root="api"):

    from app.docuparser import register_routes
    register_routes(api, app)
    

