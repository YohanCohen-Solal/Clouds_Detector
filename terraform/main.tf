# Configure the AWS provider
provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = var.region
}


# Create an EC2 instance
resource "aws_instance" "web_server" {
  ami           = "ami-0b33d91d"
  instance_type = "t2.micro"

  # Add storage to the instance
  root_block_device {
    volume_size = "8"
  }

  # Add a security group to the instance
  vpc_security_group_ids = [aws_security_group.sg.id]

  # Add a public IP address to the instance
  associate_public_ip_address = true
}

# Create a security group
resource "aws_security_group" "sg" {
  name        = "web_server_sg"
  description = "Security group for web server"

  # Allow incoming HTTP traffic
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "local_exec" "configure_server" {
  depends_on = [aws_instance.web_server]
  command     = "ansible-playbook -i 'localhost,' -c local configure.yml"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
  acl    = "private"
}

resource "aws_s3_bucket_object" "model1" {
  bucket = aws_s3_bucket.my_bucket.id
  key    = "model1.pkl"
  source = "path/to/model1.pkl"
}

resource "aws_s3_bucket_object" "model2" {
  bucket = aws_s3_bucket.my_bucket.id
  key    = "model2.pkl"
  source = "path/to/model2.pkl"
}
