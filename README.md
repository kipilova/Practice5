# Практика 5 - Использование Docker в приложении Flask с БД

## Развертывание решения:

1. Установка Docker и Docker Compose.
2. Запуск проекта с помощью Docker Compose.
   
docker-compose -p <app_name> up --build

4. Тестирование приложения.
Приложение будет доступно по ссылке http://localhost:5000

![image](https://github.com/user-attachments/assets/7de28789-b2ff-4d62-af17-d5f759e1dadc)

Для просмотра базы данных в браузере нужно перейти по ссылке: http://localhost:5000/data

![image](https://github.com/user-attachments/assets/ba4c6366-3c97-46a9-9213-742454065d8f)

Базу данных можно также просмотреть в терминале с помощю команд.
Для этого необходимо ввести 

docker exec -it <app_name>-db-1 psql -U postgres -d counter_db

а затем 

SELECT * FROM "table_Counter";

![image](https://github.com/user-attachments/assets/8f3606dc-6f7a-470a-acba-c910b4a3c932)

4. Остановка и удаление контейнеров.

docker-compose -p <app_name> down

docker volume rm <app_name>_pgdata





