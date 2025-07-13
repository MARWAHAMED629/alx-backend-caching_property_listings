# ALX Backend Caching Property Listings

A Django project that demonstrates various caching strategies for a property listings application using Redis and PostgreSQL.

## Features

- **Django Property Listings App**: Complete CRUD operations for property management
- **Redis Caching**: Multiple caching strategies implemented
- **PostgreSQL Database**: Robust data storage
- **Docker Support**: Easy deployment with Docker Compose
- **Cache Metrics**: Redis performance monitoring

## Project Structure

```
alx-backend-caching_property_listings/
├── alx_backend_caching_property_listings/  # Main Django project
│   ├── settings.py                         # Django settings with Redis/PostgreSQL config
│   └── urls.py                             # Main URL configuration
├── properties/                             # Properties app
│   ├── models.py                           # Property model
│   ├── views.py                            # Views with caching decorators
│   ├── urls.py                             # App URL configuration
│   ├── utils.py                            # Cache utilities and metrics
│   ├── signals.py                          # Cache invalidation signals
│   ├── apps.py                             # App configuration
│   └── management/commands/                # Django management commands
│       └── show_cache_metrics.py           # Cache metrics command
├── docker-compose.yml                      # Docker services configuration
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- pip

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd alx-backend-caching_property_listings
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Docker services**
   ```bash
   docker-compose up -d
   ```

4. **Run Django migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## Caching Implementation

### 1. View-Level Caching (Task 1)
- **File**: `properties/views.py`
- **Implementation**: `@cache_page(60 * 15)` decorator
- **Cache Duration**: 15 minutes
- **Endpoint**: `GET /properties/`

### 2. Low-Level Caching (Task 2)
- **File**: `properties/utils.py`
- **Function**: `get_all_properties()`
- **Cache Duration**: 1 hour (3600 seconds)
- **Cache Key**: `'all_properties'`

### 3. Cache Invalidation (Task 3)
- **File**: `properties/signals.py`
- **Triggers**: Property create/update/delete
- **Action**: Automatically deletes `'all_properties'` cache

### 4. Cache Metrics (Task 4)
- **File**: `properties/utils.py`
- **Function**: `get_redis_cache_metrics()`
- **Metrics**: Hit ratio, miss ratio, total requests
- **Command**: `python manage.py show_cache_metrics`

## API Endpoints

### Property Listings
- **URL**: `GET /properties/`
- **Response**: JSON array of properties
- **Caching**: 15-minute page cache + 1-hour queryset cache

### Cache Metrics
- **Command**: `python manage.py show_cache_metrics`
- **Output**: Redis performance statistics

## Database Schema

### Property Model
```python
class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

## Docker Services

### PostgreSQL
- **Image**: `postgres:latest`
- **Port**: `5432`
- **Database**: `property_db`
- **User**: `property_user`
- **Password**: `property_pass`

### Redis
- **Image**: `redis:latest`
- **Port**: `6379`
- **Database**: `1` (for Django cache)

## Configuration

### Django Settings
- **Database**: PostgreSQL with psycopg2
- **Cache Backend**: Redis with django-redis
- **Cache Location**: `redis://redis:6379/1`

### Environment Variables
Set these in your environment or docker-compose.yml:
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password

## Testing

1. **Start the services**
   ```bash
   docker-compose up -d
   python manage.py runserver
   ```

2. **Test the API**
   ```bash
   curl http://localhost:8000/properties/
   ```

3. **Check cache metrics**
   ```bash
   python manage.py show_cache_metrics
   ```

## Cache Strategy Summary

1. **Page-Level Caching**: 15-minute cache for the entire view response
2. **Queryset Caching**: 1-hour cache for database queries
3. **Automatic Invalidation**: Cache cleared on model changes
4. **Performance Monitoring**: Real-time cache hit/miss metrics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is part of the ALX Backend Development curriculum. 