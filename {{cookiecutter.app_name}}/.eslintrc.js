module.exports = {
  "extends": "airbnb-base",
  "parser": "@babel/eslint-parser",
  "parserOptions": {
    "requireConfigFile": false,
  },
  "rules": {
    "no-param-reassign": 0,
    "import/no-extraneous-dependencies": 0,
    "import/prefer-default-export": 0,
    "consistent-return": 0,
    "no-confusing-arrow": 0,
    "no-underscore-dangle": 0
  },
  "env": {
    "browser": true,
    "node": true
  },
  "globals": {
    "__dirname": true,
    "jQuery": true,
    "$": true
  }
}
