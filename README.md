<h1> Containerizing a simple Python flask application and pushing to AWS ECR using OIDC</h1>
	
<h3>What is needed;</h3>

AWS account and I created an ECR repository which I will push my image to

docker installed- Linux (Docker desktop for Mac and Windows users)

create an OIDC from the IAM console

create an IAM role that is integrated with the created 

a Github account for the pipeline

- In the project folder activate a virtual environment, which is best for dependency isolation.

            python -m venv venv
  
           venv\Scripts\activate
  
  Or 
        Cd into the scripts and activate the environment. Give a space after the dot
         Don't forget to cd back into your project folder

- Install flask
  
       Pip install flask

- Run the app

      Python main.py
 check your application locally localhost:port if it's running.
CONGRATULATIONS! You have created a basic flask application
Deactivate 

- Create a Dockerfile in the same directory as the application. Build your image
  
	     docker buildx build -t myapp .
  
	     docker ls

- you can run a container to also check that all is working fine
  
	    docker run -d -p 5000:5000  myapp .
	
- Commit to your desired VSC  and in the repo settings>>secrets>> add any secret like account ID etc.
  
	
I have other ideas to enhance your application, but that is not the focus for now. The focus is to dockerize an application and push it to AWS ECR.


1. Create additional routes for different pages.
2. Use Flask templates (Jinja2) to render dynamic HTML content.
3. Incorporate a database (e.g., SQLite, MySQL, or PostgreSQL) to store and retrieve data.
4. Implement user authentication and authorization.
5. Deploy your Flask app to a web hosting service or cloud platform.


<h2>Building Flask Web Application, Dockerize and Push to AWS Elastic Container Registry</h2>

 The real idea of this project was to authenticate securely to our cloud environments with OpenID connect using a GitHub actions workflow. Hardcoding values like 
 access keys in my opinion are violating the least privileged rule by increasing the scope of Github's permission to access AWS resources. Let us walk through
 integrating OpenID connect into GitHub actions workflows to securely authenticate with cloud providers like AWS for
 example. OpenID Connect (OIDC) ensures GitHub Actions workflows can access resources in Amazon Web Services (AWS), 
 without the need to store the AWS credentials as long-lived GitHub secrets. Using an IAM role and an identity
 provider we can generate temporary credentials 


1. Create an identity provider for AWS
   

   Open AWS Console -> Identity and Access Management (IAM) -> Identity providers -> Add Provider


       Provider URL: https://token.actions.githubusercontent.com
       Audience:sts.amazonaws.com

3. Create an IAM role for GitHub actions to assume.
   
   This role will specify the permissions and policies for your AWS resources. In this case, we are working
   with AWS ECR. still on the IAM console, click on roles>>>create>>>web identity>>> choose the identity you created
   populate the other fields, and add the organization, repo, and branch you want to push from>>>> Next then give your role a name and create.

       githubactions-role = arn:aws:iam::${{ secrets.AWS_ACCOUNT_ID }}:role/githubactions-role
   
   Note: give your role permissions awsfullaccess/awsec2containerregistryfullaccess/EC2InstanceProfileForImageBuilderECRContainerBuilds.

   add this role to your workflow. I would not go into the details of the actions workflow because that is the focus today.
   You can decide to make your entire role a secret in GitHub or just your account ID in the role arn. If your workflow is on a push then
   you should get your actions triggered. Once your pipeline is completed you can check your repo to see your image.

