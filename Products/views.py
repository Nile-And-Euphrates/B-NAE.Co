from django.shortcuts import render
from rest_framework.decorators  import api_view
from django.http.response import JsonResponse 
from .models import Product
from .seriallizers import ProductSerializer
from rest_framework.response import Response  
from rest_framework import status , filters
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins , generics , viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here. 

# def no_rest_no_model(request):

#     products=[
#         {
#         'id':1,
#         "name":"omar",
#         },
#         {
#         'id':2,
#         "name":"khaled",
#         },
#     ]

#     return JsonResponse(products,safe=False)


# def no_rest_from_model(request): 
#     data =Product.objects.all()
#     response ={
#         "products":list(data.values())
#     }  
#     return JsonResponse(response)


# @api_view(["GET","POST"])
# def FBV_List(request):
#     #get
#     if request.method == "GET":
#         data =Product.objects.all()
#         serializer = ProductSerializer(data,many=True)
#         return Response(serializer.data)
#     #post
#     elif request.method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def FBV_id(request,id):
#     try:
#         product =Product.objects.get(id=id)
#     except Product.DoesNotExist :
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     #get
#     if request.method == 'GET':
#         serializer = ProductSerializer(product,many=True)
#         return Response(serializer.data)
    
#     #post
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     #delete
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # class CBV_List(APIView):
# #     def get(self,request):
# #         product =Product.objects.all()
# #         serializer=ProductSerializer(product,many=True)
# #         return Response(serializer.data)
# #     def post(self,request):
# #         serializer=ProductSerializer(data = request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status =status.HTTP_201_CREATED)
# #         return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST) 
# # class CBV_Id(APIView):
#     def get_object(self,id):
#         try: 
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             raise Http404
#     def get(self, request, id ):
#         product=self.get_object(id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     def put(self, request, id ):
#         product=self.get_object(id)
#         serializer = ProductSerializer(product,data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)
    
#     def delete(self , request , id):
#         product=self.get_object(id)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class mixins_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
# class mixins_id(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView ):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, id):
#         return self.retrieve(request)
#     def put(self, request , id):
#         return self.update(request)
#     def delete(self, request , id):
#         return self.destroy(request)


class generics_list(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class generics_id(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # طباعة البيانات المرسلة من الـ front-end
        print(request.data)  # يعرض جميع البيانات المرسلة
        print(request.FILES)  # يعرض الملفات المرسلة (مثل الصور)

        return super().update(request, *args, **kwargs)


# class viewsets_product(viewsets.ModelViewSet):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backend = [filters.SearchFilter]
#     search_fields = ["id"]