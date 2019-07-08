FROM python:3.7.3-alpine

COPY ./ /app

RUN apk --update add --no-cache --virtual .build-deps \
        git build-base mariadb-dev && \
    pip --no-cache-dir install -r /app/requirements.txt && \
    apk del .build-deps && \
    apk -q --no-cache add mariadb-dev su-exec nginx supervisor curl

RUN chown -R nobody:nogroup /app && \
  python /app/manage.py collectstatic --noinput && \
  mv /app/nginx.conf /etc/nginx/conf.d/default.conf &&\
  mkdir -p /etc/supervisor.d && \
  mkdir -p /run/nginx && \
  mv /app/webapp.ini /etc/supervisor.d/

EXPOSE 8000 
EXPOSE 80
WORKDIR /app

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1
    
CMD ["/usr/bin/supervisord"]