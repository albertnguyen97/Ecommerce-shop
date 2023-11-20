# Ecommerce-shop
Django, Reactjs, mysql

<h5>Database:</h5>

sudo apt update
sudo apt install mysql-server -y
sudo mysql_secure_installation
sudo mysql -u root -p
CREATE USER 'bigcat'@'localhost' IDENTIFIED BY 'yourpassword';
CREATE DATABASE djangodb;
GRANT ALL PRIVILEGES ON djangodb.* TO 'bigcat'@'localhost';
FLUSH PRIVILEGES;
EXIT;
