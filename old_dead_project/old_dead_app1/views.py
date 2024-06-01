from django.shortcuts import render, redirect
from .forms import CountryForm
from old_dead_app1.models import Worker, Department, Country


def index_page(request):
    """Вносим новую запись в таблицу"""
    # new_worker = Worker(department_id=1, name='Vlad', surname='Sponoff', salary=60000)
    # new_worker.save()

    """2 способ - ниже"""
    # Worker.objects.create(department_id=1, name='Semen', surname='Sponoff', salary=0)

    """меняем значения полей таблицы"""
    # worker_to_change = Worker.objects.get(id=2)  # получаем объект по ключу
    # print(worker_to_change)
    # worker_to_change.salary = '110000'  # меняем метрику
    # print(worker_to_change)
    # worker_to_change.save()  # сохраняем изменения
    # print(worker_to_change)

    """2 способ"""
    # Worker.objects.filter(id=2).update(salary=140000)
    # print(Worker.objects.get(id=2))

    """Получаем ВСЕ данные из модели"""
    # all_workers = Worker.objects.all()
    # print(all_workers)

    """Получаем данные по фильтру"""
    # workers_filtered = Worker.objects.filter(department_id=1, salary=60000)  # Filtering by Dept_id and salary
    # print(workers_filtered)

    """Получаем каждую запись отдельно"""
    # for i in all_workers:
    #     print(f'Worker id: {i.id}, Name: {i.name}, Surname: {i.surname}, Salary: {i.salary}, '
    #           f'Department: {i.department}, Department ID: {i.department_id}')

    return render(request, 'index.html')


def structure(request):
    """Получаем ВСЕ данные из модели"""
    departments = Department.objects.all()
    # print(departments)  # Non - filtering

    """Получаем данные по фильтру"""
    # print(Department.objects.filter(name='Sales'))  # Filtering by Dept_name
    return render(request, template_name='structure.html', context={'departments': departments})


def about_page(request):
    all_departments = Department.objects.all()
    all_workers = Worker.objects.all()
    names_surnames = []
    only_worker = Worker.objects.get(id=2)
    for i in all_workers:
        names_surnames.append(i.name + " " + i.surname)

    return render(request,
                  'about.html',
                  context={
                      'departments': all_departments,
                      'workers': all_workers,
                      'names': names_surnames,
                      'worker': only_worker
                  })


def upload_flag(request):
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('countries')
    else:
        form = CountryForm()
    return render(request, 'upload_flag.html', {'form': form})


def countries_page(request):
    all_countries = Country.objects.all()
    return render(request, 'countries.html', context={'countries': all_countries})
