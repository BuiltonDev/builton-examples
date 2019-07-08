'use strict';
const utils = require('./utils');
const twilio = utils.getTwillio();

module.exports.user_created = async (event) => {
  if (utils.checkSecret(event)) {
    const body = JSON.parse(event.body);
    const user = body.object;
    if (user) { // If user doesn't exist, the endpoint is being verified
      if (!user.mobile_phone_number) {
        throw new Error('This user doesn\'t have a phone number');
      }
      try {
        const response = await twilio.messages
          .create({
            from: 'whatsapp:+14155238886',
            body: 'Hello World! Thank you for registering on our website!',
            to: `whatsapp:${user.mobile_phone_number}`
          })
        console.log(response);
      } catch (err) {
        return {
          statusCode: 500,
          err
        }
      }
    }
  } else {
    const err = 'Could not verify the signature';
    return {
      statusCode: 500,
      err
    }
  }
  
  return {
    statusCode: 200
  };
};
