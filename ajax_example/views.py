from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.core import serializers

from models import city_info, Orders


def page_render(request, template):
	"""return page"""
	return render(request, template, {})


def ajax_math_responce(request, type):
	if request.is_ajax() and request.method == 'POST':
		result = 0
		if type == 'sum':
			result = float(request.POST.get('first_operand')) + float(request.POST.get('second_operand'))
		elif type == 'dif':
			data = request.POST.get('data').split('&')
			result = float(data[1][14:len(data[1])]) - float(data[2][15:-1])
		elif type == 'mult':
			result = float(request.POST.get('first_operand')) / float(request.POST.get('second_operand'))
		elif type == 'div':
			result = float(request.POST.get('first_operand')) * float(request.POST.get('second_operand'))
		return  HttpResponse(result)
	else:
	 	raise Http404('Not found')


def ajax_data_base_responce(request):
	return JsonResponse(serializers.serialize('json', city_info.objects.all()), safe=False)


def ajax_sort_responce_first(request):
	if request.is_ajax() and request.method == 'GET':
		if 'startValue' in request.GET and 'endValue' in request.GET:
			start_value = int(request.GET.get('startValue'))
			end_value = int(request.GET.get('endValue'))
			return JsonResponse(serializers.serialize('json', city_info.objects.all()[start_value:end_value]), safe=False)
		else:
			raise Http404('Not found')
	else:
		raise Http404('Not found')


def ajax_sort_responce_second(request):
	if request.is_ajax() and request.method == 'GET':
		if 'customersName' in request.GET:
			customers_name = request.GET.get('customersName')
			customers_data = None
			if customers_name == 'all':
				customers_data = serializers.serialize('json', Orders.objects.order_by('orders_customer'))
			else:
				customers_data = serializers.serialize('json', Orders.objects.filter(orders_customer=customers_name))
			return JsonResponse(customers_data, safe=False)
		else:
			raise Http404('Not found')
	else:
		raise Http404('Not found')


def ajax_sort_responce_third(request):
	if request.is_ajax() and request.method == 'GET':
		return HttpResponse(0)