<img width="1343" height="309" alt="Structure" src="https://github.com/user-attachments/assets/480ffde6-e0e4-4485-aa1b-3b8d22942ddb" />
<img width="1906" height="960" alt="ec2" src="https://github.com/user-attachments/assets/1db858d0-0e64-4167-9db9-95a8ee8d5e95" />
<img width="1911" height="966" alt="ec2_role" src="https://github.com/user-attachments/assets/1bf53539-3abf-4d50-88a4-2bd9902752dc" />
<img width="1902" height="948" alt="lambda" src="https://github.com/user-attachments/assets/dafe95a0-3413-4175-b4ac-3578a525b59d" />
<img width="1918" height="986" alt="lambda_code" src="https://github.com/user-attachments/assets/8a357bb9-ac14-4404-83e7-d1de3f4ace5c" />
<img width="1915" height="917" alt="lambda_test" src="https://github.com/user-attachments/assets/03db0e7e-67d4-4d39-87e9-86e6ff5475b0" />
<img width="1875" height="916" alt="EC2_stop" src="https://github.com/user-attachments/assets/806c2055-ccbf-4e6a-b245-2b6487a7ec81" />
<img width="1912" height="927" alt="Alarm_setting" src="https://github.com/user-attachments/assets/6475d0ef-357b-4a19-98ad-c820671765c5" />
<img width="1654" height="649" alt="Alarm_action" src="https://github.com/user-attachments/assets/a0d3f1aa-b561-4b57-b7d7-a4d27e629ce9" />
<img width="1901" height="900" alt="Alarm_trigger" src="https://github.com/user-attachments/assets/25890101-0599-4c37-9a05-f9814df38242" />



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
