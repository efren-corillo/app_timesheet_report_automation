from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.group([
        Route.get("/generate-weekly-report", "ReportsController@generateWeeklyReport"),
        Route.get("/get-contractors", "ContractorsController@getContractors"),
    ],
    prefix="/api",
    name="api.")
]
