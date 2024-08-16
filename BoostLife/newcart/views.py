from django.shortcuts import render
from .models import DeliveryCharge
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import json
@login_required(login_url='backend/login')
def charge(request):
    productapp=DeliveryCharge.objects.all()

    context={
        'banform': productapp
    }
    return render(request,'backend/chargelist.html',context)
@login_required(login_url='backend/login')
def chargeadd(request):
    if request.method == "POST":
        product = DeliveryCharge()
        charge = request.POST.get('charge')

        product.charge = charge

        product.save()

        return redirect('chargeapp')
    # categories = Catagory.objects.get(status=True)
    return render(request, 'backend/add_charge.html')
@login_required(login_url='backend/login')
def delete_charge(request, myid):
    productapp=DeliveryCharge.objects.get(id=myid)
    productapp.delete()
    return redirect('chargeapp')
@login_required(login_url='backend/login')
def edit_charge(request, myid):
    sel_proform=DeliveryCharge.objects.get(id=myid)
    pro = DeliveryCharge.objects.all()
    # categories = Catagory.objects.filter(status=True)
    context = {

        'pro': pro,
        'sel_proform':sel_proform,

    }
    return render(request,'backend/edit_charge.html',context)
@login_required(login_url='backend/login')
def update_charge(request, myid):
    productapp=DeliveryCharge.objects.get(id=myid)

    productapp.charge = request.POST.get('charge')

    productapp.save()

    return redirect('chargeapp')
# Create your views here.



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer,CartGetSerializer
from registration.models import CustomUser
from product.models import Product
from rest_framework.permissions import IsAuthenticated

class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            u_id = request.data.get('u_id')

            # Check if product with given ID exists
            product = Product.objects.filter(id=product_id).first()
            if not product:
                return Response({"error": "Product does not exist."}, status=status.HTTP_404_NOT_FOUND)

            # Check if user with given ID exists
            user = CustomUser.objects.filter(id=u_id).first()
            if not user:
                return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)

            # Get the cart item for the given product and user if it exists, otherwise create it
            cart_items = Cart.objects.filter(product_id=product, u_id=user)

            if cart_items.exists():
                # If the item already exists, choose the first one (or apply your own logic)
                cart_item = cart_items.first()
                cart_item.quantity += 1
                cart_item.price = cart_item.quantity * product.item_new_price
            else:
                # If the item is newly created, set its initial quantity and price
                cart_item = Cart.objects.create(product_id=product, u_id=user, quantity=1,
                                                price=product.item_new_price)

            # Save the cart item
            cart_item.save()

            # Save the cart item
            cart_item.save()

            # Serialize the cart item
            serializer = CartSerializer(cart_item)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class CartDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Get the user_id from query parameters
            user_id = request.query_params.get('user_id')

            # Validate user_id parameter
            if not user_id:
                return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve all cart items for the specified user_id
            cart_items = Cart.objects.filter(u_id=user_id)

            # Serialize the cart items
            serializer = CartGetSerializer(cart_items, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from .models import Stock
class IncreaseQuantity(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            cart_id = request.data.get('cart_id')

            # Retrieve the cart item
            cart_item = Cart.objects.get(id=cart_id)
            stock=Stock.objects.get(item_id=cart_item.product_id)
            # Check if quantity is less than opening stock
            if cart_item.quantity < stock.openingstock:
                # Increment quantity
                cart_item.quantity += 1
                cart_item.save()

                # Update total price
                cart_item.price = cart_item.product_id.item_new_price * cart_item.quantity
                cart_item.save()

                return Response({"message": "Quantity increased successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Quantity cannot be increased beyond opening stock."},
                                status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class DecreaseQuantity(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            cart_id = request.data.get('cart_id')

            # Retrieve the cart item
            cart_item = Cart.objects.get(id=cart_id)

            # Ensure quantity is greater than 1 before decrementing
            if cart_item.quantity > 1:
                # Decrement quantity
                cart_item.quantity -= 1
                cart_item.save()

                # Update total price
                cart_item.price = cart_item.product_id.item_new_price * cart_item.quantity
                cart_item.save()

                return Response({"message": "Quantity decreased successfully."}, status=status.HTTP_200_OK)
            else:
                cart_item.delete()
                return Response({"error": "Quantity cannot be less than 1."}, status=status.HTTP_400_BAD_REQUEST)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RemoveCartItem(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            cart_id = request.query_params.get('cart_id')

            # Check if cart_id parameter is provided and if it's a valid integer
            if not cart_id.isdigit():
                return Response({"error": "Valid cart_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the cart item
            cart_item = Cart.objects.get(id=int(cart_id))

            # Delete the cart item
            cart_item.delete()

            return Response({"message": "Cart item removed successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid cart_id provided."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class CartTotalPrice(APIView):
#     def get(self, request):
#         try:
#             # Get the user_id from query parameters
#             user_id = request.query_params.get('user_id')
#
#             # Check if user_id parameter is provided
#             if user_id is None:
#                 return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Check if user_id is a valid integer
#             if not str(user_id).isdigit():
#                 return Response({"error": "Valid user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#             # Retrieve all cart items for the specified user_id
#             cart_items = Cart.objects.filter(u_id=user_id)
#
#             # Calculate total price by summing the prices of all cart items
#             total_price = sum(cart_item.price for cart_item in cart_items)
#
#             return Response({"total_price": total_price}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
from datetime import date
from django.utils import timezone
from .models import DeliveryCharge
import math
class CartTotalPrice(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            pick_up = request.query_params.get('pick_up')
            if pick_up == '1':
                delivery_charge = 0
            else:
                delivery_charge = DeliveryCharge.objects.first().charge

            user_id = request.query_params.get('user_id')

            if user_id is None:
                return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            if not str(user_id).isdigit():
                return Response({"error": "Valid user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            cart_items = Cart.objects.filter(u_id=user_id)
            total_price = sum(cart_item.price for cart_item in cart_items)
            previous_price = total_price
            discounted_price = 0
            today_date = date.today()

            # Removed CartCoupon and wallet value logic

            if delivery_charge:
                total_price += delivery_charge

            total_price = math.ceil(total_price * 100) / 100
            previous_price = math.ceil(previous_price * 100) / 100
            discounted_price = math.ceil(discounted_price * 100) / 100
            if delivery_charge:
                delivery_charge = math.ceil(delivery_charge * 100) / 100
            rounded_total_price = math.ceil(total_price)

            return Response({
                "total_price": rounded_total_price,
                "previous_price": previous_price,
                "discounted_price": discounted_price,
                "delivery_charge": delivery_charge if delivery_charge else 0
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes



class IncreaseQuantityMain(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            user_id = request.data.get('user_id')

            # Retrieve the cart item
            cart_item = Cart.objects.get(product_id=product_id, u_id=user_id)
            stock = Stock.objects.get(item_id=product_id)

            # Check if quantity is less than opening stock
            if cart_item.quantity < stock.openingstock:
                # Increment quantity
                cart_item.quantity += 1
                cart_item.save()

                # Update total price
                cart_item.price = cart_item.product_id.item_new_price * cart_item.quantity
                cart_item.save()

                return Response({"message": "Quantity increased successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Quantity cannot be increased beyond opening stock."},
                                status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Stock.DoesNotExist:
            return Response({"error": "Stock information not available for the product."},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class DecreaseQuantityMain(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            user_id = request.data.get('user_id')

            # Retrieve the cart item
            cart_item = Cart.objects.get(product_id=product_id, u_id=user_id)

            # Ensure quantity is greater than 1 before decrementing
            if cart_item.quantity > 1:
                # Decrement quantity
                cart_item.quantity -= 1
                cart_item.save()

                # Update total price
                cart_item.price = cart_item.product_id.item_new_price * cart_item.quantity
                cart_item.save()

                return Response({"message": "Quantity decreased successfully."}, status=status.HTTP_200_OK)
            else:
                cart_item.delete()
                return Response({"error": "Quantity cannot be less than 1." ,"status":0}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Cart item does not exist." ,"status":0}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class CartDetailsMainAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Get the user_id from query parameters
            user_id = request.query_params.get('user_id')
            product_id = request.query_params.get('product_id')

            # Validate user_id parameter
            if not user_id:
                return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve all cart items for the specified user_id
            cart_items = Cart.objects.filter(u_id=user_id,product_id=product_id)

            # Serialize the cart items
            serializer = CartGetSerializer(cart_items, many=True)

            return Response(serializer.data[0], status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)