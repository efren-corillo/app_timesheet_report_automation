from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from app.models.User import User

class ReportsController(Controller):

    def generateWeeklyReport(self, request: Request, response: Response):
#         staff_users = User.where('type', 'staff').where('is_active', True).get()
#
#         staff_data = []
#         for user in staff_users:
#             staff_data.append(user)
        
        return response.json({
            'status': 'success',
            'message': 'Report generated successfully',
            'data': ['a','b','c']
            # 'data': [user.serialize() for user in staff_data]
        })
