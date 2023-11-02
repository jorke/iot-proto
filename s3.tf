resource "aws_s3_bucket" "this" {
  bucket = "${local.name}-${data.aws_region.current.name}"
  tags = local.tags
}

resource "aws_s3_bucket_object" "filedesc" {
  bucket = aws_s3_bucket.this.id
  key = "/${local.proto_desc}"
  source = "./${local.proto_desc}"
  etag = filemd5("./${local.proto_desc}")
}

resource "aws_s3_bucket_policy" "iot" {
  bucket = aws_s3_bucket.this.id
  policy = data.aws_iam_policy_document.iot.json
}

data "aws_iam_policy_document" "iot" {
  statement {
    principals {
      type        = "Service"
      identifiers = ["iot.amazonaws.com"]
    }
    actions = ["s3:GetObject"]
    resources = [
      "${aws_s3_bucket.this.arn}/${local.proto_desc}",
    ]
  }
}
