copy python  file  under  /home/username/my_project/cgi-bin  directory  
copy index.html  under the  /var/www/html 
sudo vi /etc/apache2/conf-available/serve-cgi-bin.conf  
-----------------------------------------------------------  
ScriptAlias /cgi-bin/ /home/username/my_project/cgi-bin/  
<Directory "/home/username/my_project/cgi-bin/">  
        AllowOverride None  
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch  
        Require all granted  
</Directory>  
-------------------------------------------------------------  
pip install  xxx   after next   
   python3 -m venv .venv  
   source .venv/bin/activate  
