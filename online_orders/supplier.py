from django.contrib.auth.models import User
from .models import Product_type,Cipher,Calculation,Product,PrimaryImageAttachment,SecondaryImageAttachment,UserType
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image,ImageOps
import base64,json

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    try:
        req = json.loads(request.body)
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        # if User.objectsreq['user']
        error,count = '',0
        for i in req['product']:
            if not (Product_type.objects.filter(product_name=i['product_type']).exists() or User.objects.filter(username=i['user']).exists()):
                error += f'{count+1},'
            else:
                pro_temp=''
                if Product.objects.filter(unique_no=i['unique_no']).exists():
                    pro = Product.objects.get(unique_no=i['unique_no']) 
                    pro_temp=pro   
                    pro.product=i['product']                   
                    pro.price=float(i['price'])                 
                    pro.quantity=float(i['quantity'] )   
                    if i['product_type'] != pro.productType.product_name:
                          pro.productType=Product_type.objects.get(product_name=i['product_type'])  
                    pro.save()        
                else:
                    pro=Product.objects.create(
                        user=User.objects.get(username=req['user']),
                        unique_no=i['unique_no'],
                        product=i['product'],
                        price=i['price'],      
                        quantity=i['quantity'],
                        productType=Product_type.objects.get(product_name=i['product_type'])
                    )
                    pro_temp=pro   
                if i['primaryImage'] and pro_temp !='':
                    name = pro_temp.unique_no
                    output = BytesIO()
                    imgdata = base64.b64decode(i['primaryImage'])
                    img = Image.open(BytesIO(imgdata))
                    img_format = img.format
                    image = ImageOps.exif_transpose(img)
                    image.save(output,img_format, optimize = True,quality=30)
                    if not PrimaryImageAttachment.objects.filter(product=pro_temp).exists():
                        pimg=PrimaryImageAttachment.objects.create(product=pro,file= ContentFile(output.getvalue(),name=f'{name}_primary.' + img_format.lower()))                 
                    else:
                        pimg = PrimaryImageAttachment.objects.get(product=pro_temp)
                        pimg.file=ContentFile(output.getvalue(),name=f'{name}_primary.' + img_format.lower())
                        pimg.save()
                    output.seek(0),
                
                if i['secondaryImage'] and pro_temp !='' :
                    siCount=SecondaryImageAttachment.objects.filter(product=pro_temp).count()
                    for index,j in enumerate(i['secondaryImage']): 
                        name = pro_temp.unique_no
                        output = BytesIO()
                        imgdata = base64.b64decode(j)
                        img = Image.open(BytesIO(imgdata))
                        img_format = img.format
                        image = ImageOps.exif_transpose(img)
                        image.save(output,img_format, optimize = True,quality=30)
                        simg=SecondaryImageAttachment.objects.create(product=pro,file= ContentFile(output.getvalue(),name=f'{name}_secondary_{index+1+siCount}.' + img_format.lower()))                 
                        output.seek(0),  
            count+=1

        if error ==''&count>0:
            return Response(
                {
                    "Success" : f'{count} products added'
                },
                status=status.HTTP_201_CREATED
            )    
        else: 
            return Response(
                {
                    "Success" : f'{count} products added & error in {error}'
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
def get_product_supplier(request):
        
    try:
        req = json.loads(request.body)
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        user,unique_no,prduct,Product_type,arr = req['user'],req['unique_no'],req['type'],''
          
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

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def delete_product(request):
    try:
        req = json.loads(request.body)
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        if req['id']:
            Product.objects.get(id=req['id']).delete()
            return Response(
                {
                    "Success" : f'deleted successfully'
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

    
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_image(request):
    req = json.loads(request.body)
    if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
    primary_url,secondary_urls='',[]
    if req['primary_image'] and req['id']:
        PrimaryImageAttachment.objects.get(Product__id=id).file.url
    
       
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def delete_image(request):
    try:
        req = json.loads(request.body)
        if UserType.objects.get(user__username=req['user']).user_type in ['SUPPLIER','ADMIN']:return Response({"error": True,"error_msg": 'User is not supplier or consumer',},status=status.HTTP_400_BAD_REQUEST)
        if req['primary_image'] and  req['id']:
            PrimaryImageAttachment.objects.get(req['id']).delete()
            return Response(
                {
                    "Success" : f'deleted successfully'
                },
                status=status.HTTP_201_CREATED
            )  
        elif req['secondary_image'] and req['id']:
            SecondaryImageAttachment.objects.get(req['id']).delete()
            return Response(
                {
                    "Success" : f'deleted successfully'
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