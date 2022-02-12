from django.shortcuts import render

from cars.models import Driver, Car


def car_detail(request, pk):
    driver = Driver.objects.get(pk=pk)
    cars = Car.objects.filter(owner_id=driver.id)

    context = {
        'cars': cars,
        'driver': driver,
    }

    return render(request, 'home.html', context)
