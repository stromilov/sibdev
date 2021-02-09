# sibdev

<p>Для запуска необходимо все файлы поместить в одну папку:</p>
<br>
папка<br>
  |__docker-compose.yml<br>
  |__Dockerfile<br>
  |__models.py<br>
  |__admin.py<br>
  |__urls.py<br>
  |__serializers.py<br>
  |__views.py<br>
  |__deal.html<br>
  |__form.py<br>
  <br><br>
  Из командной строки перейти в папку и выполнить команду:<br>
    docker-compose up<br>
    
  Должна начаться сборка образа sibdev_sibdev.<br>
  Если сборка прошла успешно то автоматически запуститься docker-контейнер с django проектом,<br>
  который будет доступен по адресу http://127.0.0.0:8000/<br><br>
  
  <p>http://127.0.0.0:8000/admin/      - админка (логин: admin пароль: 123) </p>
  <p>http://127.0.0.0:8000/api/form/   - форма загрузки файла file.csv</p>
  <p>http://127.0.0.0:8000/api/deals/  - страница api со списком клентов</p>
  <br>
  <br>
 
