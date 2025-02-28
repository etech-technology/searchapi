# search-app
final training project

# Search API Project

This project provides a **FastAPI-based Search API** deployed on **AWS EKS** using **Helm, Terraform, and GitHub Actions CI/CD**.  
It includes **PagerDuty alerting** whenever a name check request is made.

---

## Features
1.**FastAPI** for a simple search API  
2.**Helm Chart** for Kubernetes deployment  
3.**GitHub Actions** for CI/CD  
4.**AWS ECR & EKS** for container management  
5.**Terraform** for infrastructure as code  
6.**PagerDuty Integration** for alerting on search requests  

---
## secrets to configure

Secret Name	Description
AWS_ACCESS_KEY_ID	--> AWS Access Key for authentication
AWS_SECRET_ACCESS_KEY	--> AWS Secret Access Key
AWS_REGION	--> AWS region where EKS and ECR are deployed (e.g., us-east-1)
AWS_ECR_REGISTRY	--> Amazon ECR registry URL (e.g., <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com)
PAGERDUTY_ROUTING_KEY	--> PagerDuty integration key for alerts
EKS_CLUSTER_NAME	--> Name of the EKS cluster (e.g., search-cluster)


