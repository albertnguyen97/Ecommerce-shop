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
pip install pymysql<br>

pip install pymysql<br>

Then, edit the __init__.py file in your project origin dir(the same as settings.py)<br>
add:<br>
import pymysql<br>
pymysql.install_as_MySQLdb()<br>

pip install cryptography<br>

social-auth-account<br>
pip install social-auth-app-django<br>
