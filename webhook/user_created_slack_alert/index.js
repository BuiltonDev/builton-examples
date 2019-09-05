const fetch = require('node-fetch');
const utils = require('./utils');

module.exports.user_created = async (event) => {
    if(utils.isPing(event)) {
        return {
            statusCode: 200
        };
	}
    if(!utils.verifySecret(event)) {
        return {
            statusCode: 401
        };
    }
	const body = JSON.parse(event.body);
    const user = body.object;
    try {
        await fetch(process.env.slackUrl, {
          method: 'POST',
          body: JSON.stringify({
            text: `New signup! ${user.first_name} ${user.last_name} (${user.email})`
          })
        });
        return {
            statusCode: 200
        };
      } catch (err) {
        return {
          statusCode: 500,
          err
        }
      }
};
