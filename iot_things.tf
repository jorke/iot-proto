resource "aws_iot_thing" "devices" {
  for_each        = toset(local.things)
  name            = "${local.name}-${each.value}"
  thing_type_name = aws_iot_thing_type.device_pub.name

  attributes = {
    "tag" = "telemetry-${each.value}"
  }
}

resource "aws_iot_certificate" "this" {
  active = true
}

resource "aws_iot_thing_principal_attachment" "this" {
  for_each  = aws_iot_thing.devices  
  principal = aws_iot_certificate.this.arn
  thing     = each.value.name
}

resource "aws_iot_thing_type" "device_pub" {
  name = "telemetry"

  properties {
    description = "a telemetry thing"
  }
}

resource "aws_iot_policy" "this" {
  name = "telemetry_policy"
  policy = jsonencode({
		Version = "2012-10-17"
		Statement = [
       {
          Action = [
            "iot:Connect",
          ]
          Effect   = "Allow"
          Resource = "arn:aws:iot:${data.aws_region.current.name}:${data.aws_caller_identity.current.id}:client/$${iot:Connection.Thing.ThingName}"
      },
      {
        Action = [
          "iot:Subscribe",
        ]
        Effect   = "Allow"
        Resource = "arn:aws:iot:${data.aws_region.current.name}:${data.aws_caller_identity.current.id}:topicfilter/$aws/things/$${iot:Connection.Thing.ThingName}/*"
      },
      {
          Action = [
            "iot:Publish",
          ]
          Effect   = "Allow"
          Resource = "arn:aws:iot:${data.aws_region.current.name}:${data.aws_caller_identity.current.id}:topic/*"
      }
		]
	}
  )
}

resource "aws_iot_policy_attachment" "thing_policy_attachment" {
  policy = aws_iot_policy.this.name
  target = aws_iot_certificate.this.arn
}
