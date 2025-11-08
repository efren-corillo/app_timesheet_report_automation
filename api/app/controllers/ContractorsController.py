from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response


class ContractorsController(Controller):
    def getContractors(self):
        return {"status": 200, "message": "contractors"}
