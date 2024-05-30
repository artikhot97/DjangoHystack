# DjangoHystack

Document 
https://django-haystack.readthedocs.io/en/master/tutorial.html#installation

This repository for the create Django-hystack with the elasticsearch.

Steps:
1. Git clone repo
2. create virtualenv into you systme - py -m venv <name_venv>
3. Install reqired libaries from the req.txt
4. Then py .\manage.py rebuild_index
5. Then py .\manage.py runserver
6. py .\manage.py createsuperuser - create superuser and enter data for the note
7. Go to the browser and enter http://127.0.0.1:8000/search. But before that make sure your elasticsearch is working on your system if not then please do it first
  - For windows - https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html
  - For Linux - https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html#elasticsearch-install-packages

    After sucessfull installation on elasticsearch hit the localhost:9200 which is default for the elasticsearch and make sure that this url returns result someting like this
    
"{
  "name" : "AIPL8186L",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "1Nbr9tIPSumGoiq54K2Zg",
  "version" : {
    "number" : "7.17.9",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "ef48222227ee6b70e502f0f0aa52435ee634d",
    "build_date" : "2023-01-31T05:34:43.3517834Z",
    "build_snapshot" : false,
    "lucene_version" : "8.11.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}"

You will see the output like this

![image](https://github.com/artikhot97/DjangoHystack/assets/61792772/65c2bf67-6f71-4ce8-8628-15bc17057654)
