# SCA confirm example

This example demonstrates how to confirm a payment with Stripe if the user has been asked to re-authenticate it because of SCA (Strong Customer Authentication).
It expects the Stripe payment intent secret and the payment id in the url in the format `https://example.com?PAYMENT_INTENT_CLIENT_SECRET={INSERT_INTENT}&PAYMENT_ID={INSERT_ID}`
It uses:
- The **[Stripe JS SDK](https://stripe.com/docs/stripe-js/elements/quickstart)**
- A **Stripe Publishable API** Key, you can find or create one through [Stripe](https://dashboard.stripe.com/apikeys) dashboard.

# Install Locally

In order to run this example locally, you need to:

1. Clone this repository

2. Replace config stripe api key with your own

3. Open index.html in your browser
