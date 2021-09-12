resource "aws_instance" "instance" {
  ami                         = var.instance_ami
  availability_zone           = "${var.aws_region}${var.aws_region_az}"
  instance_type               = var.instance_type
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.sg.id]
  subnet_id                   = aws_subnet.subnet.id
  key_name                    = "t430"

  root_block_device {
    delete_on_termination = true
    encrypted             = false
    volume_size           = var.root_device_size
    volume_type           = var.root_device_type
  }

  tags = {
    "Owner"               = var.owner
    "Name"                = "${var.owner}-instance"
    "KeepInstanceRunning" = "false"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} > ec2_public_ip.txt"
  }
}


resource "aws_key_pair" "ssh-key" {
  key_name   = "t430"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrSu3aXjpWdmCHYvYOwtrlBUamnUJawjublrGM0SSzV3SVA0RMPU+o+eSqU1YTUH/XP15PAUZSo17rTFPjTLBXTJ5A7W8gnPJuWiRd1IiIdzpqEuUOhC0Oq5lcdlMkJ8O+/Y8IsJbvnWO29hdwzxxA50KEYOu1vI0AU4m6jUuDfT8CcSjpmUK5+xrO2pGZNFZtX+D7t/yzJHO1DY/DWJLBxvaPZZMAJd8uv/4PIxD7F9ZnWv7RxW+TkWvsGHOwsh1wGue9sG6JF91ZPpq/maWT/vzwGQxtGZzr+S2XsfCZnI7/a8gD3GFxfUVHU1XVlvEEbFzz51E+VH5Igbz1hwij michaelbest55@hotmail.com"
}
