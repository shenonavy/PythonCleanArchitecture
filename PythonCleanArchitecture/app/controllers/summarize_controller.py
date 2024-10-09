
from flask import request
from app.controllers import router
from app.services.summarize_service import SummarizeService

summarize_service = SummarizeService()

@router.route('/api/summarize', methods=['post'])
def get_summery():
    req_data = request.get_json()
    text = req_data['paragraph']
    summery = summarize_service.get_summery(text)
    return summery