terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.38"
    }
  }
}
 
provider "aws" {
  profile = "default"
  region  = var.aws_region
}
