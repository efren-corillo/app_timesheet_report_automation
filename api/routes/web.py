from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.group([
        Route.get("/generate-weekly-report", "ReportsController@generateWeeklyReport"),
    ],
    prefix="/api",
    name="api.")
]
