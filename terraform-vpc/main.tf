provider "aws" {
  region = var.aws_region
}

#Create security group with firewall rules
resource "aws_security_group" "Project-SG" {
  name        = var.security_group
  description = "security group for Assignment "
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "ssh"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags= {
    Name = var.security_group
  }
}
resource "aws_instance" "ec2-instance" {
  ami           = var.ami_id
  key_name = var.key_name
  user_data = "${file("setup_ec2.sh")}"
  instance_type = var.instance_type
  security_groups= [var.security_group]
  tags= {
    Name = var.tag_name
  }
}

# Create Elastic IP address
resource "aws_eip" "instance" {
  vpc      = true
  instance = aws_instance.ec2-instance.id
tags= {
    Name = "project_elastic_ip"
  }
}

