from django.shortcuts import render, redirect, get_object_or_404
from .models import Catagory,Product,Level
from newcart.models import Stock
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='backend/login')
def catagory(request):
    catagoryapp=Catagory.objects.all()

    context={
        'banform': catagoryapp

    }
    return render(request,'backend/catagory.html',context)
@login_required(login_url='backend/login')
def catgoryadd(request):
    if request.method == "POST":
        contact = Catagory()
        name = request.POST.get('name')
        image = request.FILES.get('image')
        contact.name = name
        contact.image = image
        contact.save()
        return redirect('catagoryapp')  # Replace 'category_list' with the name of the URL you want to redirect to
    return render(request, 'backend/catgoryadd.html')
@login_required(login_url='backend/login')
def catdelete_item(request, myid):
    catagoryapp=Catagory.objects.get(id=myid)
    catagoryapp.delete()
    return redirect('catagoryapp')
@login_required(login_url='backend/login')
def catedit_item(request, myid):
    sel_catform=Catagory.objects.get(id=myid)
    cat = Catagory.objects.all()
    context = {
        'cat': cat,
        'sel_proform':sel_catform

    }
    return render(request,'backend/catagoryedit.html',context)
@login_required(login_url='backend/login')
def catupdate_item(request, myid):
    catagoryapp=Catagory.objects.get(id=myid)

    catagoryapp.name = request.POST.get('name')
    if request.FILES.get('image'):
        catagoryapp.image = request.FILES.get('image')

    catagoryapp.save()
    return redirect('catagoryapp')


@login_required(login_url='backend/login')
def level(request):
    catagoryapp=Level.objects.all()

    context={
        'banform': catagoryapp

    }
    return render(request,'backend/level.html',context)
@login_required(login_url='backend/login')
def leveladd(request):
    if request.method == "POST":
        contact = Level()
        name = request.POST.get('name')
        image = request.FILES.get('image')
        contact.name = name
        contact.image = image
        contact.save()
        return redirect('levelapp')  # Replace 'category_list' with the name of the URL you want to redirect to
    return render(request, 'backend/Leveladd.html')
@login_required(login_url='backend/login')
def leveldelete_item(request, myid):
    catagoryapp=Level.objects.get(id=myid)
    catagoryapp.delete()
    return redirect('levelapp')
@login_required(login_url='backend/login')
def leveledit_item(request, myid):
    sel_catform=Level.objects.get(id=myid)
    cat = Level.objects.all()
    context = {
        'cat': cat,
        'sel_proform':sel_catform

    }
    return render(request,'backend/leveledit.html',context)
@login_required(login_url='backend/login')
def levelupdate_item(request, myid):
    catagoryapp=Level.objects.get(id=myid)

    catagoryapp.name = request.POST.get('name')
    if request.FILES.get('image'):
        catagoryapp.image = request.FILES.get('image')

    catagoryapp.save()
    return redirect('levelapp')


@login_required(login_url='backend/login')
def product(request):
    productapp=Product.objects.all()

    context={
        'banform': productapp

    }
    return render(request,'backend/product.html',context)

from newcart.models import Stock


@login_required(login_url='backend/login')
def productadd(request):
    if request.method == "POST":
        title = request.POST.get('title')
        # weight_units=request.POST.get('weight_units')
        description = request.POST.get('description')
        item_photo = request.FILES.get('item_photo')
        # item_quantity = request.POST.get('item_quantity')
        item_old_price = request.POST.get('item_old_price')
        item_new_price = request.POST.get('item_new_price')

        discount = request.POST.get('discount')
        cat_name = request.POST.get('category')  # Get the selected category name
        category = Catagory.objects.get(id=cat_name)
        recommended = request.POST.get('recommended') == 'on'
        most_popular = request.POST.get('most_popular') == 'on'
        goal = int(request.POST.get('goal'))

        # Calculate item_new_price based on item_old_price and discount
        # item_new_price = float(item_old_price) * (1 - float(discount) / 100)
        item_new_price = round(float(item_new_price), 2)
        item_old_price = round(float(item_old_price), 2)
        # Create the item object
        item = Product.objects.create(
            name=title,
            # item_measurement=weight_units,
            description=description,
            image=item_photo,
            # item_quantity=item_quantity,
            item_old_price=item_old_price,
            discount=discount,
            item_new_price=item_new_price,
            status=True,
            cat_name=category,
            most_popular=most_popular,
            recommended=recommended,
            goal=goal
        )
        Stock.objects.create(openingstock=0, item_id=item)


        # existing_items = Item.objects.all()
        #
        # for item in existing_items:
        #     # Check if a Stock entry already exists for this item
        #     existing_stock = Stock.objects.filter(item_id=item).exists()
        #
        #     # If a Stock entry doesn't exist, create one with opening stock = 0
        #     if not existing_stock:
        #         Stock.objects.create(openingstock=1, item_id=item)
        return redirect('productapp')

        # If the request method is not POST, render the form
    categories = Catagory.objects.all()
    return render(request, 'backend/productadd.html', {'categories': categories})
@login_required(login_url='backend/login')
def delete_item(request, myid):
    productapp=Product.objects.get(id=myid)
    productapp.delete()
    return redirect('productapp')
@login_required(login_url='backend/login')
def edit_item(request, myid):
    sel_proform=Product.objects.get(id=myid)
    pro = Product.objects.all()
    categories = Catagory.objects.filter(status=True)
    context = {
        'pro': pro,
        'sel_proform':sel_proform,
        'categories':categories

    }
    return render(request,'backend/productedit.html',context)
@login_required(login_url='backend/login')
def update_item(request, myid):
    productapp = Product.objects.get(id=myid)
    productapp.name = request.POST.get('title')
    productapp.description = request.POST.get('description')
    if request.FILES.get('image'):
        productapp.image = request.FILES.get('image')
    productapp.cat_name_id = request.POST.get('category')  # Assuming you have a category ID in the form

    productapp.item_old_price = request.POST.get('item_old_price')
    productapp.discount = request.POST.get('discount')
    productapp.item_new_price = request.POST.get('item_new_price')

    productapp.most_popular = 'most_popular' in request.POST  # Check if most_popular checkbox is checked
    productapp.recommended = 'recommended' in request.POST  # Check if recommended checkbox is checked

    productapp.goal = request.POST.get('goal')

    productapp.save()

    return redirect('productapp')  # Redirect to the appropriate URL
@login_required(login_url='backend/login')
def view_item(request, myid):
    sel_proform = Product.objects.get(id=myid)
    pro = Product.objects.all()
    context = {
        'proform': pro,
        'sel_proform': sel_proform

    }
    return render(request, 'backend/productview.html', context)

@login_required(login_url='backend/login')
def activate_product(request, product_id):
    banner = get_object_or_404(Product, id=product_id)
    banner.status = True
    banner.save()
    return redirect('productapp')  # Redirect to your banner list view

@login_required(login_url='backend/login')
def deactivate_product(request, product_id):
    banner = get_object_or_404(Product, id=product_id)
    banner.status = False
    banner.save()
    return redirect('productapp')  # Redirect to your banner list view
# Create your views here.

from rest_framework import generics
from .models import Catagory, Product
from .serializers import CatagorySerializer,ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
@permission_classes([IsAuthenticated])
class CatagoryListView(generics.ListAPIView):
    serializer_class = CatagorySerializer

    def get_queryset(self):
        return Catagory.objects.filter(status=True)

@permission_classes([IsAuthenticated])
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_name = self.request.query_params.get('category_id', None)
        if category_name is not None:
            queryset = queryset.filter(cat_name__id=category_name)
        return queryset

#through product id
@permission_classes([IsAuthenticated])
class ProductListThroughIdView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_name = self.request.query_params.get('product_id', None)
        if category_name is not None:
            queryset = queryset.filter(id=category_name)
        return queryset
@permission_classes([IsAuthenticated])
class RecommendedProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(recommended=True,status=True, stock__openingstock__gt=0)
@permission_classes([IsAuthenticated])
class MostPopularProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(most_popular=True,status=True, stock__openingstock__gt=0)

@permission_classes([IsAuthenticated])
class GoalwiseProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        goal = self.request.query_params.get('goal', None)
        if goal is not None:
            queryset = queryset.filter(goal=goal,status=True, stock__openingstock__gt=0)
        return queryset






@permission_classes([IsAuthenticated])
class CatagoryListViewFive(generics.ListAPIView):
    serializer_class = CatagorySerializer

    def get_queryset(self):
        return Catagory.objects.filter(status=True)[:5]

@permission_classes([IsAuthenticated])
class ProductListViewFive(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_name = self.request.query_params.get('category_id', None)
        if category_name is not None:
            queryset = queryset.filter(cat_name__id=category_name)
        return queryset[:5]
@permission_classes([IsAuthenticated])
class RecommendedProductListViewFive(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(recommended=True,status=True, stock__openingstock__gt=0)[:5]
@permission_classes([IsAuthenticated])
class MostPopularProductListViewFive(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(most_popular=True,status=True, stock__openingstock__gt=0)[:5]

@permission_classes([IsAuthenticated])
class GoalwiseProductListViewFive(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        goal = self.request.query_params.get('goal', None)
        if goal is not None:
            queryset = queryset.filter(goal=goal,status=True, stock__openingstock__gt=0)
        return queryset[:4]




@login_required(login_url='backend/login')
def stock(request):
    catagoryapp=Stock.objects.all()

    context={
        'banform': catagoryapp

    }

    return render(request,'backend/inventory_list.html',context)
@login_required(login_url='backend/login')
def edit_stock(request, myid):
    sel_proform=Stock.objects.get(id=myid)
    pro = Stock.objects.all()
    # categories = Catagory.objects.filter(status=True)
    context = {

        'pro': pro,
        'item':sel_proform,

    }
    return render(request,'backend/edit_inventory.html',context)
@login_required(login_url='backend/login')
def update_stock(request,stock_id):
    if request.method == 'POST':
        openingstock = request.POST.get('openingstock')

        try:
            stock = Stock.objects.get(id=stock_id)
            stock.openingstock = openingstock
            stock.save()

            messages.success(request, 'Stock updated successfully.')
        except Stock.DoesNotExist:
            messages.error(request, 'Stock does not exist.')
        except Exception as e:
            messages.error(request, str(e))

    return redirect('stock')
@login_required(login_url='backend/login')
def update_all_stock(request):
    if request.method == 'POST':

        for key, value in request.POST.items():
            if key.startswith('openingstock_'):
                stock_id = key.split('_')[1]
                try:
                    stock = get_object_or_404(Stock, pk=stock_id)
                    stock.openingstock = value
                    stock.save()
                except Exception as e:
                    # Handle exceptions as needed
                    pass
    return redirect('stock')
@login_required(login_url='backend/login')
def allstock(request):
    catagoryapp=Stock.objects.all()

    context={
        'banform': catagoryapp

    }

    return render(request,'backend/allinventory_list.html',context)
