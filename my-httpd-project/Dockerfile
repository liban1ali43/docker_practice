FROM redhat/ubi9:latest
WORKDIR /var/www/html
RUN dnf -y install httpd \
    && dnf clean all
COPY index.html .
EXPOSE 8080
RUN sed -i 's/^Listen 80$/Listen 8080/' /etc/httpd/conf/httpd.conf
CMD ["httpd", "-D", "FOREGROUND"]   