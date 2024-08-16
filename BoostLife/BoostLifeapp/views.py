from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Partner,Package,Store

@login_required(login_url='backend/login')
def partner_add(request):
    if request.method == "POST":
        partner_id = request.POST.get('partner_id')
        logo = request.FILES.get('logo')
        name = request.POST.get('name')
        store_name = request.POST.get('store_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        # Create the Partner object
        Partner.objects.create(
            partner_id=partner_id,
            logo=logo,
            name=name,
            store_name=store_name,
            address=address,
            phone_number=phone_number
        )
        return redirect('partner_list')

    return render(request, 'backend/partner_add.html')

@login_required(login_url='backend/login')
def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'backend/partner_list.html', {'partners': partners})

@login_required(login_url='backend/login')
def partner_edit(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)

    if request.method == "POST":
        partner.name = request.POST.get('name')
        partner.store_name = request.POST.get('store_name')
        partner.address = request.POST.get('address')
        partner.phone_number = request.POST.get('phone_number')
        if request.FILES.get('logo'):
            partner.logo = request.FILES.get('logo')
        partner.save()

        return redirect('partner_list')

    return render(request, 'backend/partner_edit.html', {'partner': partner})

@login_required(login_url='backend/login')
def partner_delete(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    partner.delete()
    return redirect('partner_list')

@login_required(login_url='backend/login')
def partner_view(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    return render(request, 'backend/partner_view.html', {'partner': partner})

@login_required(login_url='backend/login')
def activate_partner(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    partner.status = True
    partner.save()
    return redirect('partner_list')  # Redirect to your partner list view

@login_required(login_url='backend/login')
def deactivate_partner(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    partner.status = False
    partner.save()
    return redirect('partner_list')  # Redirect to your partner list view


@login_required(login_url='backend/login')
def add_package(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		package_amount = request.POST.get('package_amount')
		description = request.POST.get('description')

		Package.objects.create(
			name=name,
			package_amount=package_amount,
			description=description
		)
		return redirect('package_list')  # Redirect to the package list view
	return render(request, 'backend/add_package.html')


@login_required(login_url='backend/login')
def edit_package(request, package_id):
	package = get_object_or_404(Package, id=package_id)

	if request.method == 'POST':
		package.name = request.POST.get('name', package.name)
		package.package_amount = request.POST.get('package_amount', package.package_amount)
		package.description = request.POST.get('description', package.description)
		package.save()
		return redirect('package_list')  # Redirect to the package list view
	return render(request, 'backend/edit_package.html', {'package': package})


@login_required(login_url='backend/login')
def delete_package(request, package_id):
	package = get_object_or_404(Package, id=package_id)
	package.delete()
	return redirect('package_list')  # Redirect to the package list view


@login_required(login_url='backend/login')
def list_packages(request):
	packages = Package.objects.all()
	return render(request, 'backend/list_packages.html', {'packages': packages})

@login_required(login_url='backend/login')
def list_store(request):
	packages = Store.objects.all()
	return render(request, 'backend/list_store.html', {'stores': packages})

@login_required(login_url='backend/login')
def store_add(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		address = request.POST.get('address')
		url = request.POST.get('url')
		image = request.FILES.get('image')

		# Create a new Store object
		store = Store(
			name=name,
			description=description,
			address=address,
			url=url,
			newimage=image
		)

		# Save the store to the database
		store.save()

		messages.success(request, f'Store "{store.name}" was added successfully!')
		return redirect('list_store')  # Redirect to the list of stores

	return render(request, 'backend/store_add.html')
@login_required(login_url='backend/login')
def delete_store(request, store_id):
	package = get_object_or_404(Store, id=store_id)
	package.delete()
	return redirect('list_store')  # Redirect to the package list view
@login_required(login_url='backend/login')
def activate_store(request, store_id):
    partner = get_object_or_404(Store, id=store_id)
    partner.status = True
    partner.save()
    return redirect('list_store')  # Redirect to your partner list view

@login_required(login_url='backend/login')
def deactivate_store(request, store_id):
    partner = get_object_or_404(Store, id=store_id)
    partner.status = False
    partner.save()
    return redirect('list_store')  # Redirect to your partner list view


@login_required(login_url='backend/login')
def edit_store(request, store_id):
	# Fetch the store object by ID or return a 404 error if not found
	store = get_object_or_404(Store, id=store_id)

	if request.method == 'POST':
		# Retrieve data from the POST request using request.POST.get()
		store.name = request.POST.get('name')
		store.address = request.POST.get('address')
		store.description = request.POST.get('description')
		store.url = request.POST.get('url')
		store.status = request.POST.get('status') == 'True'  # Convert the status to a boolean

		# Handle the file upload
		if request.FILES.get('newimage'):
			store.newimage = request.FILES.get('newimage')

		# Save the updated store object
		store.save()

		# Set success message and redirect to store list
		messages.success(request, 'Store details updated successfully.')
		return redirect('list_store')

	# Render the form with existing store data for GET request
	context = {
		'store': store,
	}
	return render(request, 'backend/edit_store.html', context)
