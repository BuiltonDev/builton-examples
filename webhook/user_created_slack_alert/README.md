# User Created > Slack Alert

This example demonstrates how to send yourself a Slack Alert whenever a new user registers to your BuiltOn company.
It uses the [BuiltOn](https://builton.dev) webhooks, a custom [Slack App](https://api.slack.com/apps) and the [Serverless](https://serverless.com) framework to create an [AWS Lambda](https://aws.amazon.com/lambda/) function.

# Install Locally

In order to run this example locally, you need to:

1. Clone this repository, and run `npm install`

2. Install the serverless framework globally with `npm install -g serverless`

3. Set up your AWS Credentials. [More information here](https://serverless.com/framework/docs/providers/aws/guide/credentials/).

4. Create a [Slack App](https://api.slack.com/apps), add the "incoming webhooks" feature, and create a webhook for your app. You can find more information on how to do that on the [Slack documentation](https://api.slack.com/incoming-webhooks)

5. Create a Builton Webhook on your dashboard.

6. Add a `secrets.dev.json` file containing your Builton Webhook Secret and your Slack URL. You can use the `secrets.example.json` as a template.

7. Run `serverless offline` to run the service locally or `serverless deploy` to run it on AWS.
