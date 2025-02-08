const checkUsername = function (username) {
  if (username.length < 6 || username.length > 16) {
    return false;
  }
  if (!/^[a-zA-Z0-9_]+$/.test(username)) {
    return false;
  }
  return true;
};

const checkPassword = function (password) {
  if (password.length < 8 || password.length > 16) {
    return false;
  }
  if (!/^[a-zA-Z0-9]+$/.test(password)) {
    return false;
  }
  return true;
};

module.exports = {
  checkUsername,
  checkPassword,
};