# Movie Picture Pipeline

CI/CD for a React frontend and Flask backend on Amazon EKS via GitHub Actions + Kustomize.

 Live URLs
- Frontend (UI):  
  http://afa87dbbbbd8d47d9b25fb20d103356b-1930844682.us-east-1.elb.amazonaws.com
- Backend (API)
  http://a51902b8268ea463399d12a10dd1f6bc-9626408512.us-east-1.elb.amazonaws.com/movies



 verify 

powershell
aws eks --region us-east-1 update-kubeconfig --name cluster
curl.exe "http://a51902b8268ea463399d12a10dd1f6bc-9626408512.us-east-1.elb.amazonaws.com/movies"

note: i think this all u asked for and a picture i'll provied down