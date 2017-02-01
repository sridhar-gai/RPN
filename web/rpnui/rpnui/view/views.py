from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from business.main import RPNCalculator
from utils import ERROR_MAP, HELP_TEXT, NOT_A_VALID_OPERATOR, INVALID_EXPRESSION_ERROR
import json


class CalculatePageView(View):
    def get(self, request):
        response = render(request, 'calculate.html', {'help_text': HELP_TEXT})
        return response

    def post(self, request):
        expression = request.POST.get('expression', '')
        result = RPNCalculator(expression).evaluate_rpn()
        has_errors = result in ERROR_MAP
        response_data = {'result': result if not has_errors else ERROR_MAP[result], 'has_errors': has_errors,
                         'is_expression_valid': not (has_errors and
                                                     result in (NOT_A_VALID_OPERATOR, INVALID_EXPRESSION_ERROR))}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
