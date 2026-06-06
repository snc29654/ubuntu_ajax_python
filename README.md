python  file  is under  /home/username/my_project/cgi-bin  directory  
sudo vi /etc/apache2/conf-available/serve-cgi-bin.conf  
-----------------------------------------------------------  
ScriptAlias /cgi-bin/ /home/username/my_project/cgi-bin/  
<Directory "/home/username/my_project/cgi-bin/">  
        AllowOverride None  
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch  
        Require all granted  
</Directory>  
-------------------------------------------------------------  
pip install  xxx   before next   
   python3 -m venv .venv  
   source .venv/bin/activate  
