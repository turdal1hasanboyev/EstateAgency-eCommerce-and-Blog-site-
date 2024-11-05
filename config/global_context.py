from apps.common.models import Company, Country

def objects(request):
    companies = Company.objects.filter(is_active=True).order_by('title')[:6]
    countries = Country.objects.filter(is_active=True).order_by('title')[:6]

    return {
        'companies': companies,
        'countries': countries,
    }