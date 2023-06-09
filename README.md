# RBK_TEST			
									
## Наглядно представить ТОП-20 материалов по просмотрам за неделю:								
1.	Оформить ТОП-20 в виде таблицы с заголовками материалов, при этом заголовок необходимо сделать активной ссылкой с возможностью перехода на статью на сайте (адрес страницы - столбец URL на листе База публикаций);								
2.	Визуализировать полученные данные								
3.	Все этапы выполнения задания должны быть сохранены в файле или описаны отдельно;								
									
### Обратите внимание: 
У каждой публикации есть уникальный id, который находится в конце адреса страницы (например, 5c4af9ed9a7947bd94fe0cc9), при этом полный адрес страницы может отличаться.								
									
	Из отчёта должны быть исключены просмотры, содержащие след. URL: 								
	test.pro								
	test.v2.pro								
	feature-rbcnews								
	/preview/								
	staging.pro								
	staging.v2.pro								
									
	Лист База публикаций - список опубликованных материалов со ссылками на сайт и заголовками								
	Лист Выгрузка - данные по просмотрам материалов за отчётный период								
									
###  Этапы выполнения задания:
1.  Код загружает данные из двух листов в Excel-файле ('Выгрузка' и 'База публикаций') в объекты Pandas DataFrame;
2. Обрабатывает данные о просмотрах (сохраненные в xlsx) и исключает из них записи, содержащие определенные шаблоны символов;
3. Объединяется и группируется по идентификаторам статей и заголовкам материалов, а также суммируются просмотры каждой статьи. Конечный результат - таблица с топ-20 статей по количеству просмотров;
4. Создается динамическая визуализация данных, в виде столбчатой диаграммы, построенной по этой таблице топ-20 статей. График дополнительно настраивается по размерам и расположению осей;
5. Последние три строки добавляют кликабельные ссылки на заголовки статей, а затем выводят таблицу (с кликабельными ссылками) или график в файл result.html. В случае отсутствия у статей ссылок на их адреса просто выводится текст таблицы без столбца "URL к материалу".              
                 
<image src="/myplot.png" alt="Визуализация">
