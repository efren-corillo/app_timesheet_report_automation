from masonite.routes import RouteGroup, Route

ROUTES = RouteGroup([
    # API routes will be added here
    Route.get("/generate-weekly-report", "ReportsController@generateReport"),
], prefix="/api")