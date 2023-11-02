provider "aws" {
  region = local.region
}

provider "aws" {
  alias  = "sydney"
  region = "ap-southeast-2"
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
data "aws_availability_zones" "available" {}
data "aws_iot_endpoint" "iot_endpoint" { endpoint_type = "iot:Data-ATS" }


locals {
  region = "ap-southeast-2"
  name   = "iot-proto"

  vpc_cidr = "10.0.0.0/16"
  azs      = slice(data.aws_availability_zones.available.names, 0, 3)

#   cluster_max             = 2
#   cluster_min             = 0
#   on_demand_base_capacity = 50
#   spot_capacity           = 50
#   spot                    = true
#   allow_ips               = var.allow_ips
  // utilisation of the cluster
#   target_capacity = "100"
#   key_pair        = var.key_pair
  things = ["a", "b", "c"]
  ingest_topic = "test/all_telemetry"
  decoded_topic = "test/decoded_telemetry"
  proto_desc = "protobuf/filedescriptor.desc"
  timestream_table = "iot_telemetry"

  tags = {
    project = local.name
    Repo = "https://github.com/jorke/iot-proto"
  }
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = local.name
  cidr = local.vpc_cidr

  azs            = local.azs
  public_subnets = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k + 48)]
  map_public_ip_on_launch = true

  tags           = local.tags
}

resource "aws_iam_policy" "timestream" {
  name = "timestream"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action =[
          "timestream:WriteRecords"
        ]
        Effect = "Allow"
        Resource = "arn:aws:timestream:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:database/${local.timestream_table}/DB/table/main_table"
      },
      {
        Action = [
          "timestream:DescribeEndpoints",
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role" "topic_role" {
  name               = "timestream_write"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "iot.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "policy_attach" {
  role       = aws_iam_role.topic_role.name
  policy_arn = aws_iam_policy.timestream.arn
}



output "endpoint" {
	value = data.aws_iot_endpoint.iot_endpoint.endpoint_address
}