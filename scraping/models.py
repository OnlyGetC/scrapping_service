from django.db import models


class Cuponi(models.Model): #не работает как надо
    cupon_name = models.CharField(max_length=50, verbose_name='Название купона', unique=True)
    slug = models.CharField(max_length=50, blank = True, unique=True)#blank говорит о том что поле может быть пустым, unique говорит о том что поле уникальное

    class Meta:
        verbose_name = 'Название купона'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.cupon_name

class questions(models.Model):
    quesion_title= models.CharField(max_length=250, verbose_name='Вопрос в краткой форме', unique=True)
    description = models.CharField(max_length=1000, verbose_name='Подробное описание вопроса', unique=True)
    answer = models.CharField(max_length=1000, verbose_name='Ответ на вопрос', unique=True)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.quesion_title

class news(models.Model):
    news_title= models.CharField(max_length=100, verbose_name='Заголовок новости', unique=True)
    news_text = models.TextField(verbose_name='Текст новости')
    #разобраться с этим полем, так как вроде требует библиотеку pillow или чето ещё news_photo = models.ImageField(verbose_name='Фото новости', height_field=100, width_field=100)
    timestamp = models.DateField(auto_now_add=True,verbose_name='Дата опубликования')# должна показывать какого числа была опубликована новость(возможно verbose name необходимо удалить, так как могут быть ошибки)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.news_title

class contacts(models.Model):
    version_contact= models.CharField(max_length=100, verbose_name='Версия контактов', unique=True)
    contact_text = models.TextField(verbose_name='Текст контакты')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.version_contact

class ticket(models.Model):
    ticket_name= models.CharField(max_length=100, verbose_name='Номер купона/билета', unique=True)
    ticket_description = models.TextField(verbose_name='Описание купона/билета')
    ticket_price = models.CharField(max_length=100, verbose_name='Цена купона/билета', unique=True)
    ticket_kolichestvo = models.CharField(max_length=100, verbose_name='Количество купонов/билетов', unique=True)

    class Meta:
        verbose_name = 'Купон/билет'
        verbose_name_plural = 'Купоны/билеты'

    def __str__(self):
        return self.ticket_name