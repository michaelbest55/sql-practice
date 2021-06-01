# General information
 
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-2"
}
 
variable "owner" {
  description = "Configuration owner"
  type        = string
  default     = "kafka-cdc"
}
 
variable "aws_region_az" {
  description = "AWS region availability zone"
  type        = string
  default     = "a"
}
 
 
# VPC variables
 
variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}
 
variable "vpc_dns_support" {
  description = "Enable DNS support in the VPC"
  type        = bool
  default     = true
}
 
variable "vpc_dns_hostnames" {
  description = "Enable DNS hostnames in the VPC"
  type        = bool
  default     = true
}
 
 
# Security Group variables
 
variable "sg_ingress_proto" {
  description = "Protocol used for the ingress rule"
  type        = string
  default     = "-1"
}
 
variable "sg_ingress_ssh" {
  description = "Port used for the ingress rule"
  type        = string
  default     = "0"
}
 
variable "sg_egress_proto" {
  description = "Protocol used for the egress rule"
  type        = string
  default     = "-1"
}
 
variable "sg_egress_all" {
  description = "Port used for the egress rule"
  type        = string
  default     = "0"
}
 
variable "sg_egress_cidr_block" {
  description = "CIDR block for the egress rule"
  type        = string
  default     = "0.0.0.0/0"
}
 
 
# Variables for Subnet
 
variable "sbn_public_ip" {
  description = "Assign public IP to the instance launched into the subnet"
  type        = bool
  default     = true
}
 
variable "sbn_cidr_block" {
  description = "CIDR block for the subnet"
  type        = string
  default     = "10.0.1.0/24"
}
 
 
# Route Table Variables
 
variable "rt_cidr_block" {
  description = "CIDR block for the route table"
  type        = string
  default     = "0.0.0.0/0"
}
 
 
# Variables for Instance
 
variable "instance_ami" {
  description = "ID of the AMI used"
  type        = string
  default     = "ami-06dc09bb8854cbde3"
}
 
variable "instance_type" {
  description = "Type of the instance"
  type        = string
  default     = "t2.large"
}
 
 
variable "root_device_type" {
  description = "Type of the root block device"
  type        = string
  default     = "gp2"
}
 
variable "root_device_size" {
  description = "Size of the root block device"
  type        = string
  default     = "8"
}
