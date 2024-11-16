<h1> Containerizing a simple Python flask application and pushing to AWS ECR using OIDC</h1>
	
- What is needed;
	AWS account and I created an ECR repository which I will push my image to
	docker installed- Linux (Docker desktop for Mac and Windows users)
	create an OIDC from the IAM console
	create an IAM role that is integrated with the created 
	a Github account for this demonstration

- In my project folder I activated a virtual environment, best for dependency isolation.

 python -m venv venv
venv\Scripts\activate
Or 
Cd into the scripts and activate the environment. Do well to give a space after the .
Don't forget to cd back into your project folder

- Install flask
Pip install flask

- Run the app

Python main.py

Deactivate 
CONGRATULATIONS! You have created a basic flask application

- Create a Dockerfile in the same directory as the application. Build your image
	     docker buildx build -t myapp .
	     docker ls

- Run a container 
	    docker run -d -p 5000:5000  myapp .
	
- Commit to your desired VSC  and in the repo settings>>secrets>> add any secret
	
Other ideas to enhance your application is to but that is not my focus. The idea is to dockerize an application and push to AWS ECR 

	

1. Create additional routes for different pages.
2. Use Flask templates (Jinja2) to render dynamic HTML content.
3. Incorporate a database (e.g., SQLite, MySQL, or PostgreSQL) to store and retrieve data.
4. Implement user authentication and authorization.
5. Deploy your Flask app to a web hosting service or cloud platform.


Building a Flask Web Application: A Step-by-Step Guide for Beginners | by Nat A Hill | Medium

 that is not the focus of this post. I want containerize this application and push to an AWSECR repo. The real thing i wanted to share securely authenticating to our cloud environments with OpenID connect. security is crucial
and we don't want to make it a habit to hardcode values like access keys. i would like to walk through
integrating OpenID connect into GitHub actions workflows to securely authenticate with cloud provider using AWS as
an example

OpenID Connect (OIDC) ensures GitHub Actions workflows can access resources in Amazon Web Services (AWS), 
without the need to store the AWS credentials as long-lived GitHub secrets.Using an IAM role and an identity
provider we can generate temporary credentials 


1. Create an identity provider to AWS
Open AWS Console -> Identity and Access Management (IAM) -> Identity providers -> Add Provider


Provider URL: https://token.actions.githubusercontent.com
Audience:sts.amazonaws.com

2. Create an IAM role that you want githubactions to assume after authenticating through OIDC. 
This role will specify the permissions and policies for your AWS resources. in this case i was working
with S3 (ensure to add the neccessary permission to this role as per you use cases)

AWS_DEV_GITHUB_ACTION_ROLE = arn:aws:iam::XXXXXXXXX:role/github_s3_copy_action


Define a trust relationship in the IAM role’s policy document that specifies the OIDC identity provider
 as a trusted entity. The trust relationship document specifies who can assume the role.

"Federated": "arn:aws:iam::XXXXXXXXXXXXXX:oidc-provider/token.actions.githubusercontent.com" 
"token.actions.githubusercontent.com:sub": "repo:mahen-github/apache-spark-framework:*"

replace xxx.. with your account ID

on the console when you are creating the role you choose web identity and it will give you all the 
options to add the provider which you created earlier and when you click next you will have a policy 
generated for you. eneusre to add permisions for the role to access the resource

awsfullaccess/awsec2containerregistryfullaccess

add this role in your workflow something like this
you can decide to make your entire role a secret in github or just your account ID in the role arn
![image](https://github.com/user-attachments/assets/0f2ae571-2f45-4291-b943-d2ae58a08d94)
