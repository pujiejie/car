from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Yezhu
from drf_yasg.utils import swagger_auto_schema, APIView

class Owner(APIView):

	@swagger_auto_schema(tags=['my'], operation_description="获取所有业主信息")
	def get(self, request):
		all_owner = Yezhu.objects.all()
		result = []
		for owner in all_owner:
			result.append({
				"id": owner.id,
				"name": owner.full_name,
				"room": owner.h_number,
				"phone": owner.phone_number,
				"cars": list(owner.license_set.all().values()),
				"create_time": owner.create_time,
				"update_time": owner.update_time
			})
		return JsonResponse(result, safe=False)
