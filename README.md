# 💰 Automated AWS Cost Optimizer

Automatically stops idle Amazon EC2 instances using AWS Lambda and Amazon CloudWatch Alarm to reduce unnecessary AWS costs.

---

## 📌 Project Overview

Cloud resources that remain running without workloads generate unnecessary costs.

This project monitors the CPU utilization of an EC2 instance. If CPU usage remains below a specified threshold for a defined period, CloudWatch triggers a Lambda function that automatically stops the EC2 instance.

---

## 🎯 Objective

Reduce AWS costs by automatically stopping idle EC2 instances.

---

## 🧰 AWS Services Used

- Amazon EC2
- AWS Lambda
- Amazon CloudWatch
- IAM

---

## ⚙️ Architecture

EC2 Instance

↓

CloudWatch Alarm

↓

Lambda Function

↓

Stop EC2 Instance

---

## 📂 Workflow

1. Launch an EC2 instance.
2. Create an IAM Role for Lambda.
3. Develop a Lambda function using Python.
4. Create a CloudWatch Alarm.
5. Monitor EC2 CPU Utilization.
6. Trigger Lambda when CPU usage is below the threshold.
7. Lambda stops the EC2 instance automatically.
8. CloudWatch Logs record the execution.

---

## 📊 CloudWatch Alarm Configuration

Metric:
CPUUtilization

Namespace:
AWS/EC2

Statistic:
Average

Threshold:
Less than 5%

Evaluation Period:
5 Minutes

Action:
Invoke Lambda Function

---

## 🔐 IAM Permissions

The Lambda execution role requires:

- EC2FullAccess
- CloudWatch Logs permissions

or the following actions:

- ec2:StopInstances
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

## 🐍 Lambda Function

The Lambda function:

- Receives the CloudWatch event
- Extracts the EC2 Instance ID
- Stops the EC2 instance using boto3

---

## 📸 Screenshots

### Architecture

![Architecture](screenshots/01-architecture.png)

### EC2 Instance

![EC2](screenshots/02-ec2-instance.png)

### CloudWatch Alarm

![Alarm](screenshots/03-cloudwatch-alarm.png)

### Lambda Function

![Lambda](screenshots/04-lambda-function.png)

### IAM Role

![IAM](screenshots/05-iam-role.png)

### Alarm Action

![Action](screenshots/06-alarm-action.png)

### Instance Running

![Running](screenshots/07-instance-running.png)

### Instance Automatically Stopped

![Stopped](screenshots/08-instance-stopped.png)

### CloudWatch Logs

![Logs](screenshots/09-cloudwatch-logs.png)

---

## 🚀 Results

✅ Automatic monitoring

✅ Automatic EC2 shutdown

✅ Reduced AWS costs

✅ No manual intervention

---

## 📈 Future Improvements

- Start instances automatically during office hours
- Email notifications using Amazon SNS
- Slack notifications
- Support multiple EC2 instances
- Tag-based instance management

---

## 👨‍💻 Author

Your Name

GitHub:
https://github.com/Kartiks18