import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Product_type,Cipher,Calculation,Product,PrimaryImageAttachment,SecondaryImageAttachment,UserType
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer


class UserRecordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product_type(request):
    try:
        req = json.loads(request.body)
        product_name = req['product_name']
        cipher = req['cipher']
        Product_type.objects.create(product_name=product_name,cipher = cipher)
        return Response(
            {
                "Success" : "Successfully added"
            },
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_cipher(request):
    try:
        req = json.loads(request.body)
        name=req['name']
        inp6=req['inp6']
        inp7=req['inp7']
        name.objects.create(name=name,inp6=inp6,inp7=inp7 )
        return Response(
            {
                "Success" : "Successfully added"
            },
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_calculation(request):
    try:
        req = json.loads(request.body)
        calc_name=req['calc_name']
        inp1=req['inp1']
        inp2=req['inp2']
        inp3=req['inp3']
        inp4=req['inp4']
        inp5=req['inp5']
        cipher =req['cipher'] 
        Code_it_calc=req['code_it_calc']
        calc_name.objects.create( calc_name= calc_name,inp1=inp1,inp2=inp2,inp3=inp3,inp4=inp4,inp5=inp5,cipher=cipher,Code_it_calc=Code_it_calc )
        return Response(
            {
                "Success" : "Successfully added"
            },
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )

#--------------------------------- Product ---------------------------------------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_product_type(request):
    try:
        req = json.loads(request.body)
        product_name = req['product_name']
        if product_name in Product_type.objects.values_list('product_name',flat=True):
            prod_type = Product_type.objects.filter(product_name=product_name)
            prod_type.delete()
        return Response(
            {
                "Success" : "Successfully Deleted"
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )     


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_cipher(request):
    try:
        req = json.loads(request.body)
        name=req['name']
        if name in Cipher.objects.values_list('name',flat=True):
            ciph=Cipher.objects.filter(name=name)
            ciph.delete()
        return Response(
            {
                "Success" : "Successfully deleted"
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )  



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_calculation(request):
    try:
        req = json.loads(request.body)
        calc_name=req['calc_name']
        if calc_name in Calculation.objects.values_list('calc_name',flat=True):
          cal_name = calc_name.objects.filter(calc_name= calc_name)
          cal_name.delete()
        return Response(
            {
                "Success" : "Successfully deleted"
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )


#------------------------------------------Get-------------------------------------------------


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_Product_type(request):
        
    try:
        req = json.loads(request.body)
        
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        user,unique_no,Product_type,arr = req['user'],req['unique_no'],req['type'],''
          
        if user and not any (unique_no,Product_type): arr = Product.objects.filter(user__username=user)    
        elif user and unique_no: arr = Product.objects.filter(unique_no=unique_no)
        elif user and Product_type and not any in (unique_no): arr = Product.objects.filter(user__username=user,productType__product_name=type)
        return Response(
                {
                    "arr" : f'{arr}'
                },
                status=status.HTTP_201_CREATED
            ) 
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_Cipher(request):
        
    try:
        req = json.loads(request.body)
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        user,unique_no,Product_type,arr = req['user'],req['unique_no'],req['type'],''
          
        if user and not any (unique_no,Product_type): arr = Product.objects.filter(user__username=user)    
        elif user and unique_no: arr = Product.objects.filter(unique_no=unique_no)
        elif user and Product_type and not any in (unique_no): arr = Product.objects.filter(user__username=user,productType__product_name=type)
        return Response(
                {
                    "arr" : f'{arr}'
                },
                status=status.HTTP_201_CREATED
            ) 
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_Calcultaion(request):
        
    try:
        req = json.loads(request.body)
        calc_name=req['calc_name']
        inp1=req['inp1']
        inp2=req['inp2']
        inp3=req['inp3']
        inp4=req['inp4']
        inp5=req['inp5']
        cipher =req['cipher'] 
        Code_it_calc=req['code_it_calc']
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        user,unique_no,Product_type,arr = req['user'],req['unique_no'],req['type'],''
          
        if user and not any (unique_no,Product_type): arr = Product.objects.filter(user__username=user)    
        elif user and unique_no: arr = Product.objects.filter(unique_no=unique_no)
        elif user and Product_type and not any in (unique_no): arr = Product.objects.filter(user__username=user,productType__product_name=type)
        return Response(
                {
                    "arr" : f'{arr}'
                },
                status=status.HTTP_201_CREATED
            ) 
    except Exception as e:
        return Response(
            {
                "error": True,
                "error_msg": str(e),
            },
            status=status.HTTP_400_BAD_REQUEST
        )



