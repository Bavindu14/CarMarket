from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vehicle, Bid, VehicleImage
from .forms import VehicleForm, BidForm, UserRegistrationForm, VehicleImageFormSet
from django.contrib.auth import authenticate, login, logout

# Home view
def home(request):
    return render(request, 'home.html')

# Vehicle list view with search
def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        vehicles = vehicles.filter(
            make__icontains=query) | vehicles.filter(
            model__icontains=query) | vehicles.filter(
            year__icontains=query)
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

# Vehicle detail view
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    bids = vehicle.bids.all().order_by('-created_at')
    if request.method == "POST" and request.user.is_authenticated and request.user != vehicle.owner:
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.vehicle = vehicle
            bid.bidder = request.user
            bid.save()
            messages.success(request, "Bid placed successfully!")
            return redirect('vehicle_detail', pk=pk)
    else:
        form = BidForm()
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle, 'bids': bids, 'form': form})

# Vehicle create view
@login_required
def vehicle_create(request):
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        formset = VehicleImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            formset.instance = vehicle
            formset.save()
            messages.success(request, "Vehicle listed successfully!")
            return redirect('vehicle_detail', pk=vehicle.pk)
        else:
            messages.error(request, "Please correct the errors below.")
            for error in form.errors.values():
                messages.error(request, error)
            for formset_form in formset:
                for error in formset_form.errors.values():
                    messages.error(request, error)
    else:
        form = VehicleForm()
        formset = VehicleImageFormSet()
    return render(request, 'vehicle_create.html', {'form': form, 'formset': formset})

# Vehicle edit view
@login_required
def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.user != vehicle.owner:
        messages.error(request, "You can only edit your own vehicles.")
        return redirect('vehicle_detail', pk=pk)
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        formset = VehicleImageFormSet(request.POST, request.FILES, instance=vehicle)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Vehicle updated successfully!")
            return redirect('vehicle_detail', pk=pk)
    else:
        form = VehicleForm(instance=vehicle)
        formset = VehicleImageFormSet(instance=vehicle)
    return render(request, 'vehicle_edit.html', {'form': form, 'formset': formset, 'vehicle': vehicle})

# Vehicle delete view
@login_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.user != vehicle.owner:
        messages.error(request, "You can only delete your own vehicles.")
        return redirect('vehicle_list')
    if request.method == "POST":
        vehicle.delete()
        messages.success(request, "Vehicle deleted successfully!")
        return redirect('vehicle_list')
    return render(request, 'vehicle_confirm_delete.html', {'vehicle': vehicle})

# User registration view
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('vehicle_list')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html', {'form': UserRegistrationForm()})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('vehicle_list')

def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        vehicles = vehicles.filter(
            make__icontains=query) | vehicles.filter(
            model__icontains=query) | vehicles.filter(
            year__icontains=query)
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})