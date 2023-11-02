resource "aws_iot_topic_rule" "this" {
  name        = "proto_rule"
  description = "Protocol Buffer rule"
  enabled     = true
  sql         = <<EOT
SELECT VALUE decode(encode(*, 'base64'), "proto", "${aws_s3_bucket.this.bucket}", "protobuf/filedescriptor.desc", "Measurements.proto", "Measurement")
FROM
  '${local.ingest_topic}'
EOT
  sql_version = "2016-03-23"
# WHERE
#   decode(encode(*, 'base64'), "proto", "${aws_s3_bucket.this.name}", "protobuf/filedescriptor.desc", "Measurements", "Measurement").name = 'hello'
  # sns {
  #   message_format = "RAW"
  #   role_arn       = aws_iam_role.role.arn
  #   target_arn     = aws_sns_topic.mytopic.arn
  # }

  # error_action {
  #   sns {
  #     message_format = "RAW"
  #     role_arn       = aws_iam_role.role.arn
  #     target_arn     = aws_sns_topic.myerrortopic.arn
  #   }
  # }
  timestream {
    database_name = aws_timestreamwrite_database.this.database_name
    role_arn = aws_iam_role.topic_role.arn
    table_name = local.timestream_table
    dimension {
      name = "name"
      value = "name"
    }
  }
  republish {
    role_arn = aws_iam_role.topic_role.arn
    topic = local.decoded_topic
  }
  tags = local.tags
}
