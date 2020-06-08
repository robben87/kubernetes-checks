yum install python3-pip.noarch <br>
pip3 install --user pipenv <br>
 <br>
export PATH=~/.local/bin:$PATH <br>
 <br>
cd in directory script
 <br>
pipenv install
 <br>
pip3 install pipenv-shebang   #Link --> https://github.com/laktak/pipenv-shebang <br>
Output Similar to:

    Creating a virtualenv for this project…
    Pipfile: /root/kubernetes-check/Pipfile
    Using /usr/bin/python3 (3.6.8) to create virtualenv…
    ⠴ Creating virtual environment...created virtual environment CPython3.6.8.final.0-64 in 266ms
      creator CPython3Posix(dest=/root/.local/share/virtualenvs/kubernetes-check-GK_gVvOF, clear=False, global=False)
      seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/root/.local/share/virtualenv/seed-app-data/v1.0.1)
      activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
    
    ✔ Successfully created virtual environment! 
    Virtualenv location: /root/.local/share/virtualenvs/kubernetes-check-GK_gVvOF
    Creating a Pipfile for this project…
    Installing kubernetes…
    Adding kubernetes to Pipfile's [packages]…
    ✔ Installation Succeeded 
    Installing numpy…
    Adding numpy to Pipfile's [packages]…
    ✔ Installation Succeeded 
    Installing pandas…
    Adding pandas to Pipfile's [packages]…
    ✔ Installation Succeeded 
    Pipfile.lock not found, creating…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    ✔ Success! 
    Updated Pipfile.lock (778713)!
    Installing dependencies from Pipfile.lock (778713)…
         ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 20/20 — 00:00:09
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
	
```
Usage:
    [root@machine ~]# ~/kubernetes-check/nagios_check.py
    usage: nagios_check.py [-h] {node,pod} ...
    
    positional arguments:
      {node,pod}
        node      check_nodes status)
        pod       check_pods status
    
    optional arguments:
      -h, --help  show this help message and exit



    [root@machine ~]# ~/kubernetes-check/nagios_check.py pod --config config
	
    [root@machine ~]# ~/kubernetes-check/nagios_check.py node --config config
```
