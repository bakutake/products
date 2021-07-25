from django.db import connection, reset_queries
import time
import functools


def query_counter(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        total_queries = len(connection.queries)
        alert = f"""
        <div class="alert alert-secondary" role="alert">
          Всего запросов: {total_queries}
          <br/>Время на выполнение запрососов: ~{(end - start):.2f}s
        </div>
        """
        result.content = alert.encode("utf-8") + result.content
        return result

    return inner_func
