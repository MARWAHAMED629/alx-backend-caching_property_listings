from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Get all properties with Redis caching for 1 hour.
    Returns cached queryset if available, otherwise fetches from database.
    """
    # Check if data is in cache
    cached_properties = cache.get('all_properties')
    
    if cached_properties is None:
        # If not in cache, fetch from database
        properties = Property.objects.all()
        # Store in cache for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
        return properties
    
    return cached_properties

def get_redis_cache_metrics():
    """
    Retrieve and analyze Redis cache hit/miss metrics.
    Returns a dictionary with cache statistics.
    """
    try:
        # Get Redis connection
        redis_client = get_redis_connection("default")
        
        # Get Redis INFO command output
        info = redis_client.info()
        
        # Extract keyspace hits and misses
        keyspace_hits = info.get('keyspace_hits', 0)
        keyspace_misses = info.get('keyspace_misses', 0)
        
        # Calculate hit ratio
        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = keyspace_hits / total_requests if total_requests > 0 else 0
        
        # Create metrics dictionary
        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'total_requests': total_requests,
            'hit_ratio': hit_ratio,
            'miss_ratio': 1 - hit_ratio if total_requests > 0 else 0
        }
        
        # Log the metrics
        logger.info(f"Redis Cache Metrics: {metrics}")
        
        return metrics
        
    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            'error': str(e),
            'keyspace_hits': 0,
            'keyspace_misses': 0,
            'total_requests': 0,
            'hit_ratio': 0,
            'miss_ratio': 0
        } 