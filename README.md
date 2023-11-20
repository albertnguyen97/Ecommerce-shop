# Ecommerce-shop
Django, Reactjs, mysql

<h1>Database:</h1>

sudo apt update<br>
sudo apt install mysql-server -y<br>
sudo mysql_secure_installation<br>
sudo mysql -u root -p<br>
CREATE USER 'bigcat'@'localhost' IDENTIFIED BY 'yourpassword';<br>
CREATE DATABASE djangodb;<br>
GRANT ALL PRIVILEGES ON djangodb.* TO 'bigcat'@'localhost';<br>
FLUSH PRIVILEGES;<br>
EXIT;<br>
