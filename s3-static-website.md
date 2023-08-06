S3

1- create bucket with same name as your registered domain
2- uncheck "Block public acess"
3- go to properties and enable static website hosting
4- add an index.html and a error.html
5- we still can visualize the contents, beacuse we dont have the permissions to interact with the object within the bucket
6- to create a bucket policy we go to permissions

JSON policy:

```{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::your-bucket-name/*"]
    }
  ]
}


7- Acess your website trhough the Bucket website endpoint 

Route 53
1- If we register a domain using Route 53 and if the bucket name is the same as the DNS name we want to use
2- Go to hosted zone, you should have one that matches the domain you registered
3- Go inside and create a record
4- Simple routing record, defining the record we can specify a subdomain
5- in Value/Route traffic to, we gonna choose "Alias to s3 website endpoint", choose the same region as the bucket, and finaly choose your bucket.
6- create record, and after a couple second you can finaly acess your bucket by the full DNS name
!! important -> in order to everything work, we should create the S3 bucket with the same name as this domain name

Cloudfront
Currently we have two problems
1- Anyone outside the region where our bucket is, will have a suboptimal experience
2- we cant deliever the site, using https, only http

Cloudfront job is to cache objects from one or more origins, wo when creating a distribution we need to specify origin domain name.

S3 Website Endpoint:
When you enable static web hosting on an S3 bucket, AWS assigns a unique website endpoint to that bucket. This endpoint allows you to access your static website directly from the S3 bucket without going through CloudFront. The URL of the website endpoint typically looks like this: "http://bucket-name.s3-website.region.amazonaws.com".

S3 Bucket Endpoint:
Every S3 bucket has a default bucket endpoint that follows a specific format: "http://bucket-name.s3.amazonaws.com". This endpoint can be used to access any content stored in the bucket, including static website files.

Viewer protocol policy -> redirect HTTP to HTTPS

INVALIDATIONS
When working with edge location, we might have update a file, and the content we deliever be outdated, beacause what is being displayed is in cache in edge location. we can improve this with invalidations:
- use absolute path for a specific file
- use /* to invalidate everything
in this way everytime we update something in our code, the content delievered will be direct from the origin

SSL certificate
In order to use https, we need a SSL certificate, and for that we will use ACM (AWS Certificate Manager)
1- Choose an alternate domain name (CNAME) to associate with the distribution -> like a prefix for your root domain (eg. root domain = nunocsilva.com -> www.nunocsilva.com)
2- Request certificate:
    1- Request public certificate
    2- In fully qualified domain name put the domain you just choosed
    3- Validation method:
        1-DNS validation -> we will be given a DNS record, that we need to add to our domain, and Route53 will query to check if the record is there, this way it will know if you control the domain.
        After request, open the certificate and click "Create record in route 53", to create the CNAME record within route53
        2- email
NOTE: the name in the certificate should match the name on domain within the certificate, that needs to match the DNS name, that need to match the certificate on the cloudfront distibution

now if we go to our domain in route 53 we can see the CNAME record there.
Finally in the cloudfront distribution editing, we can choose the certificate created, save changes
This willl deploy the certificate and configurations to the entire CloudFront network

After deployment completed, go to your domain in route 53, create a record, simple routing, name the record the same as the one we created the certificate for. 
    1- record type - A
    2- endpoint - Alias to Cloudfront distribution 

Now we can acess https://www.nunocsilva.com, with this being loaded from Cloudfront using HTTPS, using a custom name and a custom SSL certificate

Using Origin Access Control (OAC) ->restrict S3 origin to be only acessed by Cloudfront distribution
Editing our distribution, we can configure origin acess control settings, create a control setting and copy the policy Cloudfront gives us to update the S3 bucket policy.
This way, any acess direct to S3 will be denied, leaving only acess to be made through Cloudfront distribution