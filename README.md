# AI_ANALAYZER_SERVICE

## Описание

**XML Parser & AI Analyzer Service** — это микросервис, который ежедневно загружает XML-файл с данными о продажах, обрабатывает его и формирует аналитический отчет с помощью Large Language Model (LLM). Отчет сохраняется в базе данных для дальнейшего анализа.

## Технологии

- **Backend**: FastAPI
- **Планировщик задач**: Celery
- **Очередь сообщений**: RabbitMQ
- **База данных**: PostgreSQL
- **Аналитика**: Large Language Model

---

## Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/dmitrylukoninpy/xml-analyzer-service.git
cd xml-analyzer-service
```
### 2. Заполнения конфиг файла [.env_template](.env_template)
### 3. Переименовать конфиг файл
```bash
mv .env_template .env
```
### 4. Запуск
```bash
docker compose up  --build 2>&1 | tee build.log
```
### 5. Остановка
```bash
docker down --rmi all
```