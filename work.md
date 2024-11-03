# EstateAgency-eCommerce-and-Blog-site-

1. GitHub repo ochdik
[GitHub] (https://github.com/turdal1hasanboyev/EstateAgency-eCommerce-and-Blog-site-.git)

* work.md fayl yaratdik
* README.md faylini sozladik
* .gitignore faylini sozladik
* Muhit (venv) py -m venv venv orqali yaratdik
* Muhitni faollashtirdik (venv\Scripts\activate)
* Django ni o'rnatib oldik (pip install django)
* kutubxonalarni yozib borish uchun requirements.txt faylini yaratdik (pip freeze > requirements.txt) orqali
2. Config va manage.py faylini yaratdik! (django-admin startproject config .) orqali
*Barcha buyruqlar va kutubxonalar muhit ya'ni (venv ni) ichida bajariladi*
3. Folder Structure
* (.env, .env.example, templates, media, apps, static)
* Barcha fayl va papkalarni joy joyiga qo'yib chiqish
* Barcha kerakli kutbxonalar o'rnatib olindi
```commandline
asgiref==3.8.1
Django==5.1.2
django-ckeditor==6.7.1
django-js-asset==2.2.0
django-query-counter==0.4.0
pillow==11.0.0
psycopg2-binary==2.9.10
python-environ==0.4.54
sqlparse==0.5.1
tabulate==0.9.0
tzdata==2024.2
```
* py manage.py collectstatic (statik fayllar yig'ildi birinchi marta)
* py manage.py makemigrations (migratsiyalar yaratildi)
* py manage.py migrate (migratsiyalar bajarildi)
* psql integratsiya boldi
* Custom User va Manager yozildi
4. Ertangi ishimiz 
* Malumotlar bazasi tahlili
* Custom User qayta tahlili
* Custom User admin.py tahlili