from django.shortcuts import render

# Главная страница
def index_page(request):
    return render(request, 'index.html')

# О сайте
def about_site(request):
    return render(request, 'about-site.html')

# Бурение нефтяных и газовых скважин
def burial_drilling(request):
    return render(request, 'professions/burial_drilling.html')

# Сооружение и эксплуатация газонефтепроводов и газонефтехранилищ
def pipeline_construction(request):
    return render(request, 'professions/pipeline_construction.html')

# Разработка и эксплуатация нефтяных и газовых месторождений
def oil_gas_development(request):
    return render(request, 'professions/oil_gas_development.html')

# Геофизические методы поисков и разведки месторождений полезных ископаемых
def geophysical_exploration(request):
    return render(request, 'professions/geophysical_exploration.html')

# Техническая эксплуатация и обслуживание электрического и электромеханического оборудования
def electro_maintenance(request):
    return render(request, 'professions/electro_maintenance.html')

# Монтаж, техническое обслуживание и ремонт промышленного оборудования
def industrial_maintenance(request):
    return render(request, 'professions/industrial_maintenance.html')

# Информационные системы и программирование
def info_sys_programming(request):
    return render(request, 'professions/info_sys_programming.html')

# Автоматические системы управления
def automatic_control_systems(request):
    return render(request, 'professions/automatic_control_systems.html')

# Экономика и бухгалтерский учет
def economics_accounting(request):
    return render(request, 'professions/economics_accounting.html')

# Геология и разведка нефтяных и газовых месторождений
def geology_exploration(request):
    return render(request, 'professions/geology_exploration.html')

# Прикладная геодезия
def applied_geodesy(request):
    return render(request, 'professions/applied_geodesy.html')
