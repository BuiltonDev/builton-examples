# User Created > WhatsApp Message (with Twilio)

This example demonstrates how to send a WhatsApp welcome message whenever a new user registers to your company on BuiltOn.
It uses the [BuiltOn](https://builton.dev) webhooks, a [Twilio account](https://www.twilio.com/) and the [Serverless](https://serverless.com) framework to create an [AWS Lambda](https://aws.amazon.com/lambda/) function.

# Install Locally

In order to run this example locally, you need to:

1. Clone this repository, and run `npm install`

2. Install the serverless framework globally with `npm install -g serverless`

3. Set up your AWS Credentials. [More information here](https://serverless.com/framework/docs/providers/aws/guide/credentials/).

4. Create a [Twilio account](https://www.twilio.com/), create a [Twilio Sandbox for WhatsApp](https://www.twilio.com/console/sms/whatsapp/learn) and join the sandbox by following the insctructions.

5. Create a Builton Webhook on your dashboard with the event type `user.created`.

6. Add a `secrets.dev.json` file containing your Builton Webhook Secret, your Twilio Account SID and your Twilio Auth Token. You can find there your Twilio keys on [this page](https://www.twilio.com/console/project/settings). Use the `secrets.example.json` as a template.

7. Use `serverless offline` to run the service locally or `serverless deploy` to run it on AWS.
