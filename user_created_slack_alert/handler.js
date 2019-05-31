'use strict';
const fetch = require('node-fetch');
const utils = require('./utils');

module.exports.user_created = async (event) => {
  if (utils.checkSecret(event)) {
    const body = JSON.parse(event.body);
    const user = body.object;
    if (user) { // If user doesn't exist, the endpoint is being verified
      try {
        const response = await fetch(process.env.slackUrl, {
          method: 'POST',
          body: JSON.stringify({
            text: `New signup! ${user.first_name} ${user.last_name} (${user.email})`
          })
        });
        console.log(response);
      } catch (err) {
        console.error(err);
        return {
          statusCode: 500,
          err
        }
      }
    }
  } else {
    const err = 'Could not verify the signature';
    console.error(err);
    return {
      statusCode: 500,
      err
    }
  }
  
  return {
    statusCode: 200
  };
};
