resource "aws_timestreamwrite_database" "this" {
  database_name = "timestream-database-iot"
  tags = local.tags
}

resource "aws_timestreamwrite_table" "this" {
  table_name = local.timestream_table
  database_name = aws_timestreamwrite_database.this.database_name
  tags = local.tags
}