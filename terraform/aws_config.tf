terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.38"
    }
  }

  required_version = "~> 0.15.3"

  backend "remote" {
    organization = "michaelbest55"

    workspaces {
      name = "kafka_cdc_project"
    }
  }

  provider "aws" {
    profile = "default"
    region  = var.aws_region
  }
}